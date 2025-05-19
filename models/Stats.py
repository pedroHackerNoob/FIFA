# import models
from views import texts_menu as textm
# craete state
def show_stats(engine, text):
    with engine.connect() as conn:
        stats_players = conn.execute(text("SELECT * FROM estadisticas"))
        print("| SHOW all players stats info\n|")
        for row in stats_players:
            print(f'| ID_stats: {row[0]} | id_player: {row[1]} | velocity: {row[2]} | strength: {row[3]} | technique {row[4]} | resistence: {row[5]} | intelligence: {row[6]} | skill: {row[7]} |')
            print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")


#
def create_stats(engine, text):

    with engine.connect() as conn:
        velocidad = int(input("| Enter velocity: "))
        fuerza = int(input("| Enter strength: "))
        tecnica = int(input("| Enter technique: "))
        resistencia = int(input("| Enter resistence: "))
        inteligencia = int(input("| Enter intelligence: "))
        habilidades = input("| Enter skill:")
        # prompt
        conn.execute(
            text("""
                 INSERT INTO estadisticas ( 
                                           velocidad, 
                                           fuerza, 
                                           tecnica, 
                                           resistencia, 
                                           inteligencia, 
                                           habilidades) 
                 VALUES (  
                          :velocidad, 
                          :fuerza, 
                          :tecnica, 
                          :resistencia, 
                          :inteligencia, 
                          :habilidades)
                 """),
            [{

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


def update_stats(engine, text):
    with engine.connect() as conn:
        id_jugador = int(input("| Enter id_player: "))
        velocidad = int(input("| Enter velocity: "))
        fuerza = int(input("| Enter strength: "))
        tecnica = int(input("| Enter technique: "))
        resistencia = int(input("| Enter resistence: "))
        inteligencia = int(input("| Enter intelligence: "))
        habilidades = input("| Enter skill:")

        conn.execute(text('''
                          UPDATE estadisticas 
                          SET velocidad = :velocidad, 
                              fuerza =:fuerza, 
                              tecnica = :tecnica, 
                              resistencia = :resistencia, 
                              inteligencia = :inteligencia, 
                              habilidades = :habilidades
                              
                              WHERE idJugador = :idJugador
                          '''),{
            "velocidad": velocidad,
            "fuerza": fuerza,
            "tecnica": tecnica,
            "resistencia": resistencia,
            "inteligencia": inteligencia,
            "habilidades": habilidades,
            "idJugador": id_jugador
        })