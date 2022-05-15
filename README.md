# Unity Templates Copier
A simple Project that has Unity Script Templates and a Python Script that will copy your Script Templates <br>
to all of your installed Unity Editors.

# How To Use the Copier
1. Find and Copy the Installation Path of Unity.
   1. Look at the example-path-to-copy.png for an example.
   2. Example Path would be ```C:\Program Files\Unity```
2. Open the config.yaml file
3. Replace the ```YOUR LOCATION```  with the installation path you copied, it should end up like this
   1. ```install_path: "F:\Program Files\Unity"```

# Script Templates
In Unity, we use Script Templates to create default C# MonoBehaviour Scripts or Assembly Definitions, etc. <br>
By creating our own Script Templates, we can design Blueprints for multiple files we  want to create within Unity.

This means, we can create Script Template files, that have the basic blueprint structure for Abstract Classes, 
Serializable Classes, Scriptable Objects, etc

## Template Filename Structure

??-TYPE-FILENAME.ext.txt<br>
??-CATEGORY__TYPE-FILENAME.ext.txt

- ?? - This is the **int** Order the Script will be shown in the Unity Editor
- CATEGORY__ - You can separate your templates into different Categories and Sub Categories as well 
- TYPE - This is the Type of Template you want to create
- FILENAME - This represents the default name your Template will have when you create it.
- ext - You must have an Extension for the Template you want to create for example .cs, .json, etc
- txt - Always end the Script Template name in .txt

## Creating your own Templates
If we apply the rules above we can create templates as follows:
- 79-File__Json-NewJsonFile.json.txt
- 80-C# Script-NewBehaviourScript.cs.txt
- 81-C# Editor Templates__Custom Editor__Custom Editor-NewCustomEditor.cs.txt

# How to Compile
1. Install Python 3.6+ if you do not have any Python version Installed
2. Create a Python Virtual Environment (Not Required)
3. Install the PyYAML Package using Pip, use the following command
   1. pip install pyyaml
4. Install the PyInstaller Package using Pip, use the following command 
   1. pip install pyinstaller
5. Copy the Build Command
   1. pyinstaller --onefile --console --icon=data_copy.ico .\copy_unity_templates.py
6. Open a Command Prompt or Terminal window at the root location of the .py file 
7. Paste the build command and Press Enter to compile to an Executable