import cv2
import numpy as np

def canny_edge_detection(image_path, low_threshold=30, high_threshold=100, kernel_size=5):
    """Mendeteksi tepi menggunakan metode Canny Edge Detection dengan parameter yang dapat disesuaikan"""

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Menggunakan GaussianBlur untuk mengurangi noise
    img_blur = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    # Menerapkan Canny Edge Detection dengan parameter yang dapat diubah
    edges = cv2.Canny(img_blur, low_threshold, high_threshold)

    cv2.imshow("Canny Edge Detection", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("canny_result.jpg", edges)

    return "canny_result.jpg"

# Contoh penggunaan dengan parameter yang dimodifikasi
canny_edge_detection("railtrain.jpg", low_threshold=40, high_threshold=120, kernel_size=3)
