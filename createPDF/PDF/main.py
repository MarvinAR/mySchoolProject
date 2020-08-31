from reportlab.pdfgen import canvas

dataSiswa = {
	"nama" : "Marvin",
	"kelas" : "VII-1",
	"laporan" : "Rapor Kelas 7 Semester 2"
}

class Data:

	def __init__(self,filename, documentTitle, heading):
		self.filename = filename
		self.documentTitle = documentTitle
		self.heading = heading
		self.info = """
		Marvin
		Kelas 8.A
		"""

myData = Data(str(dataSiswa['nama'] + dataSiswa['kelas'] + ".pdf"), "Daftar Belanjaan", dataSiswa['laporan'])
myPdf = canvas.Canvas(myData.filename)
myPdf.setTitle(myData.documentTitle)

#PRINT ON PAPER
#myPdf.drawString(225, 750, myData.heading) #x,y,heading

myPdf.setFont("Helvetica", 30)
myPdf.setFillColorRGB(255,0,0)
myPdf.drawCentredString(300, 770, "Laporan Rapor kelas")
myPdf.line(30, 760, 500, 760)
#			x1  y1   x2   y2

#object baru untuk menginisiasi text yang banyak sekalikgus
myText = myPdf.beginText(40, 680)
myText.setFont("Helvetica", 18)

Lines = ["1. Daging Sapi", "2. Daging Ayam"]

for line in Lines:
	myText.textLine(line)
myPdf.drawText(myText)

myPdf.drawInlineImage("sapi.jpg", 10, 15)
myPdf.drawInlineImage("ayam.jpg", 50, 15)

myPdf.save()
#print("OK")