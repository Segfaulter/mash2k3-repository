import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def MAINdz():
        main.GA("Plugin","dubzonline")
        main.addDir('A-Z','http://www.dubzonline.net/anime-list/',614,"%s/art/wfs/az.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Dubbed Series','lseries',618,"%s/art/wfs/latest2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Dubbed Episodes','lepi',618,"%s/art/wfs/latest2.png"%selfAddon.getAddonInfo("path"))
        main.addLink('Featured Anime Series','year','')
        link=main.OPENURL('http://www.dubzonline.net/')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('<li><a href="/anime-list/" ><span>Anime List</span></a></li>','').replace('<li><a href="/contact-us/" ><span>Contact Us</span></a></li>','').replace('<li><a href="/" class="active"><span>Home</span></a></li>','')
        match = re.compile('href=".+?">([^<]+)</a></h2></div><div class=".+?">Date Posted:.+?<br /><p><img src="(.+?)" width=".+?" height=".+?" alt=".+?" align=".+?" style=".+?"/>(.+?)<strong>.+?<strong>.+?href="http://www.dubzonline.net/watch(.+?)"').findall(link)
        for name, thumb, desc, url in match:
                main.addDir2(name,'http://www.dubzonline.net/watch'+url,616,thumb,desc)

def latestLIST(murl):
        link=main.OPENURL('http://www.dubzonline.net/')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('<li><a href="/anime-list/" ><span>Anime List</span></a></li>','').replace('<li><a href="/contact-us/" ><span>Contact Us</span></a></li>','').replace('<li><a href="/" class="active"><span>Home</span></a></li>','')
        if murl=='lseries':
                match = re.compile('<li><a href="([^<]+)">(.+?)</a></li>').findall(link)
                for url, name in match:
                            main.addDir(name,'http://www.dubzonline.net/'+url,616,'')

        if murl=='lepi':
                match = re.compile('<li><a href="([^<]+)" title=".+?" >(.+?)</a> </li>').findall(link)
                for url, name in match:
                            main.addPlay(name,url,617,'')
       
def AtoZdz():
        main.addDir('0-9','http://www.iwatchonline.to/main/content_more/tv/?startwith=09&start=0',589,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
        for i in string.ascii_uppercase:
            main.addDir(i,'http://www.dubzonline.net/anime-list/',615,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
        main.GA("Tvshows","A-ZTV")
        main.VIEWSB()

def AZLIST(mname,murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.compile('<li><a href="([^<]+)">(.+?)</a></li>').findall(link)
        for url, name in match:
            if name[0]==mname or name[0]==mname.lower():
                    main.addDir(name,url,616,'')

def EPILIST(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descs=re.compile('<img src=".+?" width=".+?" height=".+?" alt=".+?" align=".+?" style=".+?"/>(.+?)</p>').findall(link)
        if len(descs)>0:
                desc=descs[0]
        else:
                desc=''
        thumbs=re.compile('<img src="(.+?)" width=".+?" height=".+?" alt=".+?" align=".+?" style=".+?"/>').findall(link)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        match = re.compile('<td style=".+?"><a style=".+?" href="([^<]+)" title=".+?">(.+?)</a></td>').findall(link)
        for url, name in match:
                    main.addSport(name,url,617,thumb,desc,'','')

def LINK(mname,murl):
        main.GA("dubzonline-"+manme,"Watched")
        sources = []
        ok=True
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.compile('''<span class='.+?'><b>.+?</b></span><iframe src="(.+?)"''').findall(link)
        for url in match:
                match2=re.compile('http://(.+?)/.+?').findall(url)
                for host in match2:
                    host = host.replace('www.','')
                    if host =='putlocker.com' or host =='sockshare.com':
                                url=url.replace('embed','file')
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)      
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        stream_url = source.resolve()
                else:
                      stream_url = False
                      return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )       
                xbmc.Player().play(stream_url, listitem)
                return ok
