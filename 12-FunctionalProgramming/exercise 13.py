distance = float(input("Distance: "))
travel_h = float(input("Travel hours: "))
travel_m = float(input("Travel minutes: "))

def f(distance, travel_h, travel_m):
    return round(distance/(travel_h+(travel_m/60)), 1)

print(f(distance, travel_h, travel_m))