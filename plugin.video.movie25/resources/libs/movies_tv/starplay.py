import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def LISTSP5(murl):
        link=main.OPENURL(murl)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        match=re.compile("<a href=\'(.+?)'.+?<font face='Calibri' color='.+?'>&nbsp;&nbsp;(.+?)</font>.+?Calibri'>([^<]+)</font></a><br>").findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for url,year,name in match:
                main.addDown3(name+' [COLOR red]('+year+')[/COLOR]',"http://87.98.161.165/"+url,58,'','')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
        if (dialogWait.iscanceled()):
                return False    
        dialogWait.close()
        del dialogWait
        main.GA("HD","Starplay")


def LINKSP5(mname,url):
        main.GA("Starplay","Watched")
        MainUrlb = "http://87.98.161.165"
        ok=True
        link=main.OPENURL(url)
        match=re.compile("\nfile: \'(.+?)\',\n \nimage: \'/(.+?)\',\n").findall(link)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        desc=' '
        for stream_url, thumb in match:
                stream_url=MainUrlb+stream_url
                listitem = xbmcgui.ListItem(mname,thumbnailImage= MainUrl+thumb)
                playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
