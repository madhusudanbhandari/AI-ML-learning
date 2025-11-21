#qr code generator
import qrcode

data=input('Enter the text of URL: ').strip()
filename=input('enter the filename: ').strip()
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color='black',back_color='white')
image.save(filename)
print('QR code saved as ')