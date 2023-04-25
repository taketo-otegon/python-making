import numpy as np
import matplotlib.pyplot as plt

# 反応係数
k1 = 0.1  # 前進反応
k2 = 0.05  # 後退反応

# 時間
t_total = 100  # 総時間
dt = 0.1  # 時間ステップ
t = np.arange(0, t_total, dt)

# 濃度の初期値
A0 = 1.0
B0 = 0.0

# 空のリストを用意
A = []
B = []

# 初期値をリストに追加
A.append(A0)
B.append(B0)

# ノイズの標準偏差
noise_std = 0.01

# 反応のシミュレーション
for i in range(1, len(t)):
    dA = (-k1 * A[i - 1] + k2 * B[i - 1]) * dt + np.random.normal(0, noise_std)
    dB = (k1 * A[i - 1] - k2 * B[i - 1]) * dt + np.random.normal(0, noise_std)
    A.append(A[i - 1] + dA)
    B.append(B[i - 1] + dB)

# グラフの描画
plt.plot(t, A, label="A")
plt.plot(t, B, label="B")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("Concentration vs Time for a Reversible Reaction with Noise")
plt.legend()
plt.show()





