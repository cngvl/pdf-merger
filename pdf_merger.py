import PyPDF2
import sys
import os

os.chdir('/Users/vietle/code/pdf-merger/pdf-files-to-merge')
merger = PyPDF2.PdfMerger(strict=False)

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        # print(file)
        merger.append(file)
os.chdir('/Users/vietle/code/pdf-merger/merged-pdf')
merger.write("Combined_PDF.pdf")
