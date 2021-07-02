import psycopg2 as psycopg2
import mysql.connector
import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

MYSQL_ENGINE = 'mysql'
PGSQL_ENGINE = 'pgsql'

app_port: str = os.getenv('APP_PORT') or 6543
db_engine: str = os.getenv('DB_ENGINE') or PGSQL_ENGINE

db_host: str = os.getenv('DB_HOST') or '127.0.0.1'
db_port: str = os.getenv('DB_PORT') or 5432

db_name: str = os.getenv('DB_NAME')
db_username: str = os.getenv('DB_USERNAME')
db_password: str = os.getenv('DB_PASSWORD')


def validate_configuration():
    if db_name is None:
        raise Exception('{} is not define.'.format('db_name'))

    if db_username is None:
        raise Exception('{} is not define.'.format('db_username'))

    if db_password is None:
        raise Exception('{} is not define.'.format('db_password'))


def get_db_connect(db_engine, db_host, db_port, db_username, db_password, db_name):
    if db_engine == MYSQL_ENGINE:
        return mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_username,
            password=db_password,
            database=db_name
        )
    else:
        return psycopg2.connect(
            host=db_host,
            port=db_port,
            user=db_username,
            password=db_password,
            dbname=db_name
        )


def get_query(db_engine):
    if db_engine == MYSQL_ENGINE:
        return "Show tables;"
    else:
        return "SELECT table_name FROM information_schema.tablesWHERE table_schema = 'public'"


@view_config(
    route_name='get_tables',
    renderer='json'
)
def get_tables(request):
    try:
        validate_configuration()
        connect = get_db_connect(db_engine, db_host, db_port, db_username, db_password, db_name)

        query = get_query(db_engine)

        cursor = connect.cursor()
        cursor.execute(query)

        return cursor.fetchall()
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('get_tables', '/')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('127.0.0.1', int(app_port), app)
    server.serve_forever()
