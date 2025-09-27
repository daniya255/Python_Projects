#                 # This program can merge your multiple pdfs into one

from pypdf import PdfReader,PdfWriter

lists=["sample.pdf","hello.pdf","new.pdf","world.pdf"]
lists.sort()
writer=PdfWriter()
for file in lists:
    reader=PdfReader(file)
    for page in reader.pages:
        writer.add_page(page)
with open ("merged.pdf","wb") as f:
    writer.write(f)
import os
# print("Current working directory:", os.getcwd())
