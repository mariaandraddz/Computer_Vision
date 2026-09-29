import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img_histograma.jpg", cv2.IMREAD_GRAYSCALE)

M, N = img.shape
Np = M * N

h = np.bincount(img.ravel(), minlength=256)
rk = np.arange(256)

p = h / Np

S = p.sum()
print(f"S = {S:.10f}")
print("Soma ≈ 1?", np.isclose(S, 1.0))
print(f"Menor p(rk): {p.min():.6f} | Maior p(rk): {p.max():.6f}")

fig, axs = plt.subplots(1, 2, figsize=(12, 4))

axs[0].bar(rk, h, width=1.0, color="gray")
axs[0].set_title("Histograma convencional")
axs[0].set_xlabel("Nível de intensidade $r_k$")
axs[0].set_ylabel("Número de pixels $n_k$")
axs[0].set_xlim(0, 255)
axs[0].grid(alpha=0.3)

axs[1].bar(rk, p, width=1.0, color="steelblue")
axs[1].set_title("Histograma normalizado")
axs[1].set_xlabel("Nível de intensidade $r_k$")
axs[1].set_ylabel("$p(r_k)$")
axs[1].set_xlim(0, 255)
axs[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig("histogramas_lado_a_lado.png", dpi=150)
plt.show()