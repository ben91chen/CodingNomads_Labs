'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

import math
# formula for r = d/t
time_ran = 30.5 / 60
miles_ran = 10

miles_per_hour = miles_ran / time_ran
print(miles_per_hour)

# miles/h to km/hr conversion
km_per_hour = miles_per_hour * 1.6
print(km_per_hour)

print(f"The runner ran about {math.trunc(miles_per_hour)} miles per hour and about {math.trunc(km_per_hour)} kilometers per hour.")




