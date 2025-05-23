# SQLAlchemy imports
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
session = Session()

# rich
import rich
from rich.console import Console
from rich.table import Table
console_r = Console()
# models imports
from models import Player as player
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
Session = sessionmaker(bind=engine)
# SHOW
def show():
    ui_text.show()
    option_show = int(input())
        # # Match
    if option_show == 1:
        match_teams.show_match(Session)
        # # Team
    elif option_show == 2:
        team_players.show_teams(Session)
        # # Players
    elif option_show == 3:
        player.show_players(Session)
        # # Players stats
    elif option_show == 4:
        player_stats.show_stats(Session)
# UPDATE
def update():
    ui_text.update()
    option_update = int(input())
    #  Match
    if option_update ==1:
        match_teams.update_match(Session)
    # Team
    elif option_update ==2:
        team_players.update_team(Session)
    # Players
    elif option_update ==3:
        player.update_player(Session)
    # # Plater Stats
    elif option_update ==4:
        player_stats.update_stats(Session)
# CREATE
def create():
    create_option = int(input())
    # match
    if create_option ==1:
        match_teams.create_match(Session)
    # Team
    elif create_option ==2:
        team_players.create_team(Session)
    # Player
    elif create_option ==3:
        player.create_player(Session)
    # Stats
    elif create_option ==4:
        player_stats.create_stats(Session)
# DELETE
def delete():
    delete_option = int(input())
    # match
    if delete_option ==1:
        match_teams.delete_match(Session)
    # Team
    elif delete_option ==2:
        team_players.delete_team(Session)
    # Player
    elif delete_option ==3:
        player.delete_player(Session)
    # Stats
    elif delete_option ==4:
        player_stats.delete_stats(Session)
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
        show()
    # UPDATE
    elif option == 2:
        ui_text.update()
        update()
    # CREATE
    elif option == 3:
        ui_text.create()
        create()
    elif option == 4:
        ui_text.delete()
        delete()
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
    option = "demo"
    ui_text.clear_terminal()
    if option == "demo":
        while True:
            menu()
            if not break_or_continue():
                ui_text.run_version(sqlalchemy.__version__)
                break

    elif option == "ban":
        match_teams.show_match(Session)
        # match_teams.update_match(Session)
        # match_teams.create_match(Session)

        # team_players.show_teams(Session)
        # team_players.update_team(Session)
        # team_players.create_team(Session)

        # player.show_players(Session)
        # player.update_player(Session)
        # player.create_player(Session)

        # player_stats.show_stats(Session)
        # player_stats.update_stats(Session)
        # player_stats.create_stats(Session)