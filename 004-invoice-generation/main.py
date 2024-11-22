import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob(r"C:\Users\kotla\Desktop\python-megacourse\004-invoice-generation\invoices\*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=12, txt=f"Invoice nr. {invoice_nr}", border=0)

    pdf.output(f"{filename}.pdf")