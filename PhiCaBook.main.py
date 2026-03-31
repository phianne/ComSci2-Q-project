import json

# load data
def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except:
        return []

# save data
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# add another debt list
def add_debt():
    data = load_data()

    name = input("Name: ")
    amount = input("Amount: ")

    new_debt = {
        "id": len(data) + 1,
        "name": name,
        "amount": amount
    }

    data.append(new_debt)
    save_data(data)

    print("Added!")

# read debts
def read_debt():
    data = load_data()

    for d in data:
        print(d)

# delete debt
def delete_debt():
    data = load_data()
    id = int(input("Enter ID: "))

    data = [d for d in data if d["id"] != id]

    save_data(data)
    print("Deleted!")

# menu
while True:
    print("\n1 Add\n2 View\n3 Delete\n4 Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_debt()
    elif choice == "2":
        read_debt()
    elif choice == "3":
        delete_debt()
    elif choice == "4":
        break
