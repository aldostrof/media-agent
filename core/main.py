#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py
====================================
Main Entry point of the application.
"""

############################## Native imports ##################################


############################## Third-Party imports #############################


############################## Local imports ###################################

from core.log.log_handling import LogManager
from core.bot.bot import BotManager

################################## Code ########################################



def app_setup():
    """
    Performs initial setup.
    """
    # initialize logging subsystem
    log_man = LogManager.get_instance()
    log_man.setup_logging_subsystem()

    # if successfull, from here, you can just call
    # logging.info(), logging.error() as you wish
    # TODO: handle exceptions

def main():
    """
    Starts the application.
    """

    # TODO: handle thrown exceptions
    app_setup()
    print("I am online!")
    botman = BotManager()
    botman.botmanager_run_bot()    


if __name__ == "__main__":
    main()
