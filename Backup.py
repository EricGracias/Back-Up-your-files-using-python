import os
import shutil

path = 'C:/Users/ERIC/OneDrive/Desktop'
print("Before moving file")
print(os.listdir(path))

source = 'C:/Users/ERIC/OneDrive/Desktop/angryBirdsStage2'
destination = 'C:/Users/ERIC/OneDrive/Desktop/Backup'

#moving contant of source to destination
dest = shutil.move(source, destination)

print("After moving file:")
print(os.listdir(path))