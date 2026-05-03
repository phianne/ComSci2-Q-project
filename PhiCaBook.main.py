import json
import os 

FILENAME = 'Phicabook.json'

def load_data():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w') as file:
            json.dump([], file)
        return []
        
    with open(FILENAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(data, filename=FILENAME):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def create_debt(new_debt):
    data = load_data()
    data.append(new_debt)
    save_data(data)
    print("Debt added.")

def delete_debt(debt_id):
    data = load_data()
    data = [debt for debt in data if debt["Id"] != debt_id]   
    save_data(data)
    print("Debt deleted.")

def read_debt():
    data = load_data()
    if not data:
        print("No records found.")
    for debt in data:
        print(debt)

def update_debt(debt_id, updated_info):
    data = load_data()
    for debt in data:
        if debt['Id'] == debt_id:   
            debt.update(updated_info)
            save_data(data)
            print("Debt updated.")
            return
    print("Debt not found.")


while True:
    print ("__________________________________________________________________________________")
    print("\n        # Hello! Welcome to Phica Book App! #")
    print ("__________________________________________________________________________________")
    print("A: Create new debt")
    print("B: Update debt")
    print("C: Read all debts")
    print("D: Delete debt")
    print("E: Exit App")

    function = input("\nSelect your task (Use capital letters): ")

    if function == "A":
        print ("\n--- Create New Debt ---")
        debt = load_data()

        idNo = 0
        for item in debt:
            idNo = item['Id'] + 1

        name = input("Customer name: ")
        try:
            am = int(input("Amount of debt: "))
        except ValueError:
            print("Invalid amount.")
            continue

        st = input("Status (paid/not paid): ")
        dt = input("Date: ")

        create_debt({
            "Id": idNo,
            "Name": name,
            "Amount": am,
            "Status": st,  
            "Date": dt
        })

    elif function == "B":
        print ("\n--- Update Debt ---")

        try:
            debt_id = int(input("ID: "))
        except ValueError:
            print("Invalid ID.")
            continue

        name = input("New Name (leave blank to skip): ")
        amount = input("New Amount (leave blank to skip): ")
        status = input("New Status (leave blank to skip): ")
        date = input("New Date (leave blank to skip): ")

        updated_info = {}

        if name:
            updated_info["Name"] = name
        if amount:
            try:
                updated_info["Amount"] = int(amount)
            except ValueError:
                print("Invalid amount skipped.")
        if status:
            updated_info["Status"] = status
        if date:
            updated_info["Date"] = date

        update_debt(debt_id, updated_info)

    elif function == "C":
        print ("\n--- All Debts ---")
        read_debt()

    elif function == "D":
        print ("\n--- Delete Debt ---")

        try:
            debt_id = int(input("Enter ID to delete: "))
            delete_debt(debt_id)
        except ValueError:
            print("Invalid ID.")

    elif function == "E":
        print("\nThank you for using Phica Book! Goodbye!")
        break   

    else:
        print("Invalid option. Try again.")

