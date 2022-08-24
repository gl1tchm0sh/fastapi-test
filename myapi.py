from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# uvicorn myapi:app --reload
app = FastAPI()

personas = {
    1: {
        "name" : "Hugo",
        "area" : "Sistemas"
    },
    2: {
        "name" : "Franco",
        "area" : "Sistemas"
    },
    3: {
        "name": "Lucas",
        "area": "Sistemas"
    }
}

class Persona(BaseModel):
    name: str
    area: str

class UpdatePersona(BaseModel):
    name: Optional[str] = None
    area: Optional[str] = None

@app.get("/")
async def index():
    return{"name": "First Data"}

@app.get("/get-user-data/{persona_id}")
async def get_persona(persona_id: int = Path(None, description="ID de persona que queres buscar", gt=0)):
    return personas[persona_id] if persona_id in personas else {"Data" : "Not found"}

@app.get("/get-by-name")
async def get_persona_name(name : Optional[str] = None):
    if name != None:
        for persona_id in personas:
            print(personas[persona_id])
            if personas[persona_id]["name"] == name:
                return personas[persona_id]
    return {"Data" : "Not found"}

@app.post("/create-persona/{persona_id}")
async def create_persona(persona_id : int, persona : Persona):
    if persona_id in personas:
        return {"Error":"ID ya registrado"}

    personas[persona_id] = dict(persona)
    return {"Data":f"Se creó el id {persona_id}"}

@app.delete("/delete-persona/{persona_id}")
async def delete_persona(persona_id : int):
    if persona_id not in personas:
        return {"Error" : "ID no encontrado"}

    del personas[persona_id]
    return {"Data" : f"Persona {persona_id} borrada"}


# @app.put("/update-student/{student_id}")
# def update_student(student_id:int, student: UpdateStudent):
#     if student_id not in students:
#         return {"Error" : "Student doesn't exist"}
#
#     if student.name != None:
#         students[student_id].name = student.name
#     if student.age != None:
#         students[student_id].age = student.age
#     if student.year != None:
#         students[student_id].year = student.year
#
#     return students[student_id]
