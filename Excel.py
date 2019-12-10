import openpyxl
import logging

class Excel:
    FileExcel=None
    FileExcelName = None
    def __init__(self, FileName):
        print("Excel Start")
        self.FileExcelName =self.FileExcelName +".xlsx"

    def DoExcel(self):
        print("Excel Do")



