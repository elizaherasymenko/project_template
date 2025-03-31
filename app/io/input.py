def input_text_from_console():
    """Function to input text from the console"""
    return input("Enter text: ")

def read_file_builtin(file_path):
    """Function to read from a file using Python's built-in capabilities"""
    with open(file_path, 'r') as file:
        return file.read()

def read_file_with_pandas(file_path):
    """Function to read from a file using the pandas library"""
    import pandas as pd
    return pd.read_csv(file_path)
