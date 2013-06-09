import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def AtoZiWATCHtv():
    main.addDir('0-9','http://www.iwatchonline.to/main/content_more/tv/?startwith=09&start=0',589,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.iwatchonline.to/main/content_more/tv/?startwith='+i.lower()+'&start=0',589,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
    main.GA("Tvshows","A-ZTV")
    main.VIEWSB()

def AtoZiWATCHm():
    main.addDir('0-9','http://www.iwatchonline.to/main/content_more/movies/?startwith=09&start=0',587,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.iwatchonline.to/main/content_more/movies/?startwith='+i.lower()+'&start=0',587,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
    main.GA("Movies","A-ZM")
    main.VIEWSB()

def iWatchMAIN():
        main.addDir('Movies','http://www.iwatchonline.org/',586,"%s/art/wfs/iwatchm.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Tv Shows','http://www.iwatchonline.org/',585,"%s/art/wfs/iwatcht.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Todays Episodes','http://www.iwatchonline.to/tv-schedule',592,"%s/art/wfs/iwatcht.png"%(selfAddon.getAddonInfo("path")))
        main.GA("Plugin","iWatchonline")

        
def iWatchMOVIES():
        main.addDir('A-Z','http://www.iwatchonline.to',595,"%s/art/wfs/azws.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Popular','http://www.iwatchonline.to/main/content_more/movies/?sort=popular&start=0',587,"%s/art/wfs/iwatchm.png"%(selfAddon.getAddonInfo("path")))
        main.addDir( 'Latest Added','http://www.iwatchonline.to/main/content_more/movies/?sort=latest&start=0',587,"%s/art/wfs/iwatchm.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Featured Movies','http://www.iwatchonline.to/main/content_more/movies/?sort=featured&start=0',587,"%s/art/wfs/iwatchm.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Latest HD Movies','http://www.iwatchonline.to/main/content_more/movies/?quality=hd&start=0',587,"%s/art/wfs/iwatchm.png"%(selfAddon.getAddonInfo("path")))
        main.addDir( 'Upcoming','http://www.iwatchonline.to/main/content_more/movies/?sort=upcoming&start=0',587,"%s/art/wfs/iwatchm.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Genre','http://www.iwatchonline.to',596,"%s/art/wfs/genrews.png"%selfAddon.getAddonInfo("path"))
        main.GA("iWatchonline","Movies")

def iWatchTV():
        main.addDir('A-Z','http://www.iwatchonline.to',593,"%s/art/wfs/azws.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Todays Episodes','http://www.iwatchonline.to/tv-schedule',592,"%s/art/wfs/iwatcht.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Featured Shows','http://www.iwatchonline.to/main/content_more/tv/?sort=featured&start=0',589,"%s/art/wfs/iwatcht.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Popular Shows','http://www.iwatchonline.to/main/content_more/tv/?sort=popular&start=0',589,"%s/art/wfs/iwatcht.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Latest Additions','http://www.iwatchonline.to/main/content_more/tv/?sort=latest&start=0',589,"%s/art/wfs/iwatcht.png"%(selfAddon.getAddonInfo("path")))
        main.addDir('Genre','http://www.iwatchonline.to',594,"%s/art/wfs/genrews.png"%selfAddon.getAddonInfo("path"))
        main.GA("iWatchonline","Tvshows")
def iWatchGenreTV():
        link=main.OPENURL('http://www.iwatchonline.to/tv-show')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<li>  <a href=".?gener=([^<]+)">  (.+?)  </a>  </li>').findall(link)
        for url,genre in match:
                main.addDir(genre,'http://www.iwatchonline.to/main/content_more/tv/?gener='+url+'&start=0',589,'')
        main.GA("Tvshows","GenreT")
def iWatchGenreM():
        link=main.OPENURL('http://www.iwatchonline.to/movies')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<li>  <a href=".?gener=([^<]+)">  (.+?)  </a>  </li>').findall(link)
        for url,genre in match:
                main.addDir(genre,'http://www.iwatchonline.to/main/content_more/movies/?gener='+url+'&start=0',587,'')
        main.GA("Movies","GenreM")                

def iWatchLISTMOVIES(murl):
        main.GA("Movies","List")   
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a href="(.+?)" class=".+?" rel=".+?"><img class=".+?" src="(.+?)" alt=""> <div class=".+?">.+?</div>  </a><div class=".+?">(.+?)<div class=".+?"><div class=".+?" data-rating=".+?"></div></div></div><div class=".+?">(.+?)<br />').findall(link)
        for url,thumb,name,desc in match:    
                main.addSport(name,url,588,thumb,desc,'','')
        if len(match)==25:
            paginate=re.compile('([^<]+)start=([^<]+)').findall(murl)
            for purl,page in paginate:
                i=int(page)+25
                main.addDir('[COLOR blue]Next[/COLOR]',purl+'start='+str(i),587,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()

def iWatchToday(murl):
        main.GA("Tvshows","TodaysList")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<img src="([^<]+)" alt="" class=".+?"><br /><a href="(.+?)">(.+?)</a>  </td>  <td style=".+?" width=".+?">(.+?)</td>  <td style=".+?" width=".+?">(.+?)</td>').findall(link)
        for thumb,url,name,episea,epiname in match:    
                main.addPlay(name+' '+episea+' '+epiname,url,588,thumb)

def iWatchLISTSHOWS(murl):
        main.GA("Tvshows","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a href="(.+?)" class=".+?" rel=".+?"><img class=".+?" src="(.+?)" alt=""> <div class=".+?">.+?</div>  </a><div class=".+?">(.+?)<div class=".+?"><div class=".+?" data-rating=".+?"></div></div></div><div class=".+?">(.+?)<br />').findall(link)
        for url,thumb,name,desc in match:    
                main.addDir2(name,url,590,thumb,desc)
        print len(match)
        if len(match)==25:
            paginate=re.compile('([^<]+)start=([^<]+)').findall(murl)
            for purl,page in paginate:
                i=int(page)+25
                main.addDir('[COLOR blue]Next[/COLOR]',purl+'start='+str(i),589,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()

def iWatchSeason(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descs=re.compile('<meta name="description" content="(.+?)">').findall(link)
        if len(descs)>0:
                desc=descs[0]
        else:
                desc=''
        thumbs=re.compile('<div class="movie-cover span2"><img src="(.+?)" alt=".+?" class=".+?" />').findall(link)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        match=re.compile('<h5><i class=".+?"></i>  (.+?)</h5>').findall(link)
        for season in match:
                main.addDir2(season,murl,591,thumb,desc)

def iWatchEpisode(mname,murl):
        seanum  = mname.split('n ')[1]
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descs=re.compile('<meta name="description" content="(.+?)">').findall(link)
        if len(descs)>0:
                desc=descs[0]
        else:
                desc=''
        thumbs=re.compile('<div class="movie-cover span2"><img src="(.+?)" alt=".+?" class=".+?" />').findall(link)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        match=re.compile('<td class="sideleft"><a href="([^<]+)"><i class="icon-play-circle"></i>(.+?)</a></td>  <td>(.+?)</td>').findall(link)
        for url,epi,name in match:
                sea=re.compile('s'+str(seanum)).findall(url)
                if len(sea)>0:
                        main.addSport(epi+'  "'+name+'"',url,588,thumb,desc,'','')                

def GetUrl(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('class="frame" src="(.+?)"').findall(link)
        link=match[0]
        return link

def iWatchLINK(mname,url):
        sources=[]
        main.GA("iWatchonline","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,10000)")
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descs=re.compile('<meta name="description" content="(.+?)">').findall(link)
        if len(descs)>0:
                desc=descs[0]
        else:
                desc=''
        thumbs=re.compile('<div class="movie-cover span2"><img src="(.+?)" alt=".+?" class=".+?" />').findall(link)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        match=re.compile('<td class="sideleft"><a href="([^<]+)" target=".+?" rel=".+?"><img src=".+?" alt="" />(.+?)</a>').findall(link)
        for url, name in match[0:30]:
                hosted_media = urlresolver.HostedMediaFile(url=GetUrl(url), title=name)
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
                listitem = xbmcgui.ListItem(mname, thumbnailImage=thumb)
                listitem.setInfo('video', {'Title': mname, 'Plot': desc} )         
                playlist.add(stream_url,listitem)
                xbmcPlayer = xbmc.Player()
                xbmcPlayer.play(playlist)
                return ok
