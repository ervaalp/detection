# detection
import cv2

# matplotlib: veri görselleştirme, grafik oluşturma kütüphanesidir.
# pyplot: grafik oluşturma fonksiyonu. (matlabdaki gibi)
from matplotlib import pyplot

#resmi aç
imaging = cv2.imread("img_bigbangteo.png")

# dönüşümleri yaptır
imaging_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY)
imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)

# Haar cascade: önceden eğitilmiş modelleri kullanarak belirli nesneleri bir görüntüde tespit etmek için kullanılan bir algoritmadır
xml_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# nesneyi algıla, özelliklerini belirle
detecting = xml_data.detectMultiScale(imaging_gray,
                                   minSize = (30, 30))
#
amountDetecting = len(detecting)  # dikdörtgene alınacak nesne sayısı

if amountDetecting != 0:
    for (a, b, width, height) in detecting:
        # rectangle: algılanan nesneyi dikdörtgen içine alma
        cv2.rectangle(imaging_rgb, (a, b),
                      (a + height, b + width),  #a,b ler köşe noktaları
                      (0, 275, 0), 5)           # (renk),kalınlık

pyplot.subplot(1, 1, 1)

pyplot.imshow(imaging_rgb)  #görüntüyü ekranda gösterme
pyplot.show() #görüntünün görüntülenmesi
