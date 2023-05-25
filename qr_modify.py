import qrcode
from PIL import Image
qr =qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=15,border=10)
qr.add_data("https://www.linkedin.com/in/riya-ghalyan-a2334719b/")
qr.make(fit=True)
img=qr.make_image(fill_color="purple",back_color="white")
img.save("Linkedin.png")
