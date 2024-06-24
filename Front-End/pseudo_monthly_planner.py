from fpdf import FPDF
  
# get start date input
date = 'dummy' # figure a way to get it here from the user
day = 2
month = "January"
daysDict = {"January": 31, "Februay": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 30, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31} # storing no. of days in each month
startMonthBoxCount = daysDict[month] - day #no. of boxes to be printed for starting month
BoxCount = daysDict[month] #no. of boxes to be printed for rest of the months
x,y,w,h = None, None, None, None #figure what these are


pdf = FPDF()
  
for i in range (0,month):
   # Add numPages for the month days
   pdf.add_page()
  
   # set style and size of font 
   # that you want in the pdf
   pdf.set_font("Arial", size = 15)
  

   # create a cell, this is just a example of how to add stuff
   pdf.cell(200, 10, txt = dummy + '' + i, 
         ln = 1, align = 'C')
   
   #create rectangles
   Rect(float x, float y, float w, float h [, string style])
  

   # add another cell
   pdf.cell(200, 10, txt = "to-do",
         ln = 2, align = 'C')
  

   # save the pdf with planner .pdf
pdf.output("planner.pdf")   
