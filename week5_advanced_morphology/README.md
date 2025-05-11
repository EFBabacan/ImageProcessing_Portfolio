# Week 5: Comprehensive Morphological Operations

This directory contains the Python script for "Week 5" of our image processing studies, focusing on a comprehensive set of morphological operations. These operations are fundamental for processing and analyzing the shapes of objects, typically in binary images, and are widely used for tasks like noise removal, object separation/joining, and feature extraction. The script primarily utilizes OpenCV and Matplotlib.

## Script Overview

* **`morphological_operations_showcase.py`**: This script demonstrates seven key morphological operations based on "Kod 3.13" from the provided PDF ("yeni.pdf" / "6. Hafta" material). It applies these operations to a binarized image and displays the results:
    1.  **Erosion**: Erodes away the boundaries of foreground objects.
    2.  **Dilation**: Expands the boundaries of foreground objects.
    3.  **Opening**: An erosion followed by a dilation (removes small noise).
    4.  **Closing**: A dilation followed by an erosion (fills small holes).
    5.  **Morphological Gradient**: The difference between dilation and erosion (highlights object outlines).
    6.  **Top Hat**: The difference between the input image and its opening (highlights bright details smaller than the kernel).
    7.  **Black Hat**: The difference between the closing of the input image and the input image (highlights dark details smaller than the kernel).

## Libraries Used

* OpenCV (`opencv-python`): For image loading, binarization (Otsu's method), and core morphological operations (`cv2.erode()`, `cv2.dilate()`, `cv2.morphologyEx()`).
* NumPy: For numerical operations and array manipulation.
* Matplotlib: For displaying the original grayscale image, the binarized image, and the results of all seven morphological operations.

## How to Run & Image Path Convention

The `morphological_operations_showcase.py` script can be run individually using a Python interpreter.

* **Image Requirement:**
    * The script is configured to load an image from a subfolder named **`sample_images`** located *within this `week5_morphological_operations` directory*.
    * You should create this `sample_images` folder if it doesn't already exist and place your desired test images (e.g., `foto1.jpeg`, `clean.jpeg`, or images with distinct shapes) inside it.
    * The `IMAGE_PATH` variable at the beginning of the script must be updated to point to the correct image file within this `sample_images` subfolder. For example:
        ```python
        IMAGE_PATH = "sample_images/foto1.jpeg"
        ```
* **Kernel (Structuring Element):** The script defines a 5x5 rectangular kernel for the morphological operations. You can experiment by changing the `kernel_size` variable or the kernel shape (e.g., `cv2.MORPH_ELLIPSE`, `cv2.MORPH_CROSS`) in the script to observe different effects.
* **Dependencies:** Ensure you have the necessary libraries installed in your Python virtual environment:
    ```bash
    pip install opencv-python numpy matplotlib
    ```

---

# Hafta 5: Kapsamlı Morfolojik Operasyonlar

Bu dizin, görüntü işleme çalışmalarımızın "Hafta 5" konularını içeren Python betiğini barındırmaktadır. Bu hafta, kapsamlı bir morfolojik operasyonlar setine odaklanılmıştır. Bu operasyonlar, genellikle ikili (binary) görüntülerdeki nesnelerin şekillerini işlemek ve analiz etmek için temeldir ve gürültü giderme, nesne ayırma/birleştirme ve özellik çıkarma gibi görevler için yaygın olarak kullanılır. Betik öncelikle OpenCV ve Matplotlib kütüphanelerini kullanır.

## Betiğe Genel Bakış

* **`morphological_operations_showcase.py`**: Bu betik, sağlanan PDF'teki ("yeni.pdf" / "6. Hafta" materyali) "Kod 3.13"e dayanarak yedi temel morfolojik operasyonu gösterir. Bu operasyonları ikili (binarize edilmiş) bir görüntüye uygular ve sonuçları görüntüler:
    1.  **Aşındırma (Erosion)**: Ön plandaki nesnelerin sınırlarını aşındırır.
    2.  **Genişletme (Dilation)**: Ön plandaki nesnelerin sınırlarını genişletir.
    3.  **Açma (Opening)**: Bir aşındırma ve ardından bir genişletmedir (küçük gürültüleri giderir).
    4.  **Kapama (Closing)**: Bir genişletme ve ardından bir aşındırmadır (küçük delikleri doldurur).
    5.  **Morfolojik Gradyan**: Genişletme ile aşındırma arasındaki farktır (nesne dış hatlarını vurgular).
    6.  **Top Hat**: Girdi görüntüsü ile açma işlemi sonucu arasındaki farktır (kernelden küçük parlak detayları vurgular).
    7.  **Black Hat**: Girdi görüntüsünün kapanması ile girdi görüntüsü arasındaki farktır (kernelden küçük karanlık detayları vurgular).

## Kullanılan Kütüphaneler

* OpenCV (`opencv-python`): Görüntü yükleme, ikilileştirme (Otsu metodu) ve temel morfolojik operasyonlar (`cv2.erode()`, `cv2.dilate()`, `cv2.morphologyEx()`) için.
* NumPy: Sayısal işlemler ve dizi manipülasyonu için.
* Matplotlib: Orijinal gri tonlamalı görüntüyü, ikilileştirilmiş görüntüyü ve yedi morfolojik operasyonun sonuçlarını göstermek için.

## Nasıl Çalıştırılır ve Resim Yolu Standardı

`morphological_operations_showcase.py` betiği Python yorumlayıcısı kullanılarak ayrı ayrı çalıştırılabilir.

* **Görüntü Gereksinimi:**
    * Betik, görüntü dosyalarını bu `week5_morphological_operations` dizini içinde bulunan **`sample_images`** adlı bir alt klasörden yükleyecek şekilde yapılandırılmıştır.
    * Bu `sample_images` klasörünü oluşturmanız (eğer henüz yoksa) ve istediğiniz test görüntülerini (örneğin, `foto1.jpeg`, `clean.jpeg` veya belirgin şekilleri olan görüntüler) içine yerleştirmeniz gerekmektedir.
    * Betiğin başındaki `IMAGE_PATH` değişkeni, bu alt klasör içindeki doğru görüntü dosyasını gösterecek şekilde güncellenmelidir. Örneğin:
        ```python
        IMAGE_PATH = "sample_images/foto1.jpeg"
        ```
* **Kernel (Yapılandırma Elemanı):** Betik, morfolojik operasyonlar için 5x5 boyutunda bir dikdörtgen kernel tanımlar. Betik içindeki `kernel_size` değişkenini veya kernel şeklini (örneğin, `cv2.MORPH_ELLIPSE`, `cv2.MORPH_CROSS`) değiştirerek farklı etkiler gözlemleyebilirsiniz.
* **Bağımlılıklar:** Python sanal ortamınızda gerekli kütüphanelerin kurulu olduğundan emin olun:
    ```bash
    pip install opencv-python numpy matplotlib
    ```
