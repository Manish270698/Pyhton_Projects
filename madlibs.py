
import random

Adjectives = list(input("Enter 3 <space> separated adjectives: ").split(' '))
Verb1 = list(input("Enter 3 <space> separated verbs: ").split(' '))
Verb2 = list(input("Enter 3 more <space> separated verbs: ").split(' '))
famous_person = list(input("Enter 3 <,> separated famous people names: ").split(','))

madlib = f"Computer programming is so {random.choice (Adjectives)}! It makes me so excited all the time bec
I love to {random. choice (Verb1)}. Stay hydrated and {random.choice (Verb2)} like you are {random.choice

print(madlib)
