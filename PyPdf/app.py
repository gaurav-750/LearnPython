import PyPDF2


# with open("first.pdf", "rb") as pdffile:
#     reader = PyPDF2.PdfFileReader(pdffile)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotate_clockwise(90)

#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page=page)

#     with open("rotateed.pdf", "wb") as output:
#         writer.write(output)

#! Combining multiple pdfs into one:
merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]

for file_name in file_names:
    merger.append(file_name)

merger.write("output.pdf")
# with open("combined.pdf", "wb") as output:
#     merger.write(output)
