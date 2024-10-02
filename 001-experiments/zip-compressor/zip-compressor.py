import PySimpleGUI
from zip_creator import make_archive

window = PySimpleGUI.Window("Zip compressor", [
    [PySimpleGUI.Text("Select files to compress"), PySimpleGUI.Input("Choose"), PySimpleGUI.FilesBrowse("Choose", key="files")],
    [PySimpleGUI.Text("Select destination folder"), PySimpleGUI.Input("Browse"), PySimpleGUI.FolderBrowse("Browse", key="folder")],
    [PySimpleGUI.Button("Compress"), PySimpleGUI.Text(key="output", text_color="lightblue")]
])

while True:
    event, values = window.read()
    print(event, values)

    file_paths = values["files"].split(";")
    folder = values["folder"]

    make_archive(file_paths, folder)
    window["output"].update("Done!")

