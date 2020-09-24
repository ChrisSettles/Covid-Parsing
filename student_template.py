from file_utils import loadWithJSON


## Will load all Harrisonburg and Rockingham data into a list of lists
## Each element in the main list will contain a list of two items, the str:date and int:cases
harrisonburg_data = loadWithJSON('harrisonburg.json')
rockingham_data = loadWithJSON('rockingham.json')

## Print all elements in the list as an example
for data in harrisonburg_data:
    date = data[0]
    cases = data[1]
    print('On '+date + ' there were '+ str(cases) +' cases in Harrisonburg')

print('When was the first positive COVID case in Rockingham County and Harrisonburg?')
print()
firstDateHarris = harrisonburg_data[0][0]
firstDateRocking = rockingham_data[0][0]
print("The first positive COVID case in Harrisonburg was on " + firstDateHarris)
print("The first positive COVID case in Rockingham County was on " + firstDateRocking)
print()
print('What day was the maximum number of cases recorded in Harrisonburg and Rockingham County?')
harrisData = []
rockingData = []
finalHarrisonDiff = 0
finalRockingDiff = 0
harrisDate = ""
rockingDate = ""
for data in harrisonburg_data:
    harrisData.extend(data)

for i in range(1, len(harrisData), 2):
        diff = harrisData[i] - harrisData[i-2]
        if diff > finalHarrisonDiff:
            finalHarrisonDiff = diff
            harrisDate = harrisData[i-1]

for data in rockingham_data:
    rockingData.extend(data)

for i in range(1, len(rockingData), 2):
    diff = rockingData[i] - rockingData[i-2]
    if diff > finalRockingDiff:
        finalRockingDiff = diff
        rockingDate = rockingData[i-1]
print()
print("The worst day for Harrisonburg for covid cases was " + harrisDate)
print("The worst day for Rockingham County for covid cases was " + rockingDate)
print()

print('What was the worst week in the city/county for new COVID cases? '
      'When was the rise in cases the fastest over a seven day period?')

casesOnlyInHarris = harrisData[1::2]
datesOnlyInHarris = harrisData[0::2]
worstWeekStartToEnd = ""
worstWeekCases = 0

startIndex = 0
endIndex = 6
previousWeek = casesOnlyInHarris[endIndex]-casesOnlyInHarris[startIndex]
while endIndex < len(casesOnlyInHarris)-1:
    week = casesOnlyInHarris[endIndex+1]-casesOnlyInHarris[startIndex+1]
    if(week > worstWeekCases):
        worstWeekCases = week
        worstWeekStartToEnd = datesOnlyInHarris[startIndex+1] + " through " + datesOnlyInHarris[endIndex+1]
    startIndex += 1
    endIndex += 1

print("The worst 7 day period for positive COVID cases in Harrisonburg was " + worstWeekStartToEnd + " with " + str(worstWeekCases) + " cases.")

casesOnlyInRocking = rockingData[1::2]
datesOnlyInRocking = rockingData[0::2]
worstWeekStartToEndR = ""
worstWeekCasesR = 0

startIndexR = 0
endIndexR = 6
previousWeekR = casesOnlyInRocking[endIndexR]-casesOnlyInRocking[startIndexR]
while endIndexR < len(casesOnlyInRocking)-1:
    weekR = casesOnlyInRocking[endIndexR+1]-casesOnlyInRocking[startIndexR+1]
    if(weekR > worstWeekCasesR):
        worstWeekCasesR = weekR
        worstWeekStartToEndR = datesOnlyInRocking[startIndexR+1] + " through " + datesOnlyInRocking[endIndexR+1]
    startIndexR += 1
    endIndexR += 1

print("The worst 7 day period for positive COVID cases in Rockingham County was " + worstWeekStartToEndR + " with " + str(worstWeekCasesR) + " cases.")