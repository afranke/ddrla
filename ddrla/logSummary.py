# logSummary.py
#
# Copyright (C) 2015 Kevin Hagner
#
# ddrla is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from logParser import LogParser
import humanize


class LogSummary:
    parser = None
    display_dict = {'get_current_status_position': 'current pos',
                    'get_rescued_bytes': 'rescued',
                    'get_nontried_bytes': 'non-tried',
                    'get_nontrimmed_bytes': 'non-trimmed',
                    'get_nonsplit_bytes': 'non-split',
                    'get_bad_bytes': 'bad-bytes'
                    }

    def __init__(self, file):
        self.parser = LogParser(file)

    def get_summary(self):
        """
            Will print all informations extracted from the log file in a text block.
        """
        return '\n'.join([self.display(k) for k in self.display_dict])

    def display(self, func_name, readable=True):
        """
            Will display the total amount of something computed by the
            logParser class. The called function has to be present in the
            self.display_dict array for having a relation between her and
            his label.
            :param func_name: function of the LogParser object to call.
            :param readable: if True, we also print the label associated.
        """
        result = ""
        if readable:
            result += self.display_dict[func_name] + ': '
        result += self.call_parser_function(func_name)
        return result

    def call_parser_function(self, func_name):
        """
            Call a function of the parser that should return an amount
            of bytes for being displayed.
            This value will be humanized for readability purpose.
        """
        val = getattr(self.parser, func_name)()
        return humanize.naturalsize(
            val if isinstance(val, int) else int(val, 0))

