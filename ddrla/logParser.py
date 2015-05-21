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

import re


class LogParser:
    """
        Parse output logs from ddrescue command for being processed by
        the software.
    """

    def __init__(self, file):
        self.logs_dictionary = []
        self.logs_statistics = {}
        self.current_status = None
        self.__init_logs_statistics()
        self.__process_log_parsing(file)

    def get_logs_dictionnary(self):
        return self.logs_dictionary

    def get_logs_statistics(self):
        return self.logs_statistics

    def get_current_status(self):
        return self.current_status

    def get_current_status_position(self):
        return self.current_status[0]

    def get_current_status_state(self):
        return self.current_status[1]

    def get_rescued_bytes(self):
        return self.logs_statistics['rescued']

    def get_nontried_bytes(self):
        return self.logs_statistics['nontried']

    def get_nontrimmed_bytes(self):
        return self.logs_statistics['nontrimmed']

    def get_nonsplit_bytes(self):
        return self.logs_statistics['nonsplit']

    def __init_logs_statistics(self):
        def set_logs_statistics_to_zero(state):
            self.logs_statistics[state] = 0

        states = [
            'nontried', 'rescued', 'nontrimmed', 'nonsplit', 'bad', 'total']
        list([set_logs_statistics_to_zero(x) for x in states])
        self.logs_statistics['total'] = 0

    def __process_log_parsing(self, file):
        """
            Format each line in an array splitted by words,
            and manage the parse.
        """
        logFile = open(file, 'r')
        for line in logFile:
            line = re.sub(' +', ' ', line)
            line = line.rstrip().split(' ')
            self.__process_file_log_line(line)

    def __process_file_log_line(self, line):
        if self.__the_line_is_a_segment_result(line):
            self.__add_entry_in_logs_dictionary(line)
            self.__update_logs_statistics(line)
        elif self.current_status is None \
                and self.__the_line_is_the_current_status(line):
            self.current_status = line

    def __the_line_is_a_segment_result(self, line_representation):
        """
            Valid log lines have the pattern:
            offset <space> lenght <space> status
            Invalid ones are comments (that start by #),
            and the current position
            line (that has only two words).
        """
        if len(line_representation) != 3:
            return False
        if line_representation[0] == '#':
            return False
        return True

    def __the_line_is_the_current_status(self, line_representation):
        """
            The status line has the pattern:
            offset <space> lenght
            and should only be present one in the file.
        """
        if len(line_representation) != 2:
            return False
        if line_representation[0] == '#':
            return False
        return True

    def __add_entry_in_logs_dictionary(self, line):
        self.logs_dictionary.append(line)

    def __update_logs_statistics(self, line):
        """
            Simple incrementation of statistic variables used for computing a
            fast report of the log content.
        """
        symbols_to_states = {'?': 'nontried',
                             '+': 'rescued',
                             '*': 'nontrimmed',
                             '-': 'bad',
                             '/': 'nonsplit'
                            }
        size_of_block = int(line[1], 16)
        self.logs_statistics[symbols_to_states[line[2]]] += size_of_block
        self.logs_statistics['total'] += size_of_block
