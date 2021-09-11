import cv2





cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

imgcounter = 0

while True:
    ret, frame= cam.read()
    if not ret:
        print("Frame not retrieved")
        break
    cv2.imshow("test", frame)


    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escaping, Closing")
        break
    elif k%256 == 32:
        img = "Chelsea1in2021!.png".format(imgcounter)
        cv2.imwrite(img, frame)
        print("() written".format(img))
        imgcounter += 1

cam.release()

cv2.destroyAllWindows
