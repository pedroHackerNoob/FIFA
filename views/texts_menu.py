from models.config_DB import console_r
# banner
def fifa_lxs():
    console_r.rule(characters="-",style="bright_white")
    console_r.print('''[bright_white] 
FFFFFFFFFFFFFFFFFFFFFFIIIIIIIIIIFFFFFFFFFFFFFFFFFFFFFF      AAA               
F::::::::::::::::::::FI::::::::IF::::::::::::::::::::F     A:::A              
F::::::::::::::::::::FI::::::::IF::::::::::::::::::::F    A:::::A             
FF::::::FFFFFFFFF::::FII::::::IIFF::::::FFFFFFFFF::::F   A:::::::A            
  F:::::F       FFFFFF  I::::I    F:::::F       FFFFFF  A:::::::::A           
  F:::::F               I::::I    F:::::F              A:::::A:::::A          
  F::::::FFFFFFFFFF     I::::I    F::::::FFFFFFFFFF   A:::::A A:::::A         
  F:::::::::::::::F     I::::I    F:::::::::::::::F  A:::::A   A:::::A        
  F:::::::::::::::F     I::::I    F:::::::::::::::F A:::::A     A:::::A       
  F::::::FFFFFFFFFF     I::::I    F::::::FFFFFFFFFFA:::::AAAAAAAAA:::::A      
  F:::::F               I::::I    F:::::F         A:::::::::::::::::::::A     
  F:::::F               I::::I    F:::::F        A:::::AAAAAAAAAAAAA:::::A    
FF:::::::FF           II::::::IIFF:::::::FF     A:::::A             A:::::A   
F::::::::FF           I::::::::IF::::::::FF    A:::::A               A:::::A  
F::::::::FF           I::::::::IF::::::::FF   A:::::A                 A:::::A 
FFFFFFFFFFF           IIIIIIIIIIFFFFFFFFFFF  AAAAAAA                   AAAAAAA
                        ''')
    console_r.print(" Fédération Internationale de Football Association")
    console_r.rule(characters="-",style="bright_white")

# home
def texts_menu():
    console_r.log("Home", style="bold magenta")
    console_r.rule("[bold magenta]Home[/bold magenta]", characters="=")
    console_r.print("|\n|\t[1] [dodger_blue2]SHOW[/dodger_blue2] \n|\t[2] [bright_yellow]UPDATE[/bright_yellow] \n|\t[3] [bright_magenta]CREATE[/bright_magenta]\n|\t[4] Exit\n|\n| Ingrese una opcion:")
# SHOW
def show():
    console_r.log("SHOW", style="dodger_blue2")
    console_r.rule("[dodger_blue2]SHOW",characters="=")
    console_r.print("|\n"
                    "|\t[1] [dodger_blue2] SHOW[/dodger_blue2] MATCHES\n"
                    "|\t[2] [dodger_blue2] SHOW[/dodger_blue2] TEAMS\n"
                    "|\t[3] [dodger_blue2] SHOW[/dodger_blue2] PLAYERS\n"
                    "|\t[4] [dodger_blue2] SHOW[/dodger_blue2] PLAYERS STATS\n"
                    "|\n| Please enter your option:")
# UPDATE
def update():
    console_r.log("UPDATE", style="bright_yellow")
    console_r.rule("[bright_yellow]UPDATE",characters="=")# SHOW
    console_r.print("|\n"
                    "|\t[1] [bright_yellow] UPDATE [/bright_yellow] MATCHES\n"
                    "|\t[2] [bright_yellow] UPDATE [/bright_yellow] TEAMS\n"
                    "|\t[3] [bright_yellow] UPDATE [/bright_yellow] PLAYERS\n"
                    "|\t[4] [bright_yellow] UPDATE [/bright_yellow] PLAYERS STATS\n|\n| Please enter your option:")
# CREATE
def create():
    console_r.log("CREATE", style="bright_magenta")
    console_r.rule("[bright_magenta]CREATE",characters="=")
    console_r.print("|\n"
                    "|\t[1] [bright_magenta] CREATE[/bright_magenta] MATCHES\n"
                    "|\t[2] [bright_magenta] CREATE[/bright_magenta] TEAMS\n"
                    "|\t[3] [bright_magenta] CREATE[/bright_magenta] PLAYERS\n"
                    "|\t[4] [bright_magenta] CREATE[/bright_magenta] PLAYERS STATS\n|\n| Please enter your option:")
#version
def run_version(var):
    console_r.rule(f"[bold red]version SQLAlchemy: {var}", align="center")