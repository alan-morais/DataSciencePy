from matplotlib import pyplot as plt
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_a = [256,128,64,32,16,8,4,2,1]
total_erro = [x + y for x , y in zip(variance, bias_a)]
xs = [i for i, _ in enumerate(variance)]
plt.plot(xs, variance, 'g-', label ='Vacincia')
plt.plot(xs,bias_a, 'r-', label='bias^2')
plt.plot(xs, total_erro, 'b:', label='total de erros')
plt.legend(loc=9)
plt.xlabel("Complexidade do modelo")
plt.title("Polarização e Variância")
plt.show()