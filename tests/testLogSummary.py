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

from ddrla.logSummary import LogSummary


class TestLogSummary(unittest.TestCase):
    package = dirname(dirname(abspath(__file__)))
    summary = None

    def setUp(self):
        testFile = join(self.package, 'data', 'ddrescue_sample.log')
        self.summary = LogSummary(testFile)

    def test_call_parser_function(self):
        rescuedBytes = self.summary.call_parser_function('get_rescued_bytes')
        self.assertEqual(rescuedBytes, '886.7 GB')

    def test_display(self):
        displayedValue = \
            self.summary.display('get_current_status_position', True)
        self.assertEqual(displayedValue, 'current pos: 506.6 GB')
        displayedValue= \
            self.summary.display('get_current_status_position', False)
        self.assertEqual(displayedValue, '506.6 GB')
        displayedValue = self.summary.display('get_rescued_bytes')

