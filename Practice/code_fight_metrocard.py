def metroCard(lastNumberOfDays):
	weekDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	possibleDays = []

	for day in range(len(weekDay)):
		if lastNumberOfDays == weekDay[day]:
			if day == len(weekDay) - 1:
				if 31 not in possibleDays:
					possibleDays.insert(day, 31)
			else:
				if weekDay[day+1] not in possibleDays:
					possibleDays.insert(day, weekDay[day+1])

	return possibleDays

print(metroCard(30))
print(metroCard(31))
print(metroCard(28))