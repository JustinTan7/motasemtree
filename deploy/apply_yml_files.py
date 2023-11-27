import os
import subprocess

def apply_yaml_files(folder_path):
    # Get a list of all files in the specified folder
    files = [file for file in os.listdir(folder_path) if file.endswith('.yaml') or file.endswith('.yml')]

    # Apply each YAML file using kubectl apply -f
    for file in files:
        file_path = os.path.join(folder_path, file)
        subprocess.run(['kubectl', 'apply', '-f', file_path])
        print(f"Applied {file_path}")

if __name__ == "__main__":

    folder_path = './'

    # Check if the specified folder exists
    if os.path.exists(folder_path):
        apply_yaml_files(folder_path)
    else:
        print(f"The folder '{folder_path}' does not exist.")
