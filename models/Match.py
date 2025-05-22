from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Match(Base):
    __tablename__ = 'partido'

    idPartido = Column(Integer, primary_key=True)
    fecha = Column(String)
    lugar = Column(String)
    idEquipo1 = Column(Integer)
    idEquipo2 = Column(Integer)

from views import texts_menu as ui_text
# Date time
import datetime
datetime = datetime.datetime.now()
# rich
from rich.console import Console
from rich.table import Table
console_r = Console()
# READ
def show_match(select, Session, engine, txt):
    try:
        ui_text.charge_bar()
        table = Table(title="All matches", show_header=True, header_style="bold magenta", show_lines=True)
        table.add_column("ID", style="bright_blue")
        table.add_column("Date", style="cyan")
        table.add_column("Place", style="bright_white")
        table.add_column("Visitor Team ID", style="green", justify="center")
        table.add_column("Local Team ID", style="red", justify="center")

        with Session() as session:
            matches = session.query(Match).all()
            for match in matches:
                table.add_row(
                    str(match.idPartido),
                    str(match.fecha),
                    str(match.lugar),
                    str(match.idEquipo1),
                    str(match.idEquipo2)
                )

            ui_text.table_print(table, "matches")
    except Exception as e:
        print(f"Error displaying matches: {str(e)}")
# UPDATE
def update_match(engine, text):
    show_match(engine, text)
    with engine.connect() as conn:
        id_partido = int(input("| Enter id_match: "))
        fecha = datetime
        lugar = input("| Enter place: ")
        id_equipo1 = int(input("| Enter id_team visitors: "))
        id_equipo2 = int(input("| Enter id_team locals: "))

        # prompt
        conn.execute(
            text("""
                 UPDATE partido
                 SET fecha   = :fecha,
                     lugar     = :lugar,
                     idEquipo1 = :idEquipo1,
                     idEquipo2 = :idEquipo2
                     
                 WHERE idpartido = :idpartido
                 """),
            [{
                "fecha": fecha,
                "lugar": lugar,
                "idEquipo1": id_equipo1,
                "idEquipo2": id_equipo2,
                "idpartido": id_partido
            }]
        )

        # ejecutar cambios
        conn.commit()
    show_match(engine, text)
# CREATE
def create_match(engine, text):
    show_match(engine, text)
    print("| Enter date: ", datetime)
    with engine.connect() as conn:
        fecha = datetime
        lugar = input("| Enter place: ")
        id_equipo1 = int(input("| Enter id_team visitors: "))
        id_equipo2 = int(input("| Enter id_team locals: "))

        conn.execute(
            text("""
                 INSERT INTO partido (fecha,
                                    lugar,
                                    idEquipo1,
                                    idEquipo2)
                 VALUES (:fecha,
                        :lugar,
                        :idEquipo1,
                        :idEquipo2)
                 """),
            {
                "fecha": fecha,
                "lugar": lugar,
                "idEquipo1": id_equipo1,
                "idEquipo2": id_equipo2
            }
        )
        # made action
        conn.commit()
        show_match(engine, text)
