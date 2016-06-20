def hotel_cost(nights):
    #The hotel costs $140 per night
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    #The car cost $40 per day
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3 and days < 7:
        cost -= 20
    return cost

def trip_cost(city, days, spending_money):
    print trip_cost("Los Angeles", 5, 600)
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money