# importing cv2

import cv2

# path

path = r'square.png'

# Reading an image in default mode

image = cv2.imread(path)

# Window name in which image is displayed

window_name = 'Image'

# Start coordinate, here (0, 0)
# represents the top left corner of image

start_point = (0, 0)

# End coordinate, here (250, 250)
# represents the bottom right corner of image

end_point = (250, 250)

# Green color in BGR

color = (0, 255, 0)

# Line thickness of 9 px

thickness = 9

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px

image = cv2.line(image, start_point, end_point, color, thickness)

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

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey()

cv2.destroyAllWindows()
