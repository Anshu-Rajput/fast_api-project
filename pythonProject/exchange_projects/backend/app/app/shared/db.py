import sqlalchemy
def return_connection():
    database_name="nex_exchange_test"
    username="nex_exchange_test"
    password="nvuojbyqkgi3hspmextw"
    server='192.3.12.162:1433'
    url=f"mssql+pymssql://{username}:{password}@{server}/{database_name}"
    engine=sqlalchemy.create_engine(url)
    connection=engine.raw_connection()
    return connection
