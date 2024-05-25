from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Please enter the amount here: "))
period = input("Please enter the period (E.g. December 2023): ")

name1 = input("Please enter your name here: ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house:  "))

name2 = input("Please enter the name of the other flatmate: ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house:  "))

the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays: ", round(flatmate1.pays(the_bill, flatmate2), 2))
print(f"{name2} pays: ", round(flatmate2.pays(the_bill, flatmate2), 2))

# pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
# pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
