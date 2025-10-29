import pandas as pd

class FileImporter:
    def __init__(self):
        pass

    def import_file():
        file_path = input("Enter the path to the file: ")
        
        if file_path.endswith('.csv'):
            pd.read_csv(file_path)
            print("CSV file imported successfully")
        else:
            raise ValueError("Unsupported file format")
        
        
