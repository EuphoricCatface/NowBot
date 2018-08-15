#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @LilNowBot -- a bot that shows xkcd.com/now
#          

# Obligatory import.
import os
import basebot

def now_handler(cmdline, meta):
    #send_chat('imgs.xkcd.com/comics/now.png', meta.msgid())
    meta['reply']('imgs.xkcd.com/comics/now.png')

# Main function. Could be omitted (but I prefer not to do).
def main():
    # botname : Name to use in logging.
    # nickname: Actual nick-name.
    # regexes : Mapping of regex-response pairs.
    # command_handlers : Mapping of !command-response pairs.
    basebot.run_minibot(botname='NowBot', nickname='LilNowBot',
                        command_handlers={
                            'now': [now_handler]
                        },
#                        regexes={
#                            '^!now$':'imgs.xkcd.com/comics/now.png'
#                        },
                        short_help='Someday, I will grow up to be @NowBot, with more commands!',
                        long_help='Shows xkcd.com/now on !now\nExpect for more commands in the future! :)',
                        )

if __name__ == '__main__': main()
