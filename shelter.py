from typing import List
from models import Animal, Adopter
from storage import StorageManager


class ShelterManager:
    def __init__(self):
        self.storage = StorageManager()
        self.animals, self.adopters = self.storage.load()

    # ---------- ANIMAL CRUD ----------

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        self.storage.save(self.animals, self.adopters)

    def remove_animal(self, animal_id: int):
        self.animals = [a for a in self.animals if a.id != animal_id]
        self.storage.save(self.animals, self.adopters)

    def get_animal(self, animal_id: int):
        return next((a for a in self.animals if a.id == animal_id), None)

    # ---------- ADOPTER CRUD ----------

    def add_adopter(self, adopter: Adopter):
        self.adopters.append(adopter)
        self.storage.save(self.animals, self.adopters)

    def adopt_animal(self, adopter_id: int, animal_id: int):
        adopter = next((a for a in self.adopters if a.id == adopter_id), None)
        animal = next((a for a in self.animals if a.id == animal_id), None)

        if adopter and animal:
            adopter.adopted_animal_id = animal_id
            self.storage.save(self.animals, self.adopters)
