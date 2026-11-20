                    #UNIT-3 

#1.Write a Python program to create a simple Contact Book using list & dictionaries. 
contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        print("Contact added successfully.")

    # View contacts
    elif choice == "2":

        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- ALL CONTACTS ---")

            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("-------------------")

    # Search contact
    elif choice == "3":

        search_name = input("Enter name to search: ")

        found = False

        for contact in contacts:

            if contact["name"].lower() == search_name.lower():
                print("\nContact Found")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete contact
    elif choice == "4":

        delete_name = input("Enter name to delete: ")

        found = False

        for contact in contacts:

            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)

                print("Contact deleted successfully.")

                found = True
                break

        if not found:
            print("Contact not found.")

    # Exit
    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice.")

#2. Student grading system list & dictionaries.

student = {}

student["name"] = input("Enter Student Name: ")
student["roll_no"] = input("Enter Roll Number: ")

marks = []

for i in range(1, 4):
    mark = float(input("Enter marks in Subject " + str(i) + ": "))
    marks.append(mark)

student["marks"] = marks

total = sum(student["marks"])
average = total / len(student["marks"])

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

student["total"] = total
student["average"] = round(average, 2)
student["grade"] = grade

print("\n===== STUDENT RESULT =====")
print("Student Name:", student["name"])
print("Roll Number:", student["roll_no"])
print("Subject Marks:", student["marks"])
print("Total Marks:", student["total"])
print("Average Marks:", student["average"])
print("Grade:", student["grade"])



#3. Frequency Counter using Dictionary
text = input("Enter a word or sentence: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\n===== CHARACTER FREQUENCY =====")

for char, count in frequency.items():
    print(char, ":", count)


#4.Student Attendance Tracker
attendance = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    status = input("Enter attendance (Present/Absent): ")

    attendance[name] = status

print("\n===== ATTENDANCE REPORT =====")

present = 0
absent = 0

for name, status in attendance.items():
    print(name, ":", status)

    if status.lower() == "present":
        present += 1
    else:
        absent += 1

print("\nTotal Students:", n)
print("Present Students:", present)
print("Absent Students:", absent)

percentage = (present / n) * 100
print("Attendance Percentage:", round(percentage, 2), "%")
