import zipfile
import pathlib

def make_archive(file_paths, destination_dir):
    with zipfile.ZipFile(pathlib.Path(destination_dir, 'archive.zip'), 'w') as archive:
        for file_path in file_paths:
            file_path = pathlib.Path(file_path)
            archive.write(file_path, arcname=file_path.name)

if __name__ == '__main__':
    print('Hello')