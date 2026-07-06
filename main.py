from fpdf import FPDF
import pandas as pd
# using FPDF we can create PDF objects
pdf = FPDF(orientation="P",unit="mm",format="A4")
# preventing automatic page break when content reaches bottom
pdf.set_auto_page_break(auto=False,margin=0)
df = pd.read_csv("topics.csv")
for index,row in df.iterrows():
# add_page is a method in PDF object instance
    pdf.add_page( )
    pdf.set_font(family = "times",style="B",size=24)
    pdf.set_text_color(100,100,100)
# w- width of cell
# h- height od the cell
#border - 0: dont show cell border,1: show cell border
#ln - 0:include break line after the cell,1: dont include break line
    pdf.cell(w=0,h=12,txt=row["Topic"],align = "L",ln=1,border= 0)
    # x1,y1 will be starting coordinate of the line and x2,y2 will be end coordinate
    pdf.line(10,22,200,22)
    pdf.ln(265)# add a break line 278 mm below from top
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R") 
    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(265)# add a break line 278 mm below from top
        pdf.set_font(family="Times",style="I",size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row["Topic"],align="R") 


pdf.output("output.pdf")


