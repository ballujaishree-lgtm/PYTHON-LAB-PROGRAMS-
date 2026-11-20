                        # UNIT - 4

#1. Log File Reader Program

try:
    file = open("log.txt", "r")

    print("===== LOG FILE CONTENTS =====")

    for line in file:
        print(line.strip())

except FileNotFoundError:
    print("Error: Log file not found!")

except PermissionError:
    print("Error: Permission denied to read the file!")

else:
    print("\nLog file read successfully!")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        pass

#2.Student data manager using files.
import csv

filename = "students.csv"

while True:
    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            marks = float(input("Enter marks: "))

            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100.")

            with open(filename, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, roll, marks])

            print("Student details added successfully!")

        elif choice == 2:
            try:
                with open(filename, "r") as file:
                    reader = csv.reader(file)

                    print("\nName\tRoll Number\tMarks")
                    for row in reader:
                        print(row[0], "\t", row[1], "\t", row[2])

            except FileNotFoundError:
                print("Student file not found!")

            else:
                print("Records displayed successfully.")

        elif choice == 3:
            search_roll = input("Enter roll number to search: ")
            found = False

            try:
                with open(filename, "r") as file:
                    reader = csv.reader(file)

                    for row in reader:
                        if row[1] == search_roll:
                            print("\nStudent Found!")
                            print("Name:", row[0])
                            print("Roll Number:", row[1])
                            print("Marks:", row[2])
                            found = True
                            break

                    if not found:
                        print("Student not found.")

            except FileNotFoundError:
                print("Student file not found!")

        elif choice == 4:
            print("Exiting Student Data Manager.")
            break

        else:
            print("Invalid choice! Enter 1 to 4.")

    except ValueError as e:
        print("Input Error:", e)

    finally:
        print("Operation completed.")



#3.CSV-based payroll management system

import csv

filename = "payroll.csv"

while True:
    print("\n===== PAYROLL MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Payroll")
    print("3. Search Employee")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")

            basic = float(input("Enter Basic Salary: "))
            hra = float(input("Enter HRA: "))
            da = float(input("Enter DA: "))
            deduction = float(input("Enter Deduction: "))

            if basic < 0 or hra < 0 or da < 0 or deduction < 0:
                raise ValueError("Salary values cannot be negative!")

            gross = basic + hra + da
            net = gross - deduction

            with open(filename, "a", newline="") as file:
                writer = csv.writer(file)

                if file.tell() == 0:
                    writer.writerow([
                        "Employee ID", "Name", "Basic Salary",
                        "HRA", "DA", "Gross Salary",
                        "Deduction", "Net Salary"
                    ])

                writer.writerow([
                    emp_id, name, basic, hra, da, gross,
                    deduction, net
                ])

            print("Employee payroll added successfully!")

        elif choice == 2:
            try:
                with open(filename, "r", newline="") as file:
                    reader = csv.reader(file)

                    print("\n===== PAYROLL DETAILS =====")

                    for row in reader:
                        print(" | ".join(row))

            except FileNotFoundError:
                print("Payroll file not found!")

            else:
                print("Payroll records displayed successfully.")

        elif choice == 3:
            search_id = input("Enter Employee ID to search: ")
            found = False

            try:
                with open(filename, "r", newline="") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        if row["Employee ID"] == search_id:
                            print("\nEmployee Found!")
                            for key, value in row.items():
                                print(key, ":", value)
                            found = True
                            break

                    if not found:
                        print("Employee not found!")

            except FileNotFoundError:
                print("Payroll file not found!")

        elif choice == 4:
            print("Thank you for using Payroll Management System!")
            break

        else:
            print("Invalid choice! Please enter 1 to 4.")

    except ValueError as e:
        print("Input Error:", e)

    finally:
        print("Operation completed.")


#4.JSON -based log file analyzer

import json

filename = "logs.json"

try:
    with open(filename, "r") as file:
        logs = json.load(file)

    error_count = 0
    warning_count = 0
    info_count = 0

    print("===== LOG FILE ANALYZER =====")

    for log in logs:
        level = log["level"].upper()
        message = log["message"]

        print(level, ":", message)

        if level == "ERROR":
            error_count += 1

        elif level == "WARNING":
            warning_count += 1

        elif level == "INFO":
            info_count += 1

    print("\n===== LOG SUMMARY =====")
    print("Total Logs:", len(logs))
    print("Error Count:", error_count)
    print("Warning Count:", warning_count)
    print("Info Count:", info_count)

except FileNotFoundError:
    print("Error: Log file not found!")

except json.JSONDecodeError:
    print("Error: Invalid JSON file!")

except KeyError as e:
    print("Error: Missing field", e)

except (TypeError, AttributeError):
    print("Error: Invalid log data format!")

else:
    print("\nLog analysis completed successfully!")

finally:
    print("Log analyzer execution completed.")




