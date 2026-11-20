
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
dashboard = RetailSalesDashboard("sales.csv")

# Call methods
dashboard.read_data()
dashboard.analyze_sales()
dashboard.display_dashboard()
