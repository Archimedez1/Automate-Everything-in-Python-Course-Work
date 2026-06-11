from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit= 'pt',format='A4')
pdf.add_page()

pdf.image('Hepheastus.jpg', w=120, h=68)

pdf.set_font(family='Times',style='B',size=24)
pdf.cell(w=0,h=50,txt='Hepheastus',align='C',ln=1)

pdf.set_font(family='Times',style='B',size=14)
pdf.cell(w=0,h=15,txt='Description',align='C',ln=1)

pdf.set_font(family='Times',style='B',size=12)
pdf.cell(w=0,h=25,txt='Hepheastus is the Greek god of fire, metalworking, stone masonry, forges and the art of sculpture.',align='C',ln=1)

pdf.set_font(family='Times',style='B',size=12)
pdf.cell(w=0,h=25,txt='He is the son of Zeus and Hera, and is married to Aphrodite.',align='C',ln=1)

pdf.set_font(family='Times',style='B',size=10)
txt1 = 'Hepheastus is often depicted as a bearded man with a hammer and anvil, working in his forge. ' \
'He is known for his skill in crafting weapons and armor for the gods and heroes of Greek mythology. ' \
'Furthermore, he is associated with volcanoes and is said to have his forge beneath Mount Etna in Sicily. ' \
'Despite his physical deformity, Hepheastus is highly respected among the gods for his craftsmanship and ingenuity.'
pdf.multi_cell(w=0,h=15,txt=txt1)

pdf.set_font(family='Times',style='B',size=14)
pdf.cell(w=100,h=25,txt='Sicily:',align='C')

pdf.set_font(family='Times',size=14)
pdf.cell(w=100,h=25,txt='Greece',align='C',ln=1)


pdf.output('output.pdf')