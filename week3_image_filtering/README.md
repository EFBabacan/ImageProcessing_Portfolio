# Week 3: Image Filtering Techniques (Comprehensive Collection)

This directory contains Python scripts demonstrating a comprehensive set of image filtering techniques. These scripts cover methods for image smoothing, noise reduction, edge detection, and frequency domain filtering, primarily using OpenCV and Matplotlib.

## Scripts Overview

The following scripts are included:

* **`mean_filter_example.py`**: Demonstrates arithmetic mean filtering using OpenCV's `cv2.blur()` for image smoothing. Shows effects of different kernel sizes.
* **`median_filter_example.py`**: Implements median filtering using OpenCV's `cv2.medianBlur()`. Highly effective for removing salt-and-pepper noise while preserving edges. Includes a function to add synthetic noise for demonstration.
* **`gaussian_filter_example.py`**: Applies Gaussian filtering using OpenCV's `cv2.GaussianBlur()`. Provides smooth blurring and is effective against Gaussian noise. Demonstrates effects on both grayscale and color images.
* **`sobel_filter_example.py`**: Implements the Sobel operator using OpenCV's `cv2.Sobel()` for detecting edges by calculating image gradients (Gx, Gy) and their magnitude.
* **`laplacian_filter_example.py`**: Demonstrates the Laplacian filter (a second-order derivative filter) using OpenCV's `cv2.Laplacian()` for edge detection, highlighting regions of rapid intensity change.
* **`conservative_smoothing_example.py`**: Implements the conservative smoothing filter manually (from scratch). This filter is effective for reducing salt-and-pepper noise while attempting to preserve edges by ensuring pixel values stay within the local neighborhood's min/max range.
* **`prewitt_filter_example.py`**: Implements the Prewitt operator for edge detection using OpenCV's `cv2.filter2D()` with custom Prewitt kernels for Gx and Gy gradients.
* **`fourier_filter_example.py`**: Demonstrates frequency domain filtering by applying a Low-Pass Filter (LPF). It involves 2D Fast Fourier Transform (FFT) using NumPy, creating a mask in the frequency domain, and then applying Inverse FFT.

*(Note: This list reflects the scripts we have prepared. Additional filters from the PDFs, if implemented, would be added here.)*

## Libraries Used

* OpenCV (`opencv-python`): For image loading, core filtering operations, and color conversions.
* NumPy: For numerical operations and image array manipulation.
* Matplotlib: For displaying original and processed images.
* Python `random` module: Used in some scripts to add synthetic noise for demonstration.
* Pillow (PIL Fork): Used for some image loading/conversion in earlier examples, ensure it's available if adapting those.

## How to Run & Image Path Convention

Each `.py` script in this directory can be run individually using a Python interpreter.

**Image Requirement:**
    * All scripts are configured to load images from a subfolder named **`sample_images`** located *within this `week3_image_filtering` directory*.
    * You should create this `sample_images` folder if it doesn't exist and place your desired test images (e.g., `foto1.jpeg`, `sea.jpg`, `flowers.jpg`, `foto2.jpg`, `glider.jpeg`, etc.) inside it.
    * The `IMAGE_PATH` variable at the beginning of each script must be updated to point to the correct image file within this subfolder. For example:
        ```python
        IMAGE_PATH = "sample_images/foto1.jpeg" 
        # or for a different image:
        IMAGE_PATH = "sample_images/flowers.jpg"
        ```
**Dependencies:** Ensure you have the necessary libraries installed in your Python virtual environment:
    ```bash
    pip install opencv-python numpy matplotlib Pillow
    ```

---

# Hafta 3: Görüntü Filtreleme Teknikleri (Kapsamlı Koleksiyon)

Bu dizin, kapsamlı bir görüntü filtreleme teknikleri setini gösteren Python betiklerini içermektedir. Bu betikler, OpenCV ve Matplotlib başta olmak üzere, gürültü azaltma, yumuşatma, kenar tespiti ve frekans alanında filtreleme gibi görevler için yöntemleri kapsar.

## Betiklere Genel Bakış

Aşağıdaki betikler bulunmaktadır:

