from fpdf import FPDF
pdf = FPDF()
numPages=100
for i in range(0, numPages):
    
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(40, 10, txt="Daily Planner", ln=1, align='L')
    top = pdf.y
    pdf.rect(5, 20, 95, 70, style='')
    pdf.rect(5, 100, 95, 132, style='')
    pdf.rect(105, 20, 100, 212, style='')
    pdf.rect(5, 245, 200, 42, style='')
pdf.output('daily_planner.pdf')