import json

course = []

json = json.dumps(course)

file = open("static/majorLists/Computer Science BA.json", "w")

file.write(json)

file.close()