# Import necessary modules
import sys
import clipboard
import json

# Define the filename for saving clipboard data
SAVED_FILE_NAME = "clipboard.json"

# Function to save data to a JSON file
def save_data(path,data):
    with open(path,"w") as file:
        json.dump(data,file)

# Function to load data from a JSON file
def load_data(path):
    try:
        with open(path,"r") as file:
            data=json.load(file)
            return data
    except:
        return {}  #this will return empty dictionary which are used for initial operation or as a fallback value when an exception occurs. 

# Check if exactly one command-line argument is provided
if len(sys.argv)==2:
    command = sys.argv[1] 
    data=load_data(SAVED_FILE_NAME)

    # If the command is "save," prompt the user for a key and save clipboard data
    if command == "save":
        key=input("Assign the key: ")
        data[key]=clipboard.paste()
        save_data(SAVED_FILE_NAME,data)   
        print("Data has been saved into multi_clipboard")

    # If the command is "load," prompt the user for a key and copy data to clipboard
    elif command == "load":
        key=input("Enter your desired key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data has been copied to clipboard")
        else:
            print("key does not exist!")

    # If the command is "delete," prompt the user for a key to remove from the clipboard
    elif command == "delete":
        key=input("Enter your desired key to remove: ")
        if key in data:
            del data[key]
            save_data(SAVED_FILE_NAME,data)
            print("Data has been deleted from clipboard")
        else:
            print("key does not exist!")
        
    # If the command is "list," display all clipboard data
    elif command == "list":
        for key in data:
            print(f"{key} : {data[key]}")

    else:
        print("unknown command")
        
# If no or incorrect command-line argument is provided, display usage instructions
else: 
    print('''Please choose:
    save : save into clipboard,
    load : copy from clipboard, 
    delete : delete from clipboard,
    list : To see all clipboard data.
    ''')
