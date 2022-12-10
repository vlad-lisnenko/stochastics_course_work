from scipy.stats import skellam
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

mu1, mu2 = 45, 16
mean, var = skellam.stats(mu1, mu2)


x = np.arange(skellam.ppf(0.01, mu1, mu2),
              skellam.ppf(0.99, mu1, mu2))

ax.plot(x, skellam.pmf(x, mu1, mu2), 'bo', ms=5,)
ax.vlines(x, 0, skellam.pmf(x, mu1, mu2), colors='b', lw=5, alpha=0.5)

with open("data.txt", "w") as file:
    for item in skellam.pmf(x, mu1, mu2):
        file.write('%f\n' % item)

plt.show()
