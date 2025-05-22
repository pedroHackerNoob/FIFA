from rich.console import Console
from rich.table import Table
console_r = Console()
#
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from views import texts_menu as ui_text
#
Base = declarative_base()
#
class Team(Base):
    __tablename__ = 'equipo'
    idEquipo = Column(Integer, primary_key=True)
    nombre = Column(String)
    pais = Column(String)

def show_teams(Session):
    try:
        ui_text.charge_bar()
        table = Table(title="All teams", show_header=True, header_style="bold magenta", show_lines=True)
        table.add_column("ID_team", style="bright_blue")
        table.add_column("name", style="cyan")
        table.add_column("country", style="bright_white")

        with Session() as session:
            teams = session.query(Team).all()
            for team in teams:
                table.add_row(
                    str(team.idEquipo),
                    str(team.nombre),
                    str(team.pais)
                )
            ui_text.table_print(table, "teams")
    except Exception as e:
        print(f"Error displaying teams: {str(e)}")

# UPDATE
def update_team(Session):
    show_teams(Session)
    id_team = int(input("| Enter id_team: "))
    nombre = input("| Enter name: ")
    pais = input("| Enter country: ")
    try:
        with Session() as session:
            team = session.query(Team).filter(Team.idEquipo == id_team).first()
            if team:
                team.nombre = nombre
                team.pais = pais
                session.commit()
                show_teams(Session)
            else:
                print(f"No team found with id {id_team}")
            show_teams(Session)

    except Exception as e:
        print(f"Error updating team: {str(e)}")
# CREATE
# def create_team(Session):
#     show_teams(engine, text)
#     with engine.connect() as conn:
#         nombre = input("| Enter name: ")
#         pais = input("| Enter country: ")
#
#         conn.execute(text('''
#                           INSERT INTO equipo (nombre, pais)
#                              VALUES (:nombre,
#                                      :pais)
#                           '''),
#                      {
#             "nombre": nombre,
#             "pais": pais
#         })
#         # made change
#         conn.commit()
#     show_teams(engine, text)