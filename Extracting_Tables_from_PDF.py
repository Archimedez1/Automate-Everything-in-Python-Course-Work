import tabula


table = tabula.read_pdf('number-table-1-100.pdf',pages=1)


print(type(table[0]))

table[0].to_csv('output.csv',index=None)