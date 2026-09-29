import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img_histograma.jpg", cv2.IMREAD_GRAYSCALE)

h = np.bincount(img.ravel(), minlength=256)

rk = np.arange(256)

print("Soma dos nk:", h.sum(), "| MxN:", img.size)

# Gráfico rk versus nk
plt.figure(figsize=(8, 4))
plt.bar(rk, h, width=1.0, color="gray")
plt.title("Histograma da imagem (256 níveis)")
plt.xlabel("Nível de intensidade $r_k$")
plt.ylabel("Número de pixels $n_k$")
plt.xlim(0, 255)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("histograma.png", dpi=150)
plt.show()