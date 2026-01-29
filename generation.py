# Random generation for a variety of items.
import json
from objects import Person
from objects import Weapon
from objects import Adjective
from objects import Place
from objects import Match

import random

def generatePerson(data):
    print("Generating a person!")
    randomKey = random.choice(list(data.keys()))
    person = Person(randomKey, data[randomKey]["Name"], data[randomKey]["Emoji_ID"], data[randomKey]["Description"], data[randomKey]["Link"], data[randomKey]["Image"])
    return person
#Returns a list with the person, emoji object, and the person's emoji id. 
def generateWeapon():
    print("Generating a weapon!")
    with open("Armory\\generate.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    selected = random.choices(list(data.keys()), weights=list(data.values()))[0]
    with open(f"Armory\\{selected}.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    randomKey = random.choice(list(data.keys()))
    weapon = Weapon(data[randomKey]["Name"], data[randomKey]["Tagline"], data[randomKey]["Description"], data[randomKey]["Image"], data[randomKey]["Link"])
    return weapon
#Returns a random weapon
def generateWeaponPair(numOfWeapons=2):
    print(f"Generating {numOfWeapons} of weapon(s)!")
    with open("Armory\\generate.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    selected = random.choices(list(data.keys()), weights=list(data.values()))[0]
    with open(f"Armory\\{selected}.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    weapons = []
    for i in range(numOfWeapons):
        randomKey = random.choice(list(data.keys()))
        weapon = Weapon(data[randomKey]["Name"], data[randomKey]["Tagline"], data[randomKey]["Description"], data[randomKey]["Image"], data[randomKey]["Link"])
        weapons.append(weapon)
    return weapons
#Generates a tiered pair of weapons. 
def generateAdjective():
    print("Generating an adjective!")
    with open("Adjectives\\generate.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    selected = random.choices(list(data.keys()), weights=list(data.values()))[0]
    with open(f"Adjectives\\{selected}.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    randomKey = random.choice(list(data.keys()))
    adjective = Adjective(data[randomKey]["Name"], data[randomKey]["Tagline"], data[randomKey]["Description"], data[randomKey]["Link"])
    return adjective
#Returns a random Adjective
def generateAdjectivePair(numOfAdjectives=2):
    print(f"Generating {numOfAdjectives} of adjective(s)!")
    with open("Adjectives\\generate.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    selected = random.choices(list(data.keys()), weights=list(data.values()))[0]
    with open(f"Adjectives\\{selected}.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    adjectives = []
    for i in range(numOfAdjectives):
        randomKey = random.choice(list(data.keys()))
        adjective = Adjective(data[randomKey]["Name"], data[randomKey]["Tagline"], data[randomKey]["Description"], data[randomKey]["Link"])
        adjectives.append(adjective)
    return adjectives
#Returns a random tiered Adjective pair
def generatePlace():
    print("Generating a location!")
    with open("Atlas\\atlas.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    randomKey = random.choice(list(data.keys()))
    place = Place(data[randomKey]["Name"], data[randomKey]["Tagline"], data[randomKey]["Description"], data[randomKey]["Link"], data[randomKey]["Image"])
    return place
#Returns a random place
def generateWeaponPairTier(tier, numOfWeapons=2):
    with open(f"Armory\\{tier}.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    weapons = []
    for i in range(numOfWeapons):
        randomKey = random.choice(list(data.keys()))
        weapon = Weapon(data[randomKey]["Name"], data[randomKey]["Tagline"], data[randomKey]["Description"], data[randomKey]["Image"], data[randomKey]["Link"])
        weapons.append(weapon)
    return weapons
#Generates a pair of weapons in the specified tier.
def generateAdjectivePairTier(tier, numOfAdjectives=2):
    with open(f"Adjective\\{tier}.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    adjectives = []
    for i in range(numOfAdjectives):
        randomKey = random.choice(list(data.keys()))
        adjective = Adjective(data[randomKey]["Name"], data[randomKey]["Tagline"], data[randomKey]["Description"], data[randomKey]["Link"])
        adjectives.append(adjective)
    return adjectives
#Generates a pair of adjectives in the specified tier.
def generatePlaceTier(tier):
    print("Generating a location!")
    with open(f"Atlas\\{tier}.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    randomKey = random.choice(list(data.keys()))
    place = Place(data[randomKey]["Name"], data[randomKey]["Tagline"], data[randomKey]["Description"], data[randomKey]["Link"], data[randomKey]["Image"])
    return place
#Generates a place in the specified list.
def generateContest(contestants, bracket="people_dict.json"):
    RNG = random.randint(0, 2)
    if RNG >= 1:
        print("Generating Death Match!")
        RNG = random.randint(0,1)
        weapons = "All"
        if RNG == 0:
            weapons = "None"
        RNG = random.randint(0,1)
        adjectives = "All"
        if RNG == 0:
            adjectives = "None"
        contest = Match(
            contestants, 
            "a death match", 
            "A death match is a fight to the death.", 
            "https://en.wikipedia.org/wiki/Combat", 
            "- Both contestants act in character with their real-life selves.\n- Both contestants are in the physical condition they were in when they reached the height of their fame while alive.\n- Both competitors know how to activate any weapons they have.", 
            adjectives, 
            "All", 
            weapons, 
            "death_match")
    else:
        print("Generating other contest!")
        with open("contests.json", "r", encoding='utf-8') as f:
            data = json.load(f)
        randomKey = random.choice(list(data.keys()))
        contest = Match(
            contestants, 
            data[randomKey]["Tagline"], 
            data[randomKey]["Description"], 
            data[randomKey]["Link"], 
            data[randomKey]["Rules"], 
            data[randomKey]["Adjectives"], 
            data[randomKey]["Locations"], 
            data[randomKey]["Weapons"], 
            data[randomKey]["Name"])

    print(f"Generating place based on: {contest.locations_allowed}")
    if contest.locations_allowed == "All":
        contest.place = generatePlace()
    elif contest.locations_allowed != "None":
        contest.place = generatePlaceTier(contest.locations_allowed)
    
    print(f"Generating weapons based on: {contest.weapons_allowed}")
    weapons = []
    if contest.weapons_allowed == "All":
        weapons = generateWeaponPair()
    elif contest.weapons_allowed != "None":
        weapons = generateWeaponPairTier(contest.weapons_allowed)
    i = 0
    if len(weapons) > 0:
        for contestant in contest.fighters:
            contestant.weapon = weapons[i]
            i+=1
    
    print(f"Generating adjectives based on: {contest.adjectives_allowed}")
    adjectives = []
    if contest.adjectives_allowed == "All":
        adjectives = generateAdjectivePair()
    elif contest.adjectives_allowed != "None":
        adjectives = generateAdjectivePairTier(contest.adjectives_allowed)
    i = 0
    if len(adjectives) > 0:
        for contestant in contest.fighters:
            contestant.adjective = adjectives[i]
            i+=1

    #print(f"Final contestants: {contestants}")
    return(contest)
# Generates the contest for the sake of fighting!