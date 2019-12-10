import os
import sys
import logging
import argparse

from Excel import Excel
from PdfConver import PdfConver

excel = None
pdf = None

def parseCommandLine():
    parser = argparse.ArgumentParser(description='AUTOSAR Spec Converter')
    parser.add_argument('-i', metavar='input file [optional]',
                        help='AUTOSAR PDF file', default=os.getcwd())
    parser.add_argument('-o', metavar='output file [optional]', default="AUTOSAR_Spec.xlsx",
                        help='Add the path to the output file. Default path: AUTOSAR_Spec.xlsx')
    return parser

def Run():
    pdf = PdfConver(args)
    pdf.DoPdf()

def main(args):
    """ Main entry point of the program """
    Run()

if __name__ == '__main__':
    parser = parseCommandLine()
    args = parser.parse_args(sys.argv[1:])
    main(args)




