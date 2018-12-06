import random
import json


with open('participants.json') as FILE:
    participants = json.load(FILE).get('people')

if len(participants) % 2 != 0:
    raise ValueError("Number of people needs to be an even number")

data = dict.fromkeys(participants)

for person in data:
    possible_receivers = [x for x in participants if x != person]
    if possible_receivers:
        receiver = random.choice(possible_receivers)
        data[person] = receiver
        if participants:
            participants.remove(receiver)

    print(f"{person} will give to {data.get(person)}")
