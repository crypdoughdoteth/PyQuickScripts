import os 

for file in os.listdir():
    
    for file in os.listdir():
            #arbitrary alterations here

        if file == "file_renamer.py":
            print (file)
            continue
            
        else: 
            new_name = file.removeprefix('Open MInds Batch 1_')
            os.rename(file, new_name)
            print (new_name)
