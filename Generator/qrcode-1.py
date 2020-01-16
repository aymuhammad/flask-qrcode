import qrcode
#qr = qrcode.make('https://www.digitalocean.com')
#qr.save('dg.png')
qr = qrcode.QRcode(
		version=1,
		box_size=15,
		border=6,
		)

data = 'https://digitalocean.com'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='red')
img.save('Dg Qrcode.png')