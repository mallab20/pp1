countries = [{"name" : "a", "population" : "1"}, {"name" : "b","population" : "2"},{"name" : "c","population" : "3"},{"name" : "d","population" : "4"},{"name" : "e","population" : "5"}]

i = 0
while i < len(countries):
    print(f'{countries[i]["name"]:10}{countries[i]["population"]:<10}')
    i += 1
