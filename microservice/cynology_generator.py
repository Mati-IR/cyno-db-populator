from owner_generator import OwnerGenerator
from dog_generator import DogGenerator
from champion_generator import ChampionGenerator
import random

class CynologyGenerator:
    owners_data = []
    dogs_data = []
    championships_data = []

    def regenerate_data(self):
        self.owners_data = self.owner_generator.generate_owners()
        self.dogs_data = self.dog_generator.generate_dogs()
        self.championships_data = self.champion_generator.generate_championships()


#todo verify init
    def __init__(self, owners_number, dogs_number):
        self.owners_number = owners_number
        self.dogs_number = dogs_number
        self.owners_ids = [f"{random.randint(10000000000, 99999999999)}" for i in range(1, owners_number)]
        self.chip_numbers = [f"{random.randint(10000000, 99999999)}" for i in range(1, dogs_number)]
        self.dog_generator = DogGenerator(dogs_number, self.owners_ids)
        self.owner_generator = OwnerGenerator(owners_number)
        self.champion_generator = ChampionGenerator(self.chip_numbers)
        self.regenerate_data()

    def get_owners(self):
        return self.owners_data

    def get_dogs(self):
        return self.dogs_data

    def get_championships(self):
        return self.championships_data

