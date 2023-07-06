spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # list comprehension method
    return [food["name"] for food in spicy_foods]
    
    # for loop method
    # names = list()
    # for n in spicy_foods:
    #     names.append(n["name"])
    # return names

# get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"] * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

# print_spicy_foods(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
# print(create_spicy_food(spicy_foods, new_food))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if cuisine == food["cuisine"]]

get_spicy_food_by_cuisine(spicy_foods, "Thai")


def print_spiciest_foods(spicy_foods):
    # method 1:
    # print([food for food in spicy_foods if food["heat_level"] > 5])

    # method 2:
    result = get_spiciest_foods(spicy_foods)
    print_spicy_foods(result)
    

# print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    # method 1:
    # new_list = ([food["heat_level"] for food in spicy_foods])
    # avg = sum(new_list)/len(new_list)
    # return avg

    # method 2:
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)

print(get_average_heat_level(spicy_foods))