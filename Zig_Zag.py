import cv2

path = r'hazard.png'

image = cv2.imread(path)

windowname = "Image"

start_p = (0,20)

end_p = (200,20)

colouredp445 = (148,0,211)

thickbabyjohnson = 9

image2 = cv2.line(image, start_p, end_p, colouredp445, thickbabyjohnson)

start_p2 = (200,20)

end_p2 = (0,100)

colouredp44 = (148,0,211)

thickbabymendy = 9

image23 = cv2.line(image, start_p2, end_p2, colouredp44, thickbabymendy)

start_p3 = (0,100)

end_p3 = (260,300)

colouredp4 = (148,0,211)

thickbabysemdo = 9

image234 = cv2.line(image, start_p3, end_p3, colouredp4, thickbabysemdo)

cv2.imshow(windowname, image)

cv2.waitKey(0)

cv2.destroyAllWindows()
