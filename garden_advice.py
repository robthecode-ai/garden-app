SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

SEASON_PLANTS = {
    "summer": "Tomatoes and peppers can grow great this time of year.",
    "winter": "Kale and spinach can grow great this time of year.",
}


def get_season_advice(season):
    return SEASON_ADVICE.get(season, "No advice for this season.\n")


def get_plant_advice(plant_type):
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


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

# Determine recommendations based on the season
recommendations = SEASON_PLANTS.get(
    season, "No recommendations for this season."
    )

# Print the generated recommendations
print("Plants to consider (check your local climate):", recommendations)
