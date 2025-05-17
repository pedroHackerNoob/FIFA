# SQLAlchemy imports
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import Player as playerdb
from views import texts_menu as textm
# credenciales
user = "root"
password = "kali"
database = "cartas_deportivas"
port = "3306"
type_db = "mysql"
engine = create_engine(f'{type_db}+py{type_db}://{user}:{password}@localhost:{port}/{database}')

# Create table: utilizar una sola vez
def create_table():
    with engine.connect() as conn:
        conn.execute(textm('''
        CREATE DATABASE IF NOT EXISTS cartas_deportivas;
USE cartas_deportivas;

create table equipo
(
    idEquipo int auto_increment
        primary key,
    nombre   varchar(50) not null,
    pais     varchar(50) null
);

create table jugador
(
    idJugador int auto_increment
        primary key,
    nombre    varchar(50)                                                   not null,
    pais      varchar(50)                                                   null,
    deporte   varchar(30)                                                   null,
    posicion  varchar(30)                                                   null,
    rareza    enum ('Común', 'Rara', 'Épica', 'Legendaria') default 'Común' null,
    nivel     int                                           default 1       null,
    imagen    varchar(255)                                                  null,
    idEquipo  int                                                           null,
    constraint jugador_ibfk_1
        foreign key (idEquipo) references equipo (idEquipo)
            on delete set null
);

create table estadisticas
(
    idEstadistica int auto_increment
        primary key,
    idJugador     int  null,
    velocidad     int  null,
    fuerza        int  null,
    tecnica       int  null,
    resistencia   int  null,
    inteligencia  int  null,
    habilidades   text null,
    constraint estadisticas_ibfk_1
        foreign key (idJugador) references jugador (idJugador)
            on delete cascade
);

create index idJugador
    on estadisticas (idJugador);

create index idEquipo
    on jugador (idEquipo);

create table partido
(
    idPartido int auto_increment
        primary key,
    fecha     date         null,
    lugar     varchar(100) null,
    idEquipo1 int          null,
    idEquipo2 int          null,
    constraint partido_ibfk_1
        foreign key (idEquipo1) references equipo (idEquipo),
    constraint partido_ibfk_2
        foreign key (idEquipo2) references equipo (idEquipo)
);

create index idEquipo1
    on partido (idEquipo1);

create index idEquipo2
    on partido (idEquipo2);

        '''))
    conn.commit()

# test de conexion
def run_version():
    # with engine.connect() as conn:
    #     print(query_result)  # Print or process the query result
    var = sqlalchemy.__version__
    print(f'version SQALchemy: {var}')
def menu():
    textm.texts_menu()
    option = 1

    match option:
        case 0:
            # create_table()
            print("xd")
        case 1:
            playerdb.info_players(engine, database, text)  # Removed text parameter


    run_version()
menu()