from fastapi import APIRouter
from src.database.model import User_Token, Client_Event_Log
from src.function.functions import get_all_tokens_and_user, get_all_events
from src.database.db_connect import SessionDep


get_request = APIRouter()


@get_request.get("/all_tokens_and_users", tags=["Ключи и пользователи"])
async def get_all_entries(session: SessionDep) -> list[User_Token]:
    return get_all_tokens_and_user(session)


@get_request.get("/token_and_user", tags=["Ключи и пользователи"])
def get_user_entry(session: SessionDep,
                   user_name: str) -> list[User_Token]:
    tokens = get_all_tokens_and_user(session)
    filtered_tokens = [
        token for token in tokens
        if user_name.lower() in token.Full_name.lower()
    ]
    return filtered_tokens


@get_request.get("/all_events", tags=["События"])
def get_events(session: SessionDep) -> list[Client_Event_Log]:
    return get_all_events(session)


@get_request.get('/user_event', tags=["События"])
def get_user_event(session: SessionDep,
                   user_name: str) -> list[Client_Event_Log]:
    events = get_all_events(session)
    filtered_events = [
        user for user in events
        if user_name.lower() in user.Full_name.lower()
    ]
    return filtered_events