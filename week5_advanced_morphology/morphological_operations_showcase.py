import cv2  # OpenCV for image loading and morphological operations
import numpy as np
import matplotlib.pyplot as plt

# Path to your image file within the sample_images subfolder of week5.
# Create 'week5_morphological_operations/sample_images/' and place your image there.
IMAGE_PATH = "sample_images/foto1.jpeg"  # Veya "flowers.jpg", "clean.jpeg" gibi başka bir resim kullan

try:
    # Load the image
    original_image_bgr = cv2.imread(IMAGE_PATH)

    if original_image_bgr is None:
        raise FileNotFoundError(f"Resim '{IMAGE_PATH}' yolunda bulunamadı veya açılamadı.")

    # Convert to grayscale
    gray_image = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2GRAY)
    print(f"'{IMAGE_PATH}' başarıyla gri tonlamalı olarak yüklendi.")

    # --- Resmi ikili (binary) hale getirme (Otsu metoduyla) ---
    # Morfolojik operasyonlar genellikle ikili görüntülerde daha net sonuçlar verir.
    # THRESH_BINARY_INV kullanarak ilgilenilen nesnelerin beyaz (255), arka planın siyah (0) olmasını sağlıyoruz.
    ret_otsu, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    print(f"Resim Otsu eşik değeri ({ret_otsu}) ile ikili hale getirildi.")
    print("Morfolojik operasyonlar için nesnelerin beyaz (255), arka planın siyah (0) olduğu varsayılır.")

    # --- Yapılandırma elemanı (kernel) tanımlama ---
    # PDF Kod 3.13 "kernel = ones((5,5), uint8)" kullanıyor.
    kernel_size = 5
    # kernel = np.ones((kernel_size, kernel_size), np.uint8) # PDF'teki gibi NumPy ile
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))  # Veya OpenCV ile
    print(f"{kernel_size}x{kernel_size} boyutunda dikdörtgen bir kernel kullanılıyor.")

    # --- PDF Kod 3.13'teki Morfolojik Operasyonları Uygulama ---

    # 1. Aşındırma (Erosion)
    eroded_image = cv2.erode(binary_image, kernel, iterations=1)

    # 2. Genişletme (Dilation)
    dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

    # 3. Açma (Opening): Aşındırma -> Genişletme
    opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

    # 4. Kapama (Closing): Genişletme -> Aşındırma
    closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    # 5. Morfolojik Gradyan: Genişletme - Aşındırma
    gradient_image = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernel)

    # 6. Top Hat: Orijinal resim - Açma işlemi sonucu
    tophat_image = cv2.morphologyEx(binary_image, cv2.MORPH_TOPHAT, kernel)

    # 7. Black Hat: Kapama işlemi sonucu - Orijinal resim
    blackhat_image = cv2.morphologyEx(binary_image, cv2.MORPH_BLACKHAT, kernel)

    print(f"'{IMAGE_PATH}' resminin ikili haline 7 morfolojik operasyon uygulandı.")

    # --- Sonuçları Matplotlib ile gösterme (PDF Şekil 3.28'e benzer) ---
    # 8 görüntü göstereceğiz: Orijinal İkili + 7 operasyon. 3x3 grid uygun olur.
    titles = [
        'Binarized Image (Input)', 'Erosion', 'Dilation',
        'Opening', 'Closing', 'Gradient',
        'Top Hat', 'Black Hat', 'Original Grayscale'  # Orijinal griyi de ekleyelim
    ]
    images_to_display = [
        binary_image, eroded_image, dilated_image,
        opened_image, closed_image, gradient_image,
        tophat_image, blackhat_image, gray_image
    ]

    plt.figure(figsize=(15, 15))  # 3x3 grid için figür boyutunu ayarla

    for i in range(len(images_to_display)):
        plt.subplot(3, 3, i + 1)
        plt.imshow(images_to_display[i], cmap='gray')
        plt.title(titles[i], fontsize=10)
        plt.xticks([])  # PDF'teki gibi eksen işaretlerini kaldır
        plt.yticks([])

    plt.tight_layout(pad=1.5)  # Alt grafikler arası boşluğu ayarla
    plt.suptitle("Morphological Operations Showcase (Kernel: 5x5)", fontsize=16, y=0.99)
    plt.subplots_adjust(top=0.95)  # Ana başlık için yer aç
    plt.show()

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    import traceback

    print(f"Beklenmedik bir hata oluştu: {e}")
    traceback.print_exc()
