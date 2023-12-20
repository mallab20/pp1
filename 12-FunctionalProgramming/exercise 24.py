speed = [48,47,54,50,42,68,39,46]

speed2 = f'Recorded values: {", ".join(map(str, speed))} Speed too high: {", ".join(map(str, list(filter(lambda x: x>50, speed))))}'
print(speed2)