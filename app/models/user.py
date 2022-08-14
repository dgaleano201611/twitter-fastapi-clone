#se van a definir los modelos para user.

from datetime import date
from typing import Optional
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class Person(BaseModel):
    person_id: int = Field(
        ...,
        gt=0,
        lt=1000000,
        example=123
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example= "Juan"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example= "Galeano"
    )
    email: EmailStr = Field(...)
    date_of_birth: Optional[date] = Field(default=None)


