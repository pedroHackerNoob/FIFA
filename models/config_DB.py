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
    option_update = 1
    if option_update ==1:
        #  Match
        match_teams.update_match(engine, text)
        match_teams.show_match(engine, text)
    elif option_update ==4:
        # # Plater Stats
        player_db.update_player(engine, text)
# test de conexion
def run_version():
    var = sqlalchemy.__version__
    print(f'version SQALchemy: {var}')
#     menu
def menu():
    textm.texts_menu()
    option = 2
    if option == 0:
        # create_table()
        print("test de conexion: \n")
        db.create_table(engine,text)
    elif option == 1:
        # SHOW
        show()
    elif option == 2:
        # UPDATE
        update()
    elif option == 3:
        player_stats.create_stats(engine, text)

    # motrar tabla jugadores

    run_version()
menu()