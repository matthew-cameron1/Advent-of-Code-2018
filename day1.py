challengeInput = open("day1_input.txt", "r")

def partOne():
	sum = 0

	for line in challengeInput:
		change = int(line)
		sum+=change

	print("Your ending frequency is:", str(sum))

def partTwo():
	seen = []
	sum = 0

	formattedInput = []

	for line in challengeInput:
		num = int(line)
		formattedInput.append(num)

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
	partTwo()

main()