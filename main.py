import random
import json
import string
import names


# Helper function to generate random phone numbers
def generate_phone_number():
    return "+1" + "".join(random.choices(string.digits, k=10))

# List of possible membership types
membership_types = ["Bronze", "Silver", "Gold"]

# List of possible cynology institute branches
branches = ["New York Cynology Institute", "Los Angeles Cynology Institute", "Chicago Cynology Institute"]

payment_titles = ["Membership fee", "Vaccination", "Treatment", "Other"]

owners_ids = []
# Generate 10 dog owner records and print them to the console
for i in range(10):
    # Generate random owner information
    name = names.get_first_name()
    surname = names.get_last_name()
    phone = generate_phone_number()
    email = name.lower() + "." + surname.lower() + "@gmail.com"
    membership_status = random.choice([True, False])
    membership_type = random.choice(membership_types)
    branch = random.choice(branches)
    payment_history = [{"date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}", "amount": random.randint(50, 200), "title": f"{random.choice(payment_titles)}"},
                       {"date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}", "amount": random.randint(50, 200), "title": f"{random.choice(payment_titles)}"},
                       {"date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}", "amount": random.randint(50, 200), "title": f"{random.choice(payment_titles)}"}]
    # Construct dictionary with owner information
    owners_ids.append(f"{random.randint(1000, 9999)}")
    owner_info = {
        "name": name + " " + surname,
        "owner_id" : f"{owners_ids[i]}",
        "phone": phone,
        "email": email,
        "membership_status": membership_status,
        "membership_type": membership_type,
        "branch": branch,
        "payment_history": payment_history
    }
    # Print owner information as a string
    #print(str(owner_info))






chip_numbers = [f"{random.randint(10000000, 99999999)}" for i in range(1, 21)]
races = ["Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Boxer", "Chihuahua"]
breeding_nickname = ["Max", "Buddy", "Rocky", "Charlie", "Cooper", "Daisy"]
pedigree_numbers = {"Labrador Retriever": [f"L{i:03d}" for i in range(1, 21)],
                    "German Shepherd": [f"G{i:03d}" for i in range(1, 21)],
                    "Golden Retriever": [f"GR{i:03d}" for i in range(1, 21)],
                    "Bulldog": [f"B{i:03d}" for i in range(1, 21)],
                    "Boxer": [f"BX{i:03d}" for i in range(1, 21)],
                    "Chihuahua": [f"C{i:03d}" for i in range(1, 21)]}
branch_registration = {"Labrador Retriever": "LRCA", "German Shepherd": "GSDCA", "Golden Retriever": "GRCA",
                        "Bulldog": "BCA", "Boxer": "BXCA", "Chihuahua": "CCA"}
colors = ["black", "white", "brown", "golden", "gray", "spotted"]
litters = [f"L{i:02d}" for i in range(1, 6)]
vaccinations_list = ["DHPP", "Rabies", "Bordetella", "Leptospirosis", "Lyme", "Parvovirus", "Rabies", "Rhinotracheitis", "Distemper", "Parainfluenza", "Adenovirus", "Coronavirus", "Parvovirus", "Canine Influenza",]
treatments_list = ["Flea medication", "Deworming", "Antibiotics", "Antifungal", "Antiparasitic", "Antiseptic", "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic", "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic", "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic", "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic", "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic", "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic", "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic", "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic", "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic", "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic", "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic", "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic", "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic", "Antidiarrheal", "Antispasmodic"]

