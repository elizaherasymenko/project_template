def output_text_to_console(text):
    """Function to output text to the console"""
    print(text)


def write_to_file_builtin(file_path, content):
    """Function to write to a file using Python's built-in capabilities"""
    with open(file_path, 'w') as file:
        file.write(content)

def write_to_file_with_pandas(file_path, content):
    """Function to write to a file using the pandas library"""
    import pandas as pd
    content.to_csv(file_path, index=False)