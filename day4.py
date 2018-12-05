inputs = open("day4_input.txt", "r")
formattedInputs = []
for line in inputs:
	formattedInputs.append(line.strip())

formattedInputs.sort()

def parse(line):
	split = line.split()
	components = len(split)

	date = split[0]
	time = split[1].replace("]", "")

	action = ""

	action = " ".join(split[2:])
	return (date, time, action)

sleep = {}

def partOne():

	guards = {}
	guard = ""
	asleep = 0
	time = 0
	for line in formattedInputs:
		parsed = parse(line)

		if "begins shift" in parsed[2]:
			guard = parsed[2].split()[1]
			asleep = 0
			time = 0

			if guard not in guards and guard not in sleep:
				guards[guard] = 0
				sleep[guard] = [0]*60

		elif "falls asleep" in parsed[2]:
			asleep = int(parsed[1].split(":")[1])
		elif "wakes up" in parsed[2]:
			time = int(parsed[1].split(":")[1])

			for total in range(asleep, time, 1):
				guards[guard]+=1
				sleep[guard][total] += 1

	guard = max(guards, key=guards.get)
	print("The guard who sleeps the most is:", guard)
	time = sleep[guard].index(max(sleep[guard]))
	print("Print he was asleep the most during hour", time)

def partTwo():
	winner = ""
	highest = 0
	index = 0

	for guard in sleep:
		arr = sleep[guard]
		biggest = max(arr)
		if (biggest > highest):
			highest = biggest
			winner = guard
			index = arr.index(biggest)

	print("The guard is", winner, "and he is asleep the most during minute", index)

def main():
	partOne()
	partTwo()

main()

