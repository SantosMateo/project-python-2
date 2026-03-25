import json
from pathlib import Path
from typing import List
from models import Animal, Adopter

DATA_FILE = Path("data/shelter.json")


class StorageManager:
    def save(self, animals: List[Animal], adopters: List[Adopter]):
        data = {
            "animals": [animal.model_dump() for animal in animals],
            "adopters": [adopter.model_dump() for adopter in adopters],
        }

        DATA_FILE.parent.mkdir(exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4, default=str)

    def load(self):
        if not DATA_FILE.exists():
            return [], []

        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        animals = [Animal(**a) for a in data.get("animals", [])]
        adopters = [Adopter(**a) for a in data.get("adopters", [])]

        return animals, adopters
