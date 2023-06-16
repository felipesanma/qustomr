import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask

logo = Image.open("logo/chasquilla.png")

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    version=2,
    border=1,
    box_size=12,
)

url_to_code = "https://blog.chasquillaengineer.com/"
qr.add_data(url_to_code)

qr_img = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=ImageColorMask(back_color=(255, 255, 255), color_mask_image=logo),
)
qr_img.save("qrcode.png")
