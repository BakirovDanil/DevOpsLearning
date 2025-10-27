from sqlmodel import Session, create_engine
from fastapi import Depends
from urllib import parse
from typing import Annotated

class Database:
    def __init__(self,
                 driver: str,
                 server: str,
                 database: str,
                 user: str,
                 password: str,
                 trust_cert: str = "yes"):
          connection_string = (f"DRIVER={driver};" \
                               f"SERVER={server};" \
                                f"DATABASE={database};" \
                                f"UID={user};" \
                                f"PWD={password};" \
                                f"TrustServerCertificate={trust_cert};")
          params = parse.quote_plus(connection_string)
          self.engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
          
    def get_session(self):
        with Session(self.engine) as session:
            yield session

db_instance = Database(
    driver = "ODBC Driver 18 for SQL Server",
    server = "10.2.0.69",
    database = "EAPDB_002_1",
    user = "SQLselect2",
    password = "GhL6deYX031201/" ,
)

SessionDep = Annotated[Session, Depends(db_instance.get_session)]