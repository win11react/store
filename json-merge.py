import json
import os
 
# function to add to JSON
def write_json(filename='store/index.json'):
    with open(filename,'r+') as file, open('template.json') as temp:
          # First we load existing data into a dict.
        file_data = json.load(file)
        y = json.load(temp)
        # Join new_data with file_data inside emp_details
        file_data.append(y)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended


     
write_json()
