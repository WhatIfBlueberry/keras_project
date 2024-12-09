import os

# Specify the path to your .txt file
file_path = "names.txt"

# Specify the directory where you want to create folders
output_directory = "C:\\Users\\Test\\Desktop\\WiSe24\\nn\\project\\data"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Read the .txt file
try:
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split the content by commas
    names = [name.strip() for name in content.split(',')]

    # Create a folder for each name
    for name in names:
        if name:  # Ensure the name is not empty
            folder_path = os.path.join(output_directory, name)
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {folder_path}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