* **`mean_filter_example.py`**: Görüntü yumuşatma için OpenCV'nin `cv2.blur()` fonksiyonunu kullanarak aritmetik ortalama filtrelemeyi gösterir. Farklı kernel boyutlarının etkilerini sergiler.
* **`median_filter_example.py`**: OpenCV'nin `cv2.medianBlur()` fonksiyonunu kullanarak medyan filtrelemeyi uygular. Kenarları korurken tuz-biber gürültüsünü gidermede oldukça etkilidir. Gösterim için yapay gürültü ekleyen bir fonksiyon içerir.
* **`gaussian_filter_example.py`**: OpenCV'nin `cv2.GaussianBlur()` fonksiyonunu kullanarak Gaussian filtrelemeyi uygular. Ortalama filtreden daha yumuşak bir bulanıklaştırma sağlar ve Gaussian gürültüsüne karşı etkilidir. Hem gri tonlamalı hem de renkli görüntüler üzerindeki etkilerini gösterir.
* **`sobel_filter_example.py`**: Görüntü gradyanlarını (Gx, Gy) ve bunların büyüklüğünü hesaplayarak kenar tespiti için OpenCV'nin `cv2.Sobel()` fonksiyonu ile Sobel operatörünü uygular.
* **`laplacian_filter_example.py`**: Hızlı yoğunluk değişimlerinin olduğu bölgeleri vurgulayan ikinci dereceden bir türev filtresi olan Laplacian filtresini kenar tespiti için OpenCV'nin `cv2.Laplacian()` fonksiyonu ile gösterir.
* **`conservative_smoothing_example.py`**: Konservatif yumuşatma filtresini manuel olarak (sıfırdan) uygular. Bu filtre, piksel değerlerinin yerel komşuluk min/maks aralığında kalmasını sağlayarak kenarları korumaya çalışırken tuz-biber gürültüsünü azaltmada etkilidir.
* **`prewitt_filter_example.py`**: Gx ve Gy gradyanları için özel Prewitt kernelleri ile OpenCV'nin `cv2.filter2D()` fonksiyonunu kullanarak kenar tespiti için Prewitt operatörünü uygular.
* **`fourier_filter_example.py`**: Frekans alanında filtrelemeyi bir Alçak Geçiren Filtre (LPF) uygulayarak gösterir. NumPy kullanarak 2 Boyutlu Hızlı Fourier Dönüşümü (FFT) yapmayı, frekans alanında bir maske oluşturmayı ve ardından Ters FFT uygulamayı içerir.

*(Not: Bu liste hazırladığımız betikleri yansıtmaktadır. PDF'lerdeki ek filtreler uygulanırsa buraya eklenecektir.)*

## Kullanılan Kütüphaneler

* OpenCV (`opencv-python`): Görüntü yükleme, temel filtreleme işlemleri ve renk dönüşümleri için.
* NumPy: Sayısal işlemler ve görüntü dizisi manipülasyonu için.
* Matplotlib: Orijinal ve işlenmiş görüntüleri göstermek için.
* Python `random` modülü: Bazı betiklerde gösterim amacıyla yapay gürültü eklemek için kullanılır.
* Pillow (PIL Forku): Önceki örneklerde bazı görüntü yükleme/dönüştürme işlemleri için kullanıldı, tüm betiklerin uyumluluğu için kurulu olması iyi olur.

## Nasıl Çalıştırılır ve Resim Yolu Standardı

Bu dizindeki her bir `.py` betiği Python yorumlayıcısı kullanılarak ayrı ayrı çalıştırılabilir.

**Görüntü Gereksinimi:**
    * Tüm betikler, görüntü dosyalarını bu `week3_image_filtering` dizini içinde bulunan **`sample_images`** adlı bir alt klasörden yükleyecek şekilde yapılandırılmıştır.
    * Bu `sample_images` klasörünü oluşturmanız ve istediğiniz test görüntülerini (örneğin, `foto1.jpeg`, `sea.jpg`, `flowers.jpg`, `foto2.jpg`, `glider.jpeg` vb.) içine yerleştirmeniz gerekmektedir.
    * Her betiğin başındaki `IMAGE_PATH` değişkeni, bu alt klasör içindeki doğru görüntü dosyasını gösterecek şekilde güncellenmelidir. Örneğin:
        ```python
        IMAGE_PATH = "sample_images/foto1.jpeg" 
        # veya farklı bir resim için:
        IMAGE_PATH = "sample_images/flowers.jpg"
        ```
**Bağımlılıklar:** Python sanal ortamınızda gerekli kütüphanelerin kurulu olduğundan emin olun:
    ```bash
    pip install opencv-python numpy matplotlib Pillow
    ```