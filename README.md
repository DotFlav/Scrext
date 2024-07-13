# Scrext
A Python tool for Windows, to quickly copy text you are unable to copy by yourself.

## Manual
Simply run the application and press the big button at the bottom. Click and drag your mouse over the area you want to scan for text. The text is then shown in the box and automatically copied to your clipboard (can be disabled in the settings). 

### Auto Installation
Just download and run one of the installers.
Basic version ~500MB (Only English training data)
Advanced version ~1000MB (Contains all availble language and script data)

### Manual Installation
- make sure Python is installed, or use the Python Installer in installations/
- install [Tesseract OCR GitHub](https://github.com/UB-Mannheim/tesseract/wiki) or use the OCR Installer in installations/
- run command: `pip install -r installations/requirements.txt`

Run app.py to start the application.

### Build the Installer
- Download and install [NSIS](https://nsis.sourceforge.io/Download)
- navigate into the project
- run `pyinstaller --onefile --noconsole --icon=images/kitty.ico --add-data "images/kitty.ico;images" --add-data "Tesseract-OCR;Tesseract-OCR" app.py` to build the .exe
- right click the installer.nsi and choose "Compile NSIS Script"


