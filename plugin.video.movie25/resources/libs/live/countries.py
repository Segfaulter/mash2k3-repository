import urllib,urllib2,re,cookielib,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)



def COUNTRIES():
        countarea='country'
        notified=os.path.join(main.datapath,str(countarea))
        if not os.path.exists(notified):
            open(notified,'w').write('version="%s",'%countarea)
            dialog = xbmcgui.Dialog()
            ok=dialog.ok('[B]Attention!!![/B]', 'This is a section provided by you the users.','what you see here is live streams posted by','xbmchub users if you want to add to it visit xbmchub.')
        main.GA("Live","Countries")
        link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/countries.xml')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>(.+?)</thumbnail>').findall(link)
        for name,url,thumb in sorted(match):
            main.addDir(name,url,144,thumb)
        main.VIEWSB()
def COUNTRIESList(mname,murl):
        main.GA("Countries-"+mname,"Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>').findall(link)
        for name,url,thumb in sorted(match):
            main.addLink(name,url,thumb)
        main.VIEWSB()
