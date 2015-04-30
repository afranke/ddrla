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

    def __init__(self, file):
        self.parser = LogParser(file)

    def call_parser_function(self, func_name):
        """
            Call a function of the parser that should return an amount
            of bytes for being displayed.
            This value will be humanized for readability purpose.
        """
        val = getattr(self.parser, func_name)()
        return humanize.naturalsize(
            val if isinstance(val, int) else int(val, 0))

