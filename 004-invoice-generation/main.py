import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

PATH = r"C:\Users\kotla\Desktop\python-megacourse\004-invoice-generation"

filepaths = glob.glob(f"{PATH}\invoices\*.xlsx")

for filepath in filepaths:
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=12, txt=f"Invoice nr. {invoice_nr}", border=0, ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=12, txt=f"{date}", border=0, ln=1)
    pdf.ln(10)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(80, 80, 80)

    # TABLE HEADERS
    columns = list(df.columns)
    for i, col in enumerate(columns):
        width = 50 if i == 1 else 35
        pdf.cell(w=width, h=8, txt=col.replace("_", " ").title(), border=1, ln=(i == len(columns) - 1))

    # TABLE CELLS
    for _i, row in df.iterrows():
        for i, col in enumerate(columns):
            width = 50 if i == 1 else 35
            pdf.cell(w=width, h=8, txt=str(row[col]), border=1, ln=(i == len(columns) - 1))

    # TOTAL PRICE
    total_sum = df["total_price"].sum()
    for i, col in enumerate(columns):
        width = 50 if i == 1 else 35
        text = str(total_sum) if col == "total_price" else ""
        pdf.cell(w=width, h=8, txt=text, border=0, ln=(i == len(columns) - 1))
    pdf.ln(10)

    # TOTAL PRICE
    pdf.cell(w=30, h=8, txt=f"The total price is: {total_sum}", border=0, ln=1)

    # LOGO
    pdf.cell(w=30, h=8, txt=f"PythonHow")
    pdf.image(f"{PATH}/pythonhow.png", w=10)

    pdf.output(f"{filename}.pdf")