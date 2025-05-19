
# Date time
import datetime
datetime = datetime.datetime.now()
# rich
from rich.console import Console
from rich.table import Table
console_r = Console()
# READ
def show_match(engine, txt):
    import time
    from tqdm import tqdm
    for i in tqdm(range(50)):
        time.sleep(0.01)
    with engine.connect() as conn:
        match = conn.execute(txt("SELECT * FROM partido"))

        table = Table(title="All matches", show_header=True, header_style="bold magenta", show_lines=True)

        table.add_column("ID_match", style="bright_blue")
        table.add_column("date", style="cyan")
        table.add_column("country", style="bright_white")
        table.add_column("visitors ID", style="green", justify="center")
        table.add_column("locals ID", style="red", justify="center")
        # impor_table.Table
        for row in match:
            table.add_row(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]))
        console_r.print(table)
# UPDATE
def update_match(engine, text):
    show_match(engine, text)
    with engine.connect() as conn:
        id_partido = int(input("| Enter id_match: "))
        fecha = datetime
        lugar = input("| Enter place: ")
        id_equipo1 = int(input("| Enter id_team visitors: "))
        id_equipo2 = int(input("| Enter id_team locals: "))

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
                "idEquipo1": id_equipo1,
                "idEquipo2": id_equipo2,
                "idpartido": id_partido
            }]
        )

        # ejecutar cambios
        conn.commit()
    show_match(engine, text)
# CREATE
def create_match(engine, text):
    show_match(engine, text)
    print("| Enter date: ", datetime)
    with engine.connect() as conn:
        fecha = datetime
        lugar = input("| Enter place: ")
        id_equipo1 = int(input("| Enter id_team visitors: "))
        id_equipo2 = int(input("| Enter id_team locals: "))

        conn.execute(
            text("""
                 INSERT INTO partido (fecha,
                                    lugar,
                                    idEquipo1,
                                    idEquipo2)
                 VALUES (:fecha,
                        :lugar,
                        :idEquipo1,
                        :idEquipo2)
                 """),
            {
                "fecha": fecha,
                "lugar": lugar,
                "idEquipo1": id_equipo1,
                "idEquipo2": id_equipo2
            }
        )
        # made action
        conn.commit()
        show_match(engine, text)
