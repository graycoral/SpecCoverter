import os
import PyPDF2
import logging
import collections

class PdfConver:
    PdfFilename = None
    FileReader = None
    FileReference = None
    path = None
    def __init__(self, arg):
        print("PdfCover Start ")
        self.path = os.path.abspath(".")
        self.PdfFilename = str(self.path) + "/"+ str(arg.i)
        self.FileReader = PyPDF2.PdfFileReader(open(self.PdfFilename, "rb"))  # PdfFileReader object

    def DoPdf(self):
        print("PdfCover DoPdf")
        self.FindReference()
        self.openPdf()
    def FindReference(self):
        self.FileReference = self.FileReader.documentInfo
        print("PdfCover FindReference : " + str(self.FileReference))
    def openPdf(self):
        number_of_pages = self.FileReader.getNumPages()
        c = collections.Counter(range(number_of_pages))
        for i in c:
            page = self.FileReader.getPage(i)
            page_content = page.extractText().encode('utf-8')
            print(page_content)

