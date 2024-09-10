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
    pass
    foods_names = [food["name"] for food in spicy_foods]
    return foods_names


# get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    pass
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods


# get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        emoji_count = int(food["heat_level"]) * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji_count}")


# print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    cuisine_foods = [food for food in spicy_foods if food["cuisine"] == cuisine]
    if len(cuisine_foods) == 1:
        cuisine_food = cuisine_foods[0]
        cuisine_foods = cuisine_food
    return cuisine_foods


# get_spicy_food_by_cuisine(spicy_foods, 'Thai')


def print_spiciest_foods(spicy_foods):
    pass
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    for food in spiciest_foods:
        emoji_count = int(food["heat_level"]) * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji_count}")


# print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    pass
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods) if spicy_foods else 0


# print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods


print(
    create_spicy_food(
        spicy_foods,
        {
            "name": "Griot",
            "cuisine": "Haitian",
            "heat_level": 10,
        },
    )
)