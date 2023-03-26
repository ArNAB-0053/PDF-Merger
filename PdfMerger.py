import PyPDF2 as pdf

# path1 = "sample.pdf"
# path2 = "dummy.pdf"
# pdfFilies = [path1, path2]
n = int(input('Enter number of pdf file you want to merge: '))

pdfFilies = []
for i in range (0, n):
    file = input("Enter pdf file name: ")
    pdfFilies.append(f"{file}.pdf")
print(pdfFilies)

merger = pdf.PdfMerger()
for filename in pdfFilies:
    pdfFilies = open(filename, 'rb')
    pdfReader = pdf.PdfReader(pdfFilies)
    merger.append(pdfReader)
pdfFilies.close()
merger.write('merged.pdf')