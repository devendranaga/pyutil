##
# Implements the logger, prints the messages in color

import enum

# define the log type
class idps_log_type(enum.IntEnum):
    VERBOSE     = 1
    INFO        = 2
    WARNING     = 3
    ERROR       = 4
    FATAL       = 5

class idps_logger:
    # initialize the logger
    def __init__(self):
        # define colors
        self.color_red      = "\x1b[31m"
        self.color_green    = "\x1b[32m"
        self.color_yellow   = "\x1b[33m"
        self.color_blue     = "\x1b[34m"
        self.color_magenta  = "\x1b[35m"
        self.color_cyan     = "\x1b[36m"
        self.color_reset    = "\x1b[0m"

        # define log level
        self.log_level      = idps_log_type.INFO

    # set log level
    def set_log_level(self, log_level):
        self.log_level = log_level

    # print verbose
    def verbose(self, val):
        if self.log_level >= idps_log_type.VERBOSE:
            print(self.color_magenta + val + self.color_reset)

    # print info
    def info(self, val):
        if self.log_level >= idps_log_type.INFO:
            print(self.color_green + val + self.color_reset)

    # print warning
    def warning(self, val):
        if self.log_level >= idps_log_type.WARNING:
            print(self.color_yellow + val + self.color_reset)

    # print error
    def error(self, val):
        if self.log_level >= idps_log_type.ERROR:
            print(self.color_red + val + self.color_red)

    # print fatal
    def fatal(self, val):
        if self.log_level >= idps_log_type.ERROR:
            print(self.color_red + val + self.color_red)
