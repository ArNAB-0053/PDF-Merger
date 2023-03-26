import PyPDF2 as pdf

# path1 = "05_PdfMerger/1.pdf"
# path2 = "05_PdfMerger/2.pdf"
# pdfFilies = [path1, path2]
n = int(input('Enter number of pdfs: '))

pdfFilies = []
for i in range (0, n):
    file = input("Enter pdf file name: ")
    pdfFilies.append(f"05_PdfMerger/{file}.pdf")
print(pdfFilies)

merger = pdf.PdfMerger()
for filename in pdfFilies:
    pdfFilies = open(filename, 'rb')
    pdfReader = pdf.PdfReader(pdfFilies)
    merger.append(pdfReader)
pdfFilies.close()
merger.write('05_PdfMerger/merged.pdf')