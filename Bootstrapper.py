import requests
import os
import zipfile
import shutil

def display_ascii_art():
    # ANSI escape code for blue text: \033[94m
    # ANSI escape code to reset color: \033[0m
    ascii_art = """
\033[94m____  ____  _   _ __  ____        ___    ____  _____ 
|  _ \|  _ \| | | |  \/  \ \      / / \  |  _ \| ____|
| | | | |_) | | | | |\/| |\ \ /\ / / _ \ | |_) |  _|  
| |_| |  _ <| |_| | |  | | \ V  V / ___ \|  _ <| |___ 
|____/|_| \_\\___/|_|  |_|  \_/\_/_/   \_\_| \_\_____|\033[0m
    """
    print(ascii_art)  # Print ASCII art in blue

def download_file(url, filename):
    print(f"Step 1: Downloading {filename} from {url}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Step 2: {filename} downloaded successfully.")

def unzip_file(filename, extract_to):
    print(f"Step 3: Unzipping {filename} to {extract_to}")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Step 4: {filename} unzipped successfully.")

def move_contents_and_delete_folder(folder_path):
    print(f"Step 5: Moving contents of {folder_path} to parent directory and deleting the folder.")
    parent_dir = os.path.dirname(folder_path)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        shutil.move(item_path, parent_dir)
    os.rmdir(folder_path)
    print(f"Step 6: {folder_path} deleted, but its contents are preserved in the parent directory.")

def main():
    display_ascii_art()
    url = "https://github.com/THEBWARE/DRUMWARE/releases/download/Exec/DRUMWARE-V1.1.35.zip"
    zip_filename = "DRUMWARE-V1.1.35.zip"
    extract_to = "DRUMWARE_V1.1.35"

    # Ensure the directory exists
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    download_file(url, zip_filename)
    unzip_file(zip_filename, extract_to)
    move_contents_and_delete_folder(extract_to)

    print("All steps completed successfully.")

if __name__ == "__main__":
    main()
