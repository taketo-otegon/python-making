import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 関数 f(x) の定義
def f(x):
    return np.sin(x) + np.cos(3*x) + np.sin(5*x)

# フーリエ係数の計算
def fourier_coefficients(n, T):
    t = np.linspace(-T/2, T/2, 1000)
    y = f(t)
    dt = T/len(t)

    a0 = (2/T) * np.sum(y) * dt
    an = lambda n: (2/T) * np.sum(y * np.cos(2 * np.pi * n * t / T)) * dt
    bn = lambda n: (2/T) * np.sum(y * np.sin(2 * np.pi * n * t / T)) * dt

    return a0, an, bn

# フーリエ級数展開
def fourier_series(x, n_max, T, a0, an, bn):
    result = a0/2
    for n in range(1, n_max + 1):
        result += an(n) * np.cos(2 * np.pi * n * x / T) + bn(n) * np.sin(2 * np.pi * n * x / T)
    return result

# パラメータ設定
n_max = 10
T = 2 * np.pi
x = np.linspace(-T/2, T/2, 1000)

# プロット設定
fig, ax = plt.subplots()
ax.set_xlim(-T/2, T/2)
ax.set_ylim(-2, 2)
line1, = ax.plot(x, f(x), label='f(x)')
line, = ax.plot(x, np.zeros_like(x),label='Fourier series')
ax.legend()


a0, an, bn = fourier_coefficients(n_max, T)

def update(num):
    line.set_ydata(fourier_series(x, num, T, a0, an, bn))
    ax.set_title('n_max = {}'.format(num))
    return line,ax

# アニメーション
ani = FuncAnimation(fig, update, frames=range(n_max+1), interval=500)

plt.show()