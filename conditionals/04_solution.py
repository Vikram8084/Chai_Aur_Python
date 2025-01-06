# Fruit Ripeness Checker 
# Detrmine if a fruit is ripe , overripe,or unripe based on its color.
# (e.g Banana:Green -unripe,Yellow-Ripe,Brown - overripe)

fruit = "Banana"

color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")

else:
    print("No proper information about color is available")
