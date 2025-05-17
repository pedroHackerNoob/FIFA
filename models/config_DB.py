# SQLAlchemy imports
from sqlalchemy import create_engine
from sqlalchemy import text
# credenciales
user = "root"
password = "kali"
database = "cartas_deportivas"
port = "3306"
type_db = "mysql"
engine = create_engine(f'{type_db}+py{type_db}://{user}:{password}@localhost:{port}/{database}')

#     conectar base de datos
def conection_db():
    print(f'\nConectando a la base de datos: {database}\n')

    with engine.connect() as conn:
        result = conn.execute(text("select * FROM jugador"))
        # print in row
        print("-------------------------------------------------------------------------")
        print("id | nombre | pais | deporte | posicion |  rareza      | nivel | equipo ")
        print("-------------------------------------------------------------------------")
        for row in result:
            print(row)
        print("-------------------------------------------------------------------------")
        # print(result.all()) print all results in file

def test():
    import sqlalchemy

    var = sqlalchemy.__version__
    print(f'version SQALCHEMY: {var}')
# conection_db()
test()