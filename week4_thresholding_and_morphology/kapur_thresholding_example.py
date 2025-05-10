import cv2
import numpy as np
import matplotlib.pyplot as plt

def kapur_threshold(image):
    hist, _ = np.histogram(image.ravel(), bins=256, range=(0, 256))
    hist = hist.astype(np.float32)
    hist /= hist.sum()

    cumsum = np.cumsum(hist)
    cumsum_inv = np.cumsum(hist[::-1])[::-1]

    entropy_b = np.zeros(256)
    entropy_f = np.zeros(256)

    for t in range(1, 255):
        if cumsum[t] > 0:
            p_b = hist[:t+1] / cumsum[t]
            entropy_b[t] = -np.sum(p_b[p_b > 0] * np.log(p_b[p_b > 0]))
        if cumsum_inv[t+1] > 0:
            p_f = hist[t+1:] / cumsum_inv[t+1]
            entropy_f[t] = -np.sum(p_f[p_f > 0] * np.log(p_f[p_f > 0]))

    total_entropy = entropy_b + entropy_f
    return np.argmax(total_entropy)

# Görüntüyü oku
IMAGE_PATH = "sample_images/foto1.jpeg"
gray_image = cv2.imread(IMAGE_PATH, 0)
if gray_image is None:
    raise FileNotFoundError(f"Görüntü bulunamadı: {IMAGE_PATH}")

# Eşikleme
thresh_kapur_val = kapur_threshold(gray_image)
binary_image_kapur = gray_image > thresh_kapur_val

# Görselleri yan yana çiz
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Gri görüntü
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Grayscale Image")
axes[0].axis('off')

# 2. Histogram
axes[1].hist(gray_image.ravel(), bins=256, range=(0, 256), color='gray')
axes[1].axvline(thresh_kapur_val, color='red', linestyle='--', label=f'Thresh: {thresh_kapur_val}')
axes[1].set_title("Histogram + Kapur Threshold")
axes[1].legend()

# 3. İkili görüntü
axes[2].imshow(binary_image_kapur, cmap='gray')
axes[2].set_title("Kapur Thresholded")
axes[2].axis('off')

plt.tight_layout()
plt.show()
