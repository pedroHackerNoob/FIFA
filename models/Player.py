#     Mostrar jugadores
def info_players( engine , database, text):
    print(f'\nConectando a la base de datos: {database}\n')

    with engine.connect() as conn:
        # print in row
        result= conn.execute(text("SELECT * FROM jugador"))
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("|All players info")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        for row in result:
            print(f'|ID: {row[0]} | name: {row[1]} | country: {row[2]} | job: {row[3]} | position {row[4]} | top: {row[5]} | level: {row[6]} | txt: {row[7]} | TeamId:{row[8]}')
        print("-----------------------------------------------------------------------------------------------------------------------------")
