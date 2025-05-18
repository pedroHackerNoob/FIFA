# SQLAlchemy imports
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
# models imports
import Player as player_db
import Stats as player_stats
from views import texts_menu as textm
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

# SHOW
def show():
    option_show = 1
    if option_show == 1:
        # # Match
        match_teams.show_match(engine, text)
    elif option_show == 2:
        # # Team
        team_players.show_teams(engine, text)
    elif option_show == 3:
        # # Players
        player_db.show_players(engine, text)
    elif option_show == 4:
        # # Players stats
        player_stats.show_stats(engine, text)

# UPDATE
def update():
    option_update = 2
    #  Match
    if option_update ==1:
        match_teams.update_match(engine, text)
        match_teams.show_match(engine, text)
    # Team
    elif option_update ==2:
        team_players.update_team(engine, text)
        team_players.show_teams(engine, text)
    # Players
    elif option_update ==3:
        player_db.update_player(engine, text)
        player_db.show_players(engine, text)
    # # Plater Stats
    elif option_update ==4:
        player_stats.update_stats(engine, text)
        player_stats.show_stats(engine, text)

# CREATE
def create():
    create_option = 4
    # match
    if create_option ==1:
        match_teams.create_match(engine, text)
        match_teams.show_match(engine, text)
    elif create_option ==2:
        team_players.create_team(engine, text)
        team_players.show_teams(engine, text)
    elif create_option ==3:
        player_db.create_player(engine, text)
        player_db.show_players(engine, text)
    elif create_option ==4:
        player_stats.create_stats(engine, text)
        player_stats.show_stats(engine, text)


#version
def run_version():
    var = sqlalchemy.__version__
    print(f'version SQALchemy: {var}')
#     menu
def menu():
    textm.texts_menu()
    option = 3
    if option == 0:
        # create_table()
        print("test de conexion: \n")
        db.create_table(engine,text)
        # SHOW
    elif option == 1:
        show()
        # UPDATE
    elif option == 2:
        update()
        # CREATE
    elif option == 3:
        create()

    # motrar tabla jugadores

    run_version()
# MAIN
menu()