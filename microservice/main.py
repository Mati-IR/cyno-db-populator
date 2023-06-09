import json
import random
import string
import names
from cynology_generator import CynologyGenerator

owners_number = 10
dogs_number = 100

generator = CynologyGenerator(owners_number, dogs_number)

owners_data = generator.get_owners()
dogs_data = generator.get_dogs()
championships_data = generator.get_championships()

# print generated data
# print(json.dumps(owners_data, indent=4))

# print(json.dumps(dogs_data, indent=4))

# print(json.dumps(championships_data, indent=4))
