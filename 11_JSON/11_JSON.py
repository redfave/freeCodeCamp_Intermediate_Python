import json
from json import JSONEncoder

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# Seria;ization
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)
with open('../11_JSON/person.json', 'w') as file:
    json.dump(person, file, indent=4, sort_keys=True)

# Deserialization
person = json.loads(personJSON)
print(person)
with open('../11_JSON/person.json', 'r') as file:
    person = json.load(file)
print(person)


# Custom Objects
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)


# Encode Method
# def encode_user(o):
#     if isinstance(o, User):
#         return {'name:': o.name, 'age': o.age, o.__class__.__name__: True}
#     else:
#         raise TypeError('Object of type User is not JSON serializable')

# Decode Method
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    else:
        return dict


# Encode Class
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)


# userJSON = json.dumps(user, default=encode_user)
# userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)

user = json.loads(userJSON)  # Not an User object but a dictionary,
print(user)

user = json.loads(userJSON, object_hook=decode_user)
print(f'User with name {user.name} is {user.age} years old')
