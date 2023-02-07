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

url = "http://chess-results.com/tnr719137.aspx?lan=2&art=2&rd=1&turdet=YES&flag=30&fbclid=IwAR2O8No7OB9_eFq12xEtuExUft9N-si4mnpMAH-Nv7bZgKtzCr86DdYvJ60"
img = generate_qr(url)
img.save("chess.png")