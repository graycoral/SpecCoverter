import os
import re
import PyPDF2
import logging
import string
import collections

searchRSWord = "RS_Main_"
searchRSSDWord = "RS_SOMEIPSD_"
reqTrace = "RequirementsTracing"

class PdfConver:
    PdfFilename = None
    FileReader = None
    FileReference = None
    path = None
    RS_SOMEIPSD = ""
    Descript = ""
    def __init__(self, arg):
        print("PdfCover Start ")
        self.path = os.path.abspath(".")
        self.PdfFilename = str(self.path) + "/"+ str(arg.i)
        self.FileReader = PyPDF2.PdfFileReader(open(self.PdfFilename, "rb"))  # PdfFileReader object

    def FindReference(self):
        self.FileReference = self.FileReader.documentInfo
        print("PdfCover FindReference : " + str(self.FileReference))

    def FindText(self, xFile, xString):
        # xfile : the PDF file in which to look
        # xString : the string to look for
        PageFound = -1
        for i in range(0, self.FileReader.getNumPages()):
            content = ""
            content += self.FileReader.getPage(i).extractText() + "\n"
            content1 = content.encodeencode('utf-8')
            ResSearch = re.search(xString, content1)
            if ResSearch is not None:
                PageFound = i
                break
        return PageFound
    def SearchandSaveData(self, save, srch, datas):
        for data in datas:
            if srch in data:
                save += srch.strip('[]b')
    def SaveData(self):
        SaveData={}
        for i in range(0, self.FileReader.getNumPages()):
            page = self.FileReader.getPage(i).extractText() + "\n"
            page_content = page.encode('utf-8')
            pageContent = None

            ResSearch = re.search(reqTrace, str(page_content))
            if ResSearch is not None:
                print("FOUND Page for Requirements Tracing")
                RSSearch = re.search(searchRSWord, str(page_content))
                if RSSearch is not None:
                    pageContent = page_content.split()
                    for search in pageContent:
                        if searchRSWord in str(search):
                            feature = str(search)
                            sIdx = feature.find(searchRSWord[0])
                            eIdx = -1
                            if feature.find(']') != -1:
                                eIdx = feature.find(']')
                            print(feature[sIdx:eIdx])
                            """ Find RS_Main """
                            feature[sIdx:eIdx]
                            """ Save RS_SOMEIPSD """
                            for content in pageContent:
                                if searchRSSDWord in str(content):
                                    RS = str(content)
                                    sIdx = RS.find(searchRSSDWord[0])
                                    eIdx = -1
                                    if RS.find(']') != -1:
                                        eIdx = RS.find(']')
                                    key = feature[sIdx:eIdx]
                                    SaveData[str(key)] = [SaveData[str(key)] + RS[sIdx:eIdx]]
                            print(SaveData)
                            """ Save Description """
                    break


    def SaveRSMain(self):
        for i in range(0, self.FileReader.getNumPages()):
            page = self.FileReader.getPage(i).extractText() + "\n"
            page_content = page.encode('utf-8')
            pageContent = None

            ResSearch = re.search(reqTrace, str(page_content))
            if ResSearch is not None:
                print("FOUND Page for Requirements Tracing")
                RSSearch = re.search(searchRSWord, str(page_content))
                if RSSearch is not None:
                    pageContent = page_content.split()
                    for search in pageContent:
                        if searchRSWord in str(search):
                            feature = str(search)
                            sIdx = feature.find(searchRSWord[0])
                            eIdx = -1
                            if feature.find(']') != -1:
                                eIdx = feature.find(']')
                            print(feature[sIdx:eIdx])
                            """ Find RS_Main """
                            feature[sIdx:eIdx]
                            """ Save RS_SOMEIPSD """
                            for content in pageContent:
                                if searchRSSDWord in str(content):
                                    RS = str(content)
                                    sIdx = RS.find(searchRSSDWord[0])
                                    eIdx = -1
                                    if RS.find(']') != -1:
                                        eIdx = RS.find(']')
                                    self.RS_SOMEIPSD += str(RS[sIdx:eIdx]) + " "
                            print(self.RS_SOMEIPSD)
                            """ Save Description """
                    break

    def SearchPdf(self):
        searchWord = "RS_SOMEIPSD_"

    def DoPdf(self):
        #self.SaveRSMain()
        self.SaveData()



