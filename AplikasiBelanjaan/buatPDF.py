from reportlab.pdfgen import canvas

databelanjaan = {"2020627": {
	"Sapi": {
		"harga": "9000", 
		"kuantitas": "2", 
		"ID": "V6N7Y6", 
		"ex_date": 8}, 
	"Aqua": {
		"harga": "3500", 
		"kuantitas": "1", 
		"ID": "R5E3H2", 
		"ex_date": 8}
		}
}

kode_tanggal = "2020627"

class Data:

	def __init__(self, filename, documentTitle, heading):
		self.filename = filename
		self.documentTitle = documentTitle
		self.heading = heading
		self.info = databelanjaan

myData = Data(str(f"{kode_tanggal}-"+databelanjaan[kode_tanggal]["Sapi"]["ID"]+"-"+databelanjaan[kode_tanggal]["Aqua"]["ID"]+".pdf"), "DAFTAR BELANJAAN", databelanjaan[kode_tanggal])
myPdf = canvas.Canvas(myData.filename)
myPdf.setTitle(myData.documentTitle)
databelanjaan
#PRINT ON PAPER
#myPdf.drawString(300, 770,myData.heading) #x,y,heading

myPdf.setFont("Helvetica", 30)
myPdf.setFillColorRGB(150,0,0)
myPdf.drawCentredString(300, 770,"DAFTAR BELANJAAN")
myPdf.line(30, 760, 560, 760)
#           x1   y1   x2   y2

#object baru untuk menginisiasi text yang banyak sekaligus
myText = myPdf.beginText(40,680)
myText.setFont("Helvetica", 18)

def buat():

	dataSapi = "Sapi : " + "Rp " + databelanjaan[kode_tanggal]["Sapi"]["harga"] + ", " + "Jumlah : " + databelanjaan[kode_tanggal]["Sapi"]["kuantitas"] + ", " + "ID : " + databelanjaan[kode_tanggal]["Sapi"]["ID"]
	dataAqua = "Aqua : " + "Rp " + databelanjaan[kode_tanggal]["Aqua"]["harga"] + ", " + "Jumlah : " + databelanjaan[kode_tanggal]["Aqua"]["kuantitas"] + ", " + "ID : " + databelanjaan[kode_tanggal]["Aqua"]["ID"]

	Lines = [dataSapi, dataAqua]
	for line in Lines:
		myText.textLine(line)
	myPdf.drawText(myText)
	print("PDF telah diupdate")
	#myPdf.drawInlineImage("pic1.JPEG", 130, 400)

	myPdf.save()
#print("OK")