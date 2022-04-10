import os
import document as d
import aspose.words as aw
from pathlib import Path
import ntpath
from docx2pdf import convert

document_list = []
saveOptions = aw.SaveFormat
# first it appends all the doc files.
# we need to filter and check if that file has a .pdf file in it
for path, subdir, files in os.walk(r"the folder name"):
    for name in files:
        if os.path.splitext(os.path.join(path, name))[1] == ".docx":
            document_list.append(os.path.join(path, name))


for document_path in document_list:
    document = aw.Document(document_path)
    convert(document_path, os.path.splitext(document_path)[0] + ".pdf")
    os.remove(document_path)