dog_data = []
for i in range(20):
    chip_number = random.choice(chip_numbers)
    race = random.choice(races)
    breeding = random.choice(breeding_nickname)
    owner_id = random.choice(owners_ids)
    dob = f"{random.randint(2019, 2021)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    pedigree_number = random.choice(pedigree_numbers[race])
    branch_reg = branch_registration[race]
    color = random.choice(colors)
    litter = random.choice(litters)
    medical_history = {"vaccinations": {f"{random.choice(vaccinations_list)}": {"date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}", "given_by": f"Dr. {names.get_last_name()}"},
                                        f"{random.choice(vaccinations_list)}": {"date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}", "given_by": "Dr. Brown"}},
                        "treatments": [{"name": f"{random.choice(vaccinations_list)}", "date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}", "given_by": f"Dr. {names.get_last_name()}"},
                                       {"name": f"{random.choice(vaccinations_list)}", "date": f"{random.randint(2022, 2023)}-{random.randint(1, 12)}-{random.randint(1, 27)}", "given_by": f"Dr. {names.get_last_name()}"}]}
    dog = {"chip_number": chip_number,
            "race": race,
            "breeding": breeding,
            "owner_id": owner_id,
            "dob": dob,
            "pedigree_number": pedigree_number,
            "branch_reg": branch_reg,
            "color": color,
            "litter": litter,
            "medical_history": medical_history}
    dog_data.append(dog)
    json_data = json.dumps(dog)
    #print(json_data)

# Generate information about dog's championship
championships = ["Champion", "Grand Champion", "Bronze Grand Champion", "Silver Grand Champion", "Gold Grand Champion"]
championships_data = []
for i in range(20):
    dog_id = random.choice(chip_numbers)
    championship = random.choice(championships)
    date = f"{random.randint(2019, 2021)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    judge = f"Judge {names.get_last_name()}"
    championship_data = {"dog_chip_number": dog_id,
                         "championship_id": random.randint(100000, 999999),
                        "championship": championship,
                        "date": date,
                        "judge": judge}
    championships_data.append(championship_data)
    json_data = json.dumps(championship_data)
    #print(json_data)

# Generate information about dogs breeding (place where dogs are bred)
kettle_names = ["Kettle 1", "Kettle 2", "Kettle 3", "Kettle 4", "Kettle 5", "Kettle 6", "Kettle 7", "Kettle 8", "Kettle 9", "Kettle 10"]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Indianapolis", "Columbus", "Fort Worth", "Charlotte", "Detroit", "El Paso", "Memphis", "Boston", "Seattle", "Denver", "Nashville", "Baltimore", "Oklahoma City", "Louisville", "Portland", "Las Vegas", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa", "Atlanta", "Colorado Springs", "Virginia Beach", "Raleigh", "Omaha", "Miami", "Oakland", "Minneapolis", "Tulsa", "Cleveland", "Wichita", "New Orleans", "Arlington", "Bakersfield", "Tampa", "Honolulu", "Aurora", "Anaheim", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi", "Pittsburgh", "Anchorage", "Stockton", "Cincinnati", "St. Paul", "Toledo", "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Buffalo", "Jersey City", "Chula Vista", "Fort Wayne", "Orlando", "St. Petersburg", "Chandler", "Laredo", "Norfolk", "Durham", "Madison", "Lubbock", "Irvine", "Winston-Salem", "Glendale", "Garland", "Hialeah", "Reno", "Chesapeake", "Gilbert", "Baton Rouge", "Irving", "Scottsdale", "North Las Vegas", "Fremont", "Boise City", "Richmond", "San Bernardino", "Birmingham", "Spokane", "Rochester", "Des Moines", "Modesto", "Fayetteville", "Tacoma", "Oxnard", "Fontana", "Columbus", "Montgomery", "Moreno Valley", "Shreveport", "Aurora", "Yonkers", "Akron", "Huntington Beach", "Little Rock", "Augusta", "Amarillo"]
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


breeding_data = []
for i in range(20):
    name = random.choice(kettle_names)
    address = f"{random.randint(1, 999)} {names.get_last_name()} Street"
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    breeding_data.append({"breeding": breeding,
                          "breeding_id": random.randint(100000, 999999),
                          "address": address,
                          "city": city,
                          "state": state,
                          "zip_code": zip_code})
    json_data = json.dumps({"breeding": breeding,
                          "address": address,
                          "city": city,
                          "state": state,
                          "zip_code": zip_code})
    #print(json_data)




