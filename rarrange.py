import os
import shutil
from datetime import datetime

def rearrange_files_by_year(input_folder):
    # Step 1: Define the path for the processed_data folder
    processed_data_path = os.path.join(os.getcwd(), 'processed_data')
    input_folder = os.path.join(os.getcwd(), input_folder)
    print(input_folder)
    # Step 2: Create the processed_data folder if it doesn't exist
    if not os.path.exists(processed_data_path):
        os.makedirs(processed_data_path)
    
    # Step 3: Walk through all directories and subdirectories in the input folder
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Ignore files in the processed_data directory itself
            # if processed_data_path in root:
            #     continue
            if ".ini" in file:
                continue
            # Step 4: Get the full path of the current file
            file_path = os.path.join(root, file)
            print(f"Trying {file_path}")
            # Step 5: Get the last modification year of the file
            mod_time = os.path.getmtime(file_path)
            year = datetime.fromtimestamp(mod_time).strftime('%Y')
            
            # Step 6: Create a year directory inside processed_data if it doesn't exist
            year_path = os.path.join(processed_data_path, year)
            if not os.path.exists(year_path):
                os.makedirs(year_path)
            
            # Step 7: Move the file to the year directory
            try:
                print(f"Moving {file_path} to {year_path}")
                shutil.copy(file_path, year_path)
            except Exception as e:
                print(file_path, str(e))
    
    print("Files have been rearranged into year-based folders.")

# Example usage:
# Replace 'your_folder_path_here' with the actual path of the folder you want to organize
input_folder_path = 'Raw_data'
rearrange_files_by_year(input_folder_path)
