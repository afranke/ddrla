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

summaryExpectedContent = """current pos: 506.6 GB
non-split: 1.5 MB
bad-bytes: 639.7 kB
non-trimmed: 244.4 MB
non-tried: 113.2 GB
rescued: 886.7 GB"""

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
        self.assertEqual(displayedValue, 'rescued: 886.7 GB')
        displayedValue = self.summary.display('get_nontried_bytes', False)
        self.assertEqual(displayedValue, '113.2 GB')
        displayedValue = self.summary.display('get_nontrimmed_bytes', False)
        self.assertEqual(displayedValue, '244.4 MB')
        displayedValue = self.summary.display('get_nonsplit_bytes', True)
        self.assertEqual(displayedValue, 'non-split: 1.5 MB')
        displayedValue = self.summary.display('get_bad_bytes')
        self.assertEqual(displayedValue, 'bad-bytes: 639.7 kB')

    def test_get_summary(self):
        summaryContent = self.summary.get_summary()
        self.assertEqual(summaryContent, summaryExpectedContent);
