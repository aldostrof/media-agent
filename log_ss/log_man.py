#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
log_manager.py
====================================
Manages initialization and details of the logging subsystem.
"""

import os
import logging
import logging.config
from os import path
from config.global_config import *

class LogManager():
    """
    This class abstracts the details of the initialization and handling of
    the logging subsystem.
    """

    def __init__(self):
        self.__CONF_FILE = "config/log.config"
        self.__LOG_FILE_FOLDER = "logs"

    def setup(self):
        """
        Setup the logging subsystem.
        This function initializes the logging subsystem with the proper
        configuration file.
        """
        # create logs directory if it does not exists
        log_folder = os.path.join(ROOT_PATH, self.__LOG_FILE_FOLDER)
        if not path.exists(log_folder):
            os.mkdir(log_folder)

        # set up the logging subsystem
        log_filepath = os.path.join(ROOT_PATH, self.__CONF_FILE)
        logging.config.fileConfig(log_filepath)