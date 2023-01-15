# DislikesCLI
A random project i made in 30 minutes to learn some flask

# Build / Compile
1. Install dependencies 
`pip install -r requirements.txt`
2. Run the command found in the `command` file and set the right directories
`pyinstaller --noconfirm --onefile --console --icon "/home/nuggy/Desktop/DislikesCLI/favicon.ico" --add-data "/home/nuggy/Desktop/DislikesCLI/templates:./templates"  "/home/nuggy/Desktop/DislikesCLI/main.py"`
3. Start the app by doing `python main.py` or by getting the `.exe` outfile which chould be in the `output` folder
