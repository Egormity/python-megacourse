import PySimpleGUI
from extractor import extract_zip

window = PySimpleGUI.Window("Zip extractor", [
    [PySimpleGUI.Text("Select zip file to extract"), PySimpleGUI.Input("Choose zip"), PySimpleGUI.FilesBrowse("Choose", key="zip")],
    [PySimpleGUI.Text("Select destination folder"), PySimpleGUI.Input("Browse folder"), PySimpleGUI.FolderBrowse("Browse", key="folder")],
    [PySimpleGUI.Button("Extract"), PySimpleGUI.Text(key="output", text_color="lightblue")]
])

while True:
    event, values = window.read()
    # print(event, values)

    zip_to_extract = values["zip"]
    folder = values["folder"]

    extract_zip(zip_to_extract, folder)
    window["output"].update("Done!")

    if event == PySimpleGUI.WIN_CLOSED:
        break
