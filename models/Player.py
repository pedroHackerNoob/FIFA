from views import texts_menu as textm
#     Mostrar jugadores
def info_players( engine , text):
    with engine.connect() as conn:
        # print in row
        result= conn.execute(text("SELECT * FROM jugador"))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("| All players info\n|")
        for row in result:
            print(f'| ID: {row[0]} | name: {row[1]} | country: {row[2]} | job: {row[3]} | position {row[4]} | top: {row[5]} | level: {row[6]} | txt: {row[7]} | TeamId: {row[8]} |')
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def update_player(engine, text):
    textm.player_update()
    with engine.connect() as conn:
        id_jugador = "1"
        nombre = input("nombre: ")
        pais = "test"
        deporte = "test"
        posicion = "test"
        rareza = "comun"
        nivel = "0"
        imagen = "test"
        id_equipo = "2"
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