import pytest
from models import Animal, Adopter, MedicalLog
from datetime import date
from pydantic import ValidationError


def test_create_valid_animal():
    animal = Animal(id=1, name="Max", species="Dog", age=3, vaccinated=True)
    assert animal.age == 3


def test_invalid_age():
    with pytest.raises(ValidationError):
        Animal(id=1, name="Max", species="Dog", age=-2, vaccinated=True)


def test_invalid_email():
    with pytest.raises(ValidationError):
        Adopter(id=1, name="John", email="wrong_email")
