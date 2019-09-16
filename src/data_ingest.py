import os
import numpy as np
import pandas as pd
import goodtables as gt
import obspy
from obspy.core import AttribDict

from data_classes import SacDataClass
from obspy import UTCDateTime


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
        self.sac_dataclass_obj = None

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

    def instantiate_sac_dataclass(self):

        _blank_sac_headers = AttribDict(
            {'delta': 0, 'depmin': 0, 'depmax': 0, 'scale': 1.0, 'b': 0.0, 'e': 0, 'a': 0,
             'internal0': 0, 't0': 0, 't5': 0, 't6': 0, 'stla': 0, 'stlo': 0,
             'stel': 0, 'stdp': 0.0, 'depmen': 0, 'cmpaz': 0, 'cmpinc': 0, 'nzyear': 0,
             'nzjday': 0, 'nzhour': 0, 'nzmin': 0, 'nzsec': 0, 'nzmsec': 0, 'nvhdr': 0, 'norid': 0, 'nevid': 0,
             'npts': 0, 'iftype': 0, 'idep': 0, 'leven': 0, 'lpspol': 0, 'lcalda': 0, 'kstnm': 'BLANK',
             'ka': 'BLANK', 'kt0': 'BLANK', 'kcmpnm': 'BLANK', 'knetwk': 'BLANK', 'kevnm': 'BLANK'})

        _local_sac_dataclass = SacDataClass("blank_source", "no_network", "no_station", "no_location", "no_channel",
                                            UTCDateTime("1970-01-01T12:00:00"), UTCDateTime("1970-01-01T12:00:01"), 200,
                                            0.005, 500, _blank_sac_headers, "sac", 1.0)

        self.sac_dataclass_obj = _local_sac_dataclass

    def map_sac_to_dataclass(self):
        pass

        self.instantiate_sac_dataclass()

        self.sac_dataclass_obj.payload = self.sac_trace.data
        self.sac_dataclass_obj.network = self.sac_trace.stats.network
        self.sac_dataclass_obj.station = self.sac_trace.stats.station
        self.sac_dataclass_obj.location = self.sac_trace.stats.location
        self.sac_dataclass_obj.channel = self.sac_trace.stats.channel
        self.sac_dataclass_obj.start_time = self.sac_trace.stats.starttime
        self.sac_dataclass_obj.end_time = self.sac_trace.stats.endtime
        self.sac_dataclass_obj.sampling_rate = self.sac_trace.stats.sampling_rate
        self.sac_dataclass_obj.delta = self.sac_trace.stats.delta
        self.sac_dataclass_obj.number_of_points = self.sac_trace.stats.npts
        self.sac_dataclass_obj.scale_factor = self.sac_trace.stats.calib
        self.sac_dataclass_obj.format = self.sac_trace.stats._format
        self.sac_dataclass_obj.sac_header = dict(self.sac_trace.stats.sac)

    def reconstruct_seconds_from_sac(self):
        """

        :return:
        ToDo move to utils file
        """
        if self.sac_dataclass_obj.number_of_points <= 0:
            raise ValueError("Error, number of datapoints must be greater than 0")
        elif not isinstance(self.sac_dataclass_obj.number_of_points, int):
            raise ValueError("Error, number of datapoints expected as an Int")


        seconds_array = np.arange(start=0,
                                  stop=self.sac_dataclass_obj.number_of_points / self.sac_dataclass_obj.sampling_rate,
                                  step=self.sac_dataclass_obj.delta)

        return seconds_array


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

        try:
            stream = obspy.read(self.input_path)
        except TypeError:
            raise ValueError("Error, the sac file cannot be read, and may be empty or corrupted")

        self.sac_trace = stream[0]

        self.map_sac_to_dataclass()

        seconds_array = self.reconstruct_seconds_from_sac()

        assert(len(seconds_array) == self.sac_dataclass_obj.number_of_points)

        self.shape_of_input = (len(seconds_array), 2)

    def data_check(self):
        """
        do data completeness and NaN checks on successfully imported data.
        :return:
        """
        pass
