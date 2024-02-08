#!/usr/bin/python3
import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    # Get the name of the folder
    folder_name = os.path.basename(folder_path)
    
    # Get the current date
    current_date = datetime.now().strftime("%Y_%m_%d")
    
    # Set the output file name
    output_file = f"{folder_name}_{current_date}.{compress_type}"
    
    try:
        if compress_type == 'zip':
            with zipfile.ZipFile(output_file, 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), 
                                   os.path.relpath(os.path.join(root, file), folder_path))
        elif compress_type == 'tar':
            with tarfile.open(output_file, 'w') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == 'tgz':
            with tarfile.open(output_file, 'w:gz') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            print("Invalid compress type.")
            return False
        
        print(f"Compression successful. Output file: {output_file}")
        return True
    except Exception as e:
        print(f"Compression failed. Error: {e}")
        return False

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    compress_type = input("Enter the desired compress type (zip, tar, tgz): ")
    
    if os.path.exists(folder_path):
        if compress_type in ['zip', 'tar', 'tgz']:
            compress_folder(folder_path, compress_type)
        else:
            print("Invalid compress type.")
    else:
        print("Folder does not exist.")

if __name__ == "__main__":
    main()
