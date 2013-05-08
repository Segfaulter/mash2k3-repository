import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def ArabicMAIN(murl):
        main.GA("Live","ArabicStream")
        thumb="%s/art/arabicstream.png"%selfAddon.getAddonInfo("path")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<details.+?<summary>(.+?)</summary><ul>(.+?)</ul></details>').findall(link)
        for name,url in match:
            main.addDir(name,url,189,thumb)
            
def ArabicList(murl):
        main.GA("ArabicStream","List")
        match=re.compile('<li><a href="(.+?)"><img src="([^<]+)" >(.+?)</a></li>').findall(murl)
        for url,thumb,name in match:
            thumb=thumb.replace(' ','%20')
            main.addPlay(name,url,188,thumb)        
        
def ArabicLink(mname,murl):
        main.GA("Arabic-"+mname,"Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = murl
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
