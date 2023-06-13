import os

import shutil

from PyPDF2 import PdfMerger

#print(os.getcwd())

os.chdir("/Users/valentin/Documents/VHS Kurse/Automatisierung mit Python/Demo Ordner")

#print(os.getcwd())

#print(os.listdir())


merger = PdfMerger()

for f in os.listdir():
    if f.startswith("."):
        continue
    #print(f)

    filename, file_type = os.path.splitext(f)
    #print(filename)
    #print(file_type)

    if "Kapitel" in filename:
        f_chapter, f_title = filename.split("-")

        f_chapter = f_chapter.strip()
        f_title = f_title.strip()
        print(f"{f_title}-{f_chapter}{file_type}")

        new_name = "{}-{}{}".format(f_title, f_chapter, file_type)

        merger.append(f)

        os.remove(f)



        os.renames(f, new_name)

merger.write(os.getcwd() + "/beste_pdf.pdf")
merger.close()

#print(os.getcwd() + "/folder 1")
#os.rmdir(os.getcwd() + "/folder 1")
shutil.rmtree(os.getcwd() + "/folder 2")




