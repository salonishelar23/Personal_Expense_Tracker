import json 
def save_expenses(expenses):
    with open("expense.json","w")as file:
        json.dump(expenses,file,indent=4)

def load_expenses():
    try:
        with open("expense.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
categories = ["food", "transport", "entertainment", "shopping", "bills", "others"]

expenses = load_expenses()

print("=" *40)
print("Welcome to Personal Expense Tracker")
print("=" *40)
print("1.ADD NEW EXPENSE")
print("2.VIEW ALL EXPENSES")
print("3.CATEGORY SUMMARY")
print("4.SET/CHECK BUDGET")
print("5.SEARCH EXPENSE")
print("6.Delete Expense")
print("7.Exit")
print("=" *40)
while True:
    try:
     choice = int(input("enter your choice (1-7): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        continue

    if choice == 1:
        print("---ADD NEW EXPENSE---")
        print(f"available categories: {','.join(categories)}")
        category = input("Enter category :").strip().lower()
        if category not in categories:
           print("Categories not available. Adding to 'others' category.")
           category = "others"
        try:
         amount = float(input("Enter an amount: 💰"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        desc = input("Enter description: ").strip()
        if not desc:
            print("Description cannot be empty. Please provide a description.")
            continue
        expense = {
           "category":category,
           "amount":amount,
           "desc":desc
        }  
        expenses.append(expense)
        save_expenses(expenses)
         
        print("\nExpense added successfully!")
        
    elif choice == 2:
        print("---All Expenses---")

        if not expenses:
           print("No Expense Added Yet.")
           continue

        for index, expense in enumerate(expenses,start = 1):
            print(f"{index}. {expense['category']} | ₹{expense['amount']:.2f} | {expense['desc']}")
            
    elif choice == 3:
        print("---Category Summary--- ")
        if not  expenses:
            print("No expenses to summarize.")
            continue

        category_totals = {}
        for expense in expenses:
            category = expense['category']
            amount = expense['amount']
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
        for category, total in category_totals.items():
            print(f"{category}: ₹{total:.2f}")

    elif choice == 4:
        print("---SET/CHECK BUDGET---")
        try:
         budget = float(input("Enter your budget: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        total_expenses = sum(expense['amount'] for expense in expenses)
        if budget <= 0:
            print("Budget must be a positive number.")
        if total_expenses > budget:
            print(f"You have exceeded your budget by ₹{total_expenses - budget:.2f}.")
        else:
            print(f"You are within your budget. Remaining budget: ₹{budget - total_expenses:.2f}.")
    
    elif choice == 5:
        print("---Search Expense---")
        search = input("Enter a keyword to search in description: ").lower()
        found_expenses = [expense for expense in expenses if search in expense['desc'].lower()]
        if found_expenses:
            for index, expense in enumerate(found_expenses, start=1):
                print(f"{index}. {expense['category']} | ₹{expense['amount']:.2f} | {expense['desc']}")
        else:
            print("No expenses found matching the search criteria.")

    elif choice == 6:
        print("---Delete expense---")
        if not expenses:
            print("No Expenses to delete.")
            continue
        for index, expense in enumerate(expenses,start=1):
            print(f"{index} {expense['category']} | ₹{expense['amount']:.2f} | {expense['desc']}")
        try:
            delete_index = int(input("Enter expense number to delete."))-1
            if 0 <= delete_index < len(expenses):
                deleted = expenses.pop(delete_index)
                save_expenses(expenses)
                print(f"Deleted: {deleted['desc']}")
            else:
                print("Invalid expense number.")
        except ValueError:
            print("please Enter a valid number")
    elif choice == 7:
        print("Exiting the Personal Expense Tracker. Goodbye!")
        break
    else:
       print("please chose a number between 1 to 7.")    