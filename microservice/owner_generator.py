import json

import names
import random

class OwnerGenerator:
    owner_data = []
    dogs_of_owner = []

    dogs_ids = []
    owners_number = 0
    owners_ids = []
    names = []
    surnames = []
    phone_numbers = []
    emails = []
    addresses = []
    cities = ["Washington", "New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Indianapolis", "Columbus", "Fort Worth", "Charlotte", "Detroit", "El Paso", "Memphis", "Boston", "Seattle", "Denver", "Nashville", "Baltimore", "Oklahoma City", "Louisville", "Portland", "Las Vegas", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa", "Atlanta", "Colorado Springs", "Virginia Beach", "Raleigh", "Omaha", "Miami", "Oakland", "Minneapolis", "Tulsa", "Cleveland", "Wichita", "Arlington", "New Orleans", "Bakersfield", "Tampa", "Honolulu", "Aurora", "Anaheim", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi", "Pittsburgh", "Lexington", "Anchorage", "Stockton", "Cincinnati", "St. Paul", "Toledo", "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Buffalo", "Jersey City", "Chula Vista", "Fort Wayne", "Orlando", "St. Petersburg", "Chandler", "Laredo", "Norfolk", "Durham", "Madison", "Lubbock", "Irvine", "Winston–Salem", "Glendale", "Garland", "Hialeah", "Reno", "Chesapeake", "Gilbert", "Baton Rouge", "Irving", "Scottsdale", "North Las Vegas", "Fremont", "Boise", "Richmond", "San Bernardino", "Birmingham", "Spokane", "Rochester", "Des Moines", "Modesto", "Fayetteville", "Tacoma", "Oxnard", "Fontana", "Columbus", "Montgomery", "Moreno Valley", "Shreveport", "Aurora", "Yonkers", "Akron", "Huntington Beach", "Little Rock", "Augusta",]
    zip_codes = []
    #countries = [random.choice(countries) for i in range(1, owners_number)]
    streets = ["Main Street", "High Street", "Park Avenue", "Broadway", "Wall Street", "Church Street", "Market Street"]
    adjectives = ["New", "Old", "Great", "Big", "Little", "High", "Long", "Wide", "Thick", "Deep", "Small", "Large", "Flat", "Green", "Blue", "Red", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White", "Bright", "Dark", "Shiny", "Glossy", "Dull", "Rough", "Smooth", "Soft", "Hard", "Cold", "Warm", "Wet", "Dry", "Clean", "Dirty", "Round", "Square", "Rectangular", "Triangular", "Diamond", "Curved", "Straight", "Sharp", "Blunt", "Heavy", "Light", "Strong", "Weak", "Healthy", "Ill", "Happy", "Sad", "Tall", "Short", "Fat", "Thin", "Narrow", "Wide", "Fragrant", "Smelly", "Noisy", "Quiet", "Loud", "Quiet", "Slow", "Sneaky", "Accurate", "Fluffy", "Fuzzy", "Rough", "Smooth", "Soft", "Hard", "Cold", "Warm", "Wet", "Dry", "Clean", "Dirty", "Round", "Square", "Rectangular", "Triangular", "Diamond", "Curved", "Straight", "Sharp", "Blunt", "Heavy", "Light", "Strong", "Weak", "Healthy", "Ill", "Happy", "Sad", "Tall", "Short", "Fat", "Thin", "Narrow", "Wide", "Fragrant", "Smelly", "Noisy", "Quiet", "Loud", "Quiet", "Slow", "Sneaky", "Accurate", "Fluffy", "Fuzzy", "Rough", "Smooth", "Soft", "Hard", "Cold", "Warm", "Wet", "Dry", "Clean", "Dirty", "Round", "Square", "Rectangular", "Triangular", "Diamond", "Curved", "Straight", "Sharp", "Blunt", "Heavy", "Light", "Strong", "Weak", "Healthy", "Ill", "Happy", "Sad", "Tall", "Short", "Fat", "Thin", "Narrow", "Wide", "Fragrant", "Smelly", "Noisy", "Quiet", "Loud", "Quiet", "Slow", "Sneaky", "Accurate", "Fluffy", "Round", "Square", "Rectangular", "Triangular"]
    nouns = ["House", "Car", "Bike", "Tree", "Flower", "Grass", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field", "Lake", "River", "Ocean", "Sky", "Mountain", "Valley", "Road", "Bridge", "Building", "School", "Hospital", "Park", "Museum", "Library", "Shop", "Restaurant", "Cafe", "Bar", "Pub", "Hotel", "Office", "Factory", "Warehouse", "Farm", "Garden", "Field"]
    membership_types = ["Bronze", "Silver", "Gold"]

    def __init__(self, owners_number, dogs_ids, owners_ids, dogs_of_owner):
        self.owners_number = owners_number
        self.owners_ids = owners_ids
        self.names = [names.get_first_name() for i in range(owners_number)]
        self.surnames = [names.get_last_name() for i in range( owners_number)]
        self.phone_numbers = [f"{random.randint(100000000, 999999999)}" for i in range(owners_number)]
        self.zip_codes = [f"{random.randint(10000, 99999)}" for i in range(owners_number)]
        self.emails = [f"{self.names[i].lower()}.{self.surnames[i].lower()}@gmail.com" for i in range(owners_number)]
        self.addresses = [f"{random.randint(1, 100)} {random.choice(self.streets)}" for i in range(owners_number)]
        self.dogs_ids = dogs_ids
        self.dogs_of_owner = dogs_of_owner

    def generate_owners(self):
        print("Generating owners data...")
        for i in range(self.owners_number):
            doggos = str(self.dogs_of_owner[self.owners_ids[i]])
            owner = {"owner_id": self.owners_ids[i],
                     "name": self.names[i],
                     "surname": self.surnames[i],
                     "breeding_nickname": f"{random.choice(self.adjectives)} {random.choice(self.nouns)}",
                     "membership_status": random.choice(["active", "inactive"]),
                     "membership_type": random.choice(self.membership_types),
                     "phone_number": self.phone_numbers[i],
                     "email": self.emails[i],
                     "city": self.cities[i],
                     "address": self.addresses[i],
                     "zip_code": self.zip_codes[i],
                     "dogs": doggos
            }
            self.owner_data.append(owner)
        json_data = json.dumps(self.owner_data)
        return self.owner_data

    def get_owners(self):
        return self.owner_data

