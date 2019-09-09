import os
import numpy as np
import pandas as pd


class IngestData:

    def __init__(self):
        self.input_path = ""
        self.data_format = False
        self.viable_flag = False
        self.length_of_input = 0


    def run(self, input_path):
        """
        core function for the method.
        :param input_path:
        :return:
        """
        pass

    def set_input_path(self, input_path):
        """
        Sets the internal filepath, if not null.
        :param input_path:  the user-provided path to the input file
        :return: None,
        """
        if input_path:
            self.input_path = input_path
        if not input_path:
            raise ValueError("Error, invalid path to data file")

    def file_type_check(self):
        """
        Checks the format of the value, and returns either a csv, wav, sac, or json flag, or a False for unsupported
        :return format_flag: flag of the file type.
        """
        if not self.input_path:
            raise ValueError("Error, invalid path to data file")

        unsupported_characters_string = r"!£$%^&*()-+=[]{}#~@:;`¬|?>,<"
        contains_unsupported_characters = bool(
            [character for character in unsupported_characters_string if (character in self.input_path)])
        if contains_unsupported_characters:
            raise ValueError("Error, unsupported characters in filename")

        file_directory, filename = os.path.split(self.input_path)

        if not filename:
            raise ValueError("Error, path only points to directory")

        if len(filename.split(".")) < 2:
            raise ValueError("Error, no file extension in filename")

        file_extension = filename.split(".")[-1]

        file_extension_flag = False

        if file_extension.lower() == "csv":
            file_extension_flag = "csv"

        elif file_extension.lower() == "json":
            file_extension_flag = "json"

        elif file_extension.lower() == "sac":
            file_extension_flag = "sac"

        elif file_extension.lower() == "wav":
            file_extension_flag = "wav"

        return file_extension_flag

    def csv_load(self):
        pass

    def json_load(self):
        pass

    def sac_load(self):
        pass

    def wav_load(self):
        pass

    def data_check(self):
        """
        do data completeness and NaN checks on successfully imported data.
        :return:
        """
        pass
