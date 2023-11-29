import json
student = {
    "name" : "Mark",
    "grades" : [1,2,3,4,5]
}

file = open("student.json", "w")
json.dump(student,file, indent = 6)
file.close()