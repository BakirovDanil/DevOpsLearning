from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

get_forms_router = APIRouter()
templates = Jinja2Templates(directory="templates/templates_forms")


@get_forms_router.get("/search_user_and_token_form")
async def get_search_form(request: Request):
    return templates.TemplateResponse(
        "search_user_form.html",
        context={"request": request}
    )