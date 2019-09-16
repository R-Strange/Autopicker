from unittest import TestCase, main
from unittest.mock import MagicMock

from obspy.core import AttribDict

from data_classes import SacDataClass
import numpy as np


# noinspection SpellCheckingInspection
class TestSacDataClass(TestCase):

    # noinspection DuplicatedCode
    @classmethod
    def setUp(cls):
        cls.TestSacDataClass = SacDataClass()
        cls.test_stream = MagicMock(return_value=None)
        cls.test_stream.trace = MagicMock(return_value=None)
        cls.test_stream.trace.data = MagicMock(return_value=None)
        cls.test_stream.trace.stats.network = MagicMock(return_value=None)
        cls.test_stream.trace.stats.station = MagicMock(return_value=None)
        cls.test_stream.trace.stats.location = MagicMock(return_value=None)
        cls.test_stream.trace.stats.channel = MagicMock(return_value=None)
        cls.test_stream.trace.stats.starttime = MagicMock(return_value=None)
        cls.test_stream.trace.stats.endtime = MagicMock(return_value=None)
        cls.test_stream.trace.stats.sampling_rate = MagicMock(return_value=None)
        cls.test_stream.trace.stats.delta = MagicMock(return_value=None)
        cls.test_stream.trace.stats.npts = MagicMock(return_value=None)
        cls.test_stream.trace.stats.calib = MagicMock(return_value=None)
        cls.test_stream.trace.stats._format = MagicMock(return_value=None)
        cls.test_stream.trace.stats.sac = MagicMock(return_value=None)

    def test_dataclass_exists(self):


    def test_simple_load(self):
        self.test_stream = MagicMock()
        self.test_stream.trace = MagicMock()
        self.test_stream.trace.data = MagicMock(return_value=np.ndarray([1, 2, 3, 4, 5]))
        self.test_stream.trace.stats.network = MagicMock(return_value="YW")
        self.test_stream.trace.stats.station = MagicMock(return_value="NAB1")
        self.test_stream.trace.stats.location = MagicMock(return_value=None)
        self.test_stream.trace.stats.channel = MagicMock(return_value="HHE")
        self.test_stream.trace.stats.starttime = MagicMock(return_value="2011-08-29T00:23:00.330000z")
        self.test_stream.trace.stats.endtime = MagicMock(return_value="2011-08-29T00:28:00.330000z")
        self.test_stream.trace.stats.sampling_Rate = MagicMock(return_value=100.0)
        self.test_stream.trace.stats.delta = MagicMock(return_value=0.01)
        self.test_stream.trace.stats.npts = MagicMock(return_value=30001)
        self.test_stream.trace.stats.calib = MagicMock(return_value=1.0)
        self.test_stream.trace.stats._format = MagicMock(return_value="SAC")
        self.test_stream.trace.stats.sac = MagicMock(return_value=AttribDict(
            {'delta': 0.01, 'depmin': -5738.68, 'depmax': 6150.5957, 'scale': 1.0, 'b': 0.0, 'e': 300.0, 'a': 62486.64,
             'internal0': 2.0, 't0': 102.571045, 't5': 100.85, 't6': 102.659996, 'stla': 13.3873, 'stlo': 41.6554,
             'stel': 1329.0, 'stdp': 0.0, 'depmen': -0.04127816, 'cmpaz': 90.0, 'cmpinc': 90.0, 'nzyear': 2011,
             'nzjday': 241, 'nzhour': 0, 'nzmin': 23, 'nzsec': 0, 'nzmsec': 330, 'nvhdr': 6, 'norid': 0, 'nevid': 0,
             'npts': 30001, 'iftype': 1, 'idep': 5, 'leven': 1, 'lpspol': 0, 'lcalda': 1, 'kstnm': 'NAB1    ',
             'ka': 'IPD0    ', 'kt0': 'ISU1    ', 'kcmpnm': 'HHE     ', 'knetwk': 'YW      ', 'kevnm': '        '}))

        self.TestSacDataClass.stream_object = self.test_stream

        self.assertEqual(self.test_stream.trace, )



if __name__ == '__main__':
    main()
