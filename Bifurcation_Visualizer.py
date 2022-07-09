#import python module
import matplotlib.pyplot as plt
#create lists for data acquisition
finalxn1_values = []
finalxn_values = []
a_values = []
xn = 0.01
a = 1
#run iterations to collect data
while a <=4:
    a_values.append(a)
    xn_values = []
    xn1_values = []
    for i in range(10000):
        xn_values.append(xn)
        xn1 = (a*xn)*(1-xn)
        xn1_values.append(xn1)
        xn = xn1
    finalxn1_values.append(xn1_values[-1])
    finalxn_values.append(xn_values[-1])
    a += 0.01
#create scatter plot using acquired data
plt.plot(a_values, finalxn_values, color = 'b')
plt.plot(a_values, finalxn1_values, color = 'r')
plt.xlabel('a')
plt.ylabel('final x')
plt.title('a vs final X from a values = 1-4 (step length = 0.01), 10000 iterations')
#display plot
plt.show()
