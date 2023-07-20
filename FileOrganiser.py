import os
import shutil

def organize_files(directory):
    # Create folders for each file type
    create_folders()

    # Scan the specified directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_type = get_file_type(filename)
            if file_type:
                move_file(directory, filename, file_type)

def create_folders():
    # Define a list of file types and their respective folder names
    file_types = {
        'Images': ['jpg', 'jpeg', 'png', 'gif'],
        'Documents': ['txt', 'doc', 'docx', 'pdf'],
        'Videos': ['mp4', 'mov', 'avi'],
        # Add more file types and folder names as needed
    }

    # Create folders for each file type (if they don't exist)
    for folder_name in file_types.keys():
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

def get_file_type(filename):
    # Extract the file extension from the filename
    _, file_extension = os.path.splitext(filename)

    # Remove the dot from the file extension
    file_extension = file_extension[1:]

    # Match the file extension with the predefined file types
    file_types = {
        'Images': ['jpg', 'jpeg', 'png', 'gif'],
        'Documents': ['txt', 'doc', 'docx', 'pdf'],
        'Videos': ['mp4', 'mov', 'avi'],
        # Add more file types and folder names as needed
    }

    for file_type, extensions in file_types.items():
        if file_extension.lower() in extensions:
            return file_type

    # If the file type is not found, return None
    return None

def move_file(directory, filename, file_type):
    source_path = os.path.join(directory, filename)
    destination_path = os.path.join(file_type, filename)

    # Move the file to the appropriate folder
    shutil.move(source_path, destination_path)

def main():
    # Prompt the user to enter the directory path
    directory = input("Enter the directory path to organize: ")

    # Call the file organizer function
    organize_files(directory)
    print("File organizing completed!")

if __name__ == "__main__":
    main()
