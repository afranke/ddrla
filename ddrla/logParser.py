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
        #TODO
