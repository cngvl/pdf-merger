import PyPDF2
import sys
import os

# Change the directory to where your copy of the repository is saved
sourceDirectoryToMerge = ''
os.chdir(sourceDirectoryToMerge)
merger = PyPDF2.PdfMerger(strict=False)

fileNumber = 1
numberOfFiles = len(os.listdir(os.curdir)) - 2

while fileNumber <= numberOfFiles:
    for file in os.listdir(os.curdir):
        if file.endswith(f'{fileNumber}.pdf'):
            merger.append(file)
            fileNumber += 1

# Change the directory to where your copy of the repository is saved
destinationDirectory = ''
os.chdir(destinationDirectory)

# For counting the number of PDF files and then naming the latest merged PDF accordingly
numberOfMergedPDFs = 0
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        # listOfPDFs.append(file)
        numberOfMergedPDFs += 1

merger.write("CombinedPDF_" + str(numberOfMergedPDFs) +".pdf")
