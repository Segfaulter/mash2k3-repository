import urllib,urllib2,re,cookielib,urlresolver
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def YOUKIDS():
    main.addDir('Sesame Street','sesamestreet',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Yo Gabba Gabba!','yogabbagabba',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Baby Tv','BabyTVChannel',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Houston Zoo','houstonzoo',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Simple Kids Crafts','simplekidscrafts',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Cartoon Network','cartoonnetwork',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Muppets Studio','MuppetsStudio',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Word World PBS','WordWorldPBS',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Big Red Hat Kids','bigredhatkids',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Baby Einstein','TerrapinStation5',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Activity Village','activityv',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Hoopla Kids','hooplakidz',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('4KidsTV','4KidsTV',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('School House Rock Kids','MrRiggyRiggs',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Arthur','MsArthurTV',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('POCOYO','pocoyotv',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Disney jr','disneyjunior',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Mickey Mouse','MickeyMouseCartoon',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Tom and Jerry','TheTomEJerryShow',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Dora','TheDoraTheExplorerHD',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('SpongeBob','Spongebob4Children',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Curious George','ngk',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Kids Camp','kidscamp',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Timon and Pumbaa','timonandpumbaa1',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Dragon Tales','DejectedDragon',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Aladdin','aladdinvids',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.GA("KidZone","YoutubeKids")
    main.VIEWSB()

def YOUList(mname,durl):
        murl='http://gdata.youtube.com/feeds/api/users/'+durl+'/uploads?start-index=1&max-results=50'
        link=main.OPENURL(murl)
        match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
        for url,desc,thumb,name in match:
                name=name.replace('<','')
                main.addSport(name,url,48,thumb,desc,'','')
        main.GA(mname,"Youtube-List")

def YOULink(mname,url):
        print url
        ok=True
        main.GA("Youtube-List","Watched")
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+url+"&hd=1"
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = url
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
