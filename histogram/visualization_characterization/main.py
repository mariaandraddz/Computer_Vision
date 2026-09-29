import cv2

img = cv2.imread("img_histograma.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Não foi possível abrir a imagem. Verifique o caminho.")

altura, largura = img.shape
total_pixels = altura * largura
i_min = int(img.min())
i_max = int(img.max())
i_media = float(img.mean())

print(f"Largura: {largura} px")
print(f"Altura: {altura} px")
print(f"Total de pixels: {total_pixels}")
print(f"Menor intensidade: {i_min}")
print(f"Maior intensidade: {i_max}")
print(f"Intensidade média: {i_media:.2f}")