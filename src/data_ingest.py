import os
import numpy as np
import pandas as pd
import goodtables as gt
import obspy


class IngestData:

    def __init__(self):
        self.input_path = ""
        self.data_format = False
        self.viable_flag = False
        self.file_exists_flag = False
        self.shape_of_input = None
        self.sac_trace = None
        self.seconds_array = None
        self.dataframe = None
        self.file_has_errors = -1
        self.file_has_headers = -1

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

    def file_exists_check(self):
        """
        Checks if the file pathed to does actually exist, and updates the self.file_exists_flag
        :return:
        """
        file_is_real = os.path.isfile(self.input_path)

        if not file_is_real:
            raise FileNotFoundError("The file cannot be found, Is the path correct or does the file exist?")

        self.file_exists_flag = file_is_real

    def file_type_check(self):
        """
        Checks the format of the value, and returns either a csv, or sac flag, or a False for unsupported
        :return format_flag: flag of the file type.
        # ToDo refactor with more os functionality
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

        elif file_extension.lower() == "sac":
            file_extension_flag = "sac"

        return file_extension_flag

    def reconstruct_seconds_from_sac(self):
        """

        :return:
        ToDo move to utils file
        """
        pass
        # stats = self.sac_trace.stats
        #
        # start_time = 0
        # end_time = stats.npts / stats.sampling_rate
        # step_size = stats.delta
        #
        # self.seconds_array = np.arange(start=start_time,
        #                                stop=end_time,
        #                                step=step_size)

    def csv_file_errors_check(self):
        """

        :return:
        # ToDo add advanced goodtables checks in, refactor for simplicity
        """
        gt_result = gt.validate(self.input_path)

        try:
            headers = gt_result["tables"][0]["headers"]
        except KeyError as error:
            if "headers" in str(error):
                print("Data quality helper: \n There is no data in the input file")
                self.file_has_errors = True
                self.file_has_headers = False
                return None
            else:
                raise

        file_has_headers = not all([header.isdigit() for header in headers])

        self.file_has_headers = file_has_headers

        if not file_has_headers:
            print("Warning, file has no headers")
            return None

        file_contains_data = bool(gt_result["tables"][0]["row-count"])
        if not file_contains_data:
            print("Data quality helper: \n There are headers but no data in the input file.")
            self.file_has_errors = True
            return None

        number_of_data_errors = gt_result["tables"][0]["error-count"]
        file_has_data_errors = bool(number_of_data_errors)
        if file_has_data_errors:
            print(
                "Data quality helper: \n There are {} errors in the input file. \n find the errors printed below:".format(
                    number_of_data_errors))
            print(gt_result["tables"][0]["errors"])
            self.file_has_errors = True

        elif not file_has_data_errors:
            print("No data quality issues found in the first 1000 rows of data.")
            self.file_has_errors = False

    def csv_load(self):

        try:
            self.file_exists_check()
        except FileNotFoundError:
            raise FileNotFoundError("The csv file cannot be found. Is the path correct, or does the file exist?")

        self.csv_file_errors_check()
        if self.file_has_errors and self.file_has_headers:
            raise ValueError("Error, data is incorrectly formatted or corrupt")

        try:
            self.dataframe = pd.read_csv(self.input_path)
        except pd.errors.EmptyDataError:
            raise ValueError("Error, the csv file is empty")
        self.shape_of_input = self.dataframe.shape

    def sac_load(self):
        try:
            self.file_exists_check()
        except FileNotFoundError:
            raise FileNotFoundError("The sac file cannot be found, Is the path correct or does the file exist?")

        stream = obspy.read(self.input_path)

        trace = stream[0].data
        metadata = stream[0].stats

        reconstruct_seconds()

        self.shape_of_input

    def data_check(self):
        """
        do data completeness and NaN checks on successfully imported data.
        :return:
        """
        pass
