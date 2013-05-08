import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def TubTubMAIN(murl):
        main.GA("TubTub","List")
        main.addLink('[COLOR red]Classics, Very Old Content[/COLOR]','','')
        thumb="%s/art/tubtub.png"%selfAddon.getAddonInfo("path")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile("""<a href="mms://(.+?)"  .+?>([^<]+)</span></a>""").findall(link)
        for url,name in match:
            main.addPlay(name,'http://'+url,186,thumb)

        
        
def TubTubLink(mname,murl):
        main.GA("TubTub-"+mname,"Watched")
        ok=True
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile("Ref2=([^<]+)").findall(link)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = match[0]
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
