# Copyright (c) 2015 Kevin Hagner
#
# ddrla is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ddrla is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ddrla.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname, abspath, join
import unittest

from ddrla.logParser import LogParser

class TestLogParser(unittest.TestCase):

    package = dirname(dirname(abspath(__file__)))

    def setUp(self):
        testFile = join(self.package, 'data', 'ddrescue_sample.log')
	self.parser = LogParser(testFile)

    def __fillTestFile(self):
        self.testFile.write(b"# This is a comment\n")
        self.testFile.write(b"0x75F3BC0000     ?\n")
        self.testFile.write(b"0x00000000  0xC2629000  +\n")
        self.testFile.write(b"0xC2629000  0x00000200  -\n")
        self.testFile.write(b"0xC2629200  0x00000C00  ?\n")
        self.testFile.write(b"0xC2629E00  0x00000200  -\n")
        self.testFile.write(b"0xC262A000  0x0013E000  +\n")
        self.testFile.write(b"0xC2768000  0x00001000  ?\n")
        self.testFile.write(b"0xC2769000  0x0013E000  +\n")
        self.testFile.write(b"0xC28A7000  0x00001000  ?\n")
        self.testFile.write(b"0xC28A8000  0x5E836000  +\n")
        self.testFile.write(b"0x1210DE000  0x00000200  -\n")
        self.testFile.write(b"0x1210DE200  0x00000C00  ?\n")
        self.testFile.write(b"0x1210DEE00  0x00000200  -\n")
        self.testFile.write(b"0x1210DF000  0xA86B7000  +\n")
        self.testFile.write(b"0x1C9796000  0x00000200  -\n")
        self.testFile.write(b"0x1C9796200  0x00000C00  ?\n")
        self.testFile.write(b"0x1C9796E00  0x00000200  -\n")
        self.testFile.write(b"0x1C9797000  0x0013D000  +\n")
        self.testFile.write(b"0x1C98D4000  0x00001000  ?\n")
        self.testFile.write(b"0x1C98D5000  0x0013E000  +\n")
        self.testFile.write(b"0x1C9A13000  0x00001000  ?\n")
        self.testFile.write(b"0x1C9A14000  0x0013E000  +\n")
        self.testFile.write(b"0x1C9B52000  0x00001000  ?\n")
        self.testFile.write(b"0x1C9B53000  0xE0B43000  +\n")
        self.testFile.write(b"0x2AA696000  0x00000200  -\n")
        self.testFile.write(b"0x2AA696200  0x00000C00  ?\n")
        self.testFile.write(b"0x2AA696E00  0x00000200  -\n")
        self.testFile.write(b"0x2AA697000  0x07F28000  +\n")
        self.testFile.write(b"0x2B25BF000  0x00000200  -\n")
        self.testFile.write(b"0x2B25BF200  0x00000C00  ?\n")
        self.testFile.write(b"0x2B25BFE00  0x00000200  -\n")
        self.testFile.write(b"0x2B25C0000  0x3DF2B3000  +\n")
        self.testFile.write(b"0x691873000  0x00000200  -\n")
        self.testFile.write(b"0x691873200  0x00000C00  ?\n")
        self.testFile.write(b"0x691873E00  0x00000200  -\n")
        self.testFile.write(b"0x691874000  0x00265000  +\n")
        self.testFile.write(b"0x691AD9000  0x00001000  ?\n")
        self.testFile.write(b"0x691ADA000  0x00132000  +\n")
        self.testFile.write(b"0x691C0C000  0x00001000  ?\n")
        self.testFile.write(b"0x691C0D000  0x00132000  +\n")
        self.testFile.write(b"0x691D3F000  0x00001000  ?\n")
        self.testFile.write(b"0x691D40000  0x002A4000  +\n")
        self.testFile.write(b"0x691FE4000  0x00001000  ?\n")
        self.testFile.write(b"0x691FE5000  0x00132000  +\n")
        self.testFile.write(b"0x692117000  0x00000200  -\n")
        self.testFile.write(b"0x692117200  0x00000C00  ?\n")
        self.testFile.write(b"0x692117E00  0x00000200  -\n")
        self.testFile.write(b"0x692118000  0x00B0A000  +\n")
        self.testFile.write(b"0x692C22000  0x00000200  -\n")
        self.testFile.write(b"0x692C22200  0x00000C00  ?\n")
        self.testFile.write(b"0x692C22E00  0x00000200  -\n")
        self.testFile.write(b"0x692C23000  0x00132000  +\n")
        self.testFile.write(b"0x692D55000  0x00001000  ?\n")
        self.testFile.write(b"0x692D56000  0x00132000  +\n")
        self.testFile.seek(0)


    def testGetLogsDictionnary(self):
        log_dict = self.parser.getLogsDictionnary()
        self.assertEqual(len(log_dict), 30204)
        map(lambda e: self.assertTrue(len(e) == 3), log_dict)
        self.assertEqual(log_dict[0], ['0x00000000', '0xC2629000', '+'])
        self.assertEqual(log_dict[-1], ['0xE8D4A51000', '0x0C365000', '?'])

    def testGetLogsStatistics(self):
	    log_stat = self.parser.getLogsStatistics()
