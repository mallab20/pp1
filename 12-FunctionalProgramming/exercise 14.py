distance = float(input("Distance: "))
travel_h = float(input("Travel hours: "))
travel_m = float(input("Travel minutes: "))

result = lambda distance, travel_h, travel_m: round(distance/(travel_h+(travel_m/60)), 1)

print(result(distance, travel_h, travel_m))