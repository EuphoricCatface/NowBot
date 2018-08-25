#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @LilNowBot -- a bot that shows xkcd.com/now
#          

# Obligatory import.
import os
import basebot
import pytz
import datetime

userdata = {
        'dummy_id':{'nick':'ㅇㅈㅇ','timezone':{'Asia/Seoul'}}
        }

def strtotz(tzstr):
    if tzstr[0:3].lower() == 'utc':
        offset = tzstr[3:]
        if offset == '':
            tzstr = 'Etc/GMT'
        else:
            try:
                offsetInt = -int(offset)
            except ValueError:
                return 'Wrong offset for UTC. Use UTC+/-<offset> (where offset is integer)'
                
            offset = '{0:+d}'.format(offsetInt)
            tzstr = 'Etc/GMT' + offset

    try:
        timezone = pytz.timezone(tzstr)
    except pytz.exceptions.UnknownTimeZoneError:
        return 'Unknown timezone. Find one from below link: !wiki List of tz database time zones'
        
    return timezone

def userdata_add(self, cmdline, meta):
    meta['reply']('Note: Adding a user to NowBot is still not fully implemented yet')
    if len(cmdline) != 3:
        return
    if not meta['msg'].sender.is_account:
        meta['reply']('You appear to be not logged in.\n'+\
                'NowBot basically associates your timezone to your euphoria account.\n'+\
                'Please log in, or contact @Catface to get yourself added to NowBot.')
        return
    
    user=dict()
    user['nick'] = meta['msg'].sender.name
    user['timezone'] = {str(cmdline[2])}
     
    userdata[meta['msg'].sender.id] = user
    print(userdata)


def timezone_handler(self, cmdline, meta):
    timefmt = '%Y-%m-%d %H:%M, %z'

    if len(cmdline) == 2:
        meta ['reply']('Usage: !now --timezone <timezone>\n' +\
                'For more info, type "!now --timezone help"')
        return 
    
    if len(cmdline) > 3:
        meta ['reply']('Usage: !now --timezone <timezone>\n' +\
                'Only one timezone is allowed. Timezones don\'t include space.\n' +\
                'For more info, type "!now --timezone help"')
        return 

    tzstr = cmdline[2]
    if tzstr == 'help':
        meta['reply']('Usage: !now --timezone <timezone>\n'+\
                'Find the timezone you want to know from the Wikipedia page\n' +\
                'https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\n' +\
                'find TZ value and put it into <timezone>\n\n' +\
                'For your convenience, UTC+/-<offset> type queries are also provided')
        return
    
    timezone = strtotz(tzstr)
    if type(timezone) is str:
        meta['reply']('Error while processing tzdata: \n' + timezone)
        return

    meta['reply'](datetime.datetime.now().astimezone(timezone).strftime(timefmt))

class NowBot(basebot.Bot):
    BOTNAME = 'NowBot'
    NICKNAME = 'LilNowBot'
    SHORT_HELP = 'Someday, I will grow up to be @NowBot, with even more commands!'
    LONG_HELP = '!now -> show xkcd.com/now\n'+\
                '!now --timezone <timezone> -> show localtime for a timezone.\n' +\
                'Someday, I will grow up to be @NowBot, with even more commands!'

    def __init__(self, *args, **kwds):
        basebot.Bot.__init__(self, *args, **kwds)

    def handle_command(self, cmdline, meta):

        if cmdline[0] == '!now':
            if len(cmdline) == 1:
                meta['reply']('imgs.xkcd.com/comics/now.png')

            elif cmdline[1] == '--timezone':
                timezone_handler(self, cmdline, meta)

            elif cmdline[1] == '--add':
                userdata_add(self, cmdline, meta)

            else:
                meta['reply']('Type !help @NowBot for help')

        basebot.Bot.handle_command(self, cmdline, meta)

def main():
    basebot.run_main(NowBot)

if __name__ == '__main__': main()

