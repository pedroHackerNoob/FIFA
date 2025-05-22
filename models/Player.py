from views import texts_menu as ui_text
from rich.table import Table
#
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
#
class Player(Base):
    __tablename__ = 'jugador'
    idJugador = Column(Integer, primary_key=True)
    nombre = Column(String)
    pais = Column(String)
    deporte = Column(String)
    posicion = Column(String)
    rareza = Column(String)
    nivel = Column(Integer)
    imagen = Column(String)
    idEquipo = Column(Integer)
#     Mostrar jugadores
def show_players(Session):
    ui_text.charge_bar()
    table = Table(title="All Players", show_header=True, header_style="bold magenta", show_lines=True)
    table.add_column("Id_Player", style="bright_blue", justify="center")
    table.add_column("name", style="cyan")
    table.add_column("country", style="bright_white")
    table.add_column("sport", style="green")
    table.add_column("position", style="red")
    table.add_column("rare", style="yellow")
    table.add_column("level", style="magenta")
    table.add_column("image", style="blue")
    table.add_column("team_id", style="turquoise2", justify="center")
    try:
        with Session() as session:
            players = session.query(Player).all()
            for player in players:
                table.add_row(
                    str(player.idJugador),
                    str(player.nombre),
                    str(player.pais),
                    str(player.deporte),
                    str(player.posicion),
                    str(player.rareza),
                    str(player.nivel),
                    str(player.imagen),
                    str(player.idEquipo)
                )
        ui_text.table_print(table, "players")
    except Exception as e:
        print(f"Error displaying players: {str(e)}")
# update plauer
def update_player(Session):
    show_players(Session)
    try:
        id_jugador = int(input("| Enter id_player: "))
        nombre = input("| Enter name: ")
        pais = input("| Enter country: ")
        deporte = input("| Enter sport: ")
        posicion = input("| Enter position: ")
        rareza = input("| Enter rarely: ")
        nivel = int(input("| Enter level:"))
        imagen = input("| Enter image: ")
        id_equipo = int(input("| Enter id_team: "))
        with Session() as session:
            player = session.query(Player).filter(Player.idJugador == id_jugador).first()
            if player:
                player.nombre = nombre
                player.pais = pais
                player.deporte = deporte
                player.posicion = posicion
                player.rareza = rareza
                player.nivel = nivel
                player.imagen = imagen
                player.idEquipo = id_equipo
                session.commit()
                show_players(Session)
            else:
                print(f"No player found with id {id_jugador}")
    except Exception as e:
        print(f"Error updating player: {str(e)}")
# create player
def create_player(Session):
    show_players(Session)
    try:
        nombre = input("| Enter name: ")
        pais = input("| Enter country: ")
        deporte = input("| Enter sport: ")
        posicion = input("| Enter position: ")
        rareza = input("| Enter rarely: ")
        nivel = int(input("| Enter level: "))
        imagen = input("| Enter image: ")
        id_equipo = int(input("| Enter id_team: "))

        with Session() as session:
            new_player = Player(nombre=nombre, pais=pais, deporte=deporte, posicion=posicion, rareza=rareza, nivel=nivel, imagen=imagen, idEquipo=id_equipo)
            session.add(new_player)
            session.commit()
            show_players(Session)
    except Exception as e:
        print(f"Error creating player: {str(e)}")
# Delete
def delete_player(Session):
    show_players(Session)
    try:
        id_player = int(input("| Enter id_player: "))
        with Session() as session:
            player = session.query(Player).filter(Player.idJugador == id_player).first()
            if player:
                session.delete(player)
                session.commit()
                show_players(Session)
            else:
                print(f"No player found with id {id_player}")
    except Exception as e:
        print(f"Error deleting player: {str(e)}")
