import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)


#READ VIDEO
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("Resources/CamVideo.mp4")
i = 0
while i < 500:
    i = i + 1
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(30) and 0xFF == ord('q'):
         break