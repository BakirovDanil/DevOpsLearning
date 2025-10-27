from typing import Annotated
from pydantic import BaseModel, ConfigDict, field_validator, Field


class User_Token(BaseModel):
    Token_ID: Annotated[str, Field()]
    Full_Serial_Number: Annotated[str, Field()]
    User_ID: Annotated[int, Field()]
    Full_name: Annotated[str, Field()]
    User_name: Annotated[str, Field()]

    model_config = ConfigDict(from_attributes=True)  # настройка для работы с данными полученными из БД


class Client_Event_Log(User_Token):
    Date_Event: Annotated[str, Field(default = "Последние два дня не использовался")]

    @field_validator("Date_Event", mode = 'before')
    def validate_date(cls, v):
        """
        Функция, которая проверяет, что полученное значение
        не является None
        """
        if v is None:
            return cls.model_fields["Date_Event"].get_default()
        return str(v)
