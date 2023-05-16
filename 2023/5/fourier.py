import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def rectangular_signal(t, T):
    return np.where(np.abs(t) < T/2, 1, 0)

def fourier_transform(signal, dt):
    N = len(signal)
    frequencies = np.fft.fftfreq(N, dt)
    spectrum = np.fft.fft(signal)
    spectrum /= N  # スケーリング係数の正規化
    return frequencies, np.abs(spectrum)

# パラメータ設定
T_max = 1.0  # 矩形信号の最大幅
dt = 0.001  # 時間刻み
t = np.arange(-10, 10, dt)  # 時間軸

# プロットの準備
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# グラフの初期化
line1, = ax1.plot([], [])
ax1.set_xlim(t[0], t[-1])
ax1.set_ylim(0, 1.5)
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax1.set_title('Rectangular Signal')

line2, = ax2.plot([], [])
ax2.set_xlim(-10, 10)
ax2.set_ylim(0, 0.05)
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Magnitude')
ax2.set_title('Fourier Transform')
ax2.grid(True)
# プロットの更新関数
def update(frame):
    T = T_max * (1 - frame/100)  # 矩形信号の幅を短くする
    signal = rectangular_signal(t, T)
    frequencies, spectrum = fourier_transform(signal, dt)

    line1.set_data(t, signal)
    line2.set_data(frequencies, spectrum)
    return line1, line2

# アニメーションの生成
animation = FuncAnimation(fig, update, frames=99, interval=50, blit=True ,repeat=False)
animation.save("./2023/5/plot-fourier-real.gif", writer="imagemagick")
# アニメーションの表示
plt.tight_layout()
plt.show()
