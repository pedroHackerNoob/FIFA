# import models
from views import texts_menu as textm
# craete state
def show_stats(engine, text):
    with engine.connect() as conn:
        stats_players = conn.execute(text("SELECT * FROM estadisticas"))
        from rich.console import Console
        from rich.table import Table
        console_r = Console()

        table = Table(title="All stats", show_header=True, header_style="bold magenta", show_lines=True)
        table.add_column("Id_stats", style="bright_blue")
        table.add_column("id_player", style="cyan", justify="center")
        table.add_column("velocity", style="bright_white")
        table.add_column("strength", style="green")
        table.add_column("technique", style="red")
        table.add_column("resistance", style="yellow")
        table.add_column("smart", style="magenta")
        table.add_column("skills", style="blue")

        # impor_table.Table
        for row in stats_players:
            table.add_row(
                str(row[0]),
                str(row[1]),
                str(row[2]),
                str(row[3]),
                str(row[4]),
                str(row[5]),
                str(row[6]),
                str(row[7])
            )
        console_r.print(table)

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