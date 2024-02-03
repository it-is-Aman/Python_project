# Multi Clipboard Manager

A Python script that simplifies clipboard data management by providing functions to save, load, delete, and list clipboard data using command-line operations.

## Features

- **Save Clipboard Data**: Save the current clipboard content under a user-specified key.

- **Load Clipboard Data**: Copy clipboard content associated with a key to the clipboard.

- **Delete Clipboard Data**: Remove clipboard data associated with a specific key.

- **List Clipboard Data**: View all stored clipboard data and their respective keys.

## Installation

1. **Prerequisites**: Ensure you have Python installed on your system.

2. **Clone the Repository**: Clone the repository to your local machine
3. **Running the Script**:

    Use the following command to execute the script:

    ```
    python multi_clipboard.py [command]
    ```
    Replace `[command]` with one of the following options:
      *  save: Save clipboard data under a user-defined key.
      *  load: Load clipboard data associated with a key.
      *  delete: Delete clipboard data by key.
      *  list: List all clipboard data.

## Usage

* Save Clipboard Data:
```
python multi_clipboard.py save
```
The script will prompt you to assign a key to the current clipboard content.


* Load Clipboard Data:
```
python multi_clipboard.py load
```
You'll be asked to provide the key for the clipboard content you want to load.


* Delete Clipboard Data:
```
python multi_clipboard.py delete
```
Specify the key of the clipboard data you want to delete.


* List Clipboard Data:
```
python multi_clipboard.py list
```
This command displays all saved clipboard data along with their respective keys.


## Data Persistence

Clipboard data is saved to a JSON file ('clipboard.json'), ensuring that your data remains available for future use, even after the script has finished executing.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please feel free to open issues and submit pull requests.