from views import texts_menu as textm
#     Mostrar jugadores
def show_players(engine, text):
    with engine.connect() as conn:
        players = conn.execute(text("SELECT * FROM jugador"))

        from rich.console import Console
        from rich.table import Table
        console_r = Console()

        table = Table(title="All Players", show_header=True, header_style="bold magenta", show_lines=True)
        table.add_column("Id_Player", style="bright_blue",justify="center")
        table.add_column("name", style="cyan")
        table.add_column("country", style="bright_white")
        table.add_column("sport", style="green")
        table.add_column("position", style="red")
        table.add_column("rare", style="yellow")
        table.add_column("level", style="magenta")
        table.add_column("image", style="blue")
        table.add_column("team_id", style="turquoise2", justify="center")


        # impor_table.Table
        for row in players:
            table.add_row(
                str(row[0]),
                str(row[1]),
                str(row[2]),
                str(row[3]),
                str(row[4]),
                str(row[5]),
                str(row[6]),
                str(row[7]),
                str(row[8]),
            )
        console_r.print(table)
# update plauer
def update_player(engine, text):
    textm.update()
    with engine.connect() as conn:
        id_jugador = int(input("| Enter id_player: "))
        nombre = input("| Enter name: ")
        pais = input("| Enter country")
        deporte = input("| Enter deport")
        posicion = input("| position")
        rareza = input("Enter rarely")
        nivel = int(input("| Enter level:"))
        imagen = input("| Enter image")
        id_equipo = int(input("| Enter id_team:"))
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