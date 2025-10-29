from ast import While
from file_import import FileImport
from data_management import data_management

file_import_obj = FileImport
data_management_obj = data_management

while True:
    choice = data_management_obj.select_menu()
    if choice == '0':
        import_file = file_import_obj.import_file()
    elif choice == '14':
        print("Exiting the application.")
        break
        



