from data_management import DataManagement

data_manager = DataManagement()

while True:
    choice = data_manager.select_menu()
    if choice == '0':
        data_manager.import_file()
    elif choice == '1':
        data_manager.view_all_transactions()
    elif choice == '5':
        data_manager.delete_transaction()
    elif choice == '13':
        data_manager.save_transactions()
    elif choice == '14':
        print("Exiting the application.")
        break
    else:
        print("Invalid option. Please try again.")


