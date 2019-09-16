from unittest import TestCase, main
from unittest.mock import *
from data_ingest import IngestData


# noinspection SpellCheckingInspection
class TestIngestData(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TestIngestData = IngestData()

    def test_set_input_path_valid_paths(self):
        valid_test_paths = ["correct.csv", "correct.sac", "different_filename.csv",
                              "123NumbersAnd_Caps.csv", r"C:\\longer_test\string\with\file\over\here.csv",
                              "/what/about/absolute/linux/paths.csv", "../or/relative/paths.csv",
                              r".\and\windows\relative\paths.csv", "./local_linux_path.csv"]

        for valid_path in valid_test_paths:
            self.TestIngestData.set_input_path(valid_path)
            self.assertEqual(self.TestIngestData.input_path, valid_path)

    def test_set_input_path_failing_paths(self):
        failing_test_paths = [""]

        for failing_path in failing_test_paths:
            self.assertRaises(ValueError, self.TestIngestData.set_input_path, failing_path)

    def test_file_type_check_csv(self):
        self.TestIngestData.input_path = "correct.csv"
        self.assertEqual(self.TestIngestData.file_type_check(), "csv")

    def test_file_type_check_sac(self):
        self.TestIngestData.input_path = "correct.sac"
        self.assertEqual(self.TestIngestData.file_type_check(), "sac")


    def test_file_type_check_longer(self):
        self.TestIngestData.input_path = "different_filename_which_is_quite_a_bit_Longer.csv"
        self.assertEqual(self.TestIngestData.file_type_check(), "csv")

    def test_file_type_check_allowed_chars(self):
        self.TestIngestData.input_path = "123NumbersAnd_Caps_are_expected.csv"
        self.assertEqual(self.TestIngestData.file_type_check(), "csv")

    def test_file_type_check_dot_in_directory_with_extension(self):
        self.TestIngestData.input_path = "test/path/with.dot/and.csv"
        self.assertEqual(self.TestIngestData.file_type_check(), "csv")

    def test_file_type_check_dot_in_directory_with_no_extension(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = "test/path/with.dot/and/no_extension"
            self.TestIngestData.file_type_check()

        self.assertEqual(str(cm.exception), "Error, no file extension in filename")

    def test_file_type_check_non_allowed_chars(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = "a!£$%^&*()=+.|<>?/`¬@;:.csv"
            self.TestIngestData.file_type_check()

        self.assertEqual(str(cm.exception), "Error, unsupported characters in filename")

    def test_file_type_check_no_extension(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = "no_extension"
            self.TestIngestData.file_type_check()

        self.assertEqual(str(cm.exception), "Error, no file extension in filename")

    def test_file_type_check_no_filename(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = ""
            self.TestIngestData.file_type_check()

        self.assertEqual(str(cm.exception), "Error, invalid path to data file")

    def test_file_type_check_only_directory(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = "/path/to/the/data/directory/only/"
            self.TestIngestData.file_type_check()

        self.assertEqual(str(cm.exception), "Error, path only points to directory")

    def test_csv_load_happy(self):
        self.TestIngestData.input_path = "../test_data/ingestion/Specimen_Event.csv"
        self.TestIngestData.csv_load()
        print(self.TestIngestData.shape_of_input)
        self.assertEqual(self.TestIngestData.shape_of_input, (30001, 2))

    def test_csv_load_lazy(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = "../test_data/ingestion/Empty_Event.csv"
            self.TestIngestData.csv_load()
        self.assertEqual(str(cm.exception), "Error, the csv file is empty")

    def test_csv_load_sad(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = "../test_data/ingestion/Corrupted_Event.csv"
            self.TestIngestData.csv_load()
        self.assertEqual(str(cm.exception), "Error, data is incorrectly formatted or corrupt")

    def test_csv_load_missing(self):
        with self.assertRaises(FileNotFoundError) as cm:
            self.TestIngestData.input_path = "../test_data/ingestion/Nonexistent_Event.csv"
            self.TestIngestData.csv_load()
        self.assertEqual(str(cm.exception), "The csv file cannot be found. Is the path correct, or does the file exist?")

    def test_sac_load_happy(self):
        self.TestIngestData.input_path = "../test_data/ingestion/Specimen_Event.sac"
        self.TestIngestData.sac_load()
        self.assertEqual(self.TestIngestData.shape_of_input, (30001, 2))

    def test_file_errors_check_csv_happy_horizontal(self):
        self.TestIngestData.input_path="../test_data/ingestion/20110829.002440.YW.NAB1.HHE.SAC"
        self.TestIngestData.sac_load()
        self.assertEqual(self.TestIngestData.shape_of_input, (30001, 2))


    def test_file_errors_check_csv_happy_lateral(self):
        self.TestIngestData.input_path="../test_data/ingestion/20110829.002440.YW.NAB1.HHN.SAC"
        self.TestIngestData.sac_load()
        self.assertEqual(self.TestIngestData.shape_of_input, (30001, 2))


    def test_file_errors_check_csv_happy_vertical(self):
        self.TestIngestData.input_path="../test_data/ingestion/20110829.002440.YW.NAB1.HHZ.SAC"
        self.TestIngestData.sac_load()
        self.assertEqual(self.TestIngestData.shape_of_input, (30001, 2))


    def test_sac_load_lazy(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = "../test_data/ingestion/Empty_Event.sac"
            self.TestIngestData.sac_load()
        self.assertEqual(str(cm.exception), "Error, file is empty")

    def test_sac_load_sad(self):
        with self.assertRaises(ValueError) as cm:
            self.TestIngestData.input_path = "../test_data/ingestion/Sad_Event.sac"
            self.TestIngestData.sac_load()
        self.assertEqual(str(cm.exception), "Error, data is incorrectly formatted or corrupt")

    def test_sac_load_missing(self):
        with self.assertRaises(FileNotFoundError) as cm:
            self.TestIngestData.input_path = "../test_data/ingestion/Nonexistent_Event.sac"
            self.TestIngestData.sac_load()
        self.assertEqual(str(cm.exception), "Error, the file cannot be found")

    def test_file_exists_check_happy(self):
        self.TestIngestData.input_path = "../test_data/ingestion/Specimen_Event.csv"
        self.TestIngestData.file_exists_check()
        self.assertTrue(self.TestIngestData.file_exists_flag)

    def test_file_exists_check_sad(self):
        with self.assertRaises(FileNotFoundError) as cm:
            self.TestIngestData.input_path = "../test_data/ingestion/Nonexistent_Event.csv"
            self.TestIngestData.file_exists_check()
        self.assertEqual(str(cm.exception), "The file cannot be found, Is the path correct or does the file exist?")

    def test_file_errors_check_csv_happy(self):
        self.TestIngestData.input_path="../test_data/ingestion/Specimen_Event.csv"
        self.TestIngestData.csv_file_errors_check()
        self.assertFalse(self.TestIngestData.file_has_errors)
        self.assertTrue(self.TestIngestData.file_has_headers)

    def test_file_errors_check_csv_sad(self):
        self.TestIngestData.input_path="../test_data/ingestion/Corrupted_Event.csv"
        self.TestIngestData.csv_file_errors_check()
        self.assertTrue(self.TestIngestData.file_has_errors)
        self.assertTrue(self.TestIngestData.file_has_headers)

    def test_file_errors_check_csv_lazy(self):
        self.TestIngestData.input_path="../test_data/ingestion/Empty_Event.csv"
        self.TestIngestData.csv_file_errors_check()
        self.assertTrue(self.TestIngestData.file_has_errors)
        self.assertFalse(self.TestIngestData.file_has_headers)

    def test_reconstruct_seconds_from_sac_happy(self):
        """mock trace"""


        self.mock_stream.trace.stats.npts = MagicMock(return_value=30001)
        self.mock_stream.trace.stats.

        self.TestIngestData.


if __name__ == '__main__':
    main()