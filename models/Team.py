from views import texts_menu as textm
def show_teams(engine, text):
    with engine.connect() as conn:
        team = conn.execute(text("SELECT * FROM equipo"))
        print("| SHOW all teams info\n|")
        for row in team:
            print(f'| ID_team: {row[0]} | name: {row[1]} | country: {row[2]} |')
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# UPDATE
def update_team(engine, text):
    with engine.connect() as conn:
        id_equipo = int(input("| Enter id_team: "))
        nombre = input("| Enter name: ")
        pais = input("| Enter country: ")
        conn.execute(text("""
                          UPDATE equipo 
                          SET nombre = :nombre,
                              pais = :pais
                          WHERE idEquipo = :idEquipo"""),{
            "nombre": nombre,
            "pais": pais,
            "idEquipo": id_equipo
        })
        # made change
        conn.commit()
# CREATE
def create_team(engine, text):
    with engine.connect() as conn:
        nombre = input("| Enter name: ")
        pais = input("| Enter country: ")

        conn.execute(text('''
                          INSERT INTO equipo (nombre, pais)
                             VALUES (:nombre, 
                                     :pais)
                          '''),
                     {
            "nombre": nombre,
            "pais": pais
        })
        # made change
        conn.commit()