                            # UNIT - 01
#1.Student Information and Academic Summary
'''
name = input("Enter Student Name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
semester = int(input("Enter Semester: "))

mark1 = float(input("Enter Marks in Subject 1: "))
mark2 = float(input("Enter Marks in Subject 2: "))
mark3 = float(input("Enter Marks in Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\nSTUDENT REPORT ")
print(f"Name       : {name}")
print(f"USN        : {usn}")
print(f"Branch     : {branch}")
print(f"Semester   : {semester}")
print(f"Total Marks: {total}")
print(f"Average    : {average:.2f}")


#2. perform the operations

a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
add=a+b
sub=a-b
div=a/b
mul=a*b
mod=a%b
floor=a//b
expo=a**b
print("Addition=",add ,"\nSubtraction:",sub,"\nMultiplication:",mul,"\nDivision:",div,
      "\nMultiplication:",mul,"\nModulus:",mod,"\nFloor division:",floor,"\nExponant:",expo)



#3(a) Simple Calculator for Two Numbers

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\nCALCULATOR ")
print(f"Addition        : {num1 + num2}")
print(f"Subtraction     : {num1 - num2}")
print(f"Multiplication  : {num1 * num2}")
print(f"Division        : {num1 / num2}")
print(f"Floor Division  : {num1 // num2}")
print(f"Modulus         : {num1 % num2}")
print(f"Power           : {num1 ** num2}")

#3(b).Area of circle 
radius = float(input("Enter radius of the circle: "))
area = 3.14159 * radius * radius
print("Area of the circle =", area)


'''
#4.Electricity Bill Generator 
print("========== ELECTRICITY BILL GENERATOR ==========")
consumer_name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")
previous_reading = float(input("Enter Previous Meter Reading (kWh): "))
current_reading = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (₹): "))
units = current_reading - previous_reading
energy_charge = units * cost_per_unit
electricity_duty = energy_charge * 0.05
fixed_charge = 100
net_bill = energy_charge + electricity_duty + fixed_charge

print("\n============== ELECTRICITY BILL ==============")
print(f"Consumer Name        : {consumer_name}")
print(f"Consumer ID          : {consumer_id}")
print(f"Units Consumed       : {units:.2f} kWh")
print(f"Energy Charge        : ₹{energy_charge:.2f}")
print(f"Electricity Duty(5%) : ₹{electricity_duty:.2f}")
print(f"Fixed Meter Charge   : ₹{fixed_charge:.2f}")
print("----------------------------------------------")
print(f"Net Bill Amount      : ₹{net_bill:.2f}")
print("==============================================")


