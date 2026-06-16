import tabula
import pandas as pd



table = tabula.read_pdf('Table+and+Text.pdf',pages = 1)

print(table[0])


table[0].to_excel('Table_and_Text.xlsx')