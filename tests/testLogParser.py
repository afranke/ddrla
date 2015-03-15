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
    parser = None

    def setUp(self):
        testFile = join(self.package, 'data', 'ddrescue_sample.log')
        self.parser = LogParser(testFile)

    def testGetLogsDictionnary(self):
        log_dict = self.parser.getLogsDictionnary()
        self.assertEqual(len(log_dict), 30204)
        map(lambda e: self.assertTrue(len(e) == 3), log_dict)
        self.assertEqual(log_dict[0], ['0x00000000', '0xC2629000', '+'])
        self.assertEqual(log_dict[-1], ['0xE8D4A51000', '0x0C365000', '?'])

    def testGetLogsStatistics(self):
        log_stat = self.parser.getLogsStatistics()
        self.assertEqual(log_stat, {
          'total': 1000204886016,
          'rescued': 886719395136,
          'nontried': 113238912320,
          'bad': 639744,
          'nontrimmed': 244389504,
          'nonsplit': 1549312
        })

    def testGetCurrentStatus(self):
        current_status = self.parser.getCurrentStatus()
        self.assertEqual(current_status, ['0x75F3BC0000', '?'])
