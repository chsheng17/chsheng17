import function

running = True

while running:
    #Display menu
    print("\nWelcome to the Malaysian Tax Input Program")
    print("1. Register")
    print("2. Login")
    print("3. View Tax Records")
    print("4. Exit")

    # Get user choice
    choice = input("Enter your choice (1-4): ")

    #choice 1
    if choice == "1":
        ic_number = function.register_user()
        print(f"\nRegistration successful for IC number: {ic_number}")

    #choice 2
    elif choice == "2":
        # Check if a user is registered before attempting login
        registered_users = function.get_registered_users()
        if registered_users:
            ic_number, password = function.verify_user(registered_users)
            if ic_number:
                #If valid login. Then proceed with tax calculation and saving data
                annual_income = float(input("Enter your annual income (RM): "))
                tax_relief = float(input("Enter your total tax relief amount (RM): "))
                tax_payable = function.calculate_tax(annual_income, tax_relief)
                print(f"\nYour calculated tax payable is RM{tax_payable:.2f}")
                function.save_to_csv([
                    [ic_number, annual_income, tax_relief, tax_payable]
                ], "tax_records.csv")
        else:
            print("\nNo registered users. Please register first.")

    #choice3
    elif choice == "3":
        tax_records = function.read_from_csv("tax_records.csv")
        if tax_records is not None:
            print("\nTax Records:")
            for row in tax_records:
                print(f"IC Number: {row['IC Number']}, Income: {row['Income']}, Tax Relief: {row['Tax Relief']}, Tax Payable: {row['Tax Payable']}")
        else:
            print("\nNo tax records found.")

    #choice 4 Exit        
    elif choice == "4":
        running = False
        print("\nThank you for using the Malaysian Tax Input Program.")
    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")