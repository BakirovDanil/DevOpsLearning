from fastapi import APIRouter

get_request = APIRouter()

@get_request.get("/")
def hello_index() -> dict:
    return {
        "message": "hello"
    }

@get_request.get("/items/latest/")
def get_latest_item():
    return {
        "item": {
            "id": "0",
            "name": "latest"
        }
    }

@get_request.get("/items/")
def get_item_by_id(item_id: int = 0) -> dict:
    return {
        "Идентификатор объекта": item_id
    }