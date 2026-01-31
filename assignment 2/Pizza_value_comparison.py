import math

def pizza_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 100) / 2
    area = math.pi * radius_m ** 2
    return price_usd / area


def compare_pizzas():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))

    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))

    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)

    if unit1 < unit2:
        print("Pizza 1 offers better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 offers better value for money.")
    else:
        print("Both pizzas offer the same value.")
compare_pizzas()