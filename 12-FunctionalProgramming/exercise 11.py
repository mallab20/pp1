def speed(x):
    y = x / 1000
    result = int(y * 3600)
    result2 = f'{x}m/s = {result}km/h'

    return result2

print(speed(10))
print(speed(35))