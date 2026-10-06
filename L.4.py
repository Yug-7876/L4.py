temperature = int(input("Enter the temperature in Celsius"))
if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("You should wear a", outfit)
else: 
    outfit = "t-shirt"
    print("It is warm today.")
    print("You should wear a", outfit)

is_raining = input("Is it raining? (yes/no): ")
if is_raining.lower() == "yes":
    print("Take an umbrella.")

wind_speed = int(input("Enter the wind speed in km/h: "))
if wind_speed > 30:
    need_windbreaker = "Yes"
    print("Wear a windbreaker over your", outfit)
else:
    need_windbreaker = "No"
    print("It is calm today")
    print("You don't need a windbreaker over your", outfit)

has_puddles = input("Are there puddles on the ground? (yes/no): ")
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)
print("")
print("Weather check complete!")
print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature, "°C")
print("Outfit Chosen:", outfit)
print("raining:", is_raining)
print("Need Windbreaker:", need_windbreaker)
print("shoes Chosen:", shoes)
print("==================================")