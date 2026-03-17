from Tracker import add_transaction, view_transactions, get_balance
from charts import show_expense_chart

while True:
    print("\nPersonal Finance Tracker")
    print("1.Add Income")
    print("2.Add Expense")
    print("3. view Transactions")
    print("4. View Balance")
    print("5. Exit")

    choice = input("Choose an option")

    if choice == "1":
        category = input("Income Source: ")
        amount = float(input("Amount: "))
        add_transaction("income", category, amount)

    elif choice == "2":
        category = input("Expense Category: ")
        amount = float(input("Amount: "))
        add_transaction("expense", category, amount)

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        print("Balance:", get_balance())

    elif choice == "5":
        show_expense_chart()

    elif choice == "6":
        break 

 