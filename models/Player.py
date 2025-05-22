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
def update_player(engine, text):
    with engine.connect() as conn:
        id_jugador = int(input("| Enter id_player: "))
        nombre = input("| Enter name: ")
        pais = input("| Enter country")
        deporte = input("| Enter sport: ")
        posicion = input("| Enter position")
        rareza = input("| Enter rarely: ")
        nivel = int(input("| Enter level:"))
        imagen = input("| Enter image: ")
        id_equipo = int(input("| Enter id_team: "))
        # prompt
        conn.execute(
            text("""
                 UPDATE jugador
                 SET nombre   = :nombre,
                     pais     = :pais,
                     deporte  = :deporte,
                     posicion = :posicion,
                     rareza   = :rareza,
                     nivel    = :nivel,
                     imagen   = :imagen,
                     idEquipo = :idEquipo
                 WHERE idJugador = :idJugador
                 """),
            [{
                "nombre": nombre,
                "pais": pais,
                "deporte": deporte,
                "posicion": posicion,
                "rareza": rareza,
                "nivel": nivel,
                "imagen": imagen,
                "idEquipo": id_equipo,
                "idJugador": id_jugador
            }]
        )

        # ejecutar cambios
        conn.commit()
    show_players(engine, text)
# create player
def create_player(engine, text):
    with engine.connect() as conn:
        nombre = input("| Enter name: ")
        pais = input("| Enter country: ")
        deporte = input("| Enter deport: ")
        posicion = input("| position: ")
        rareza = input("| Enter rarely: ")
        nivel = int(input("| Enter level: "))
        imagen = input("| Enter image: " )
        id_equipo = int(input("| Enter id_team: "))

        # create new player prompt
        conn.execute(text('''
                          INSERT INTO jugador (nombre
                                              ,pais,
                                               deporte,
                                               posicion,
                                               rareza,
                                               nivel,
                                               imagen,
                                               idEquipo) 
                             VALUES ( :nombre, 
                                      :pais, 
                                      :deporte, 
                                      :posicion, 
                                      :rareza, 
                                      :nivel, 
                                      :imagen, 
                                      :idEquipo )'''),
                              {
                                 "nombre": nombre,
                                 "pais": pais,
                                 "deporte": deporte,
                                 "posicion": posicion,
                                 "rareza": rareza,
                                 "nivel": nivel,
                                 "imagen": imagen,
                                 "idEquipo": id_equipo,
                              }
                          )
        # made change
        conn.commit()