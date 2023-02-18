import qrcode

def generate_qr(url):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    return img

url = "https://lichess.org/swiss/o42POW4c"
img = generate_qr(url)
img.save("torneo.png")