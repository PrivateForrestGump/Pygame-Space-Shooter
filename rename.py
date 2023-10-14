import os


def rename_files_and_folders(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, file.lower().replace(' ', '_'))
            os.rename(file_path, new_file_path)
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            new_dir_path = os.path.join(root, directory.lower().replace(' ', '_'))
            os.rename(dir_path, new_dir_path)


# Provide the path to the directory you want to rename
directory_path = 'images'

rename_files_and_folders(directory_path)