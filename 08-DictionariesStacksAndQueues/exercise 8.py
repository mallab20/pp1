person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person.get("name"))
print(person["name"])
print(person.get("hobby"))
print(person["hobby"])
person.update({"surname" : "Nowak"})
print(person.get("surname"))

person["married"] = not person["married"]
# person["married"] = False - nie wolno tak

person["gender"] = "male"
person["hobby"] += ["bicycle"]
person["hobby"].append("bicycle2")
person["phone"]["work phone"] = "313131444"

print(person)
