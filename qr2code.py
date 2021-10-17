import qrcode

datty = "download.jpg"

qr = qrcode.QRCode(version= 1, box_size=10, border = 1)

qr.add_data(datty)

qr.make(fit = True)

img = qr.make_image(fill_color = 'blue', back_color = 'green')

img.save('MYname23234.jpg')
