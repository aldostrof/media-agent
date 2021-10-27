#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bot.py
====================================
Contains classes, methods and function which simplify the creation and
interaction with a Telegram-based bot.
"""

## Native imports ##############################################################

import os

## Third-Party imports #########################################################

import configparser

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

## Local imports ###############################################################

from core.log.log_handling import LogManager
from config.global_config import ROOT_PATH

## Constants ###################################################################


## Code ########################################################################

class BotManager():

    __CONFIG_FILE_RELPATH = "config/bot.config"
    __CONFIG_FILE_ABSPATH = os.path.join(ROOT_PATH, __CONFIG_FILE_RELPATH)
    __BOTCONFIG_ID        = "bot_config"
    __BOTCONFIG_TOKEN     = "bot_token"    
    
    def botmanager_init_token(self):
        
        configfile_abspath = self.__CONFIG_FILE_ABSPATH        
        config = configparser.ConfigParser()        
        config.read(configfile_abspath)
        return config[self.__BOTCONFIG_ID][self.__BOTCONFIG_TOKEN]

    def __init__(self):
        self.__logger = LogManager.get_instance()
        self.__bot_token = self.botmanager_init_token() # TODO: handle exceptions
        self.__bot_id = hash(self.__bot_token)
        self.__updater = None

    # TODO: move callbacks in a separate module
    def __botmanager_callback_start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def __botmanager_callback_echo(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def __botmanager_setup(self):

        # TODO handle exceptions
        self.__updater = Updater(token=self.__bot_token, use_context=True)
        dispatcher = self.__updater.dispatcher
        start_handler = CommandHandler('start', self.__botmanager_callback_start)
        dispatcher.add_handler(start_handler)
        echo_handler = MessageHandler(Filters.text & (~Filters.command), self.__botmanager_callback_echo)
        dispatcher.add_handler(echo_handler)


    def botmanager_run_bot(self):

        # TODO handle exceptions
        self.__botmanager_setup()
        self.__updater.start_polling()

