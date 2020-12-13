import qrcode
import os

directory="/home/david/Documents/WoutDavid.github.io/html"
for file in os.listdir(directory):
    if file.endswith("html"):
        url = directory +"/" + file
        without_extension=os.path.splitext(file)
        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save("/home/david/Documents/WoutDavid.github.io/QRcodes/" + "QR_" + without_extension[0])
