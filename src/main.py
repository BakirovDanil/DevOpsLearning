from fastapi import FastAPI
import uvicorn
from requests.GET_REQUEST import get_request

app = FastAPI()
app.include_router(get_request)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=80)