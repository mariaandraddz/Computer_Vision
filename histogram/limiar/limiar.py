import cv2
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

img = cv2.imread("img_histograma.jpg", cv2.IMREAD_GRAYSCALE)
M, N = img.shape
Np = M * N
h = np.bincount(img.ravel(), minlength=256)
rk = np.arange(256)


h_suave = np.convolve(h, np.ones(9) / 9, mode="same")
T_sugerido = 130 + int(np.argmin(h_suave[130:200]))
print("T sugerido pelo vale:", T_sugerido)
T = T_sugerido

plt.figure(figsize=(8, 4))
plt.bar(rk, h, width=1.0, color="gray")
plt.axvline(T, color="red", linestyle="--", linewidth=2, label=f"T = {T}")
plt.title("Histograma com o limiar escolhido")
plt.xlabel("Nível de intensidade $r_k$")
plt.ylabel("Número de pixels $n_k$")
plt.xlim(0, 255)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("histograma_com_limiar.png", dpi=150)

B = np.where(img > T, 255, 0).astype(np.uint8)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))
axs[0].imshow(img, cmap="gray", vmin=0, vmax=255)
axs[0].set_title("Imagem original (tons de cinza)")
axs[0].axis("off")
axs[1].imshow(B, cmap="gray", vmin=0, vmax=255)
axs[1].set_title(f"Imagem limiarizada (T = {T})")
axs[1].axis("off")
plt.tight_layout()
plt.savefig("original_vs_limiarizada.png", dpi=150)

cv2.imwrite("imagem_binaria.png", B)
print("pixels 0:", (B == 0).sum(), "| pixels 255:", (B == 255).sum())