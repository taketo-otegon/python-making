import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定義する関数
def f(x):
    return x

# フーリエ係数の計算
def fourier_coefficients(f, n_max, L):
    a0 = (1/L) * np.trapz(f(x), x)
    an = []
    bn = []
    for n in range(1, n_max+1):
        integrand_cos = lambda x: f(x) * np.cos(2 * np.pi * n * x / L)
        integrand_sin = lambda x: f(x) * np.sin(2 * np.pi * n * x / L)
        an.append((1/L) * np.trapz(integrand_cos(x), x))
        bn.append((1/L) * np.trapz(integrand_sin(x), x))
    return a0, an, bn

# フーリエ級数の計算
def fourier_series(x, a0, an, bn, L):
    series = np.zeros_like(x)
    series += a0/2
    for n in range(1, len(an)+1):
        series += an[n-1] * np.cos(2 * np.pi * n * x / L)
        series += bn[n-1] * np.sin(2 * np.pi * n * x / L)
    return series

# 計算パラメータの設定
L = 2 * np.pi # 周期
x = np.linspace(-L, L, 1000)

# グラフの設定
fig, ax = plt.subplots()
line1, = ax.plot(x, f(x), label='f(x)')
line2, = ax.plot([], [], label='Fourier series')

ax.legend()

# アニメーションの更新関数
def update(n_max):
    a0, an, bn = fourier_coefficients(f, n_max, L)
    series = fourier_series(x, a0, an, bn, L)
    line2.set_data(x, series)
    ax.set_title('n_max = {}'.format(n_max))

# アニメーションの作成
ani = FuncAnimation(fig, update, frames=range(1,101), interval=100)

# アニメーションの表示
plt.show()