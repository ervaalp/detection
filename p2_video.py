import cv2

#yüz sınıflandırıcısı
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

#video yakalama
video_capture = cv2.VideoCapture(0)

#çevirme ve dikdörtgen içine alma işlemleri
#videoddan kareleri alıp griye çevirmeyi unutmaa!
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
   
    for (a, b, width, height) in faces:
        cv2.rectangle(imaging_rgb, (a, b),
                      (a + height, b + width), 
                      (0, 275, 0), 5)
    return faces

# videoda çerçeve oluşturma
while True:
    result, video_frame = video_capture.read()  
    if result is False:
        break 

    #detect_bounding_box ile akışın her saniyesinde yüz tespiti yapar
    faces = detect_bounding_box(video_frame) 

    cv2.imshow(video_frame)  # çerçeve göster

cv2.destroyAllWindows() #programı(kamerayı) kapat
