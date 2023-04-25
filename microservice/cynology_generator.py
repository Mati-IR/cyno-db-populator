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
        self.dog_generator.generate_dogs(self.owners_data)
        self.dogs_data = self.dog_generator.kill_stray_dogs()
        self.championships_data = self.champion_generator.generate_championships()


    def __init__(self, owners_number, dogs_number):
        self.owners_number = owners_number
        self.dogs_number = dogs_number
        self.owners_ids = [f"{random.randint(10000000000, 99999999999)}" for i in range(owners_number)]
        self.dogs_ids = [f"{random.randint(10000000, 99999999)}" for i in range(dogs_number)]
        # assign 1 to 3 dogs to each owner
        self.dogs_of_owners = {owner_id: random.sample(self.dogs_ids, random.randint(1, 3)) for owner_id in self.owners_ids}
        self.dog_generator = DogGenerator(dogs_number, self.dogs_ids, self.owners_ids)
        self.owner_generator = OwnerGenerator(owners_number,self.dogs_ids, self.owners_ids, self.dogs_of_owners)
        self.champion_generator = ChampionGenerator(self.dogs_ids)
        self.regenerate_data()

    def get_owners(self):
        return self.owners_data

    def get_dogs(self):
        return self.dogs_data

    def get_championships(self):
        return self.championships_data

