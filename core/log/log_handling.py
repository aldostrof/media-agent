#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
log_handling.py
====================================
Manages initialization and details of the logging subsystem.
"""

import os
import logging
import logging.config
from os import path
import config.global_config

class LogManager():
    """
    This class abstracts the details of the initialization and handling of
    the logging subsystem.
    """

    __instance = None

    @staticmethod
    def get_instance():
        """
        This method can be used to obtain a LogManager object.
        This is the only way of doing that.
        """
        if LogManager.__instance is None:
            LogManager.__instance = LogManager()
        return LogManager.__instance

    def __init__(self):        
        self.__conf_file = "config/log.config"
        self.__log_file_folder = "logs"
        self.__initialized = False

    def setup_logging_subsystem(self):
        """
        Setup the logging subsystem.
        This function initializes the logging subsystem with the proper
        configuration file.
        """
        # create logs directory if it does not exists
        log_folder = os.path.join(config.global_config.ROOT_PATH, self.__log_file_folder)
        if not path.exists(log_folder):
            os.mkdir(log_folder)

        # set up the logging subsystem
        log_filepath = os.path.join(config.global_config.ROOT_PATH, self.__conf_file)
        logging.config.fileConfig(log_filepath)

        # TODO check exceptions and, if none, set the following variable to True
        self.__initialized = True

    def log_info(self, msg, log_exc=False, log_stack=False, stack_lvl=1):
        if self.__initialized:
            logging.info(msg, exc_info=log_exc, stack_info=log_stack, stack_level=stack_lvl)
        else:
            pass
            # TODO: raise exception if logging subsystem is not initialized

    def log_warn(self, msg, log_exc=False, log_stack=False, stack_lvl=1):
        if self.__initialized:
            logging.warn(msg, exc_info=log_exc, stack_info=log_stack, stack_level=stack_lvl)
        else:
            pass
            # TODO: raise exception if logging subsystem is not initialized

    def log_error(self, msg, log_exc=False, log_stack=False, stack_lvl=1):
        if self.__initialized:
            logging.error(msg, exc_info=log_exc, stack_info=log_stack, stack_level=stack_lvl)
        else:
            pass
            # TODO: raise exception if logging subsystem is not initialized
    


