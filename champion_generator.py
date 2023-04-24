import random
import json
import names

class ChampionGenerator:
    championships = ["Bronze Grand Champion", "Silver Grand Champion", "Gold Grand Champion"]

    def __init__(self, chip_numbers):
        self.chip_numbers = chip_numbers

    def get_championships(self):
        championships_data = []
        for i in range(20):
            dog_id = random.choice(self.chip_numbers)
            championship = random.choice(self.championships)
            date = f"{random.randint(2019, 2021)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            judge = f"Judge {names.get_last_name()}"
            championship_data = {"dog_chip_number": dog_id,
                                 "championship_id": random.randint(100000, 999999),
                                 "championship": championship,
                                 "date": date,
                                 "judge": judge}
            championships_data.append(championship_data)
        return championships_data