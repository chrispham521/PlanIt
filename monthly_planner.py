from fpdf import FPDF
import math
import cgi


form = cgi.FieldStorage()
startDate = form.getvalue('start_date')
print(startDate)

# # startDate = '03/10/2022'  # figure a way to get start date here from the user
# # derive date values from the input format
# startMonth, startDay, startYear = startDate.split('/')
# startMonth, startDay, startYear = int(
#     startMonth), int(startDay), int(startYear)

# # storing strings for each month variable
# daysDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
#             8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

# # storing no. of days in each month
# daysDict2 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# # no. of boxes to be printed for starting month
# startMonthBoxCount = daysDict2[startMonth] - startDay
# # no. of boxes to printed after the starting month
# boxCount = 0

# # calculate no. of pages for the first month of the planner
# numPages = math.ceil(startMonthBoxCount / 3)
# day = startDay

# # Printing the first month of the planner
# pdf = FPDF()

# for i in range(0, numPages):
#     while day <= daysDict2[startMonth]:
#         # pdf.add_page(orientation = '', format = 'A5', same = False)
#         pdf.add_page()
#         top = pdf.y
#         pdf.set_font("Arial", size=15)

#         if day <= daysDict2[startMonth]:
#             txt = f'{daysDict[startMonth]} {day}'
#             pdf.cell(40, 10, txt=txt, ln=1, align='L')
#         if day <= daysDict2[startMonth]-1:
#             pdf.y, pdf.x = top, 75
#             day += 1
#             txt = f'{daysDict[startMonth]} {day}'
#             pdf.cell(40, 10, txt=txt, ln=1, align='L')
#         if day <= daysDict2[startMonth]-1:
#             pdf.y, pdf.x = top, 140
#             day += 1
#             txt = f'{daysDict[startMonth]} {day}'
#             pdf.cell(40, 10, txt=txt, ln=1, align='L')

#         pdf.y = 235
#         pdf.cell(15, 10, txt="Notes", ln=1, align='C')

#         pdf.rect(10, 20, 60, 212, style='')
#         pdf.rect(75, 20, 60, 212, style='')
#         pdf.rect(140, 20, 60, 212, style='')
#         pdf.rect(10, 245, 190, 42, style='')
#         day += 1


# # print the rest of the planner after the starting month
# day = 1

# for j in range(startMonth+1, 13):
#     while day <= daysDict2[j]:
#         # pdf.add_page(orientation = '', format = 'A5', same = False)
#         pdf.add_page()
#         top = pdf.y
#         pdf.set_font("Arial", size=15)

#         if day <= daysDict2[j]:
#             txt = f'{daysDict[j]} {day}'
#             pdf.cell(40, 10, txt=txt, ln=1, align='L')
#         if day <= daysDict2[j]-1:
#             pdf.y, pdf.x = top, 75
#             day += 1
#             txt = f'{daysDict[j]} {day}'
#             pdf.cell(40, 10, txt=txt, ln=1, align='L')
#         if day <= daysDict2[j]-1:
#             pdf.y, pdf.x = top, 140
#             day += 1
#             txt = f'{daysDict[j]} {day}'
#             pdf.cell(40, 10, txt=txt, ln=1, align='L')

#         pdf.y = 235
#         pdf.cell(15, 10, txt="Notes", ln=1, align='C')

#         pdf.rect(10, 20, 60, 212, style='')
#         pdf.rect(75, 20, 60, 212, style='')
#         pdf.rect(140, 20, 60, 212, style='')
#         pdf.rect(10, 245, 190, 42, style='')
#         day += 1
#     day = 1

# pdf.output('planner.pdf')

