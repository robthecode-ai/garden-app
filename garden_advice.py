def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# User input for the season and plant type
season = input("Enter the season: ").strip().lower()
plant_type = input("Enter the plant type: ").strip().lower()

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
advice += get_season_advice(season)

# Determine advice based on the plant type
advice += get_plant_advice(plant_type)

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
