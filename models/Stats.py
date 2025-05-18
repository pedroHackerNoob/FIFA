# import models
from views import texts_menu as textm
# craete state
def show_stats(engine, text):
    with engine.connect() as conn:
        stats_players = conn.execute(text("SELECT * FROM estadisticas"))
        # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("| SHOW all players stats info\n|")
        for row in stats_players:
            print(f'| ID_stats: {row[0]} | id_player: {row[1]} | velocity: {row[2]} | strength: {row[3]} | technique {row[4]} | resistence: {row[5]} | intelligence: {row[6]} | skill: {row[7]} |')
            print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")


#
def create_stats(engine, text):

    with engine.connect() as conn:
        id_jugador = "5"
        velocidad = "10"
        fuerza = "10"
        tecnica = "10"
        resistencia = "10"
        inteligencia = "10"
        # habilidades = input("| Ingrese habilidad")
        habilidades = "maniaco"
        # prompt
        conn.execute(
            text("""
                 INSERT INTO estadisticas (idJugador, 
                                           velocidad, 
                                           fuerza, 
                                           tecnica, 
                                           resistencia, 
                                           inteligencia, 
                                           habilidades) 
                 VALUES ( :idJugador, 
                          :velocidad, 
                          :fuerza, 
                          :tecnica, 
                          :resistencia, 
                          :inteligencia, 
                          :habilidades)
                 """),
            [{
                "idJugador": id_jugador,
                "velocidad": velocidad,
                "fuerza": fuerza,
                "tecnica": tecnica,
                "resistencia": resistencia,
                "inteligencia": inteligencia,
                "habilidades": habilidades,
            }]
        )

        # ejecutar cambios
        conn.commit()
