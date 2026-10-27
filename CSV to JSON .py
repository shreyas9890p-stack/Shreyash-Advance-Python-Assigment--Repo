import csv
import json

employees = []

with open("employees.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        row["EmployeeID"] = int(row["EmployeeID"])
        row["Salary"] = int(row["Salary"])
        employees.append(row)

with open("employees.json", "w") as jsonfile:
    json.dump(employees, jsonfile, indent=4)

print("Employee data successfully converted to JSON.")
