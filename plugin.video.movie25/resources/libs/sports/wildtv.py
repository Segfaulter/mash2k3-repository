import urllib,urllib2,re,cookielib,string, urlparse,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def WILDTV(murl):
        main.GA("Sports","Wildtv")
        link=main.OPENURL(murl)
        match=re.compile('<option value="(.+?)">(.+?)</option>').findall(link)
        for idnum, name in match:
            url='https://www.wildtv.ca/show/'+idnum
            main.addDir(name,url,93,"%s/art/wildtv.png"%selfAddon.getAddonInfo("path"))

def LISTWT(murl):
        main.GA("Wildtv","Wildtv-list")
        link=main.OPENURL(murl)
        match=re.compile('alt="Video: (.+?)" href="(.+?)">\r\n<img class=".+?" src="(.+?)"').findall(link)
        for name, url, thumb in match:
            thumb='https:'+thumb
            url='https://www.wildtv.ca/' +url
            main.addPlay(name,url,94,thumb)

def LINKWT(mname,murl):
        main.GA("Wildtv-list","Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Playing Link,3000)")
        link=main.OPENURL(murl)
        ok=True
        stream=re.compile('streamer: "(.+?)",').findall(link)
        Path=re.compile('file: "mp4:med/(.+?).mp4",').findall(link)
        if len(Path)>0:
            desc=re.compile('<meta name="description" content="(.+?)" />').findall(link)
            if len(desc)>0:
                desc=desc[0]
            else:
                desc=''
            thumb=re.compile('image: "(.+?)",').findall(link)
            if len(thumb)>0:
                thumb='https:'+thumb[0]
            else:
                thumb=''
            stream_url = stream[0]+'/'
            if selfAddon.getSetting("wild-qua") == "0":
                    playpath = 'mp4:high/'+Path[0]+'.mp4'
            elif selfAddon.getSetting("wild-qua") == "1":
                    playpath = 'mp4:med/'+Path[0]+'.mp4'
            playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playlist.clear()
            listitem = xbmcgui.ListItem(mname, thumbnailImage= thumb)
            listitem.setProperty('PlayPath', playpath);
            listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
            playlist.add(stream_url,listitem)
            xbmcPlayer = xbmc.Player()
            xbmcPlayer.play(playlist)
            return ok
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link not found,3000)")
