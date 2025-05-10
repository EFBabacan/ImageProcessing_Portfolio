# Week 4: Image Thresholding and Morphological Operations

This directory contains Python scripts for "Week 4", covering various image thresholding techniques and an introduction to basic morphological operations. Thresholding is a key step in image segmentation, while morphological operations are used to process and analyze the shapes of objects, typically in binary images. These scripts primarily utilize OpenCV and Matplotlib.

## Scripts Overview

The following scripts are included in this week's studies:

* **`static_thresholding_example.py`**: Demonstrates five static (fixed value) thresholding types available in OpenCV's `cv2.threshold()` function (Binary, Binary Inverse, Truncate, To Zero, and To Zero Inverse). Allows experimentation with different global threshold values. (Corresponds to "5.pdf" - Kod 3.10)
* **`otsu_thresholding_example.py`**: Implements Otsu's binarization method using `cv2.threshold()` with the `cv2.THRESH_OTSU` flag. This method automatically determines an optimal global threshold value, particularly effective for bimodal images. Displays the original image, its histogram with Otsu's calculated threshold, and the resulting binarized image. (Corresponds to "5.pdf" - Kod 3.11)
* **`kapur_entropy_thresholding_example.py`**: Implements Kapur's entropy method for automatic image thresholding. The provided script uses a manual calculation of Kapur's algorithm to find an optimal threshold by maximizing the sum of entropies of foreground and background pixels. Displays the original image, its histogram with Kapur's threshold, and the binarized image. (Corresponds to "5.pdf" - Kod 3.12)
* **`morphological_operations_example.py`**: Demonstrates fundamental morphological operations such as Erosion, Dilation, Opening, and Closing using OpenCV functions like `cv2.erode()`, `cv2.dilate()`, and `cv2.morphologyEx()`. These operations are typically applied to binary images.

## Libraries Used

* OpenCV (`opencv-python`): For image loading, thresholding operations, and morphological operations.
* NumPy: For numerical operations and array manipulation, essential for image data.
* Matplotlib: For displaying original images, processed images, and histograms.
* `scikit-image`: (Was considered for Kapur's method, but the current `kapur_entropy_thresholding_example.py` uses a manual approach to avoid import issues encountered earlier).
* Python `random` module: (May be used if noise is added for demonstrating certain operations).

## How to Run & Image Path Convention

Each `.py` script in this directory can be run individually using a Python interpreter.

* **Image Requirement:**
    * All scripts are configured to load images from a subfolder named **`sample_images`** located *within this `week4_thresholding_and_morphology` directory*.
    * You should create this `sample_images` folder if it doesn't already exist and place your desired test images (e.g., `foto1.jpeg`, `clean.jpeg`, `flowers.jpg`) inside it.
    * The `IMAGE_PATH` variable at the beginning of each script must be updated to point to the correct image file within this `sample_images` subfolder. For example:
        ```python
        IMAGE_PATH = "sample_images/foto1.jpeg"
        # or for a different image:
        IMAGE_PATH = "sample_images/flowers.jpg"
        ```
* **Dependencies:** Ensure you have the necessary libraries installed in your Python virtual environment:
    ```bash
    pip install opencv-python numpy matplotlib Pillow scikit-image
    ```
    *(Note: `scikit-image` might not be strictly necessary for the current set of scripts if only the manual Kapur implementation is used and no other skimage functions are utilized.)*

---

# Hafta 4: Görüntü Eşikleme ve Morfolojik Operasyonlar

Bu dizin, "Hafta 4" konularını kapsayan, çeşitli görüntü eşikleme tekniklerini ve temel morfolojik operasyonlara bir girişi gösteren Python betiklerini içermektedir. Eşikleme, görüntü segmentasyonunda önemli bir adımdır. Morfolojik operasyonlar ise genellikle ikili (binary) görüntülerdeki nesnelerin şekillerini işlemek ve analiz etmek için kullanılır. Bu betikler öncelikle OpenCV ve Matplotlib kütüphanelerini kullanır.

## Betiklere Genel Bakış

Bu haftaki çalışmalarda aşağıdaki betikler bulunmaktadır:

* **`static_thresholding_example.py`**: OpenCV'nin `cv2.threshold()` fonksiyonunda bulunan beş farklı statik (sabit değerli) eşikleme türünü (Binary, Binary Inverse, Truncate, To Zero, ve To Zero Inverse) gösterir. Kullanıcıların farklı global eşik değerleriyle denemeler yapmasına olanak tanır. ("5.pdf" - Kod 3.10'a karşılık gelir)
* **`otsu_thresholding_example.py`**: `cv2.THRESH_OTSU` bayrağı ile `cv2.threshold()` fonksiyonunu kullanarak Otsu'nun ikilileştirme yöntemini uygular. Bu yöntem, özellikle bimodal (iki tepe noktalı histograma sahip) görüntüler için otomatik olarak en uygun global eşik değerini belirler. Orijinal görüntüyü, Otsu'nun hesapladığı eşik ile histogramını ve sonuçtaki ikili görüntüyü gösterir. ("5.pdf" - Kod 3.11'e karşılık gelir)
* **`kapur_entropy_thresholding_example.py`**: Otomatik görüntü eşikleme için Kapur'un entropi yöntemini uygular. Sağlanan betik, Kapur algoritmasının manuel bir implementasyonunu kullanmaktadır. Ön plan ve arka plan piksellerinin entropileri toplamını maksimize ederek gri tonlamalı bir görüntüyü ikili hale getirmek için en uygun eşik değerini hesaplar. Orijinal görüntüyü, Kapur eşiği ile histogramını ve ikili görüntüyü gösterir. ("5.pdf" - Kod 3.12'ye karşılık gelir)
* **`morphological_operations_example.py`**: OpenCV'nin `cv2.erode()`, `cv2.dilate()` ve `cv2.morphologyEx()` gibi fonksiyonlarını kullanarak Aşındırma (Erosion), Genişletme (Dilation), Açma (Opening) ve Kapama (Closing) gibi temel morfolojik operasyonları gösterir. Bu operasyonlar genellikle ikili görüntülere uygulanır.

