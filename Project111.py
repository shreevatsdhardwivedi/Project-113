import os
import shutil

# .exe .msi

from_dir = "c:/users/pushkal/downloads"
to_dir = "c:/users/pushkal/.whiteHat/New DownLoads"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:

    name, extentions = os.path.splitext(file_name)
    #print(name)
    #print(extentions)

    if extentions == ' ':
        continue
    if extentions in ['.gif', '.png', '.jpeg', '.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir '/' + "image_files"
        path3 = to_dir '/' + "image_files" + '/' + file_name
        if os.path.exists(path2):
            print("Moving " + file_name + ".....")

            shutil.move(path1, path3)

        else:
          os.markedis(path2)
          print("Moving " + file_name + ".....")  
          shutil.move(path1,path2)