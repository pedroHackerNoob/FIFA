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

    with engine.connect() as conn:
        id_jugador = 1
        nombre = "miado"
        pais = "test"
        deporte = "test"
        posicion = "tes"
        rareza = "comun"
        nivel = "0"
        imagen = "test"
        id_equipo = "1"
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

        conn.commit()