from shelter import ShelterManager
from models import Animal


def test_add_animal(monkeypatch):
    shelter = ShelterManager()

    initial_count = len(shelter.animals)

    animal = Animal(id=99, name="TestDog", species="Dog", age=2, vaccinated=True)
    shelter.add_animal(animal)

    assert len(shelter.animals) == initial_count + 1
