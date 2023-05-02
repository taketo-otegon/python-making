import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ステップ関数定義

def f(x):
    y = x<0
    return y.astype(int)

#それぞれの係数の計算

a0 = 1

def an(n):
    return 0

def bn(n):
    if n%2==0:
        return 0
    else:
        return -2/(np.pi*n)

# フーリエ級数の計算
def fourier_series(x,n_max, L):
    series = np.zeros_like(x)
    series += a0/2
    for n in range(1, n_max + 1):
        series += an(n) * np.cos(2 * np.pi * n * x / L)
        series += bn(n) * np.sin(2 * np.pi * n * x / L)
    return series

# 計算パラメータの設定
L = 2 * np.pi # 周期
x = np.linspace(-L/2, L/2, 1000)

# グラフの設定
fig, ax = plt.subplots()
line1, = ax.plot(x, f(x), label='f(x)')
line2, = ax.plot([], [], label='step n = 0') 
ax.set_ylim(-0.5,1.5)
ax.legend()

# アニメーションの更新関数
def update(n_max):
    series = fourier_series(x,n_max, L)
    line2.set_data(x, series)
    ax.set_title('n_max = {}'.format(n_max))

# アニメーションの作成
ani = FuncAnimation(fig, update, frames=range(1,101), interval=100)

ani.save("plot-fourier-step.gif", writer="imagemagick")
# アニメーションの表示
plt.show()
