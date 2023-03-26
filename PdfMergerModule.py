import PyPDF2 as pdf

class PdfMerger():
    def __init__(self) -> None:
        pass

    def pdfMerger(numberOfPdf = 2):

        pdfFilies = []

        try: 
            for i in range (0, numberOfPdf):
                file = input("Enter pdf file name: ")
                pdfFilies.append(f"{file}.pdf")
            print(pdfFilies)

        except Exception as e:
            print("An error occure: ",e)

        merger = pdf.PdfMerger()
        for filename in pdfFilies:
            pdfFilies = open(filename, 'rb')
            pdfReader = pdf.PdfReader(pdfFilies)
            merger.append(pdfReader)
        pdfFilies.close()
        merger.write('merged.pdf') 

    pdfMerger(2)


