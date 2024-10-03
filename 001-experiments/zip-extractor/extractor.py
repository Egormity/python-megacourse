import zipfile

def extract_zip(zip_path, destination_folder):
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(destination_folder)