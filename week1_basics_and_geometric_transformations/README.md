# Week 1: Image Processing Basics & Geometric Transformations

This directory contains the initial Python scripts from the first week of image processing studies. The focus is on loading images, understanding their basic properties, and applying fundamental geometric transformations.

## Scripts Overview

* **`get_image_dimensions.py`**: Loads an image (grayscale), prints its dimensions (height, width) to the console, and displays the grayscale image using Matplotlib. Based on PDF 1 - Örnek 1.
* **`get_image_resolution.py`**: Loads an image, attempts to read its resolution (DPI) from metadata, prints the result to the console, and displays the original image using Matplotlib. Based on PDF 1 - Örnek 2.
* **`bilinear_interpolation.py`**: Defines and demonstrates the bilinear interpolation algorithm. It loads a real image ("foto1.jpeg"), calculates the interpolated pixel value at specific non-integer coordinates for both grayscale and color versions, and prints the results. (Optional visualization code included but commented out). Based on PDF 1 - Kod 2.3.
* **`affine_transformations.py`**: Implements various affine transformations (scaling, rotation, shear, translation, mirroring) on an image using transformation matrices and Pillow/NumPy. It displays the original and transformed images side-by-side using Matplotlib. Based on PDF 1 - Kod 2.4.

## Libraries Used

* Pillow (PIL Fork)
* NumPy
* Matplotlib
* OpenCV (`opencv-python`) - *Used in later weeks, ensure it's installed if running all scripts.*

## How to Run

Each `.py` script in this directory can be run individually using a Python interpreter.

* **Image Requirement:** Most scripts require an image file (e.g., `foto1.jpeg`) to be present **in the same directory** as the script itself. Please ensure you have an image file with the correct name (matching the `IMAGE_PATH` variable inside the script) in this folder.
* **Dependencies:** Ensure you have the necessary libraries installed in your virtual environment:
    ```bash
    pip install Pillow numpy matplotlib opencv-python
    ```

---

# Hafta 1: Görüntü İşleme Temelleri ve Geometrik Dönüşümler

Bu dizin, görüntü işleme çalışmalarının ilk haftasına ait başlangıç seviyesi Python betiklerini içermektedir. Odak noktası, görüntüleri yüklemek, temel özelliklerini anlamak ve temel geometrik dönüşümleri uygulamaktır.

## Betiklere Genel Bakış

* **`get_image_dimensions.py`**: Bir görüntüyü (gri tonlamalı) yükler, boyutlarını (yükseklik, genişlik) konsola yazdırır ve gri tonlamalı görüntüyü Matplotlib kullanarak gösterir. PDF 1 - Örnek 1'e dayanmaktadır.
* **`get_image_resolution.py`**: Bir görüntü yükler, meta verilerinden çözünürlüğünü (DPI) okumayı dener, sonucu konsola yazdırır ve orijinal görüntüyü Matplotlib kullanarak gösterir. PDF 1 - Örnek 2'ye dayanmaktadır.
* **`bilinear_interpolation.py`**: Bilineer enterpolasyon algoritmasını tanımlar ve gösterir. Gerçek bir görüntüyü ("foto1.jpeg") yükler, belirli tam sayı olmayan koordinatlardaki enterpole edilmiş piksel değerini hem gri tonlamalı hem de renkli versiyonlar için hesaplar ve sonuçları yazdırır. (İsteğe bağlı görselleştirme kodu dahil edilmiştir ancak yorum satırı halindedir). PDF 1 - Kod 2.3'e dayanmaktadır.
* **`affine_transformations.py`**: Dönüşüm matrisleri ve Pillow/NumPy kullanarak bir görüntü üzerinde çeşitli afin dönüşümleri (ölçekleme, döndürme, kaydırma, öteleme, aynalama) uygular. Orijinal ve dönüştürülmüş görüntüleri Matplotlib kullanarak yan yana gösterir. PDF 1 - Kod 2.4'e dayanmaktadır.

## Kullanılan Kütüphaneler

* Pillow (PIL Forku)
* NumPy
* Matplotlib
* OpenCV (`opencv-python`) - *Sonraki haftalarda kullanıldı, tüm betikleri çalıştırıyorsanız kurulu olduğundan emin olun.*

## Nasıl Çalıştırılır

Bu dizindeki her bir `.py` betiği Python yorumlayıcısı kullanılarak ayrı ayrı çalıştırılabilir.

* **Görüntü Gereksinimi:** Çoğu betik, bir görüntü dosyasının (örneğin `foto1.jpeg`) betiğin kendisiyle **aynı dizinde** bulunmasını gerektirir. Lütfen bu klasörde doğru ada sahip (betik içindeki `IMAGE_PATH` değişkeniyle eşleşen) bir görüntü dosyanız olduğundan emin olun.
* **Bağımlılıklar:** Sanal ortamınızda gerekli kütüphanelerin kurulu olduğundan emin olun:
    ```bash
    pip install Pillow numpy matplotlib opencv-python
    ```