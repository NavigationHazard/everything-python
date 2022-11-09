from PyPDF2 import PdfFileReader
import pandas as pd
import tabula

reader = tabula.read_pdf('example.pdf', pages='all')
tabula.convert_into("example.pdf", "iplmatch.csv", output_format="csv", pages="all")

