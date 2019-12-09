import sys
import PyPDF2
import textract


class SpecConvert:
    pfr = ""
    def __init__(self, PDFfilename):
        self.pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb"))  # PdfFileReader object

    def openPdf():
        number_of_pages = pfr.getNumPages()
        c = collections.Counter(range(number_of_pages))
        for i in c:
            page = pfr.getPage(i)
            page_content = page.extractText()
            print page_content.encode('utf-8')

