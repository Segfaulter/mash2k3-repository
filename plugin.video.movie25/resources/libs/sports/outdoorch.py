import urllib,urllib2,re,cookielib,string, urlparse
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def OC():
        main.addDir('All Videos','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Hunting','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Hunting',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Fishing','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Fishing',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Shooting','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Shooting',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Off Road','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Off-Road',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Adventure','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Adventure',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Conservation','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Conservation',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        main.GA("Sports","OutChannel")

def OCList(murl):
        link=main.OPENURL(murl)
        match=re.compile('<item><titl[^>]+>([^<]+)</title><description>(.+?)</description>.+?<plrelease:url>(.+?)</plrelease:url></plfile:release></media:content><pubDate>.+?</pubDate><plmedia:defaultThumbnailUrl>(.+?)</plmedia:defaultThumbnailUrl>').findall(link)
        for name,desc,url,thumb in match:
                main.addSport(name,url,52,thumb,desc,'','')
        main.GA("Sports","OC-List")

def OCLink(mname,url):
        main.GA("OC-List","Watched")
        link=main.OPENURL(url)
        ok=True
        match=re.compile('<video src="(.+?)" title="(.+?)" abstract="(.+?)" copyright="Outdoor Channel"').findall(link)
        for video, title, desc in match:
                print video
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = video
        listitem = xbmcgui.ListItem(mname)
        listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
