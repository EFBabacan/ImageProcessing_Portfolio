# Week 2: Histograms and Color Spaces

This directory contains Python scripts covering topics from the second week of the image processing studies, focusing on histograms, histogram equalization techniques, and color space conversions.

## Scripts Overview

* **`create_grayscale_histograms.py`**: Loads a grayscale image and displays its intensity histogram using different numbers of bins (256, 64, and 8 bins). Based on PDF Kod 2.5.
* **`create_color_histograms.py`**: Loads a color image and calculates/displays the histograms for each color channel (Blue, Green, Red) and the grayscale version on a single plot. Uses OpenCV. Based on PDF Kod 2.6.
* **`histogram_equalization.py`**: Applies standard histogram equalization to a grayscale image to improve contrast and displays the original/equalized images and their histograms. Uses OpenCV. Based on PDF Kod 2.7.
* **`clahe_equalization.py`**: Applies Contrast Limited Adaptive Histogram Equalization (CLAHE) to a grayscale image, providing potentially better local contrast enhancement than standard equalization. Displays original/CLAHE images and histograms. Uses OpenCV. Based on PDF Kod 2.8.
* **`rgb_to_hsv_conversion.py`**: Converts an RGB image to the HSV (Hue, Saturation, Value) color space using Pillow and displays the original image along with the separated H, S, V channels. Based on PDF Kod 2.9 (using library function).
* **`rgb_to_cmyk_conversion.py`**: Converts an RGB image to the CMYK (Cyan, Magenta, Yellow, Key/Black) color space using Pillow and displays the original image along with the separated C, M, Y, K channels. Based on PDF Kod 2.10 (using library function).

## Libraries Used

* OpenCV (`opencv-python`)
* Pillow (PIL Fork)
* NumPy
* Matplotlib

## How to Run

Each `.py` script in this directory can be run individually using a Python interpreter.

* **Image Requirement:** The scripts require an image file (e.g., `foto1.jpeg`, `img1.jpg`, etc.) to be present **in the same directory** as the script itself. Make sure to update the `IMAGE_PATH` variable inside each script to match the name of your image file.
* **Dependencies:** Ensure you have the necessary libraries installed in your virtual environment:
    ```bash
    pip install opencv-python Pillow numpy matplotlib
    ```

---

# Hafta 2: Histogramlar ve Renk Uzayları

Bu dizin, görüntü işleme çalışmalarının ikinci haftasına ait konuları içeren Python betiklerini barındırmaktadır. Bu hafta histogramlar, histogram eşitleme teknikleri ve renk uzayı dönüşümleri üzerine odaklanılmıştır.

## Betiklere Genel Bakış

* **`create_grayscale_histograms.py`**: Gri tonlamalı bir görüntü yükler ve farklı sayıda kutucuk (bin) kullanarak (256, 64 ve 8) yoğunluk histogramını görüntüler. PDF Kod 2.5'e dayanmaktadır.
* **`create_color_histograms.py`**: Renkli bir görüntü yükler ve her bir renk kanalının (Mavi, Yeşil, Kırmızı) ve gri tonlamalı versiyonunun histogramlarını tek bir grafik üzerinde hesaplar/görüntüler. OpenCV kullanır. PDF Kod 2.6'ya dayanmaktadır.
* **`histogram_equalization.py`**: Kontrastı iyileştirmek için gri tonlamalı bir görüntüye standart histogram eşitleme uygular ve orijinal/eşitlenmiş görüntüleri ile histogramlarını görüntüler. OpenCV kullanır. PDF Kod 2.7'ye dayanmaktadır.
* **`clahe_equalization.py`**: Gri tonlamalı bir görüntüye Kontrast Sınırlı Uyarlamalı Histogram Eşitleme (CLAHE) uygular, potansiyel olarak standart eşitlemeden daha iyi yerel kontrast iyileştirmesi sağlar. Orijinal/CLAHE görüntülerini ve histogramlarını görüntüler. OpenCV kullanır. PDF Kod 2.8'e dayanmaktadır.
* **`rgb_to_hsv_conversion.py`**: Bir RGB görüntüsünü Pillow kullanarak HSV (Renk Tonu, Doygunluk, Değer) renk uzayına dönüştürür ve orijinal görüntü ile ayrıştırılmış H, S, V kanallarını görüntüler. PDF Kod 2.9'a dayanmaktadır (kütüphane fonksiyonu kullanılarak).
* **`rgb_to_cmyk_conversion.py`**: Bir RGB görüntüsünü Pillow kullanarak CMYK (Camgöbeği, Galibarda, Sarı, Siyah) renk uzayına dönüştürür ve orijinal görüntü ile ayrıştırılmış C, M, Y, K kanallarını görüntüler. PDF Kod 2.10'a dayanmaktadır (kütüphane fonksiyonu kullanılarak).

## Kullanılan Kütüphaneler

* OpenCV (`opencv-python`)
* Pillow (PIL Forku)
* NumPy
* Matplotlib

## Nasıl Çalıştırılır

Bu dizindeki her bir `.py` betiği Python yorumlayıcısı kullanılarak ayrı ayrı çalıştırılabilir.

* **Görüntü Gereksinimi:** Betiklerin çalışması için bir görüntü dosyasının (örneğin `foto1.jpeg`, `img1.jpg` vb.) betiğin kendisiyle **aynı dizinde** bulunması gerekmektedir. Her betiğin içindeki `IMAGE_PATH` değişkenini kendi görüntü dosyanızın adıyla güncellediğinizden emin olun.
* **Bağımlılıklar:** Sanal ortamınızda gerekli kütüphanelerin kurulu olduğundan emin olun:
    ```bash
    pip install opencv-python Pillow numpy matplotlib
    ```