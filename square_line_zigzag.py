
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



start_point3 = (0, 0)

# End coordinate, here (250, 250)
# represents the bottom right corner of image

end_point3 = (250, 250)

# Green color in BGR

color = (0, 255, 0)

# Line thickness of 9 px

thickness = 9

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px

image = cv2.line(image, start_point3, end_point3, color, thickness)

sp = (170,0)

edp = (170,170)

adamcolourson = (255,0,0)

thickbenmendy = 12

imaging = cv2.line(image, sp, edp, adamcolourson, thickbenmendy)

spd = (0,40)

edp2 = (700,120)

adolfcoliter = (255,0,0)

thickgylfi = 12

imaging2 = cv2.line(image, spd, edp2, adolfcoliter, thickgylfi)

spde = (200,0)

edp3 = (300,120)

andycolourson = (255,0,0)

thickgriffy = 12

imaging3 = cv2.line(image, spde, edp3, andycolourson, thickgriffy)


cv2.imshow(windowname, image)

cv2.waitKey(0)

cv2.destroyAllWindows()
