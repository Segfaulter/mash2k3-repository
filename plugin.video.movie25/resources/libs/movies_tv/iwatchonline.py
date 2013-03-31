import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def LISTTV(murl):
        Tvurl='http://www.iwatchonline.org/tv-show'
        link=main.OPENURL(murl)
        match=re.compile('<a href="(.+?)" ><img src="(.+?)"  border=".+?"  alt=.+?  title=(.+?)  id=".+?"  style').findall(link)
        for url,thumb,name in match:
                name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                namelen=len(name)     
                main.addPlay(name,url,29,thumb)
        paginate=re.compile('http://www.iwatchonline.org/tv-show/(.+?).?limit=18').findall(murl)
        paginate2=re.compile('http://www.iwatchonline.org/tv-show/(.+?).?page=(.+?)&limit=18').findall(murl)
        for section in paginate:
                if (len(paginate) > 0)and (len(paginate2) == 0) :
                        purl = Tvurl + '/'+section+'?page=2&limit=18'
                        main.addDir('[COLOR blue]Page 2[/COLOR]',purl,28,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
                
        paginate=re.compile('http://www.iwatchonline.org/tv-show/(.+?).?page=(.+?)&limit=18').findall(murl)
        for section, page in paginate:
                if (len(paginate) > 0):
                        pg= int(page) +1
                        purl = Tvurl + '/'+section+'?page='+str(pg)+'&limit=18'
                        main.addDir('[COLOR red]Home[/COLOR]','http://www.iwatchonline.org',0,"%s/art/home.png"%selfAddon.getAddonInfo("path"))
                        main.addDir('[COLOR blue]Page '+ str(pg)+'[/COLOR]',purl,28,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()
        main.GA("TV","iWatchonline")

def VIDEOLINKST(mname,url):
        main.GA("iWatchonline","Watched")
        Mainurl ='http://www.iwatchonline.org'
        url=Mainurl+url
        sources = []
        ok=True
        match=re.compile('http://www.iwatchonline.org/episode/(.+?)-.+?').findall(url)
        for movieid in match:
                url=url + '?tmpl=component&option=com_jacomment&view=comments%20&contentoption=com_content&contentid='+ movieid
        link=main.OPENURL(url)
        match=re.compile('<a href="(.+?)" target="_BLANK" class="vidLinks">(.+?)</a>').findall(link)
        for url, name in match:
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                        stream_url = source.resolve()
                else:
                        stream_url = False
                        return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )         
                xbmc.Player().play(stream_url, listitem)
                return ok
