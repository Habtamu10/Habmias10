# Simple Expense Tracker
from datetime import date

class Expense:
    def __init__(self, description, amount, category="general"):
        self.description = description
        self.amount = float(amount)
        self.category = category
        self.date = date.today().isoformat()

    def __str__(self):
        return f"{self.date} | {self.category:10} | ${self.amount:8.2f} | {self.description}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add(self, description, amount, category="general"):
        self.expenses.append(Expense(description, amount, category))

    def total(self):
        return sum(e.amount for e in self.expenses)

    def by_category(self):
        cats = {}
        for e in self.expenses:
            cats[e.category] = cats.get(e.category, 0) + e.amount
        return cats

    def display(self):
        print(f"{'Date':12} {'Category':12} {'Amount':10} Description")
        print("-" * 55)
        for e in self.expenses:
            print(e)
        print("-" * 55)
        print(f"Total: ${self.total():.2f}")

tracker = ExpenseTracker()
tracker.add("Groceries", 45.50, "food")
tracker.add("Bus pass", 30.00, "transport")
tracker.add("Python book", 25.00, "education")
tracker.add("Coffee", 5.00, "food")
tracker.display()
print("\nBy category:", tracker.by_category())
