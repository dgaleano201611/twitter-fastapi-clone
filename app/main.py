#python
from typing import Optional

#pydantic

#fastapi
from fastapi import FastAPI
from fastapi import Body, Query
from config import get_settings, Settings
from fastapi import Depends

#mis clases
from models.user import Person



app = FastAPI()


@app.get("/")
async def home(settings: Settings = Depends(get_settings)):
    return {
        "Hello": "World",
        "environment": settings.environment,
        "testing": settings.testing
    }

#users

#endpoint que crea una persona. se usa el metodo http post ya que se desea enviar los datos de la 
#persona. se debe hacer la peticion por medio de un request body -> es un modelo. 
@app.post("/person/new")
async def create_person(person: Person = Body(...)):
    return person

#endpoint que muestra en detalle un usuario, se usa el metodo http get ya que se desea traer 
# algunos datos de la persona. esto se hace por medio de un query parameter
@app.get("/person/detail")
async def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1,
        max_length=50,
        title="Person name",
        description="This is the person name, It is between 1 to 50 characters",
        example="Juan"
    ),
    age: Optional[int] = Query(
        None,
        gt=17,
        lt=100,
        title="Age",
        description="This is the age. It's mayor 17",
        example=18

    )
):
    return {name: age}

