import glob

PATH = r"C:\Users\kotla\Desktop\python-megacourse\001 - todo app\files"

filepaths = glob.glob(f"{PATH}\*.py")

for filepath in filepaths:
    with open(filepath, "r") as file:
        print(file.read())