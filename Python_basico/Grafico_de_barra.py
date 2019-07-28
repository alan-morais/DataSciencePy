from matplotlib import pyplot as plt
filmes = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
Oscars = [5, 11, 3, 8, 10]
xs = [i + 0.1 for i, _ in enumerate(filmes)]
plt.bar(xs, Oscars)
plt.ylabel("# de premiações")
plt.xlabel("Filmes")
plt.title("Melhores Filmes")
plt.xticks([i + 0.1 for i, _ in enumerate(filmes)], filmes)
plt.show()