import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.movie25/art/hosts', ''))

def LISTSP2(murl):
        if murl=='3D':
                main.addDir('Search Newmyvideolinks','movieNEW',102,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                check=main.OPENURL('http://newmyvideolinks.com/category/movies/3-d-movies/')
                match=re.compile('<p><a href=".+?" >Next Page &raquo;</a></p>').findall(check)
                if len(match)>0:
                        urllist=['http://newmyvideolinks.com/category/movies/3-d-movies/','http://newmyvideolinks.com/category/movies/3-d-movies/page/2/']
                else:
                        urllist=['http://newmyvideolinks.com/category/movies/3-d-movies/']
        elif murl=='TV':
                main.addDir('Search Newmyvideolinks','tvNEW',102,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                urllist=['http://newmyvideolinks.com/category/tv-shows/','http://newmyvideolinks.com/category/tv-shows/page/2/','http://newmyvideolinks.com/category/tv-shows/page/3/','http://newmyvideolinks.com/category/tv-shows/page/4/','http://newmyvideolinks.com/category/tv-shows/page/5/','http://newmyvideolinks.com/category/tv-shows/page/6/','http://newmyvideolinks.com/category/tv-shows/page/7/','http://newmyvideolinks.com/category/tv-shows/page/8/','http://newmyvideolinks.com/category/tv-shows/page/9/','http://newmyvideolinks.com/category/tv-shows/page/10/']
        else:
                main.addDir('Search Newmyvideolinks','movieNEW',102,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                urllist=['http://newmyvideolinks.com/category/movies/bluray/','http://newmyvideolinks.com/category/movies/bluray/page/2/','http://newmyvideolinks.com/category/movies/bluray/page/3/','http://newmyvideolinks.com/category/movies/bluray/page/4/','http://newmyvideolinks.com/category/movies/bluray/page/5/','http://newmyvideolinks.com/category/movies/bluray/page/6/','http://newmyvideolinks.com/category/movies/bluray/page/7/','http://newmyvideolinks.com/category/movies/bluray/page/8/','http://newmyvideolinks.com/category/movies/bluray/page/9/','http://newmyvideolinks.com/category/movies/bluray/page/10/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for xurl in urllist:
                link=main.OPENURL(xurl)
                match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
                if len(match)>0:
                        for url,thumb,name in match:
                                if murl=='TV':
                                        match=re.compile('720p').findall(name)
                                        if (len(match)>0):
                                                main.addDir(name,url,35,thumb)
                                     
                                else:
                                        main.addDir(name,url,35,thumb)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False   

                else:
                        match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)" alt=".+?" width=".+?" height=".+?" class=".+?" />').findall(link)
                        for url,name,thumb in match:
                                if murl=='TV':
                                        match=re.compile('720p').findall(name)
                                        if (len(match)>0):
                                                main.addDir(name,url,35,thumb)
                                                
                                else:
                                        main.addDir(name,url,35,thumb)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False   
        dialogWait.close()
        del dialogWait
        main.GA("HD-3D-HDTV","Newmyvideolinks")

def SearchhistoryNEW(murl):
        if murl == 'tvNEW':
            seapath=os.path.join(main.datapath,'Search')
            SeaFile=os.path.join(seapath,'SearchHistoryTv')
            if not os.path.exists(SeaFile):
                url='tvNEW'
                SEARCHNEW(url)
            else:
                main.addDir('Search','tvNEW',101,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
                thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
                searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                for seahis in reversed(searchis):
                        url=seahis
                        seahis=seahis.replace('%20',' ')
                        main.addDir(seahis,url,101,thumb)
        elif murl == 'movieNEW':
            seapath=os.path.join(main.datapath,'Search')
            SeaFile=os.path.join(seapath,'SearchHistory25')
            if not os.path.exists(SeaFile):
                url='movieNEW'
                SEARCHNEW(url)
            else:
                main.addDir('Search','movieNEW',101,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
                thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
                searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                for seahis in reversed(searchis):
                        url=seahis
                        seahis=seahis.replace('%20',' ')
                        main.addDir(seahis,url,101,thumb)
            

def SEARCHNEW(murl):
        if murl == 'movieNEW':
                seapath=os.path.join(main.datapath,'Search')
                SeaFile=os.path.join(seapath,'SearchHistory25')
                try:
                    os.makedirs(seapath)
                except:
                    pass
                keyb = xbmc.Keyboard('', 'Search Movies')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        surl='http://newmyvideolinks.com/index.php?s='+encode
                        if not os.path.exists(SeaFile) and encode != '':
                            open(SeaFile,'w').write('search="%s",'%encode)
                        else:
                            if encode != '':
                                open(SeaFile,'a').write('search="%s",'%encode)
                        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                        for seahis in reversed(searchis):
                            print seahis
                        if len(searchis)>=10:
                            searchis.remove(searchis[0])
                            os.remove(SeaFile)
                            for seahis in searchis:
                                try:
                                    open(SeaFile,'a').write('search="%s",'%seahis)
                                except:
                                    pass
        elif murl == 'tvNEW':
                seapath=os.path.join(main.datapath,'Search')
                SeaFile=os.path.join(seapath,'SearchHistoryTv')
                try:
                    os.makedirs(seapath)
                except:
                    pass
                keyb = xbmc.Keyboard('', 'Search TV Shows')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        surl='http://newmyvideolinks.com/index.php?s='+encode
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
                surl='http://newmyvideolinks.com/index.php?s='+encode
        link=main.OPENURL(surl)
        match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
        if len(match)>0:
                for url,thumb,name in match:
                            main.addDir(name,url,35,thumb)

        else:
                match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)" alt=".+?" width=".+?" height=".+?" class=".+?" />').findall(link)
                for url,name,thumb in match:
                            main.addDir(name,url,35,thumb)
        main.GA("Newmyvideolinks","Search")
        
def LISTEtowns(murl):
        if murl=='3D':
                main.addDir('Search Etowns','movieNEW',550,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                try:
                        urllist=['http://go.etowns.net/category/movies/3-d-movies/','http://go.etowns.net/category/movies/3-d-movies/page/2/']
                except:
                        urllist=['http://go.etowns.net/category/movies/3-d-movies/']
        elif murl=='TV':
                main.addDir('Search Etowns','tvNEW',550,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                urllist=['http://go.etowns.net/category/tv-shows/','http://go.etowns.net/category/tv-shows/page/2/','http://go.etowns.net/category/tv-shows/page/3/','http://go.etowns.net/category/tv-shows/page/4/','http://go.etowns.net/category/tv-shows/page/5/','http://go.etowns.net/category/tv-shows/page/6/','http://go.etowns.net/category/tv-shows/page/7/','http://go.etowns.net/category/tv-shows/page/8/','http://go.etowns.net/category/tv-shows/page/9/','http://go.etowns.net/category/tv-shows/page/10/']
        else:
                main.addDir('Search Etowns','movieNEW',550,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                urllist=['http://go.etowns.net/category/movies/bluray/','http://go.etowns.net/category/movies/bluray/page/2/','http://go.etowns.net/category/movies/bluray/page/3/','http://go.etowns.net/category/movies/bluray/page/4/','http://go.etowns.net/category/movies/bluray/page/5/','http://go.etowns.net/category/movies/bluray/page/6/','http://go.etowns.net/category/movies/bluray/page/7/','http://go.etowns.net/category/movies/bluray/page/8/','http://go.etowns.net/category/movies/bluray/page/9/','http://go.etowns.net/category/movies/bluray/page/10/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for xurl in urllist:
                link=main.OPENURL(xurl)
                match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
                if len(match)>0:
                        for url,thumb,name in match:
                                if murl=='TV':
                                        match=re.compile('720p').findall(name)
                                        if (len(match)>0):
                                                main.addDir(name,url,35,thumb)
                                     
                                else:
                                        main.addDir(name,url,35,thumb)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False   

                else:
                        match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)" alt=".+?" width=".+?" height=".+?" class=".+?" />').findall(link)
                        for url,name,thumb in match:
                                if murl=='TV':
                                        match=re.compile('720p').findall(name)
                                        if (len(match)>0):
                                                main.addDir(name,url,35,thumb)
                                                
                                else:
                                        main.addDir(name,url,35,thumb)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False   
        dialogWait.close()
        del dialogWait
        main.GA("HD-3D-HDTV","Etowns")

def SearchhistoryEtowns(murl):
        if murl == 'tvNEW':
            seapath=os.path.join(main.datapath,'Search')
            SeaFile=os.path.join(seapath,'SearchHistoryTv')
            if not os.path.exists(SeaFile):
                url='tvNEW'
                SEARCHNEW(url)
            else:
                main.addDir('Search','tvNEW',549,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
                thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
                searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                for seahis in reversed(searchis):
                        url=seahis
                        seahis=seahis.replace('%20',' ')
                        main.addDir(seahis,url,549,thumb)
        elif murl == 'movieNEW':
            seapath=os.path.join(main.datapath,'Search')
            SeaFile=os.path.join(seapath,'SearchHistory25')
            if not os.path.exists(SeaFile):
                url='movieNEW'
                SEARCHNEW(url)
            else:
                main.addDir('Search','movieNEW',101,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
                thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
                searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                for seahis in reversed(searchis):
                        url=seahis
                        seahis=seahis.replace('%20',' ')
                        main.addDir(seahis,url,101,thumb)
            

def SEARCHEtowns(murl):
        if murl == 'movieNEW':
                seapath=os.path.join(main.datapath,'Search')
                SeaFile=os.path.join(seapath,'SearchHistory25')
                try:
                    os.makedirs(seapath)
                except:
                    pass
                keyb = xbmc.Keyboard('', 'Search Movies')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        surl='http://go.etowns.net/index.php?s='+encode
                        if not os.path.exists(SeaFile) and encode != '':
                            open(SeaFile,'w').write('search="%s",'%encode)
                        else:
                            if encode != '':
                                open(SeaFile,'a').write('search="%s",'%encode)
                        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                        for seahis in reversed(searchis):
                            print seahis
                        if len(searchis)>=10:
                            searchis.remove(searchis[0])
                            os.remove(SeaFile)
                            for seahis in searchis:
                                try:
                                    open(SeaFile,'a').write('search="%s",'%seahis)
                                except:
                                    pass
        elif murl == 'tvNEW':
                seapath=os.path.join(main.datapath,'Search')
                SeaFile=os.path.join(seapath,'SearchHistoryTv')
                try:
                    os.makedirs(seapath)
                except:
                    pass
                keyb = xbmc.Keyboard('', 'Search TV Shows')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        surl='http://go.etowns.net/index.php?s='+encode
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
                surl='http://go.etowns.net/index.php?s='+encode
        link=main.OPENURL(surl)
        match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
        if len(match)>0:
                for url,thumb,name in match:
                            main.addDir(name,url,35,thumb)

        else:
                match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)" alt=".+?" width=".+?" height=".+?" class=".+?" />').findall(link)
                for url,name,thumb in match:
                            main.addDir(name,url,35,thumb)
        main.GA("Etowns","Search")


def LINKSP2(mname,url):
        link=main.OPENURL(url)
        link=link.replace('http://go.etowns.net','')
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        match=re.compile('<li><a href="h(.+?)">(.+?)</a></li>').findall(link)
        for murl, name in match:
                thumb=name.lower()
                murl='h'+murl
                hosted_media = urlresolver.HostedMediaFile(url=murl, title=name)
                match2=re.compile("{'url': '(.+?)', 'host': '(.+?)', 'media_id': '.+?'}").findall(str(hosted_media))
                for murl,host in match2:
                        main.addDown2(mname+' [COLOR blue]'+name+'[/COLOR]',murl,209,art+thumb+".png",art+thumb+".png")
        

def LINKSP2B(mname,murl):
        main.GA("Newmyvideolinks","Watched") 
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
        listitem.setInfo('video', {'Title': mname, 'Year': ''} )
        hosted_media = urlresolver.HostedMediaFile(murl)
        source = hosted_media
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
        else:
              stream_url = False
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok


def UFCNEW():
        try: 
                urllist=['http://newmyvideolinks.com/index.php?s=ufc','http://newmyvideolinks.com/page/2/?s=ufc']
        except:
                urllist=['http://newmyvideolinks.com/index.php?s=ufc']
        for surl in urllist:
                link=main.OPENURL(surl)
                match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
                if len(match)>0:
                        for url,thumb,name in match:
                                match=re.compile('UFC').findall(name)
                                if len(match)>0:
                                        main.addDir(name,url,35,thumb)

                else:
                        match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)" alt=".+?" width=".+?" height=".+?" class=".+?" />').findall(link)
                        for url,name,thumb in match:
                                match=re.compile('UFC').findall(name)
                                if len(match)>0:
                                       main.addDir(name,url,35,thumb)
        main.GA("Newmyvideolinks","UFC")
