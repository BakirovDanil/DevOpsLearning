from sqlalchemy import text
from src.database.model import User_Token, Client_Event_Log


def get_all_tokens_and_user(session):
    """
    Функция, которая осуществляет получение списка токенов
    и привязанных пользователей
    """
    with open("C:\\Users\\002BakirovDT\\Desktop\\Script-1(User_with_Tokens).sql", "r") as f:  # получение кода скрипта
        sql_script = f.read()

    results = session.exec(text(sql_script)).all()
    tokens = [User_Token.model_validate({"Token_ID": result[0],
                                         "Full_Serial_Number": result[1],
                                         "User_ID": result[2],
                                         "Full_name": result[3],
                                         "User_name": result[4]
                                         }) for result in results]
    return tokens


def get_all_events(session):
    """
    Функция, которая осуществляет получение
    журнала событий из базы данных
    """
    with open("C:\\Users\\002BakirovDT\\Desktop\\Script(ClientEventLog).sql", "r") as f:  # получение кода скрипта
        sql_script = f.read()

    results = session.exec(text(sql_script)).all()
    events = [Client_Event_Log.model_validate({"Token_ID": result[0],
                                               "Full_Serial_Number": result[1],
                                               "User_ID": result[2],
                                               "Full_name": result[3],
                                               "User_name": result[4],
                                               "Date_Event": result[5]
                                               }) for result in results]
    return events