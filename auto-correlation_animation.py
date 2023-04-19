import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 信号を生成する関数
def create_signal(t, freq=1, amplitude=1, phase=0, noise_level=0):
    signal = amplitude * np.sin(2 * np.pi * freq * t + phase)
    noise = noise_level * np.random.normal(0, 1, len(t))
    return signal + noise

# 自己相関関数
def autocorrelation(signal, lag):
    n = len(signal)
    mean = np.mean(signal)
    signal1 = signal[lag:] - mean
    signal2 = signal[:n - lag] - mean
    return np.sum(signal1 * signal2) / ((n - lag) * np.std(signal) ** 2)

# サンプルデータ生成
np.random.seed(0)
t = np.linspace(0, 10, 1000)
signal = create_signal(t, freq=2, amplitude=1, phase=0, noise_level=0.2)

# アニメーションの初期設定
fig, (ax1, ax2) = plt.subplots(2, 1)
line1, = ax1.plot(t, signal, color='lightblue')  # 止まっている信号のグラフを青色に設定
line2, = ax2.plot([], [])
ax1.set_title("Signal")
ax2.set_title("Autocorrelation")
ax2.set_xlim(0, len(t) // 2)
ax2.set_ylim(-1, 1)
lags = np.arange(0, len(t) // 2)

# アニメーション更新関数
def update(frame):
    shifted_signal = np.roll(signal, -frame)
    line1.set_ydata(shifted_signal)
    line1.set_color('blue')  # ずらしている信号のグラフを赤色に設定
    autocorr = [autocorrelation(shifted_signal, lag) for lag in lags[: frame + 1]]
    line2.set_data(lags[: frame + 1], autocorr)
    return line1, line2,

# アニメーション作成
ani = FuncAnimation(fig, update, frames=len(t) // 2, interval=20, blit=True, init_func=lambda: (line1, line2))

# タイトルが重ならないように調整
plt.tight_layout()

plt.show()
