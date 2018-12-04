inputs = open("day2_input.txt", "r")
formattedInputs = []

for line in inputs:
	formattedInputs.append(line.strip())

testInputs = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

def partOne():
	twoTotals = 0
	threeTotals = 0

	for line in formattedInputs:
		twos = 0
		threes = 0
	for char in line:

		count = line.count(char)

		if count == 2 and twos == 0:
			twos+=1
		elif count == 3 and threes == 0:
			threes+=1
	twoTotals+=twos
	threeTotals+=threes

	checksum = twoTotals*threeTotals
	print("checksum:", str(checksum))

def partTwo():
	for boxOne in formattedInputs:
		for boxTwo in formattedInputs:

			for index in range(len(boxOne)):
				charOne = boxOne[index]
				charTwo = boxTwo[index]

				if charOne != charTwo:
					boxOneSplit = boxOne.split(charOne, 1)
					boxTwoSplit = boxTwo.split(charTwo, 1)

					if boxOneSplit == boxTwoSplit:
						match = boxOne

						characters = match[:index] + match[index+1:]
						print ("The final characters are:", characters)
						return
					else:
						break

def main():
	partOne()
	partTwo()

main()
