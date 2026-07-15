import csv
import os
from datetime import datetime

file_name = "expenses.csv"

# Create file if it doesn't exist
if not os.path.exists(file_name):
    file = open(file_name, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Title", "Amount", "Date"])
    file.close()

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":
        title = input("Expense Name: ")
        amount = input("Amount: ")

        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        file = open(file_name, "a", newline="")
        writer = csv.writer(file)
        writer.writerow([title, amount, date])
        file.close()

        print("Expense Added Successfully!")

    # View Expenses
    elif choice == "2":
        file = open(file_name, "r")
        reader = csv.DictReader(file)

        print("\n------ Expenses ------")

        count = 1
        for row in reader:
            print(f"{count}. {row['Title']} - ₹{row['Amount']} - {row['Date']}")
            count += 1

        file.close()

    # Total Expense
    elif choice == "3":
        file = open(file_name, "r")
        reader = csv.DictReader(file)

        total = 0

        for row in reader:
            total += float(row["Amount"])

        file.close()

        print("\nTotal Expense = ₹", total)

    # Delete Expense
    elif choice == "4":
        file = open(file_name, "r")
        reader = csv.DictReader(file)

        expenses = []

        print("\n------ Expenses ------")
        index = 1

        for row in reader:
            expenses.append(row)
            print(f"{index}. {row['Title']} - ₹{row['Amount']} - {row['Date']}")
            index += 1

        file.close()

        if len(expenses) == 0:
            print("No Expenses Found!")
        else:
            delete = int(input("Enter expense number to delete: "))

            if 1 <= delete <= len(expenses):
                expenses.pop(delete - 1)

                file = open(file_name, "w", newline="")
                writer = csv.writer(file)

                writer.writerow(["Title", "Amount", "Date"])

                for expense in expenses:
                    writer.writerow([
                        expense["Title"],
                        expense["Amount"],
                        expense["Date"]
                    ])

                file.close()

                print("Expense Deleted Successfully!")
            else:
                print("Invalid Number!")

    # Exit
    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
