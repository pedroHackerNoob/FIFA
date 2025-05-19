# READ
def show_match(engine, txt):
    with engine.connect() as conn:
        match = conn.execute(txt("SELECT * FROM partido"))
        print("| All matches:\n|")
        for row in match:
            print(f'| ID_match: {row[0]} | date: {row[1]} | country: {row[2]} | visit: {row[3]} | local: {row[4]} |')
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# UPDATE
def update_match(engine, text):
    with engine.connect() as conn:
        id_partido = "1"
        fecha = "2023-01-01"
        lugar = "londres"
        id_equipo1 = "1"
        id_equipo2 = "2"

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
# CREATE
def create_match(engine, text):
    with engine.connect() as conn:
        fecha = "2023-01-02"
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
