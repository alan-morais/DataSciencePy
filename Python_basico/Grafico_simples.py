from matplotlib import pyplot as plt
anos = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(anos, gdp, color ='blue', marker='s', linestyle='solid')

plt.title("GDP Nominal")
plt.ylabel("Bilhões de $")
plt.xlabel("Anos")
plt.show()