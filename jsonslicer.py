import json 
import os 


for file in os.listdir():

    json_file_path = f'C:\\Users\\Desktop\\pythonscripts\\{file}'


    if file == "jsonslicer.py":
        print (file)
        continue
        
    else:
            
        with open (json_file_path, "r") as theFile:
            data = json.load(theFile)
            

            #arbitrary alterations here
        name = data ['name']
        name = name.removeprefix("Image #")        
        data['image'] = f"https://arweave.net/path/{name}.png"

        print (name)

        with open (json_file_path, "w") as theFile:
            json.dump(data, theFile, indent = 6)
