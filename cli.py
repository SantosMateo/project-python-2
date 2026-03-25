from shelter import ShelterManager
from models import Animal, Adopter


def main():
    shelter = ShelterManager()

    while True:
        print("\n--- Animal Shelter Manager ---")
        print("1. Add Animal")
        print("2. View Animals")
        print("3. Add Adopter")
        print("4. Adopt Animal")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            animal = Animal(
                id=int(input("ID: ")),
                name=input("Name: "),
                species=input("Species: "),
                age=int(input("Age: ")),
                vaccinated=input("Vaccinated (yes/no): ").lower() == "yes",
            )
            shelter.add_animal(animal)

        elif choice == "2":
            for a in shelter.animals:
                print(a)

        elif choice == "3":
            adopter = Adopter(
                id=int(input("ID: ")),
                name=input("Name: "),
                email=input("Email: ")
            )
            shelter.add_adopter(adopter)

        elif choice == "4":
            adopter_id = int(input("Adopter ID: "))
            animal_id = int(input("Animal ID: "))
            shelter.adopt_animal(adopter_id, animal_id)

        elif choice == "5":
            break


if __name__ == "__main__":
    main()
