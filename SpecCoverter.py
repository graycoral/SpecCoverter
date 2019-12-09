import PyPDF2

PDFfilename = "AUTOSAR_PRS_SOMEIPServiceDiscoveryProtocol.pdf" #filename of your PDF/directory where your PDF is stored

pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object

pg4 = pfr.getPage(126) #extract pg 127

writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object
#add pages
writer.addPage(pg4)

NewPDFfilename = "allTables.pdf" #filename of your PDF/directory where you want your new PDF to be
with open(NewPDFfilename, "wb") as outputStream:
    writer.write(outputStream) #write pages to new PDF