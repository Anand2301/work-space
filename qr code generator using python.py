import qrcode
a=input("")
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
qr.add_data(a)
qr.make(fit=True)
img=qr.make_image(back_color="white",fill_color="green")
img.save("qr.png")
u=input()
p=input()
if u=="anand.e" and p=="2001.":
    img.show("qr.png")
else:
    print("enter the correct data")
