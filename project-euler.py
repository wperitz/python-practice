import numpy
import pandas
import matplotlib

################################################
# Problem 1

sum1 = 0
n = 1

while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        sum1 += n
    n += 1

print(sum1)


################################################
# Problem 2

x = 1
y = 2
sum2 = 0

while y <= 4000000:
    if y % 2 == 0:
        sum2 += y
    x, y = y, x + y 

print(sum2)


################################################
# Problem 3


