# SQLAlchemy imports
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
# clear import
import os
import platform
# models imports
import Player as player_db
import Stats as player_stats
from views import texts_menu as ui_text
import Team as team_players
import Match as match_teams
import DataBase as db
# credenciales
user = "root"
password = "kali"
database = "cartas_deportivas"
port = "3306"
type_db = "mysql"
engine = create_engine(f'{type_db}+py{type_db}://{user}:{password}@localhost:{port}/{database}')
# clear function
def clear_terminal():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    ui_text.tyler()
# SHOW
def show():
    clear_terminal()
    ui_text.show()
    option_show = int(input("Please enter your option:"))
        # # Match
    if option_show == 1:
        clear_terminal()
        match_teams.show_match(engine, text)
        # # Team
    elif option_show == 2:
        clear_terminal()
        team_players.show_teams(engine, text)
        # # Players
    elif option_show == 3:
        clear_terminal()
        player_db.show_players(engine, text)
        # # Players stats
    elif option_show == 4:
        clear_terminal()
        player_stats.show_stats(engine, text)

# UPDATE
def update():
    clear_terminal()
    ui_text.update()
    option_update = int(input("Please enter your option:"))
    #  Match
    if option_update ==1:
        clear_terminal()
        match_teams.update_match(engine, text)
        match_teams.show_match(engine, text)
    # Team
    elif option_update ==2:
        clear_terminal()
        team_players.update_team(engine, text)
        team_players.show_teams(engine, text)
    # Players
    elif option_update ==3:
        clear_terminal()
        player_db.update_player(engine, text)
        player_db.show_players(engine, text)
    # # Plater Stats
    elif option_update ==4:
        clear_terminal()
        player_stats.update_stats(engine, text)
        player_stats.show_stats(engine, text)

# CREATE
def create():
    clear_terminal()
    ui_text.create()
    create_option = int(input("Please enter your option:"))
    # match
    if create_option ==1:
        clear_terminal()
        match_teams.create_match(engine, text)
        match_teams.show_match(engine, text)
    # Team
    elif create_option ==2:
        clear_terminal()
        team_players.create_team(engine, text)
        team_players.show_teams(engine, text)
    # Player
    elif create_option ==3:
        clear_terminal()
        player_db.create_player(engine, text)
        player_db.show_players(engine, text)
    # Stats
    elif create_option ==4:
        clear_terminal()
        player_stats.create_stats(engine, text)
        player_stats.show_stats(engine, text)

#version
def run_version():
    var = sqlalchemy.__version__
    print(f'version SQALchemy: {var}')
#     menu
def menu():
    ui_text.tyler()
    ui_text.texts_menu()
    option = int(input("Please enter your option:"))
    # option = 3
        # create_table()
    if option == 0:
        print("test de conexion: \n")
        db.create_table(engine,text)
        # SHOW
    # SHOW
    elif option == 1:
        show()
    # UPDATE
    elif option == 2:
        update()
    # CREATE
    elif option == 3:
        create()
    # show version
    run_version()
# MAIN
menu()