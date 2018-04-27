import json


with open('mapa1.json') as json_file:
	base = json.load(json_file)
	for val in base["layers"][1]["data"]:
		print val


