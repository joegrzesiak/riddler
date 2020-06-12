# https://fivethirtyeight.com/features/how-long-will-the-bacterial-colony-last/

# each bacterium has .8 chance of splitting and .2 chance of dying
# what is the probability this will last forever, when starting with 1 bacterium?

import random

def processDay(bacteria):
    new_bacteria = 0
    for i in range(bacteria):
        live_chance = random.random()
        if live_chance < 0.8:
            new_bacteria += 2
    return new_bacteria


days = int(input("Enter number of days to simulate: "))
trials = int(input("Enter number of trials to do: "))
death_count = 0
death_by_day = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #yeah this is sloppy and enough
for trial in range(trials):
    bacteria_count = 1
    for day in range(days):
        if bacteria_count == 0:
            death_count += 1
            death_by_day[day-1] += 1
            break
        else:
            bacteria_count = processDay(bacteria_count)

print("% of dying", death_count/trials)
print("extinctions by day", death_by_day)
probability_by_day = [((x / trials)) for x in death_by_day]
print("probability of extinction by day", probability_by_day)
