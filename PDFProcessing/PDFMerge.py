import PyPDF2
import sys
input_File=sys.argv[1:]
def PdF_Combiner(Pdf_List):
    Merger=PyPDF2.PdfFileMerger()
    for file in Pdf_List:
        Merger.append(file)
    Merger.write("Super.Pdf")
PdF_Combiner(input_File)