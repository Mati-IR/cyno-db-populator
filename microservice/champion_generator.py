import random
import json
import names

class ChampionGenerator:
    championships_data = []

    championships_types = ["Bronze Grand Champion", "Silver Grand Champion", "Gold Grand Champion"]

    def __init__(self, dogs_ids):
        self.dogs_ids = dogs_ids

    def generate_championships(self):
        print("Generating championships...")
        for i in range(int(len(self.dogs_ids) * 2)):
            dog_id = random.choice(self.dogs_ids)
            championship = random.choice(self.championships_types)
            date = f"{random.randint(2019, 2021)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            judge = f"Judge {names.get_last_name()}"
            championship_data = {"dog_id": dog_id,
                                 "championship_id": random.randint(100000, 999999),
                                 "championship": championship,
                                 "date": date,
                                 "judge": judge}
            self.championships_data.append(championship_data)
        return self.championships_data

    def get_championships(self):
        return self.championships_data
