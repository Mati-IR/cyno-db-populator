import random
import names
import json
class DogGenerator:
    dog_data = []

    owners_ids = []
    dogs_number = 0
    chip_numbers = []
    races = ["Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Boxer", "Chihuahua"]
    pedigree_numbers = {}
    branch_registration = {"Labrador Retriever": "LRCA", "German Shepherd": "GSDCA", "Golden Retriever": "GRCA",
                           "Bulldog": "BCA", "Boxer": "BXCA", "Chihuahua": "CCA"}
    colors = ["black", "white", "brown", "golden", "gray", "spotted"]
    litters = [f"L{i:02d}" for i in range(1, 6)]
    sex = ["M", "F"]
    dog_names = ["Bella", "Max", "Charlie", "Buddy", "Rocky", "Daisy", "Lucy", "Jack", "Toby", "Bailey", "Coco", "Lola", "Szarik", "Rex", "Luna", "Lucky", "Molly", "Sam", "Milo", "Oscar", "Teddy", "Lily", "Jasper", "Loki", "Lilly", "Duke", "Maggie", "Bentley", "Gus", "Frankie", "Harley", "Buster", "George", "Henry", "Rosie", "Zoe", "Ollie", "Archie", "Mia", "Cody", "Layla", "Riley", "Zoey", "Coco", "Lola", "Szarik", "Rex", "Luna", "Lucky", "Molly", "Sam", "Milo", "Oscar", "Teddy", "Lily", "Jasper", "Loki", "Lilly", "Duke", "Maggie", "Bentley", "Gus", "Frankie", "Harley", "Buster", "George", "Henry", "Rosie", "Zoe", "Ollie", "Archie", "Mia", "Cody", "Layla", "Riley", "Zoey", "Coco", "Lola", "Szarik", "Rex", "Luna", "Lucky", "Molly", "Sam", "Milo", "Oscar", "Teddy", "Lily", "Jasper", "Loki", "Lilly", "Duke", "Maggie", "Bentley", "Gus", "Frankie", "Harley", "Buster", "George", "Henry", "Rosie", "Zoe", "Ollie", "Archie", "Mia", "Cody", "Layla", "Riley", "Zoey", "Coco", "Lola", "Szarik", "Rex", "Luna", "Lucky", "Molly", "Sam", "Milo", "Oscar", "Teddy", "Lily", "Jasper", "Loki", "Lilly", "Duke", "Maggie", "Bentley", "Gus", "Frankie", "Harley", "Buster", "George", "Henry", "Rosie", "Zoe", "Ollie"]
    vaccinations_list = ["DHPP", "Rabies", "Bordetella", "Leptospirosis", "Lyme", "Parvovirus", "Rabies",
                         "Rhinotracheitis", "Distemper", "Parainfluenza", "Adenovirus", "Coronavirus", "Parvovirus",
                         "Canine Influenza", ]
    dog_treatments = [
        "Deworming",
        "Flea and tick prevention",
        "Heartworm prevention",
        "Spaying or neutering",
        "Dental cleaning",
        "Ear cleaning",
        "Eye drops or ointment",
        "Medications for allergies",
        "Pain relief medication",
        "Antibiotics",
        "Surgery",
        "Chemotherapy",
        "Radiation therapy",
        "Behavioral therapy",
        "Acupuncture",
        "Chiropractic adjustments",
        "Massage therapy",
        "Hydrotherapy",
        "Therapeutic exercise",
        "Nutritional supplements",
        "Prescription diet",
        "Training and socialization classes"
    ]

    def __init__(self, dogs_number, owners_ids):
        self.owners_ids = owners_ids
        self.dogs_number = dogs_number
        self.chip_numbers = [f"{random.randint(10000000, 99999999)}" for i in range(1, dogs_number)]
        self.pedigree_numbers = {"Labrador Retriever": [f"L{i:03d}" for i in range(1, dogs_number)],
                            "German Shepherd": [f"G{i:03d}" for i in range(1, dogs_number)],
                            "Golden Retriever": [f"GR{i:03d}" for i in range(1, dogs_number)],
                            "Bulldog": [f"B{i:03d}" for i in range(1, dogs_number)],
                            "Boxer": [f"BX{i:03d}" for i in range(1, dogs_number)],
                            "Chihuahua": [f"C{i:03d}" for i in range(1, dogs_number)]}

    def generate_dogs(self):
        for i in range(20):
            chip_number = random.choice(self.chip_numbers)
            race = random.choice(self.races)
            owner_id = random.choice(self.owners_ids)
            date_of_birth = f"{random.randint(2019, 2021)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            pedigree_number = random.choice(self.pedigree_numbers[race])
            branch_reg = self.branch_registration[race]
            color = random.choice(self.colors)
            litter = random.choice(self.litters)
            medical_history = {"vaccinations": {f"{random.choice(self.vaccinations_list)}": {
                "date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}",
                "given_by": f"Dr. {names.get_last_name()}"},
                                                f"{random.choice(self.vaccinations_list)}": {
                                                    "date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}",
                                                    "given_by": "Dr. Brown"}},
                               "treatments": [{"name": f"{random.choice(self.vaccinations_list)}",
                                               "date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}",
                                               "given_by": f"Dr. {names.get_last_name()}"},
                                              {"name": f"{random.choice(self.vaccinations_list)}",
                                               "date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}",
                                               "given_by": f"Dr. {names.get_last_name()}"}]}
            dog = {"chip_number": chip_number,
                   "race": race,
                   "sex": random.choice(self.sex),
                   "breeding": random.choice(self.dog_names),
                   "owner_id": owner_id,
                   "date_of_birth": date_of_birth,
                   "pedigree_number": pedigree_number,
                   "branch_reg": branch_reg,
                   "color": color,
                   "litter": litter,
                   "medical_history": medical_history}
            self.dog_data.append(dog)
        json_data = json.dumps(dog)
        return self.dog_data

    def get_dogs(self):
        return self.dog_data
