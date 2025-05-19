from views import texts_menu as textm
#     Mostrar jugadores
def show_players(engine, text):
    with engine.connect() as conn:
        # print in row
        result= conn.execute(text("SELECT * FROM jugador"))
        print("| SHOW all players info\n|")
        for row in result:
            print(f'| ID_player: {row[0]} | name: {row[1]} | country: {row[2]} | job: {row[3]} | position {row[4]} | top: {row[5]} | level: {row[6]} | txt: {row[7]} | TeamId: {row[8]} |')
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
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
        pais = input("| Enter country")
        deporte = input("| Enter deport")
        posicion = input("| position")
        rareza = input("Enter rarely")
        nivel = int(input("| Enter level:"))
        imagen = input("| Enter image")
        id_equipo = int(input("| Enter id_team:"))

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