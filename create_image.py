from string import Template


# Use this script with python3 create_image.py

with open("microbit-template.svg", "r") as f1:

	d = {}
	f2 = open("config.txt", "r")
	opacities = f2.read().rstrip("\n").split("_")
	f2.close()
	for i, opacity in enumerate(opacities):
		d["l" + str(i+1)] = opacity + "%"

	src = Template(f1.read())
	result = src.substitute(d)
	f3 = open("output.svg", "w")
	f3.write(result)
	f3.close()