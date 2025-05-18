class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string.")
        self.name = name
        self._pets = []

    def pets(self):
        """Returns the full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner, if the pet is of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        
        if pet.owner is not None and pet.owner != self:
            raise Exception("This pet already has an owner.")
        
        
        if pet.owner is not None and pet.owner != self:
            pet.owner._pets.remove(pet)  
            
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str) or not isinstance(pet_type, str):
            raise Exception("Name and pet type must be strings.")
        
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            owner.add_pet(self)

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type})"
    

owner1 = Owner("John")
owner2 = Owner("Alice")


pet1 = Pet(name="Buddy", pet_type="dog")
pet2 = Pet(name="Fluffy", pet_type="cat", owner=owner1)
pet3 = Pet(name="Charlie", pet_type="bird", owner=owner2)


owner1.add_pet(pet1)

print(owner1.pets())  
print(owner1.get_sorted_pets())  
print(Pet.all)