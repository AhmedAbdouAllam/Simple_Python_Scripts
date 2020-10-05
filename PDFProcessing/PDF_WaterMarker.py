import sys,PyPDF2

InputFiles=sys.argv[2:]
WaterMarkFile=sys.argv[1]
with open (WaterMarkFile,'rb') as water_mark:
    water_read=PyPDF2.PdfFileReader(water_mark)
    water_page=water_read.getPage(0)

    for file in InputFiles:
        merger=PyPDF2.PdfFileMerger()
        writer=PyPDF2.PdfFileWriter()
        with open ("WaterMarked_"+file,'wb') as writen:
            with open(file,'rb') as PDF_File:
                reader=PyPDF2.PdfFileReader(PDF_File)
                for i in range(reader.numPages):
                    page=reader.getPage(i)
                    page.mergePage(water_page)
                    writer.addPage(page)
            writer.write(writen)



