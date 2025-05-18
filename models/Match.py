# READ
def show_match(engine, txt):
    with engine.connect() as conn:
        match = conn.execute(txt("SELECT * FROM partido"))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("| SHOW all match info\n|")
        for row in match:
            print(f'| ID_match: {row[0]} | fecha: {row[1]} | lugar: {row[2]} | equipo1: {row[3]} | equipo2: {row[4]} |')
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# UPDATE
def update_match(engine, text):
    with engine.connect() as conn:
        id_partido = "1"
        fecha = "2023-01-01"
        lugar = "londres"
        id_Equipo1 = "1"
        id_Equipo2 = "2"

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
                "idEquipo1": id_Equipo1,
                "idEquipo2": id_Equipo2,
                "idpartido": id_partido
            }]
        )

        # ejecutar cambios
        conn.commit()