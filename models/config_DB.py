# SQLAlchemy imports
from sqlalchemy import create_engine
from sqlalchemy import text
# credenciales
user = "root"
password = "kali"
database = "cartas_deportivas"
port = "3306"
type_db = "mysql"
#     conectar base de datos
def conection_db():
    print(f'conectando a la base de datos {database}')
    engine = create_engine(f'{type_db}+py{type_db}://{user}:{password}@localhost:{port}/{database}')

    with engine.connect() as conn:
        result = conn.execute(text("select * FROM jugador"))
        # print in row
        for row in result:
            print(row)
        # print(result.all())


# test
def test():
    import sqlalchemy

    var = sqlalchemy.__version__
    print(f'version SQALCHEMY: {var}')

conection_db()