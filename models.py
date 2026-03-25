from pydantic import BaseModel, field_validator, EmailStr
from datetime import date
from typing import Optional, List


class MedicalLog(BaseModel):
    visit_date: date
    description: str
    vaccinated: bool

    @field_validator("visit_date")
    def date_cannot_be_future(cls, value):
        if value > date.today():
            raise ValueError("Visit date cannot be in the future")
        return value


class Animal(BaseModel):
    id: int
    name: str
    species: str
    age: int
    vaccinated: bool
    medical_logs: List[MedicalLog] = []

    @field_validator("age")
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Age must be a positive integer")
        return value


class Adopter(BaseModel):
    id: int
    name: str
    email: EmailStr
    adopted_animal_id: Optional[int] = None

    @field_validator("name")
    def name_not_empty(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value
