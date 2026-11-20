                    #UNIT - 5

# 1. Bank account system using OOP 

class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid deposit amount!")
        else:
            self.balance += amount
            print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully!")

    def check_balance(self):
        print("Current Balance: Rs.", self.balance)

    def display_details(self):
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: Rs.", self.balance)


# Creating an object

name = input("Enter Account Holder Name: ")
account_number = input("Enter Account Number: ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(name, account_number, balance)

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == 3:
            account.check_balance()

        elif choice == 4:
            account.display_details()

        elif choice == 5:
            print("Thank you for using our bank!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter a valid number!")



# Library Management System using OOP

class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        book = {
            "name": name,
            "author": author,
            "status": "Available"
        }

        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        print("\n===== BOOK DETAILS =====")

        if not self.books:
            print("No books available!")
        else:
            for book in self.books:
                print("Book:", book["name"])
                print("Author:", book["author"])
                print("Status:", book["status"])
                print("------------------")

    def issue_book(self):
        name = input("Enter book name to issue: ")

        for book in self.books:
            if book["name"].lower() == name.lower():
                if book["status"] == "Available":
                    book["status"] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")

    def return_book(self):
        name = input("Enter book name to return: ")

        for book in self.books:
            if book["name"].lower() == name.lower():
                if book["status"] == "Issued":
                    book["status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return

        print("Book not found!")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        library.issue_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")




# Dice Simulator using OOP

import random

class Dice:

    def __init__(self):
        self.number = 0

    def roll_dice(self):
        self.number = random.randint(1, 6)
        print("Dice rolled!")
        print("You got:", self.number)

    def play_again(self):
        while True:
            choice = input("\nRoll the dice again? (yes/no): ")

            if choice.lower() == "yes":
                self.roll_dice()

            elif choice.lower() == "no":
                print("Thanks for playing!")
                break

            else:
                print("Invalid choice! Enter yes or no.")


dice = Dice()

print("===== DICE SIMULATOR =====")

dice.roll_dice()
dice.play_again()



# Retail Sales Dashboard using OOP, CSV and Matplotlib

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()



# Retail Sales Dashboard using OOP, CSV and Matplotlib

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()



# Retail Sales Dashboard using OOP, CSV and Matplotlib

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()



# Retail Sales Dashboard using OOP, CSV and Matplotlib

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()


# Create object

# Retail Sales Dashboard using OOP, CSV and Matplotlib

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()


# Create object

# Retail Sales Dashboard using OOP, CSV and Matplotlib

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()


# Create object

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()


# Create object

# Retail Sales Dashboard using OOP, CSV and Matplotlib

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()



# Retail Sales Dashboard using OOP, CSV and Matplotlib

import csv
import matplotlib.pyplot as plt


class RetailSalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.sales = []

    # Read CSV file
    def read_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    if quantity < 0 or price < 0:
                        raise ValueError("Negative values are not allowed!")

                    row["Quantity"] = quantity
                    row["Price"] = price
                    row["Revenue"] = quantity * price

                    self.sales.append(row)

            if not self.sales:
                raise ValueError("No sales records found!")

            print("CSV data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except ValueError as e:
            print("Data Error:", e)

        except KeyError as e:
            print("Missing CSV column:", e)

    # Calculate sales details
    def analyze_sales(self):

        if not self.sales:
            print("No data available for analysis!")
            return

        total_revenue = sum(item["Revenue"] for item in self.sales)
        total_quantity = sum(item["Quantity"] for item in self.sales)

        highest = max(self.sales, key=lambda x: x["Revenue"])

        print("\n===== RETAIL SALES REPORT =====")
        print("Total Revenue: Rs.", total_revenue)
        print("Total Products Sold:", total_quantity)
        print("Highest Revenue Product:", highest["Product"])
        print("Highest Product Revenue: Rs.", highest["Revenue"])

    # Display graphs
    def display_dashboard(self):

        if not self.sales:
            print("No data available for graphs!")
            return

        products = [item["Product"] for item in self.sales]
        revenue = [item["Revenue"] for item in self.sales]

        # Bar Chart
        plt.figure(figsize=(8, 5))
        plt.bar(products, revenue)
        plt.title("Product-wise Sales Revenue")
        plt.xlabel("Products")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        # Pie Chart
        plt.figure(figsize=(7, 7))
        plt.pie(revenue, labels=products, autopct="%1.1f%%")
        plt.title("Sales Revenue Distribution")
        plt.show()




