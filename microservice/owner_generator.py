import json

import names
import random

class OwnerGenerator:
    owner_data = []

    # properties of object
    owners_number = 0
    owners_ids = []
    names = []
    surnames = []
    phone_numbers = []
    emails = []
    addresses = []
    #cities = [random.choice(cities) for i in range(1, owners_number)]
    zip_codes = []
    #countries = [random.choice(countries) for i in range(1, owners_number)]
    streets = ["Main Street", "High Street", "Park Avenue", "Broadway", "Wall Street", "Church Street", "Market Street"]
    adjectives = ["New", "Old", "Great", "Big", "Little", "High", "Long", "Wide", "Thick", "Deep", "Small", "Large", "Flat", "Green", "Blue", "Red", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White", "Bright", "Dark", "Shiny", "Glossy", "Dull", "Rough", "Smooth", "Soft", "Hard", "Cold", "Warm", "Wet", "Dry", "Clean", "Dirty", "Round", "Square", "Rectangular", "Triangular", "Diamond", "Curved", "Straight", "Sharp", "Blunt", "Heavy", "Light", "Strong", "Weak", "Healthy", "Ill", "Happy", "Sad", "Tall", "Short", "Fat", "Thin", "Narrow", "Wide", "Fragrant", "Smelly", "Noisy", "Quiet", "Loud", "Quiet", "Slow"]
    nouns = ["House", "Car", "Bike", "Tree", "Flower", "Grass", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field"]
    membership_types = ["Bronze", "Silver", "Gold"]

    def __init__(self, owners_number):
        self.owners_number = owners_number
        self.owners_ids = [f"{random.randint(10000000, 99999999)}" for i in range(owners_number)]
        self.names = [names.get_first_name() for i in range(owners_number)]
        self.surnames = [names.get_last_name() for i in range( owners_number)]
        self.phone_numbers = [f"{random.randint(100000000, 999999999)}" for i in range(owners_number)]
        self.zip_codes = [f"{random.randint(10000, 99999)}" for i in range(owners_number)]
        self.emails = [f"{self.names[i].lower()}.{self.surnames[i].lower()}@gmail.com" for i in range(owners_number)]
        self.addresses = [f"{random.randint(1, 100)} {random.choice(self.streets)}" for i in range(owners_number)]

    def generate_owners(self):
        for i in range(self.owners_number):
            owner = {"owner_id": self.owners_ids[i],
                     "name": self.names[i],
                     "surname": self.surnames[i],
                     "kennel name": f"{random.choice(self.adjectives)} {random.choice(self.nouns)}",
                     "membership status": random.choice(["active", "inactive"]),
                     "membership type": random.choice(self.membership_types),
                     "phone_number": self.phone_numbers[i],
                     "email": self.emails[i],
                     "address": self.addresses[i],
                     "zip_code": self.zip_codes[i]}
            self.owner_data.append(owner)
        json_data = json.dumps(self.owner_data)
        return self.owner_data

    def get_owners(self):
        return self.owner_data