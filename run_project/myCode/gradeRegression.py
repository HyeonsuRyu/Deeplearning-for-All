def leastSquares(x, y):
    xAvg = sum(x)/len(x)
    yAvg = sum(y)/len(y)
    a = 0
    b = 0

    for i in range(len(x)):
        a += (x[i]-xAvg)*(y[i]-yAvg)
        b += (x[i]-xAvg)*(x[i]-xAvg)

    return a/b

def bias(x, y, a):
    return sum(y)/len(y)-a*sum(x)/len(x)

import numpy as np
import matplotlib.pyplot as plt

x = [2, 4, 6, 8]
y = [81, 93, 91, 97]

#X = int(input("Enter x: ", end = "", default = "86"))
X = 7

a = leastSquares(x, y)
b = bias(x, y, a)

regression = a*X+b

print("y prediction is ", regression)

predictLine = list()
for i in range(10):
    predictLine.append(a*i+b)
plt.plot(x, y, 'bo')
plt.plot(X, regression, 'ro')
plt.plot(predictLine)
plt.axis([0, 10, 0, 100])
plt.show()
