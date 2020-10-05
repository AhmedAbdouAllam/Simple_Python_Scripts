import sys
from PIL import Image,ImageFilter
from pathlib import Path
Input_File_Name=sys.argv[1]
Output_File_Name=sys.argv[2]
InputFile=Path(".\\"+Input_File_Name+"\\")


OutputFile=Path(Output_File_Name)
if  not OutputFile.is_dir():
    Path(Output_File_Name+"\\").mkdir(parents=True, exist_ok=True)

Paths=Path(Input_File_Name).glob('**/*.jpg')
if InputFile.is_dir():
    for x in Paths:
         img=Image.open(str(x))
         img.save(Output_File_Name+"\\"+str(x).split("\\")[1].split(".")[0]+".png","PNG")


