import PyPDF2
import sys
import os

# Change the directory to where your copy of the repository is saved
sourceDirectoryToMerge = ''
os.chdir(sourceDirectoryToMerge)
merger = PyPDF2.PdfMerger(strict=False)

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

# Change the directory to where your copy of the repository is saved
destinationDirectory = ''
os.chdir(destinationDirectory)

listOfPDFs = []
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        listOfPDFs.append(file)

merger.write("CombinedPDF_" + str(len(listOfPDFs)) +".pdf")
