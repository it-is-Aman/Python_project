Multi Clipboard Manager

A Python script that allows you to manage and organize your clipboard data efficiently. You can save, load, delete, and list clipboard data using simple command-line operations.
Features

    Save Clipboard Data: Save clipboard content under a specified key for easy retrieval.

    Load Clipboard Data: Retrieve clipboard content associated with a key and copy it to the clipboard.

    Delete Clipboard Data: Remove clipboard data associated with a specific key.

    List Clipboard Data: View all clipboard data along with their respective keys.

Installation

    Requirements: Make sure you have Python installed on your system.

    Clone the Repository:

    bash

git clone https://github.com/your-username/multi-clipboard-manager.git
cd multi-clipboard-manager

Run the Script:

bash

    python multi_clipboard.py [command]

    Replace [command] with one of the following:
        save: Save clipboard data under a key.
        load: Load clipboard data associated with a key.
        delete: Delete clipboard data by key.
        list: List all clipboard data.

Usage

    Save Clipboard Data:

    bash

python multi_clipboard.py save

The script will prompt you to assign a key to the clipboard content.

Load Clipboard Data:

bash

python multi_clipboard.py load

You'll be asked to enter the key for the clipboard content you want to load.

Delete Clipboard Data:

bash

python multi_clipboard.py delete

Provide the key of the clipboard data you want to delete.

List Clipboard Data:

bash

    python multi_clipboard.py list

    This will display all saved clipboard data along with their respective keys.

Data Persistence

Clipboard data is saved in a JSON file, ensuring that your data is persistently available even after script execution.
Contributing

Contributions are welcome! Feel free to open issues and pull requests.