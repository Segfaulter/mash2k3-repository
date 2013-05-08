import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def MAINSG():
        main.addDir('Search','sg',612,"%s/art/wfs/search.png"%selfAddon.getAddonInfo("path"))
        main.addDir('A-Z','http://seriesgate.tv/',610,"%s/art/wfs/az.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Episodes','http://seriesgate.tv/latestepisodes/',602,"%s/art/wfs/latest.png"%selfAddon.getAddonInfo("path"))
        HOMESG()
        main.GA("Plugin","SeriesGate")
        #main.addDir('TV Series','http://watch-freeseries.mu/tvseries',506,"%s/art/wfs/series.png"%selfAddon.getAddonInfo("path"))
        #main.addDir('Year','http://watch-freeseries.mu/',505,"%s/art/wfs/year.png"%selfAddon.getAddonInfo("path"))
        #main.addDir('Genre','http://watch-freeseries.mu/',502,"%s/art/wfs/genre.png"%selfAddon.getAddonInfo("path"))
def HOMESG():
        url='http://seriesgate.tv/'
        link=main.OPENURL(url)
        main.addLink('[COLOR red]Updated Shows[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[0:5]:
            main.addDir(name,url,604,thumb)
        main.addLink('[COLOR red]Knee Slapping Comedies[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[5:10]:
            main.addDir(name,url,604,thumb)
        main.addLink('[COLOR red]Turmoil and Tears: Drama[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[10:15]:
            main.addDir(name,url,604,thumb)
        main.addLink('[COLOR red]Rumbling and Tumbling Action[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[15:20]:
            main.addDir(name,url,604,thumb)
        main.addLink("[COLOR red]Editor's Flicks[/COLOR]",'','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[20:25]:
            main.addDir(name,url,604,thumb)
        main.addLink('[COLOR red]New to SeriesGate[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[25:30]:
            main.addDir(name,url,604,thumb)
            
def AtoZSG():
        main.addDir('0-9','0-9',611,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
        for i in string.ascii_uppercase:
                main.addDir(i,i,611,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
        main.GA("SeriesGate","A-Z")
        main.VIEWSB()
        
def AllShows(murl):
        gurl='http://seriesgate.tv/'
        link=main.OPENURL(gurl)
        match=re.compile('{"n":"(.+?)","u":"(.+?)","i":"(.+?)"}').findall(link)
        for name,surl,imdb, in match:
                name2 =name
                if name[0:3]=='The':
                    name2=name.replace('The ','')
                if murl == '0-9':
                    if name2[0:1] <= '9':
                        durl='http://seriesgate.tv/'+surl+'/'
                        thumb ='http://cdn.seriesgate.tv/6/cover/110x160/'+surl+'.png'
                        main.addDir(name,durl,604,thumb)
                    
                elif name2[0:1] == murl:
                    durl='http://seriesgate.tv/'+surl+'/'
                    thumb ='http://cdn.seriesgate.tv/6/cover/110x160/'+surl+'.png'
                    main.addDir(name,durl,604,thumb)
        main.GA("SeriesGate","AllShows")
def LISTEpiSG(murl):
    link=main.OPENURL(murl)
    match=re.compile('<a href="(.+?)"><div  class=".+?"><img  class=".+?" src=""  data-original ="(.+?)" width=".+?" height=".+?"  alt=".+?" title = "(.+?)" /><div class=".+?"><span style=".+?">(.+?)</span><div class=".+?"></div><span>(.+?)</span><div class=".+?">').findall(link)
    for url,thumb,epiname, showname, seep in match:
        durl = url+'more_sources/'
        main.addPlay(showname+' [COLOR red]'+seep+'[/COLOR]'+" "+'"'+epiname+'"',durl,609,thumb)
    main.GA("SeriesGate","Latest-list")
def LISTSeasonSG(mname,murl):
    link=main.OPENURL(murl)
    match=re.compile('<div class="season_page">\n\t\t\t\t\t\t<a href="(.+?)" >(.+?)</a>').findall(link)
    for url, seaname in match:
        num=re.compile('Season ([^<]+)').findall(seaname)
        if selfAddon.getSetting("meta-view") == "true":
            print num[0]
            cover = main.grab.get_seasons(mname, None, num[0], overlay=6)
            print str(cover)
            covers= re.compile("cover_url.+?'(.+?)'").findall(str(cover))
            for thumb in covers:
                thumb = str(thumb)
                thumb= thumb.replace("',","%s/art/tv2.png"%selfAddon.getAddonInfo("path"))
                print thumb
        else:
            thumb=''
        durl = murl+url
        main.addDir(seaname,durl,605,str(thumb))
        xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
        main.GA("SeriesGate","Sea-list")
def LISTEpilistSG(mname,murl):
    link=main.OPENURL(murl)
    #match=re.compile('<div class=".+?" style=".+?" >(.+?)- <span><a href = ".+?">.+?</a></span></div><div class=".+?" >(.+?)</div><div class = ".+?"></div><div style=".+?"><a href="(.+?)"><img src="(.+?)" width=".+?" height=".+?"  alt=".+?" title = "(.+?)" ></a></div><div class = ".+?" style = ".+?"><div class="s_page_season_description">(.+?)</div>').findall(link)
    #if len(match) == 0:
    match=re.compile('<div class=".+?" style=".+?" >(.+?)- <span><a href = ".+?">.+?</a></span></div><div class=".+?" >(.+?)</div><div class = ".+?"></div><div style=".+?"><a href="(.+?)"><img src="(.+?)" width=".+?" height=".+?"  alt=".+?" title = "(.+?)" ></a>').findall(link)
    for seep, airdate, url, thumb, epiname in match:
        durl = 'http://seriesgate.tv'+url+'more_sources/'
        main.addPlay(seep+" "+'"'+epiname+'"',durl,609,thumb,)
    main.GA("SeriesGate","Epi-list")

def SearchhistorySG():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='sg'
            SEARCHSG(url)
        else:
            main.addDir('Search','sg',608,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,608,thumb)
            
            


def SEARCHSG(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'sg':
            keyb = xbmc.Keyboard('', 'Search For Shows or Episodes')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://seriesgate.tv/search/indv_episodes/'+encode+'/'
                    if not os.path.exists(SeaFile) and encode != '':
                        open(SeaFile,'w').write('search="%s",'%encode)
                    else:
                        if encode != '':
                            open(SeaFile,'a').write('search="%s",'%encode)
                    searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                    for seahis in reversed(searchis):
                        continue
                    if len(searchis)>=10:
                        searchis.remove(searchis[0])
                        os.remove(SeaFile)
                        for seahis in searchis:
                            try:
                                open(SeaFile,'a').write('search="%s",'%seahis)
                            except:
                                pass


        else:
            encode = murl
            surl='http://seriesgate.tv/search/indv_episodes/'+encode+'/'    
        req = urllib2.Request(surl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        main.addLink('[COLOR red]Shows[/COLOR]','','')
        match=re.compile('src = "([^<]+)" height=".+?" width=".+?" alt=""  /></a><div class = ".+?" style=".+?"><div class = ".+?"><a href = "([^<]+)">([^<]+)</a></div><a href = ".+?">').findall(link)
        for thumb,url,name in match:
                main.addDir(name,url,604,thumb)
        main.addLink('[COLOR red]Episodes[/COLOR]','','')
        match=re.compile('src="([^<]+)" width=".+?" height=".+?"  /></a></div><div style=".+?"><a style=".+?" href = "([^<]+)"><span style=".+?">([^<]+)</span></a><span style=".+?">EPISODE</span><div class=".+?"></div><span style=".+?">([^<]+)</span>').findall(link)
        for thumb,url,epiname, name in match:
                durl = url+'more_sources/'
                main.addPlay(name+' [COLOR red]"'+epiname+'"[/COLOR]',durl,609,thumb)
        main.GA("SeriesGate","Search")


def GETLINKSG(murl):
        durl= 'http://seriesgate.tv'+murl
        link=main.OPENURL(durl)
        link=link.replace('var url = "http://cdn.seriesgate.tv','')
        match=re.compile('var url = "(.+?)";').findall(link)
        for url in match:
                return url

def VIDEOLINKSSG(mname,murl):
        main.GA("SG","Watched")
        sources = []
        ok=True
        link=main.OPENURL(murl)
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,5000)")
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('href="([^<]+)" TARGET=".+?" >([^<]+)</a>').findall(link)
        for url, host in sorted(match):
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
