# SQLAlchemy imports
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
# rich
import rich
from rich.console import Console
console_r = Console()
# clear import
import os
import platform
# models imports
from models import Player as player_db
from models import Stats as player_stats
from views import texts_menu as ui_text
from models import Team as team_players
from models import Match as match_teams
from models import DataBase as db
# credenciales
user = "root"
password = "kali"
port = "3306"
engine = create_engine(f'mysql+pymysql://{user}:{password}@localhost:{port}/cartas_deportivas')
# clear function
def clear_terminal():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    ui_text.fifa_lxs()
# SHOW
def show():
    clear_terminal()
    ui_text.show()
    option_show = int(input())
        # # Match
    if option_show == 1:
        match_teams.show_match(engine, text)
        # # Team
    elif option_show == 2:
        team_players.show_teams(engine, text)
        # # Players
    elif option_show == 3:
        player_db.show_players(engine, text)
        # # Players stats
    elif option_show == 4:
        player_stats.show_stats(engine, text)

# UPDATE
def update():
    clear_terminal()
    ui_text.update()
    option_update = int(input())
    #  Match
    if option_update ==1:
        match_teams.show_match(engine, text)
        match_teams.update_match(engine, text)
        match_teams.show_match(engine, text)
    # Team
    elif option_update ==2:
        team_players.show_teams(engine, text)
        team_players.update_team(engine, text)
        team_players.show_teams(engine, text)
    # Players
    elif option_update ==3:
        match_teams.show_match(engine, text)
        player_db.update_player(engine, text)
        player_db.show_players(engine, text)
    # # Plater Stats
    elif option_update ==4:
        match_teams.show_match(engine, text)
        player_stats.update_stats(engine, text)
        player_stats.show_stats(engine, text)

# CREATE
def create():
    ui_text.create()
    create_option = int(input())
    # match
    if create_option ==1:
        match_teams.show_match(engine, text)
        match_teams.create_match(engine, text)
        match_teams.show_match(engine, text)
    # Team
    elif create_option ==2:
        team_players.show_teams(engine, text)
        team_players.create_team(engine, text)
        team_players.show_teams(engine, text)
    # Player
    elif create_option ==3:
        player_db.show_players(engine, text)
        player_db.create_player(engine, text)
        player_db.show_players(engine, text)
    # Stats
    elif create_option ==4:
        player_stats.show_stats(engine, text)
        player_stats.create_stats(engine, text)
        player_stats.show_stats(engine, text)
#     menu
def menu():

    ui_text.texts_menu()
    option = int(input())
    # option = 3
        # create_table()
    if option == 0:
        print("test de conexion: \n")
        # db.create_table(engine,text)
        # SHOW
    # SHOW
    elif option == 1:
        clear_terminal()
        show()
    # UPDATE
    elif option == 2:
        clear_terminal()
        update()
    # CREATE
    elif option == 3:
        clear_terminal()
        create()
# bucle
def break_or_continue():
    option = console_r.input("[black on bright_yellow]Enter [B]reak or [C]ontinue: ")
    if option.lower() == "b":
        return False
    elif option.lower() == "c":
        return True
    else:
        print("Invalid option. Please enter B or C.")
        return break_or_continue()
# MAIN
def test():
    clear_terminal()
    option = "banner"

    if option == "demo":
        while True:
            clear_terminal()
            ui_text.run_version(sqlalchemy.__version__)
            # menu()
            if not break_or_continue():
                break

    elif option == "banner":
        # clear_terminal()
        print("xd")
