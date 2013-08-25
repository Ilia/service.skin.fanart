#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2013 BOXiK
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    This script is based on script.randomitems & script.wacthlist
#    Thanks to their original authors

import os
import sys
import xbmc
import xbmcgui
import xbmcaddon
import random
import datetime
import _strptime
import urllib

if sys.version_info < (2, 7):
    import simplejson
else:
    import json as simplejson

__addon__        = xbmcaddon.Addon()
__addonversion__ = __addon__.getAddonInfo('version')
__addonid__      = __addon__.getAddonInfo('id')
__addonname__    = __addon__.getAddonInfo('name')
__localize__    = __addon__.getLocalizedString

class Main:
    def __init__(self):
        self.WINDOW = xbmcgui.Window(10000)
        while (not xbmc.abortRequested):
            if not xbmc.Player().isPlayingVideo() and not monitor.screensaver:
                json_string = '{"jsonrpc": "2.0",  "id": 1, "method": "VideoLibrary.GetMovies", "params": {"properties": ["art", "title", "year", "genre"], "limits": {"end": %d},' % 1
                json_query = xbmc.executeJSONRPC('%s "sort": {"method": "random" }, "filter": {"field": "playcount", "operator": "lessthan", "value": "1"}}}' % json_string)
                json_query = unicode(json_query, 'utf-8', errors='ignore')
                json_query = simplejson.loads(json_query)
                if json_query.has_key('result') and json_query['result'].has_key('movies'):
                    item = json_query['result']['movies'][0]
                    art = item['art']
                    self.WINDOW.setProperty("Movie.Art(fanart)", art.get('fanart',''))
                    self.WINDOW.setProperty("Movie.Title", item['title'])
                    self.WINDOW.setProperty("Movie.Year", str(item['year']))
                    self.WINDOW.setProperty("Movie.Genre", " / ".join(item['genre']))
                del json_query
            xbmc.sleep(15000) 


class MyMonitor( xbmc.Monitor ):
    def __init__( self, *args, **kwargs ):
        xbmc.Monitor.__init__( self )
        self.screensaver = False 

    def onSettingsChanged( self ):
        pass

    def onScreensaverDeactivated( self ):
        print __addonid__ + " - screensaver Deactivated"
        self.screensaver = False 

    def onScreensaverActivated( self ):    
        print __addonid__ + " - screensaver Activated"
        self.screensaver = True

    def onDatabaseUpdated( self, database ):
        pass

monitor = MyMonitor()

if (__name__ == "__main__"):
    Main()
    del Main