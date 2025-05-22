# import models
from rich.console import Console
from rich.table import Table
from views import texts_menu as ui_text
#
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
#
console_r = Console()

class Stats(Base):
    __tablename__ = 'estadisticas'
    idEstadistica = Column(Integer, primary_key=True)
    idJugador = Column(Integer)
    velocidad = Column(Integer)
    fuerza = Column(Integer)
    tecnica = Column(Integer)
    resistencia = Column(Integer)
    inteligencia = Column(Integer)
    habilidades = Column(String)

# show
def show_stats(Session):
    ui_text.charge_bar()

    table = Table(title="All stats", show_header=True, header_style="bold magenta", show_lines=True)
    table.add_column("Id_stats", style="bright_blue")
    table.add_column("id_player", style="cyan", justify="center")
    table.add_column("velocity", style="bright_white")
    table.add_column("strength", style="green")
    table.add_column("technique", style="red")
    table.add_column("resistance", style="yellow")
    table.add_column("smart", style="magenta")
    table.add_column("skills", style="blue")
    try:
        with Session() as session:
            stats = session.query(Stats).all()
            for stat in stats:
                table.add_row(
                    str(stat.idEstadistica),
                    str(stat.idJugador),
                    str(stat.velocidad),
                    str(stat.fuerza),
                    str(stat.tecnica),
                    str(stat.resistencia),
                    str(stat.inteligencia),
                    str(stat.habilidades)
                )
            ui_text.table_print(table, "players stats")
    except Exception as e:
        print(f"Error displaying stats: {str(e)}")
#create
def create_stats(Session):

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
# update
def update_stats(engine, text):
    show_stats(engine, text)
    with engine.connect() as conn:
        id_estadistica = int(input("| Enter id stats: "))
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
                              
                              WHERE idEstadistica = :idEstadistica
                          '''),{
            "velocidad": velocidad,
            "fuerza": fuerza,
            "tecnica": tecnica,
            "resistencia": resistencia,
            "inteligencia": inteligencia,
            "habilidades": habilidades,
            "idEstadistica": id_estadistica
        })
        conn.commit()

    show_stats(engine, text)