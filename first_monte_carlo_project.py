import numpy as np
import matplotlib.pyplot as plt

# задаем параметры модели геометрического броуновского движения
mu_A = 0.05 # среднее значение доходности актива A
sigma_A = 0.2 # стандартное отклонение доходности актива A
mu_B = 0.03 # среднее значение доходности актива B
sigma_B = 0.15 # стандартное отклонение доходности актива B
rho = 0.8 # коэффициент корреляции между доходностями активов A и B
T = 1 # срок моделирования
N = 252 # количество шагов моделирования
dt = T/N # шаг по времени
trials = 50 # количество повторов для каждого актива



# задаем начальные цены активов
S0_A = 100 # начальная цена актива A
S0_B = 80 # начальная цена актива B

# задаем матрицу корреляций
corr_matrix = np.array([[1, rho], [rho, 1]])

# задаем массивы для цен активов
prices_A = np.zeros((trials, N+1))
prices_B = np.zeros((trials, N+1))

# заполняем массивы цен активов
for t in range(trials):
    # генерируем случайные нормально распределенные числа
    random_numbers = np.random.multivariate_normal(mean=[0, 0], cov=corr_matrix, size=N)
    # задаем начальные цены
    prices_A[t, 0] = S0_A
    prices_B[t, 0] = S0_B
    for i in range(1, N+1):
        # считаем новые цены активов
        prices_A[t, i] = prices_A[t, i-1]*np.exp((mu_A - 0.5*sigma_A**2)*dt + sigma_A*np.sqrt(dt)*random_numbers[i-1][0])
        prices_B[t, i] = prices_B[t, i-1]*np.exp((mu_B - 0.5*sigma_B**2)*dt + sigma_B*np.sqrt(dt)*random_numbers[i-1][1])

# рисуем графики цен активов
for t in range(trials):
    plt.plot(prices_A[t], label='Asset A')
plt.legend()
plt.show()

for t in range(trials):
    plt.plot(prices_B[t], label='Asset B')
plt.legend()
plt.show()
# Calculate annualized expected returns, volatility, and Sharpe ratio for each instrument
annualized_returns_A = np.mean(prices_A[:, -1]/S0_A)**(252/T)-1
annualized_returns_B = np.mean(prices_B[:, -1]/S0_B)**(252/T)-1

annualized_volatility_A = np.std(prices_A[:, -1]/S0_A)*(252**0.5)
annualized_volatility_B = np.std(prices_B[:, -1]/S0_B)*(252**0.5)

sharpe_ratio_A = annualized_returns_A / annualized_volatility_A
sharpe_ratio_B = annualized_returns_B / annualized_volatility_B

print("Expected annualized returns for Asset A: {:.2%}".format(annualized_returns_A))
print("Expected annualized returns for Asset B: {:.2%}".format(annualized_returns_B))
print("Annualized volatility for Asset A: {:.2%}".format(annualized_volatility_A))
print("Annualized volatility for Asset B: {:.2%}".format(annualized_volatility_B))
print("Sharpe ratio for Asset A: {:.2f}".format(sharpe_ratio_A))
print("Sharpe ratio for Asset B: {:.2f}".format(sharpe_ratio_B))