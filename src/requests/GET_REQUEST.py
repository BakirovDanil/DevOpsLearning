from fastapi import APIRouter, Request
from src.function.functions import get_all_events
from src.database.db_connect import SessionDep
from fastapi.templating import Jinja2Templates


get_request = APIRouter()
templates = Jinja2Templates(directory = "templates")


@get_request.get("/")
def get_main_page(request: Request):
    return templates.TemplateResponse(
        "main_form.html",
        context={'request': request}
    )


@get_request.get("/all_users_and_events", tags=["События"])
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
        "tokens_with_users.html",
        context={'request': request,
                 "events": filtered_events}
    )


@get_request.get('/all_users_not_used_tokens', tags=["События"])
def get_user_not_used_token(session: SessionDep,
                            request: Request):
    users_not_used_token = [
        user for user in get_all_events(session)
        if user.Date_Event == "Последние два дня не использовался"
    ]
    return templates.TemplateResponse(
        "users_not_used_tokens.html",
        context={'request': request,
                 'users': users_not_used_token}
    )


@get_request.get('/get_users_not_used_tokens', tags=["События"])
def get_user_not_used_token(session: SessionDep,
                            user_name: str,
                            request: Request):
    users_not_used_token_by_username = [
        user for user in get_all_events(session)
        if (user.Date_Event == "Последние два дня не использовался" and user_name.lower() in user.Full_name.lower())
    ]
    return templates.TemplateResponse(
        "users_not_used_tokens.html",
        context={'request': request,
                 'users': users_not_used_token_by_username}
    )