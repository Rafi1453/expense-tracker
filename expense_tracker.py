# Expense Tracker - Amar prothom Python project
# Author: Rafi

print("======================")
print("   EXPENSE TRACKER")
print("======================")

name = input("Tomar naam likho: ")
print("Shagotom,", name + "!")
expenses = []

while True:
    print()
    print("1. Khoroch add koro")
    print("2. Sob khoroch dekho")
    print("3. Exit")

    choice = input("Ki korba? (1/2/3): ")

    if choice == "1":
        item = input("Ki kinso? ")
        amount = float(input("Koto euro? "))
        expenses.append([item, amount])
        print("Add hoye gese!")

    elif choice == "2":
        total = 0
        for e in expenses:
            print(e[0], "-", e[1], "EUR")
            total = total + e[1]
        print("Total:", total, "EUR")

    elif choice == "3":
        print("Allah Hafez,", name)
        break

    else:
        print("1, 2 ba 3 dao!")