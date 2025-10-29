from data_management import data_management

data_management_obj = data_management

while True:
    choice = data_management_obj.select_menu()
    if choice == '0':
        import_file = data_management_obj.import_file()
    elif choice == '14':
        print("Exiting the application.")
        break
        



