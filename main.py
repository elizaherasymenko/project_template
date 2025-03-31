import os
from app.io.input import input_text_from_console, read_file_builtin, read_file_with_pandas
from app.io.output import output_text_to_console, write_to_file_builtin, write_to_file_with_pandas


def main():
    user_input = input_text_from_console()

    content_builtin = read_file_builtin("data/text_example.txt")

    content_pandas = read_file_with_pandas("data/text_example.csv")

    output_text_to_console(user_input)
    output_text_to_console(content_builtin)
    output_text_to_console(content_pandas)

    write_to_file_builtin("data/text_output.txt", user_input)

    write_to_file_with_pandas("data/text_output.csv", content_pandas)


if __name__ == "__main__":
    main()
