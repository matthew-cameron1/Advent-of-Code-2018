file = open("day5_input.txt", "r")
inputs = file.readlines()
file.close()

alphabet = "abcdefghijklmnopqrstuvwxyz"

def partOne():
	cont = True
	poly = inputs[0]
	while (cont):
		(cont, poly) = change(poly)
	print("Part one output:", len(poly))

def partTwo():
	sizes = {}

	for char in alphabet:
		poly = inputs[0]
		poly = poly.replace(char, "").replace(char.upper(), "")

		cont = True

		while (cont):
			(cont, poly) = change(poly)
		sizes[poly] = len(poly)
	
	key_min = min(sizes.keys(), key=(lambda k: sizes[k]))
	print("Part two output:", sizes[key_min])

def change(poly):
	length = len(poly)

	for char in alphabet:
		poly = poly.replace(char+char.upper(), "").replace(char.upper()+char, "")

	newLen = len(poly)
	return ((length != newLen), poly)

def main():
	partOne()
	partTwo()

main()