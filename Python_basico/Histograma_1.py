from matplotlib import pyplot as plt
mensoes = [500, 505]
anos = [2013, 2014]
plt.bar([2012.6, 2013.6], mensoes, 0.8)
plt.xticks(anos)
plt.ylabel("# Falando DataScience")
plt.ticklabel_format(useOffset=False)
plt.axis([2012.5, 2014.5, 499, 506])
plt.title("Grande aumento!")
plt.show()