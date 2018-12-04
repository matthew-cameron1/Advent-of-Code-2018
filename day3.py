fileInput = open("day3_input.txt", "r")
formattedInput = []

for line in fileInput:
	formattedInput.append(line.strip())

def partOne():
	cols = 1000
	sheet = [[0] * cols for i in range(cols)]

	for spec in formattedInput:
		id = spec.split("@")[0]
		offsets = spec.split(" ")[2]
		offX = int(offsets.split(",")[0].replace(":", ""))
		offY = int(offsets.split(",")[1].replace(":", ""))

		dimensions = spec.split(" ")[3]
		dimX = int(dimensions.split("x")[0])
		dimY = int(dimensions.split("x")[1])

		for x in range(offX, (offX+dimX), 1):
			for y in range(offY, (offY+dimY), 1):
				if sheet[x][y] == 0:
					sheet[x][y] = 1
				else:
					sheet[x][y] += 1

	total = 0

	for x in range(1000):
		for y in range(1000):
			val = sheet[x][y]

			if val > 1:
				total+=1
	print("Total square inches that overlap:", total)

def partTwo():
	cols = 1000
	sheet = [[0] * cols for i in range(cols)]
	seen = {}
	for spec in formattedInput:
		id = spec.split("@")[0]
		seen[id.strip()] = 1
		offsets = spec.split(" ")[2]
		offX = int(offsets.split(",")[0].replace(":", ""))
		offY = int(offsets.split(",")[1].replace(":", ""))

		dimensions = spec.split(" ")[3]
		dimX = int(dimensions.split("x")[0])
		dimY = int(dimensions.split("x")[1])

		for x in range(offX, (offX+dimX), 1):
			for y in range(offY, (offY+dimY), 1):
				if sheet[x][y] == 0:
					sheet[x][y] = id.strip()
				else:
					seen[id.strip()] += 1
					seen[sheet[x][y]] += 1
	print("The id without an overlap is:", min(seen, key=seen.get))

def main():
	partOne()
	partTwo()

main()