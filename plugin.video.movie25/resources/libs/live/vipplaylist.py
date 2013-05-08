import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)



def VIPplaylists(murl):
        vip='unknown'
        poster=re.compile('k1m05').findall(murl)
        if len(poster)>0:
                vip='k1m05'
        poster2=re.compile('maxpowers').findall(murl)
        if len(poster2)>0:
                vip='MaxPowers'
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail><date>(.+?)</date>').findall(link)
        for name,url,thumb,date in match:
            main.addDir(name+'         [COLOR red]Updated '+date+'[/COLOR]',url,182,thumb)
        main.GA("Live",vip+"-Playlists")


def VIPList(mname,murl):
        vip='unknown'
        poster=re.compile('k1m05').findall(murl)
        if len(poster)>0:
                vip='k1m05'
        poster2=re.compile('maxpowers').findall(murl)
        if len(poster2)>0:
                vip='MaxPowers'
        mname  = mname.split('[C')[0]
        main.GA(vip+"-Playlists",mname)
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<item><titl[^>]+>([^<]+)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail></item>').findall(link)
        for name,url,thumb in sorted(match):
            main.addPlay(name+' '+vip ,url,183,thumb)


def VIPLink(mname,murl):
        main.GA(mname,"Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = murl
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
