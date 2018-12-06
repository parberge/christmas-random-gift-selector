import random
import json


with open('participants.json') as FILE:
    participants = json.load(FILE).get('people')

data = dict.fromkeys(participants)

for person in data:
    if participants:
        possible_receivers = [x for x in participants if x != person]
        if possible_receivers:
            receiver = random.choice(possible_receivers)
            data[person] = receiver
            participants.remove(receiver)

    print(f"{person} will give to {data.get(person)}")
