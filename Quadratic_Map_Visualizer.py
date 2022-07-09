#import python modules
import seaborn as sns
import matplotlib.pyplot as plt
#obtain dataset through equation and iterations
xn_values = []
xn1_values = []
xn = 0.01
for i in range(100000):
    xn_values.append(xn)
    xn1 = (4*xn)*(1-xn)
    xn1_values.append(xn1)
    xn = xn1
#plot the graph
sns.lineplot(x = xn_values, y = xn1_values).set(title = 'Xn+1 vs Xn for init cond. a = 4 and Xn = 0.01, 100000 iterations', xlabel = 'Xn', ylabel = 'Xn+1')
plt.show()
