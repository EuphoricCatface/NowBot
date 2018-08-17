#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @LilNowBot -- a bot that shows xkcd.com/now
#          

# Obligatory import.
import os
import basebot

def now_handler(self, cmdline, meta):
    if len(cmdline) == 1:
        meta['reply']('imgs.xkcd.com/comics/now.png')

class NowBot(basebot.Bot):
    BOTNAME = 'NowBot'
    NICKNAME = 'LilNowBot'
    SHORT_HELP = 'Someday, I will grow up to be @NowBot, with even more commands!'
    LONG_HELP = 'I show xkcd.com/now on the command "!now"\n'+\
                'Someday, I will grow up to be @NowBot, with even more commands!'

    def __init__(self, *args, **kwds):
        basebot.Bot.__init__(self, *args, **kwds)

    def handle_command(self, cmdline, meta):
        if cmdline[0] == '!now':
            now_handler(cmdline, meta)
        basebot.Bot.handle_command(self, cmdline, meta)

def main():
    basebot.run_main(NowBot)

if __name__ == '__main__': main()

