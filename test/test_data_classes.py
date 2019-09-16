from unittest import TestCase, main
from unittest.mock import MagicMock

from dataclasses import fields

from obspy import UTCDateTime
from obspy.core import AttribDict

from data_classes import SacDataClass
import numpy as np

def blank_sac_dataclass_load_helper(sac_data_class, test_stream):
    sac_data_class.network = test_stream.trace.stats.network
    sac_data_class.station = test_stream.trace.stats.station
    sac_data_class.location = test_stream.trace.stats.location
    sac_data_class.channel = test_stream.trace.stats.channel
    sac_data_class.start_time = test_stream.trace.stats.starttime
    sac_data_class.end_time = test_stream.trace.stats.endtime
    sac_data_class.sampling_rate = test_stream.trace.stats.sampling_rate
    sac_data_class.delta = test_stream.trace.stats.delta
    sac_data_class.number_of_points = test_stream.trace.stats.npts
    sac_data_class.scale_factor = test_stream.trace.stats.calib
    sac_data_class.format = test_stream.trace.stats._format
    sac_data_class.sac_header = test_stream.trace.stats.sac


# noinspection SpellCheckingInspection
class TestStaticSacDataClass(TestCase):

    # noinspection DuplicatedCode
    @classmethod
    def setUp(cls):
        blank_sac_headers = AttribDict(
            {'delta': 0.005, 'depmin': -5000, 'depmax': 6000, 'scale': 1.0, 'b': 0.0, 'e': 300.0, 'a': 62486.64,
             'internal0': 2.0, 't0': 102.571045, 't5': 100.85, 't6': 102.659996, 'stla': 13.3873, 'stlo': 41.6554,
             'stel': 1329.0, 'stdp': 0.0, 'depmen': -0.04127816, 'cmpaz': 90.0, 'cmpinc': 90.0, 'nzyear': 2011,
             'nzjday': 241, 'nzhour': 0, 'nzmin': 23, 'nzsec': 0, 'nzmsec': 330, 'nvhdr': 6, 'norid': 0, 'nevid': 0,
             'npts': 30001, 'iftype': 1, 'idep': 5, 'leven': 1, 'lpspol': 0, 'lcalda': 1, 'kstnm': 'NAB1    ',
             'ka': 'IPD0    ', 'kt0': 'ISU1    ', 'kcmpnm': 'HHE     ', 'knetwk': 'YW      ', 'kevnm': '        '})


        cls.TestSacDataClass = SacDataClass("blank_source", "no_network", "no_station", "no_location", "no_channel", UTCDateTime("1970-01-01T12:00:00"), UTCDateTime("1970-01-01T12:00:01"), 200, 0.005, 500, blank_sac_headers, "sac", 1.0)

        cls.test_stream = MagicMock()
        cls.test_stream.trace = MagicMock()
        cls.test_stream.trace.data = MagicMock(return_value=np.ndarray([1, 2, 3, 4, 5]))
        cls.test_stream.trace.stats.network = MagicMock(return_value="YW")
        cls.test_stream.trace.stats.station = MagicMock(return_value="NAB1")
        cls.test_stream.trace.stats.location = MagicMock(return_value=None)
        cls.test_stream.trace.stats.channel = MagicMock(return_value="HHE")
        cls.test_stream.trace.stats.starttime = MagicMock(return_value="2011-08-29T00:23:00.330000z")
        cls.test_stream.trace.stats.endtime = MagicMock(return_value="2011-08-29T00:28:00.330000z")
        cls.test_stream.trace.stats.sampling_Rate = MagicMock(return_value=100.0)
        cls.test_stream.trace.stats.delta = MagicMock(return_value=0.01)
        cls.test_stream.trace.stats.npts = MagicMock(return_value=30001)
        cls.test_stream.trace.stats.calib = MagicMock(return_value=1.0)
        cls.test_stream.trace.stats._format = MagicMock(return_value="SAC")
        cls.test_stream.trace.stats.sac = MagicMock(return_value=AttribDict(
            {'delta': 0.01, 'depmin': -5738.68, 'depmax': 6150.5957, 'scale': 1.0, 'b': 0.0, 'e': 300.0, 'a': 62486.64,
             'internal0': 2.0, 't0': 102.571045, 't5': 100.85, 't6': 102.659996, 'stla': 13.3873, 'stlo': 41.6554,
             'stel': 1329.0, 'stdp': 0.0, 'depmen': -0.04127816, 'cmpaz': 90.0, 'cmpinc': 90.0, 'nzyear': 2011,
             'nzjday': 241, 'nzhour': 0, 'nzmin': 23, 'nzsec': 0, 'nzmsec': 330, 'nvhdr': 6, 'norid': 0, 'nevid': 0,
             'npts': 30001, 'iftype': 1, 'idep': 5, 'leven': 1, 'lpspol': 0, 'lcalda': 1, 'kstnm': 'NAB1    ',
             'ka': 'IPD0    ', 'kt0': 'ISU1    ', 'kcmpnm': 'HHE     ', 'knetwk': 'YW      ', 'kevnm': '        '}))

    def test_simple_stats_load(self):

        blank_sac_dataclass_load_helper(self.TestSacDataClass, self.test_stream)

        # self.assertEqual(self.test_stream.trace.stats, self.TestSacDataClass.source_name)
        self.assertEqual(self.test_stream.trace.stats.network, self.TestSacDataClass.network)
        self.assertEqual(self.test_stream.trace.stats.station, self.TestSacDataClass.station)
        self.assertEqual(self.test_stream.trace.stats.location, self.TestSacDataClass.location)
        self.assertEqual(self.test_stream.trace.stats.channel, self.TestSacDataClass.channel)
        self.assertEqual(self.test_stream.trace.stats.starttime, self.TestSacDataClass.start_time)
        self.assertEqual(self.test_stream.trace.stats.endtime, self.TestSacDataClass.end_time)
        self.assertEqual(self.test_stream.trace.stats.sampling_rate, self.TestSacDataClass.sampling_rate)
        self.assertEqual(self.test_stream.trace.stats.delta, self.TestSacDataClass.delta)
        self.assertEqual(self.test_stream.trace.stats.npts, self.TestSacDataClass.number_of_points)
        self.assertEqual(self.test_stream.trace.stats.sac, self.TestSacDataClass.sac_header)
        self.assertEqual(self.test_stream.trace.stats._format, self.TestSacDataClass.format)
        self.assertEqual(self.test_stream.trace.stats.calib, self.TestSacDataClass.scale_factor)

if __name__ == '__main__':
    main()
