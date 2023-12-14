
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {
        "name" : "john",
        "age" : "17",
        "class" : "12"
    },
    2: {
        "name" : "abby",
        "age" : "17",
        "class" : "12"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None
    


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id] 

@app.get("/get-by-name")
def get_student(*,name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    
    return {"Data : Not available"}

@app.post("/create-student/{student_id}")
def create_students(student_id : int, student : Student):
    if student_id in students:
        return {"Error" : "Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student : UpdateStudent):
    if student_id not in students:
        return {"Error" : "STudent doesnt exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error" : "Student deleted successfully"}
    del students[student_id]
    return {"message: Deleted"}