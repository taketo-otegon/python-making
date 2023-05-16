import numpy as np
import matplotlib.pyplot as plt

#短形信号の定義
def rectangular_signal(t, T,r):
    return np.where(np.abs(t) < T/r, 1, 0)

#フーリエ変換の計算
def fourier_transform(signal, dt):
    N = len(signal)
    frequencies = np.fft.fftfreq(N, dt)
    spectrum = np.fft.fft(signal)
    spectrum /= N  # スケーリング係数の正規化
    return frequencies, np.abs(spectrum)

# パラメータ設定
T = 1.0  # 矩形信号の幅
dt = 0.001  # 時間刻み
t = np.arange(-10, 10, dt)  # 時間軸
r = 10
# 矩形信号の生成
signal = rectangular_signal(t, T,r)
# フーリエ変換の計算
frequencies, spectrum = fourier_transform(signal, dt)

# 結果のプロット
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Rectangular Signal')

plt.subplot(1, 2, 2)
plt.plot(frequencies, spectrum)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.xlim(-10,10)
plt.title('Fourier Transform')

plt.tight_layout()
plt.show()