from rich.console import Console
from rich.table import Table
console_r = Console()
from views import texts_menu as textm
def show_teams(engine, text):
    import time
    from tqdm import tqdm
    for i in tqdm(range(50)):
        time.sleep(0.01)
    with engine.connect() as conn:
        team = conn.execute(text("SELECT * FROM equipo"))

        table = Table(title="All teams", show_header=True, header_style="bold magenta", show_lines=True)
        table.add_column("ID_team", style="bright_blue")
        table.add_column("name", style="cyan")
        table.add_column("country", style="bright_white")
        # impor_table.Table
        for row in team:
            table.add_row(str(row[0]), str(row[1]), str(row[2]))
        console_r.print(table)
# UPDATE
def update_team(engine, text):
    show_teams(engine, text)
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
    show_teams(engine, text)
# CREATE
def create_team(engine, text):
    show_teams(engine, text)
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
    show_teams(engine, text)