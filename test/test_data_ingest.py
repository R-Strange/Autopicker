import unittest

from data_ingest import IngestData


class TestIngestData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TestIngestData = IngestData()

    def test_run_valid_paths(self):
        valid_test_paths = ["correct.csv", "correct.json", "correct.sac", "correct.wav", "different_filename.csv",
                              "123NumbersAnd_Caps.csv", r"C:\\longer_test\string\with\file\over\here.csv",
                              "/what/about/absolute/linux/paths.csv", "../or/relative/paths.csv",
                              r".\and\windows\relative\paths.csv", "./local_linux_path.csv"]

        for valid_path in valid_test_paths:
            TestIngestData.run(valid_path)
            self.assertEqual(self.TestIngestData.input_path, valid_path)

    def test_run_failing_paths(self):
        failing_test_paths = [""]

        for failing_path in failing_test_paths:
            self.assertRaises(self.TestIngestData.run(failing_path), ValueError)


    def test_file_type_check_csv(self):
        self.TestIngestData.input_path = "correct.csv"
        self.assertEqual(self.TestIngestData.file_type_check, "csv")


    def test_file_type_check_json(self):
        self.TestIngestData.input_path = "correct.json"
        self.assertEqual(self.TestIngestData.file_type_check, "json")


    def test_file_type_check_sac(self):
        self.TestIngestData.input_path = "correct.sac"
        self.assertEqual(self.TestIngestData.file_type_check, "sac")


    def test_file_type_check_wav(self):
        self.TestIngestData.input_path = "correct.wav"
        self.assertEqual(self.TestIngestData.file_type_check, "wav")


    def test_file_type_check_longer(self):
        self.TestIngestData.input_path = "different_filename_which_is_quite_a_bit_Longer.csv"
        self.assertEqual(self.TestIngestData.file_type_check, "csv")


    def test_file_type_check_allowed_chars(self):
        self.TestIngestData.input_path = "123NumbersAnd_Caps_are_expected.csv"
        self.assertEqual(self.TestIngestData.file_type_check, "csv")


    def test_file_type_check_non_allowed_chars(self):
        self.TestIngestData.input_path = "a!£$%^&*()=+|<>?/`¬@;:.csv"
        self.assertFalse(self.TestIngestData.file_type_check)


    def test_file_type_check_no_extension(self):
        self.TestIngestData.input_path = "no_extension"
        self.assertFalse(self.TestIngestData.file_type_check)


    def test_file_type_check_no_filename(self):
        self.TestIngestData.input_path = ""
        self.assertFalse(self.TestIngestData.file_type_check)