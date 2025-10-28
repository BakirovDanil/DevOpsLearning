from fastapi import APIRouter, Request
from src.function.functions import get_all_events
from src.database.db_connect import SessionDep
from fastapi.templating import Jinja2Templates


get_request = APIRouter()
templates = Jinja2Templates(directory = "templates")


@get_request.get("/", tags=["События"])
def get_events(session: SessionDep,
               request: Request):
    all_events = get_all_events(session)
    return templates.TemplateResponse(
        "tokens_with_users.html",
        context={'request': request,
                 "events": all_events}
    )


@get_request.get('/get_user_event', tags=["События"])
def get_user_event(session: SessionDep,
                   user_name: str,
                   request: Request):
    events = get_all_events(session)
    filtered_events = [
        user for user in events
        if user_name.lower() in user.Full_name.lower()
    ]
    return templates.TemplateResponse(
        "token_with_user.html",
        context={'request': request,
                 "events": filtered_events}
    )