from views import texts_menu as textm
def show_teams(engine, text):
    with engine.connect() as conn:
        team = conn.execute(text("SELECT * FROM equipo"))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("| SHOW all teams info\n|")
        for row in team:
            print(f'| ID_team: {row[0]} | name: {row[1]} | country: {row[2]} |')
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")