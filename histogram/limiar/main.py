import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img_histograma.jpg", cv2.IMREAD_GRAYSCALE)
M, N = img.shape
Np = M * N

def limiarizar(imagem, T):
    """B = 0 se I <= T, 255 se I > T"""
    return np.where(imagem > T, 255, 0).astype(np.uint8)

T = 191

T1, T2, T3 = 60, T, 220
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
for ax, t, nome in zip(axs, [T1, T2, T3], ["T1", "T2", "T3"]):
    ax.imshow(limiarizar(img, t), cmap="gray", vmin=0, vmax=255)
    ax.set_title(f"{nome} = {t}")
    ax.axis("off")
plt.tight_layout()
plt.savefig("tres_limiares.png", dpi=150)

T_otsu, B_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
T_otsu = int(T_otsu)
B_T = limiarizar(img, T)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))
axs[0].imshow(B_T, cmap="gray", vmin=0, vmax=255)
axs[0].set_title(f"Limiar escolhido (T = {T})")
axs[1].imshow(B_otsu, cmap="gray", vmin=0, vmax=255)
axs[1].set_title(f"Otsu (T_Otsu = {T_otsu})")
for ax in axs:
    ax.axis("off")
plt.tight_layout()
plt.savefig("comparacao_T_otsu.png", dpi=150)

N0 = int(np.sum(B_T == 0))
N1 = int(np.sum(B_T == 255))
P0, P1 = N0 / Np, N1 / Np
print(f"N0 = {N0} | N1 = {N1} | P0 = {P0:.6f} | P1 = {P1:.6f}")
print("P0 + P1 =", P0 + P1)