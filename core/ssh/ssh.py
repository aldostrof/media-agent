#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ssh.py
====================================
Contains classes, methods and function which abstract and simplify the creation
and the communication over a SSH connection.
Support for SCP file transfer is provided, too.
"""

## Native imports ##############################################################

import os

## Third-Party imports #########################################################

import configparser
from paramiko import SSHClient
from paramiko import AutoAddPolicy
## Local imports ###############################################################

from core.log.log_handling import LogManager
from config.global_config import ROOT_PATH

## Constants ###################################################################


## Code ########################################################################

class SSHManager():

    # Constants
    __CONFIG_FILE_RELPATH = "config/ssh.config"
    __CONFIG_FILE_ABSPATH = os.path.join(ROOT_PATH, __CONFIG_FILE_RELPATH)
    __SSH_LOGIN_ID        = "ssh-login"
    __MEDIA_INFO_ID       = "media-info"
    __SSH_USERNAME_ID     = "username"
    __SSH_PASSWORD_ID     = "password"
    __SSH_HOST_ID         = "host"
    __SSH_PORT_ID         = "port"
    __MEDIA_ROOTPATH_ID   = "root_path"
    __MEDIA_TVSHOWS_ID    = "tvshows_folder"
    __MEDIA_MOVIES_ID     = "movies_folder"
    __MEDIA_PHOTOS_ID     = "photos_folder"
    __MEDIA_MUSIC_ID      = "music_folder"

    # Class Variables
    __clientHandle         = None
    __ssh_username         = None
    __ssh_password         = None
    __ssh_host             = None
    __ssh_port             = None
    __media_rootpath       = None
    __media_tvshows_folder = None
    __media_movies_folder  = None
    __media_photos_folder  = None
    __media_music_folder   = None
    __logger               = None

    def SSHManager_initConfig(self):
        configfile_abspath = self.__CONFIG_FILE_ABSPATH        
        config = configparser.ConfigParser()        
        config.read(configfile_abspath)
        # NOTE: following are mandatory parameters; TODO: we should check for their existence.
        self.__ssh_username   = config[self.__SSH_LOGIN_ID][self.__SSH_USERNAME_ID]
        self.__ssh_password   = config[self.__SSH_LOGIN_ID][self.__SSH_PASSWORD_ID]
        self.__ssh_host       = config[self.__SSH_LOGIN_ID][self.__SSH_HOST_ID]
        self.__media_rootpath = config[self.__MEDIA_INFO_ID][self.__MEDIA_ROOTPATH_ID]
        
        # check for optional parameters
        if config.has_option(self.__SSH_LOGIN_ID, self.__SSH_PORT_ID):
            self.__ssh_port = config[self.__SSH_LOGIN_ID][self.__SSH_PORT_ID]
            self.__logger.log_info("Optional parameter found in configuration, port number={}".format(self.__ssh_port))

        if config.has_option(self.__MEDIA_INFO_ID, self.__MEDIA_TVSHOWS_ID):
            self.__media_tvshows_folder = config[self.__MEDIA_INFO_ID][self.__MEDIA_TVSHOWS_ID]
            self.__logger.log_info("Optional parameter found in configuration, media tvshows={}".format(self.__media_tvshows_folder))
        
        if config.has_option(self.__MEDIA_INFO_ID, self.__MEDIA_MOVIES_ID):
            self.__media_movies_folder = config[self.__MEDIA_INFO_ID][self.__MEDIA_MOVIES_ID]
            self.__logger.log_info("Optional parameter found in configuration, media movies={}".format(self.__media_movies_folder))

        if config.has_option(self.__MEDIA_INFO_ID, self.__MEDIA_PHOTOS_ID):
            self.__media_photos_folder = config[self.__MEDIA_INFO_ID][self.__MEDIA_PHOTOS_ID]     
            self.__logger.log_info("Optional parameter found in configuration, media photos={}".format(self.__media_photos_folder))  
        
        if config.has_option(self.__MEDIA_INFO_ID, self.__MEDIA_MUSIC_ID):
            self.__media_music_folder = config[self.__MEDIA_INFO_ID][self.__MEDIA_MUSIC_ID]     
            self.__logger.log_info("Optional parameter found in configuration, media music={}".format(self.__media_music_folder))  


    def __init__(self):
        self.__logger = LogManager.get_instance()
        self.SSHManager_initConfig()

    @staticmethod
    def getInstance():
        if SSHManager.__clientHandle is None:
            SSHManager.__clientHandle = SSHManager()
        return SSHManager.__clientHandle

    def getFolderContents(self, path):
        # path is built starting from rootpath
        targetpath=self.__media_rootpath+"/"+path
        self.__logger.log_info(targetpath)
        stdin, stdout, stderr = self.__clientHandle.exec_command("ls {}".format(targetpath))
        command_output = stdout.read().decode("utf8")
        return command_output.splitlines()

    def getMoviesFolder(self):
        if self.__media_movies_folder is not None:
            return self.__media_movies_folder
        else:
            pass # TODO: raise exception

    def getTVShowsFolder(self):
        if self.__media_tvshows_folder is not None:
            return self.__media_tvshows_folder
        else:
            pass # TODO: raise exception

    def getPhotosFolder(self):
        if self.__media_photos_folder is not None:
            return self.__media_photos_folder
        else:
            pass # TODO: raise exception

    def getMusicFolder(self):
        if self.__media_music_folder is not None:
            return self.__media_music_folder
        else:
            pass # TODO: raise exception

    def setupSSHConnection(self):
        self.__clientHandle = SSHClient()
        self.__clientHandle.set_missing_host_key_policy(AutoAddPolicy)
        # todo: check exception for connection errors
        if(self.__ssh_port is None):
            self.__clientHandle.connect(self.__ssh_host, self.__ssh_username, self.__ssh_password)
        else:
            self.__clientHandle.connect(self.__ssh_host, self.__ssh_port, self.__ssh_username, self.__ssh_password)

    def closeSSHConnection(self):
        self.__clientHandle.close()
