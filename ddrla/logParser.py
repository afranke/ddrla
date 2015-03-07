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
    logsDictionary = []
    logsStatistics = {}

    def __init__(self, file):
        self.__initLogsStatistics();
        self.__processLogParsing(file)

    def getLogsDictionnary(self):
        return self.logsDictionary;

    def getLogsStatistics(self):
        return self.logsStatistics;

    def __initLogsStatistics(self):
        self.logsStatistics['nontried'] = 0
        self.logsStatistics['rescued'] = 0
        self.logsStatistics['nontrimmed'] = 0
        self.logsStatistics['nonsplit'] = 0
        self.logsStatistics['bad'] = 0
        self.logsStatistics['total'] = 0

    def __processLogParsing(self, file):
        """
            Format each line in an array splitted by words, and manage the parse.
        """
        logFile = open(file, 'r')
        for line in logFile:
            line = re.sub(' +', ' ', line);
            line = line.rstrip().split(' ')
            self.__processFileLogLine(line)

    def __processFileLogLine(self, line):
        if self.__theLineIsASegmentResult(line):
            self.__addEntryInLogsDictionary(line)
            self.__updateLogsStatistics(line)

    def __theLineIsASegmentResult(self, lineRepresentation):
        """
            Valid log lines have the pattern:
            offset <space> lenght <space> status
            Invalid ones are comments (that start by #), and the current position
            line (that has only two words).
        """
        if len(lineRepresentation) != 3:
            return False
        if lineRepresentation[0] == '#':
            return False
        return True

    def __addEntryInLogsDictionary(self, line):
        self.logsDictionary.append(line)

    def __updateLogsStatistics(self, line):
        """
            Simple incrementation of statistic variables used for computing a
            fast report of the log content.
        """
        sizeOfBlock = int(line[1], 16)
        if line[2] == '?':
            self.logsStatistics['nontried'] += sizeOfBlock
        elif line[2] == '+':
            self.logsStatistics['rescued'] += sizeOfBlock
        elif line[2] == '*':
            self.logsStatistics['nontrimmed'] += sizeOfBlock
        elif line[2] == '/':
            self.logsStatistics['nonsplit'] += sizeOfBlock
        elif line[2] == '-':
            self.logsStatistics['bad'] += sizeOfBlock
        self.logsStatistics['total'] += sizeOfBlock
