import numpy as np
import pandas as pd

class IngestData:

    def __init__(self):
        self.input_path = ""
        self.viable_flag = False

    def run(self, input_path):
        pass

    def file_type_check(self, input_path):
        pass

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