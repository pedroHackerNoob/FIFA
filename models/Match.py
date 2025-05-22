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
def show_match(Session):
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
def update_match(Session):

    try:
        show_match(Session)
        id_partido = int(input("| Enter id_match: "))
        fecha = datetime
        lugar = input("| Enter place: ")
        id_equipo1 = int(input("| Enter id_team visitors: "))
        id_equipo2 = int(input("| Enter id_team locals: "))
        with Session() as session:
            match = session.query(Match).filter(Match.idPartido == id_partido).first()
            if match:
                match.fecha = fecha
                match.lugar = lugar
                match.idEquipo1 = id_equipo1
                match.idEquipo2 = id_equipo2
                session.commit()
                show_match(Session)
            else:
                print(f"No match found with id {id_partido}")
    except Exception as e:
        print(f"Error updating match: {str(e)}")
# CREATE
def create_match(Session):
    show_match(Session)
    try:
        fecha = datetime
        lugar = input("| Enter place: ")
        id_equipo1 = int(input("| Enter id_team visitors: "))
        id_equipo2 = int(input("| Enter id_team locals: "))
        with Session() as session:
            new_match = Match(fecha=fecha, lugar=lugar, idEquipo1=id_equipo1, idEquipo2=id_equipo2)
            session.add(new_match)
            session.commit()
            show_match(Session)
    except Exception as e:
        print(f"Error creating match: {str(e)}")
# Delete
def delete_match(Session):
    show_match(Session)
    try:
        id_match = int(input("| Enter id_match: "))
        with Session() as session:
            match = session.query(Match).filter(Match.idPartido == id_match).first()
            if match:
                session.delete(match)
                session.commit()
                show_match(Session)
            else:
                print(f"No match found with id {id_match}")
    except Exception as e:
        print(f"Error deleting match: {str(e)}")

