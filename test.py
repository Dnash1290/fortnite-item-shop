import os
folder_name = "bundle 1 The Weeknd"
index = 2

folder = folder_name.split()
print(folder)
if int(folder[1]) == index:
    print("pass")
else:
    folder[1] = str(index)
    new_name = ""
    for word in folder:
        new_name += " "+word
        
print(new_name)