## Kullanılan Kütüphaneler

* OpenCV (`opencv-python`): Görüntü yükleme, eşikleme ve morfolojik operasyonlar için.
* NumPy: Sayısal işlemler ve görüntü dizisi manipülasyonu için.
* Matplotlib: Orijinal ve işlenmiş görüntüleri ile histogramları göstermek için.
* `scikit-image`: (Kapur metodu için düşünülmüştü, ancak mevcut `kapur_entropy_thresholding_example.py` betiği daha önce karşılaşılan import sorunları nedeniyle manuel bir yaklaşım kullanmaktadır).
* Python `random` modülü: (Bazı örneklerde gösterim amacıyla yapay gürültü eklemek için kullanılabilir).

## Nasıl Çalıştırılır ve Resim Yolu Standardı

Bu dizindeki her bir `.py` betiği Python yorumlayıcısı kullanılarak ayrı ayrı çalıştırılabilir.

* **Görüntü Gereksinimi:**
    * Tüm betikler, görüntü dosyalarını bu `week4_thresholding_and_morphology` dizini içinde bulunan **`sample_images`** adlı bir alt klasörden yükleyecek şekilde yapılandırılmıştır.
    * Bu `sample_images` klasörünü oluşturmanız (eğer henüz yoksa) ve istediğiniz test görüntülerini (örneğin, `foto1.jpeg`, `clean.jpeg`, `flowers.jpg`) içine yerleştirmeniz gerekmektedir.
    * Her betiğin başındaki `IMAGE_PATH` değişkeni, bu alt klasör içindeki doğru görüntü dosyasını gösterecek şekilde güncellenmelidir. Örneğin:
        ```python
        IMAGE_PATH = "sample_images/foto1.jpeg"
        # veya farklı bir resim için:
        IMAGE_PATH = "sample_images/flowers.jpg"
        ```
* **Bağımlılıklar:** Python sanal ortamınızda gerekli kütüphanelerin kurulu olduğundan emin olun:
    ```bash
    pip install opencv-python numpy matplotlib Pillow scikit-image
    ```
    *(Not: Sadece sağlanan manuel Kapur implementasyonunu kullanıyorsanız ve başka skimage fonksiyonları kullanılmıyorsa `scikit-image` kesinlikle gerekli olmayabilir.)*