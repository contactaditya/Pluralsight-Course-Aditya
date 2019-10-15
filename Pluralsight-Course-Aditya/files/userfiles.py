import sys
import os
import json

from pathlib import Path


def main(my_directory):
    entries = os.scandir('{}'.format(my_directory))
    for entry in entries:
        print(entry.name)


def get_list_of_files(directory_name):
    # create a list of file and sub directories
    # names in the given directory
    list_of_files = os.listdir(directory_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(directory_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)

    return all_files


def get_list_of_files_and_folders(username, level=2):
    file_info = []
    path = '\\packages'
    directory = username + path
    print(directory)

    for root, dirs, files in os.walk(directory):
        _root = root.replace(directory, '')  # you may need to remove the "+ '\\'"
        if _root.count(os.sep) < level:
            for file_name in files:
                print(os.path.join(root, file_name))
                file_info.append({'path': '{}'.format(os.path.join(root, file_name)), 'type': 'file'})
            for directory_name in dirs:
                print(os.path.join(root, directory_name))
                file_info.append({'path': '{}'.format(os.path.join(root, directory_name)), 'type': 'folder'})

    for x in range(len(file_info)):
        print(file_info[x])

    my_json_string = json.dumps(file_info)

    print(my_json_string)


if __name__ == '__main__':
    #  list_of_files = get_list_of_files(sys.argv[1])
    # Print the files
    # for elem in list_of_files:
    # print(elem)
    get_list_of_files_and_folders(sys.argv[1])