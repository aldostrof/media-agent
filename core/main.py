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
from core.ssh.ssh import SSHManager

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
    #botman = BotManager()
    #botman.botmanager_run_bot()

    sshman = SSHManager.getInstance()
    sshman.setupSSHConnection()
    movies  = sshman.getFolderContents(sshman.getMoviesFolder())
    photos  = sshman.getFolderContents(sshman.getPhotosFolder())
    tvshows = sshman.getFolderContents(sshman.getTVShowsFolder())
    music   = sshman.getFolderContents(sshman.getMusicFolder())
    print(movies)
    print(photos)
    print(tvshows)
    print(music)
    sshman.closeSSHConnection()



if __name__ == "__main__":
    main()
