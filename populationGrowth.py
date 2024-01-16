import math
population = 312032486
secondsPerYear = 31536000
secondsPerLeapYear = 31622400
birthRate = 7
newBirths = 0
deathRate = 13
deaths = 0
immigrationRate = 45
newImmigrants = 0
totalGrowth = 0
daysEllapsed = 0

for i in range(1, secondsPerLeapYear+1):

    if i % birthRate == 0: population=population+1; newBirths=newBirths+1
    if i % deathRate == 0: population=population-1; deaths=deaths+1
    if i % immigrationRate == 0: population=population+1; newImmigrants=newImmigrants+1

daysEllapsed = daysEllapsed + (i//86400)
totalGrowth = newBirths - deaths + newImmigrants
print(f'The population at the start of 2024 is 312032486')
print(f'By the end of year 2024, we will have seen {math.ceil(daysEllapsed)} days, Total population: {population}, new births: {newBirths}, deaths: {deaths}, new immigrants: {newImmigrants}, Total growth {totalGrowth}\n')


for j in range(2025, 2029):
    for i in range(1, secondsPerYear+1):

        if i % birthRate == 0: population=population+1; newBirths=newBirths+1
        if i % deathRate == 0: population=population-1; deaths=deaths+1
        if i % immigrationRate == 0: population=population+1; newImmigrants=newImmigrants+1

    daysEllapsed = daysEllapsed + (i//86400)
    totalGrowth = newBirths - deaths + newImmigrants
    print(f'By the end of year {j}, we will have seen {math.ceil(daysEllapsed)} days, The countries total population: {population}, New births: {newBirths}, Deaths: {deaths}, New immigrants: {newImmigrants}, Total growth {totalGrowth}\n')
print(f'At an average population growth rate of {math.ceil(totalGrowth/daysEllapsed)} per day.')
