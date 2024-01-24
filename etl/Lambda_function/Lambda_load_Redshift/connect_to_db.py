import psycopg2 as psy
import boto3
import json

ssm_client = boto3.client('ssm')

def get_ssm_param(param_name):
    print(f'get_ssm_param: getting param_name=${param_name}')
    parameter_details = ssm_client.get_parameter(Name=param_name)
    redshift_details = json.loads(parameter_details['Parameter']['Value'])

    host = 'host'
    user = redshift_details['user']
    db = redshift_details['database-name']
    print(f'get_ssm_param loaded for db=${db}, user=${user}, host=${host}')
    return redshift_details

def open_sql_database_connection_and_cursor():
    try:
        print('open_sql_database_connection_and_cursor - new connection starting...')
        db_connection = psy.connect(host='host',
                                    database='database',
                                    user='user',
                                    password='password',
                                    port='port')
        cursor = db_connection.cursor()
        print('open_sql_database_connection_and_cursor - connection ready')
        return db_connection, cursor
    except psy.Error as e:
    #except ConnectionError as e:
        print(f'open_sql_database_connection_and_cursor - failed to open connection:\n{e}')
        raise e
