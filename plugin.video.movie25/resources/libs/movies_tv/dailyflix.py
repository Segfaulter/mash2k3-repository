import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def LISTSP3(murl):
        if murl == 'HD':
                url='http://www.dailyflix.net/index.php?/forum/196-hd-movies-2012-2013/page__sort_key__last_post__sort_by__Z-A'
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('href="([^<]+)" title=.+? class=.+?><span itemprop="name">(.+?)</span>').findall(link)
        for url, name in match:
                main.addPlay(name,url,54,'')
        main.GA("HD-TV","Dailyfix")


def LINKSP3(mname,url):
        main.GA("Dailyfix","Watched")
        sources = []
        ok=True
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,3000)")
        link=main.OPENURL(url)
        match=re.compile("<a href='(.+?)' class='.+?' title='.+?' rel='.+?'>.+?</a").findall(link)
        for murl in match:
                host=re.compile("http://(.+?).com/.+?").findall(murl)
                for hname in host:
                        hname=hname.replace('www.','')
                        hosted_media = urlresolver.HostedMediaFile(url=murl, title=hname)
                        sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Movie doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Actual HD Movie Requires Buffer Time,7000)")
                        stream_url = source.resolve()
                else:
                        stream_url = False
                        return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )
                
                xbmc.Player().play(stream_url, listitem)
                return ok
