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
        id_Equipo = "2"
        nombre = "RBG"
        pais = "alemania"

        # prompt
        conn.execute(
            text("""
                 UPDATE equipo
                 SET nombre   = :nombre,
                     pais     = :pais,
                 WHERE idEquipo = :idEquipo
                 """),
            [{
                "nombre": nombre,
                "pais": pais,
                "idEquipo": id_Equipo,
            }]
        )

        # ejecutar cambios
        conn.commit()