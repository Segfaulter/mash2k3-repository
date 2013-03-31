import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)



def MAINFMA():
        main.GA("Plugin","FMA")
        main.addDir('All Movies','movies',570,"%s/art/wfs/az.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest','http://www.freemoviesaddict.com/',568,"%s/art/wfs/latest2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Genre','genre',571,"%s/art/wfs/genre.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Year','year',571,"%s/art/wfs/year.png"%selfAddon.getAddonInfo("path"))

def AtoZFMA():
        main.addDir('0-9','http://www.freemoviesaddict.com/movies/letter/123',568,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
        for i in string.ascii_uppercase:
                main.addDir(i,'http://www.freemoviesaddict.com/movies/letter/'+i,568,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
        main.GA("FMA","A-Z")
        main.VIEWSB()

def GENREFMA(murl):
        url='http://www.freemoviesaddict.com/'
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        if murl=='genre':
            thumb="%s/art/folder.png"%selfAddon.getAddonInfo("path")
            match=re.compile('<li><a href="/movies/genre/(.+?)">(.+?)</a></li>').findall(link)
            for url, name in match:
                main.addDir(name,'http://www.freemoviesaddict.com/movies/genre/'+url,568,thumb)
            ("FMA","Genre")
        if murl=='year':
            thumb="%s/art/folder.png"%selfAddon.getAddonInfo("path")
            match=re.compile('<li><a href="/movies/year/(.+?)">(.+?)</a></li>').findall(link)
            for url, name in match:
                main.addDir(name,'http://www.freemoviesaddict.com/movies/year/'+url,568,thumb)
            ("FMA","Year")
    
def LISTFMA(murl):
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
    match=re.compile('<img class=\'.+?\' src=\'(.+?)\' alt=\'.+?\' />.+?<a class=\'.+?\' href=\'/(.+?)\'>(.+?)</a>.+?<a href=\'/movies/year/.+?\'>(.+?)</a>.+?<a href=\'/movies/genre/.+?\'>(.+?)</a>.+?</span><span class=".+?">(.+?)</span>').findall(link)
    for thumb,url,name, year, gen, desc in match:
        durl = 'http://www.freemoviesaddict.com/'+url
        main.addSport(name,durl,569,thumb,desc,year,gen)
    paginate = re.compile('<span class="pagination_next"><a class="pagination_link" href="(.+?)">').findall(link)
    if len(paginate)>0:
        main.addDir('Next','http://www.freemoviesaddict.com/'+paginate[0],568,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
    main.GA("FMA","list")
    xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
    main.VIEWS()



def LINKFMA(mname,murl):
        main.GA("FMA","Watched")
        sources = []
        ok=True
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,3000)")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        desc=re.compile('<meta name="description" content="(.+?)"').findall(link)
        match=re.compile('<span class=\'.+?\'>(.+?)</span></p><div class=\'.+?\'><img src=\'(.+?)\' /></div><a class=\'.+?\' href="(.+?)"').findall(link)
        for host, thumb, url in match:
                durl='http://www.freemoviesaddict.com/'+url
                redirect=main.REDIRECT(durl)
                print "fff "+redirect
                hosted_media = urlresolver.HostedMediaFile(url=redirect, title=host)
                sources.append(hosted_media)
                
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving links,3000)")
                        stream_url = source.resolve()
                else:
                      stream_url = False
                      return
                listitem = xbmcgui.ListItem(mname, thumbnailImage= thumb)
                listitem.setInfo('video', {'Title': mname, 'Plot': desc[0]} )       
                xbmc.Player().play(stream_url, listitem)
                return ok
