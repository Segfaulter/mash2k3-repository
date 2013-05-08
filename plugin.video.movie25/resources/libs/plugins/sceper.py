import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def MAINSCEPER():
        main.GA("Plugin","Sceper")
        main.addDir('Search Movies & TV Shows','s',543,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Movies','movies',540,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Tv Shows','tvshows',540,"%s/art/wfs/scepert.png"%selfAddon.getAddonInfo("path"))
        
def MORTSCEPER(murl):
        if murl=='movies':
            main.GA("Sceper","Movies")
            main.addDir('All Movies','http://sceper.ws/home/category/movies',541,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Cartoons','http://sceper.ws/home/category/movies/cartoons',541,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Foreign Movies','http://sceper.ws/home/category/movies/movies-foreign',541,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
            main.addDir('HDTV 720p Movies','http://sceper.ws/home/category/movies/movies-hdtv-720p',541,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
            main.addDir('BluRay Rip Movies (BDRC,BDRip,BRRip)','http://sceper.ws/home/category/movies/movies-bluray-rip',541,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
            main.addDir('HDDVD Rip Movies','http://sceper.ws/home/category/movies/movies-hddvd-rip',541,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
            main.addDir('DVD Rip Movies','http://sceper.ws/home/category/movies/movies-dvd-rip',541,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
            main.addDir('DVD Screener Movies','http://sceper.ws/home/category/movies/movies-screener/movies-screener-dvd',531,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))
            main.addDir('R5 Movies','http://sceper.ws/home/category/movies/movies-r5',541,"%s/art/wfs/sceperm.png"%selfAddon.getAddonInfo("path"))

        elif murl=='tvshows':
            main.GA("Sceper","Tv")
            main.addDir('All TV Shows','http://sceper.ws/home/category/tv-shows',545,"%s/art/wfs/scepert.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Anime/Cartoon TV Shows','http://sceper.ws/home/category/tv-shows/animes',545,"%s/art/wfs/scepert.png"%selfAddon.getAddonInfo("path"))
            main.addDir('HDTV 720p TV Shows','http://sceper.ws/home/category/tv-shows/tv-shows-x264',545,"%s/art/wfs/scepert.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Documentary TV Shows','http://sceper.ws/home/category/tv-shows/documentaries',545,"%s/art/wfs/scepert.png"%selfAddon.getAddonInfo("path"))

            
def LISTSCEPER(name,murl):
        main.GA("Sceper","List")
        link=main.OPENURL(murl)
        i=0
        audiolist=[]
        desclist=[]
        genrelist=[]
        link=link.replace('\xc2\xa0','').replace('\n','')
        audio=re.compile('>Audio:</.+?>(.+?)<b').findall(link)
        if len(audio)>0:
            for aud in audio:
                aud=aud.replace('</span><span style="font-family: arial"> ','').replace('<span style="color: #ff0000;">','').replace('</span>','').replace('<span style="color: #ff9900">','').replace('<span style="color: #ff6600">','').replace('<span style="color: #ff0000">','').replace('</span><span style="font-family: arial">','').replace('<span style="font-family: arial">','').replace('<span style="font-family: arial;">','')
                audiolist.append(aud)
        else:
            audiolist.append('Audio Unknown')
        descr=re.compile('>Release Description</div><p>(.+?)</p>').findall(link)
        if len(descr)>0:
            for desc in descr:
                desc=desc.replace('</span><span style="font-family: arial"> ','').replace('<span style="color: #ff0000;">','').replace('</span>','')
                desclist.append(desc)
        else:
            desclist.append('Description Unavailable')
        genre=re.compile('>Genre:</span>(.+?)<br').findall(link)
        if len(genre)>0:
            for gen in genre:
                gen=gen.replace('</span><span style="font-family: arial"> ','').replace('<span style="color: #ff0000;">','').replace('</span>','')
                genrelist.append(gen)
        else:
            genrelist.append('Genre Unknown')
        match=re.compile('<a href="([^<]+)">([^<]+)</a></h2>\t\t<div class=".+?">\t\t\t\t<div class=".+?">Release Info</div><p><a href="(.+?)"').findall(link)
        for url,name,thumb in match:
            if len(audiolist)<8:
                audiolist.append('Audio Unknown')
            if len(desclist)<8:
                desclist.append('Description Unavailable')
            if len(genrelist)<8:
                genrelist.append('Genre Unknown')
            main.addSport(name+' [COLOR red]'+audiolist[i]+'[/COLOR]',url,544,thumb,desclist[i],'',genrelist[i])
            i=i+1
        paginate = re.compile('<a href=\'([^<]+)\' class=\'nextpostslink\'>').findall(link)
        if len(paginate)>0:
            main.addDir('Next',paginate[0],541,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

def LISTSCEPER2(name,murl):
        link=main.OPENURL(murl)
        link=link.replace('\xc2\xa0','').replace('\n','')
        match=re.compile('<a href="([^<]+)">([^<]+)</a></h2>\t\t<div class=".+?">').findall(link)
        for url,name in match:
            main.addPlay(name,url,544,'')
        paginate = re.compile('<a href=\'([^<]+)\' class=\'nextpostslink\'>').findall(link)
        if len(paginate)>0:
            main.addDir('Next',paginate[0],545,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))


def SearchhistorySCEPER():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            url='extra'
            SEARCHSCEPER(url)
        else:
            main.addDir('Search','extra',542,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,542,thumb)
            
            
        
def SEARCHSCEPER(murl):
        main.GA("Sceper","Search")
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'extra':
            keyb = xbmc.Keyboard('', 'Search Movies')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://sceper.ws/home/search/'+encode+'/'
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
                surl='http://sceper.ws/home/search/'+encode+'/'
        link=main.OPENURL(surl)
        i=0
        link=link.replace('\xc2\xa0','').replace('\n','')
        match=re.compile('<a href="([^<]+)">([^<]+)</a></h2>').findall(link)
        for url,name in match:
            main.addPlay(name,url,544,'')


def VIDEOLINKSSCEPER(mname,murl):
        main.GA("Sceper","Watched")
        link=main.OPENURL(murl)
        sources=[]
        ok=True
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,3000)")
        match=re.compile('<a href="([^<]+)">htt').findall(link)
        for url in match:
            print url
            vlink=re.compile('rar').findall(url)
            if len(vlink)==0:
                match2=re.compile('http://(.+?)/.+?').findall(url)
                for host in sorted(match2):   
                    host = host.replace('www.','')
                    match3=re.compile('720p').findall(url)
                    match4=re.compile('mp4').findall(url)
                    if len(match3)>0:
                        host =host+' [COLOR red]HD[/COLOR]'
                    elif len(match4)>0:
                        host =host+' [COLOR green]SD MP4[/COLOR]'
                    else:
                        host =host+' [COLOR blue]SD[/COLOR]'
                        
                    hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                    sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Link is being Resolved,5000)")
                        stream_url = source.resolve()
                else:
                      stream_url = False
                      return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )       
                xbmc.Player().play(stream_url, listitem)
                return ok
