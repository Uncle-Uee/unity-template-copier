import os
import shutil
import yaml

my_script_templates_path = "ScriptTemplates"  # Put all your script templates in this folder

unity_script_templates_path = "Editor\\Data\\Resources\\ScriptTemplates"  # Do Not Edit


def copy_script_templates():
    with open('config.yaml', mode='r') as file:
        config = yaml.load(file.read(), Loader=yaml.FullLoader)

    unity_path = config['unity']['install_path']
    unity_versions = os.listdir(unity_path)  # Get All Unity Versions Installed

    # Get Full Path to Unity ScriptTemplates Folder for each Unity Version
    unity_script_templates_paths = [os.path.join(unity_path, unity_version_path, unity_script_templates_path) for unity_version_path in
                                    unity_versions]

    # Compile a list of Paths for your Script Templates
    my_templates = [os.path.join(my_script_templates_path, script_template) for script_template in os.listdir(my_script_templates_path)]

    # Copy your Script Templates to each ScriptTemplate Path for each Unity Version
    print("Copying Start.\n")
    for target_directory in unity_script_templates_paths:
        print(f"Copying To {target_directory}")
        for my_template_file in my_templates:
            print(f"Copying {my_template_file}")
            shutil.copy(my_template_file, target_directory)
        print()
    print("Copying Complete.")
    os.system("pause")


if __name__ == '__main__':
    copy_script_templates()
