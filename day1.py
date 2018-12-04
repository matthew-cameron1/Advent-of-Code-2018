challengeInput = open("day1_input.txt", "r")

formattedInput = []

for line in challengeInput:
	formattedInput.append(int(line))

def partOne():
	sum = 0

	for line in formattedInput:
		sum+=line

	print("Your ending frequency is:", str(sum))

def partTwo():
	seen = []
	sum = 0

	iter = 0
	for i in range(len(formattedInput)):
		print(i)
		if i >= len(formattedInput):
			i = 0

		num = formattedInput[i]
		sum += num
		if sum in seen:
			break
		else:
			seen.append(sum)

		seen.append(sum)

	print("Found", sum)

def main():
	partOne()
	partTwo()

main()