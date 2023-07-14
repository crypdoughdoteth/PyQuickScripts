import os 


for file in os.listdir():

    json_file_path = f'C:\\Users\\{file}'
    
    for file in os.listdir():
            #arbitrary alterations here

        if file == "jsonslicer.py":
            print (file)
            continue
            
        else: 
            new_name = file.split('1_')
            modified_name = new_name[0] + new_name[1]
            os.rename(file, modified_name)
            print (modified_name)