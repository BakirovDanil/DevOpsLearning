from fastapi import FastAPI
import uvicorn
from requests.GET_REQUEST import get_request
from fastapi.staticfiles import StaticFiles


app = FastAPI(title = "Web for JMS",
              description = "API для получения информации с JMS")


app.include_router(get_request)
app.mount("/static", StaticFiles(directory="templates"), 'static')


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=80)