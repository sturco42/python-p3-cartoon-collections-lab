dwarves = ["Doc", "Dopey", "Grumpy", "Bashful"]

def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        number = i + 1
        print(f"{number}. {dwarves[i]}")
roll_call_dwarves(dwarves)

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def summon_captain_planet(planeteer_calls):
    calls = []
    for i in range(len(planeteer_calls)):
        call = f"{planeteer_calls[i].capitalize()}!"
        calls.append(call)
    print(calls)
    return calls
summon_captain_planet(planeteer_calls)

short_words = ["puff", "go", "two"]
assorted_words = ["two", "go", "industrious", "bop"]

def long_planeteer_calls(words):
    for i in words:
        if len(i) > 4:
            print(True)
            return True
    print(False)
    return False
long_planeteer_calls(short_words)
long_planeteer_calls(assorted_words)

cheeses = ["cheddar", "gouda", "camembert"]
snacks = ["crackers", "gouda", "thyme"]
ingredients = ["garlic", "rosemary", "bread"]

def find_the_cheese(foods):
    for food in foods:
        if food in cheeses:
            print(food)
            return food
# find_the_cheese(cheeses)
find_the_cheese(snacks)
find_the_cheese(ingredients)