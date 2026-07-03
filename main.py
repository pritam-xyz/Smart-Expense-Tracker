import csv
import os

file_name = "expenses.csv"

# Create file if it doesn't exist
if not os.path.exists(file_name):
    file = open(file_name, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Title", "Amount"])
    file.close()


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Expense Name: ")
        amount = input("Amount: ")

        file = open(file_name, "a", newline="")
        writer = csv.writer(file)
        writer.writerow([title, amount])
        file.close()

        print("Expense Added Successfully!")

    elif choice == "2":
        file = open(file_name, "r")
        reader = csv.reader(file)

        print("\n------ Expenses ------")

        for row in reader:
            print(row)

        file.close()

    elif choice == "3":
        file = open(file_name, "r")
        reader = csv.DictReader(file)

        total = 0

        for row in reader:
            total = total + float(row["Amount"])

        file.close()

        print("\nTotal Expense = ₹", total)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")