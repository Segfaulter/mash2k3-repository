import urllib,urllib2,re,cookielib, urlresolver
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def CHANNELCList(murl):
        link=main.OPENURL(murl)
        match=re.compile('<li>(.+?): <a href="(.+?)">(.+?)</a> </li>').findall(link)
        for date,url,name in match:
            main.addPlay(name+' [COLOR red]'+date+'[/COLOR]',url,547,'')

def CHANNELCLink(mname,murl):
        main.GA("ChannelCut","Watched")
        sources = []
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,3000)")
        link=main.OPENURL(murl)
        ok=True
        site = re.findall('channelcut',murl)
        if len(site)>0:
            match=re.compile('<p><a href="(.+?)" rel=".+?">.+?</a></p>').findall(link)
        else:
            match=re.compile('<td><a href="(.+?)" target="').findall(link)
        for url in match:
                match2=re.compile('http://(.+?)/.+?').findall(url)
                for host in match2:
                    host = host.replace('www.','')
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)     
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,5000)")
                        stream_url = source.resolve()
                else:
                      stream_url = False
                      return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )       
                xbmc.Player().play(stream_url, listitem)
                return ok
