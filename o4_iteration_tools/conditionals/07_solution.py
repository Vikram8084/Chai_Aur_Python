# Coffee customization
# Customize a coffe order: "Small","Medium", or "Large" with an option for "Extra Shot" of espresso

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = order_size + "coffee"

print("Order: ",coffee)