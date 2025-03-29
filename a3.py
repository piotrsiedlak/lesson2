import numpy as np
import scipy.stats as stats

prices = [183.25, 171.25, 190.25, 203, 177, 183.75, 159.75, 182.5, 175.75, 173.5]

mean_price = np.mean(prices)
std_price = np.std(prices, ddof=1)

n = len(prices)

confidence_level = 0.95
alpha = 1 - confidence_level
t_critical = stats.t.ppf(1 - alpha / 2, df = n - 1)

std_error = std_price / np.sqrt(n)

margin_of_error = t_critical * std_error
lower_bound = mean_price - margin_of_error
upper_bound = mean_price + margin_of_error

print(f"Średnia cena: {mean_price:.2f} zł")
print(f"Odchylenie standardowe: {std_price:.2f} zł")
print(f"95% przedział ufności dla średniej ceny: ({lower_bound:.2f} zł, {upper_bound:.2f} zł)")
