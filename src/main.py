from fastapi import FastAPI
import uvicorn
from requests.GET_REQUEST import get_request
from requests.GET_FORMS import get_forms_router


app = FastAPI(title = "Web for JMS",
              description = "API для получения информации с JMS")


app.include_router(get_request)
app.include_router(get_forms_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host = '0.0.0.0', reload=True, port=80)