class Dog_generator:
    dogs_number = 0
    chip_numbers = []
    races = ["Labrador Retriever", "German Shepherd", "Golden Retriever", "Bulldog", "Boxer", "Chihuahua"]
    breeding_nickname = ["Max", "Buddy", "Rocky", "Charlie", "Cooper", "Daisy"]
    pedigree_numbers = {}
    branch_registration = {"Labrador Retriever": "LRCA", "German Shepherd": "GSDCA", "Golden Retriever": "GRCA",
                           "Bulldog": "BCA", "Boxer": "BXCA", "Chihuahua": "CCA"}
    colors = ["black", "white", "brown", "golden", "gray", "spotted"]
    litters = [f"L{i:02d}" for i in range(1, 6)]
    vaccinations_list = ["DHPP", "Rabies", "Bordetella", "Leptospirosis", "Lyme", "Parvovirus", "Rabies",
                         "Rhinotracheitis", "Distemper", "Parainfluenza", "Adenovirus", "Coronavirus", "Parvovirus",
                         "Canine Influenza", ]
    treatments_list = ["Flea medication", "Deworming", "Antibiotics", "Antifungal", "Antiparasitic", "Antiseptic",
                       "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic",
                       "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic",
                       "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic",
                       "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic",
                       "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic",
                       "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic",
                       "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic",
                       "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic",
                       "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic",
                       "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic",
                       "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic",
                       "Antidiarrheal", "Antispasmodic", "Antibacterial", "Antifungal", "Antiparasitic", "Antiseptic",
                       "Antiviral", "Antihistamine", "Antipruritic", "Antipyretic", "Anticoagulant", "Antiemetic",
                       "Antidiarrheal", "Antispasmodic"]

    def __init__(self, dogs_number):
        self.dogs_number = dogs_number
        self.chip_numbers = [f"{random.randint(10000000, 99999999)}" for i in range(1, dogs_number)]
        self.pedigree_numbers = {"Labrador Retriever": [f"L{i:03d}" for i in range(1, dogs_number)],
                            "German Shepherd": [f"G{i:03d}" for i in range(1, dogs_number)],
                            "Golden Retriever": [f"GR{i:03d}" for i in range(1, dogs_number)],
                            "Bulldog": [f"B{i:03d}" for i in range(1, dogs_number)],
                            "Boxer": [f"BX{i:03d}" for i in range(1, dogs_number)],
                            "Chihuahua": [f"C{i:03d}" for i in range(1, dogs_number)]}

    def get_dogs(self):
        dog_data = []
        for i in range(20):
            chip_number = random.choice(self.chip_numbers)
            race = random.choice(self.races)
            breeding = random.choice(self.breeding_nickname)
            owner_id = random.choice(self.owners_ids)
            dob = f"{random.randint(2019, 2021)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
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
                   "breeding": breeding,
                   "owner_id": owner_id,
                   "dob": dob,
                   "pedigree_number": pedigree_number,
                   "branch_reg": branch_reg,
                   "color": color,
                   "litter": litter,
                   "medical_history": medical_history}
            dog_data.append(dog)
        json_data = json.dumps(dog)
        return dog_data

# use the class above and print dogs, every dog in single line
dogs_number = 20
dog = Dog_generator(dogs_number)
dogs = dog.get_dogs()
for i in range(dogs_number):
    print(dogs[i])

class Owner_genrator:
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

    def __init__(self, owners_number):
        self.owners_number = owners_number
        self.owners_ids = [f"{random.randint(10000000, 99999999)}" for i in range(1, owners_number)]
        self.names = [names.get_first_name() for i in range(1, owners_number)]
        self.surnames = [names.get_last_name() for i in range(1, owners_number)]
        self.phone_numbers = [f"{random.randint(100000000, 999999999)}" for i in range(1, owners_number)]
        self.self.zip_codes = [f"{random.randint(10000, 99999)}" for i in range(1, owners_number)]

    def get_owners(self):
        owner_data = []
        for i in range(self.owners_number):
            owner = {"owner_id": self.owners_ids[i],
                     "name": self.names[i],
                     "surname": self.surnames[i],
                     "phone_number": self.phone_numbers[i],
                     "email": self.emails[i],
                     "address": self.addresses[i],
                     "zip_code": self.zip_codes[i]}
            owner_data.append(owner)
        json_data = json.dumps(owner_data)
        return owner_data