from fpdf import FPDF
import pandas 

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv(r'C:\Users\kotla\Desktop\python-megacourse\003-pdf-template\topics.csv')

pageNum = 0

for index, row in df.iterrows():
    pageNum += 1

    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=1)
    pdf.line(10, 25, 200, 25)

    pdf.ln(260)
    pdf.set_font(family='Times', style='I', size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=f"{pageNum}. {row['Topic']}", align='R', ln=1, border=0)

    for i in range(row['Pages'] - 1):
        pageNum += 1 

        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=f"{pageNum}. {row['Topic']}", align='R', ln=1, border=0)

pdf.output('output.pdf')