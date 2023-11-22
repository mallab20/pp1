arr = ["1","7","3","7","5"]

file = open("movies.txt", "w")

for element in arr:
    file.write(element+"\n")

file.close()