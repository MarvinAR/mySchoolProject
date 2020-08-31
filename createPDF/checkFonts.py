from reportlab.pdfgen import canvas

pdf = canvas.Canvas("FI")

for font in pdf.getAvailableFonts():
	print(font)