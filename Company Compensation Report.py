from datetime import datetime 
import json

def average(workers) :
    return round(sum(workers) / len(workers), 1) if workers else 0

company = {}
highest_salary = 0
lowest_salary = float('inf')
top_paid_employee    = ""
lowest_paid_employee = ""
departement_top_paid_employee = ""
departement_low_paid_employee = ""

while True :
    departement = input(" The departement ,'Done' to finish or 'Exit' to quit : ").strip()

    if departement.capitalize() == 'Exit' :
        print("program is closed, see you next time ! ")
        break
    if departement.capitalize() == 'Done' :
        break
    if departement == "" :
        print("enter a valid departement name !")
        continue
    if departement not in company :
        company[departement] = {}

    while True :

        employee = input(f" Enter employee name from {departement} or 'Done' to finish : " )

        if employee.capitalize() == 'Done' :
            break
        if employee == "" :
            print("enter a valid employee name !")
            continue
        try :
            salary = int(input(f" enter the salary of {employee} : "))
            if salary < 0 :
                print(" the salary can't be negative !")
                continue

        except ValueError :
            print("a valid number !")  
            continue

        company[departement][employee] = salary

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")   


if company :
    average_departements = {}


    for departements,employees in company.items() :
        for employee,salaries in employees.items() :
            if salaries > highest_salary :
                highest_salary = salaries
                top_paid_employee = employee
                departement_top_paid_employee = departements

            if salaries < lowest_salary :
                lowest_salary = salaries
                lowest_paid_employee = employee
                departement_low_paid_employee = departements


        all_salaries        = list(employees.values())            
        average_departement = average(all_salaries)
        average_departements[departements] = average_departement

# FINAL REPORT Dic
report = {
    "timestamp": timestamp,
    "top_paid_employee": {
        "name": top_paid_employee,
        "salary": highest_salary,
        "department": departement_top_paid_employee
    },
    "lowest_paid_employee": {
        "name": lowest_paid_employee,
        "salary": lowest_salary,
        "department": departement_low_paid_employee
    },
    "average_departments": average_departements,
    "company": company
}

# save t json 
with open("company_report.json", "w") as f:
    json.dump(report, f, indent=4)

# save a readable txt for user
with open("company_report.txt", "w") as f:
    f.write(f"Report generated on: {timestamp}\n\n")
    f.write("=== Top Paid Employee ===\n")
    f.write(f"Name: {top_paid_employee}\n")
    f.write(f"Salary: {highest_salary}\n")
    f.write(f"Department: {departement_top_paid_employee}\n\n")

    f.write("=== Lowest Paid Employee ===\n")
    f.write(f"Name: {lowest_paid_employee}\n")
    f.write(f"Salary: {lowest_salary}\n")
    f.write(f"Department: {departement_low_paid_employee}\n\n")

    f.write("=== Average Salary per Department ===\n")
    for dep, avg in average_departements.items():
        f.write(f"{dep}: {avg}\n")

    f.write("\n=== Company Structure ===\n")
    for dep, employees in company.items():
        f.write(f"\n{dep}:\n")
        for emp, sal in employees.items():
            f.write(f"  - {emp}: {sal}\n")

print("\nReport saved to 'company_report.json' and 'company_report.txt'.")



