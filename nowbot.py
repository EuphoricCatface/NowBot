#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @LilNowBot -- a bot that shows xkcd.com/now
#          

# Obligatory import.
import os
import basebot

class NowBot(basebot.BaseBot):
    BOTNAME = 'NowBot'
    NICKNAME = 'LilNowBot'
    SHORT_HELP = 'Someday, I will grow up to be @NowBot, with even more commands!'
    LONG_HELP = 'I show xkcd.com/now on the command "!now"\n'+\
                'Someday, I will grow up to be @NotBot, with even more commands!'

    def __init__(self, *args, **kwds):
        basebot.BaseBot.__init__(self, *args, **kwds)
        SHORT_HELP = 'Someday, I will grow up to be @NowBot, with even more commands!'
        LONG_HELP = 'I show xkcd.com/now on the command "!now"\n'+\
                    'Someday, I will grow up to be @NotBot, with even more commands!'

    def handle_command(self, cmdline, meta):
        if cmdline[0] != '!now':
            return
        if len(cmdline) == 1:
            meta['reply']('imgs.xkcd.com/comics/now.png')

def main():
    basebot.run_main(NowBot)

if __name__ == '__main__': main()

