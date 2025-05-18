def show_match(engine, txt):
    with engine.connect() as conn:
        match = conn.execute(txt("SELECT * FROM partido"))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("| SHOW all match info\n|")
        for row in match:
            print(f'| ID_match: {row[0]} | fecha: {row[1]} | lugar: {row[2]} | equipo1: {row[3]} | equipo2: {row[4]} |')
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")