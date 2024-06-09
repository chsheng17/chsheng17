import csv

def register_user():
    while True:
        ic_number = str(input("Enter your IC number: "))
        if len(ic_number) == 12:
            password = ic_number[8:12]
            with open("registered_users.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([ic_number, password])
            return ic_number
        else:
            print("IC number must be 12 digits. Please try again.")

def get_registered_users():
    try:
        with open("registered_users.csv", "r") as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def verify_user(registered_users):
    ic_number = input("Enter your IC number: ")
    password = input("Enter your password: ")
    for row in registered_users:
        if row[0] == ic_number and row[1] == password:
            return ic_number, password
    return None, None

def calculate_tax(annual_income, tax_relief):
    chargeable_income=annual_income - tax_relief
    if chargeable_income <= 5000:
        tax_payable = 0
    elif chargeable_income <= 20000:
        tax_payable = (chargeable_income-5000) * 0.01
    elif chargeable_income <= 35000:
        tax_payable = (chargeable_income-20000) * 0.03 + 150
    elif chargeable_income <= 50000:
        tax_payable = (chargeable_income-35000) * 0.06 + 600
    elif chargeable_income <= 70000:
        tax_payable = (chargeable_income-50000) * 0.11 + 1500
    elif chargeable_income <= 100000:
        tax_payable = (chargeable_income-70000) * 0.19 + 3700
    elif chargeable_income <= 400000:
        tax_payable = (chargeable_income-100000) * 0.25 + 9400
    elif chargeable_income <= 600000:
        tax_payable = (chargeable_income-400000) * 0.26 + 84400
    elif chargeable_income <= 2000000:
        tax_payable = (chargeable_income-600000) * 0.28 + 136400
    else:
        tax_payable = (chargeable_income-2000000) * 0.3 + 528400
    return tax_payable

def save_to_csv(data, filename):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:  #Check if file is empty
            writer.writerow(["IC Number", "Income", "Tax Relief", "Tax Payable"])
        writer.writerows(data)
        
def read_from_csv(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return None