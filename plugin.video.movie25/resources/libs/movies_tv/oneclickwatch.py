import urllib,urllib2,re,cookielib,urlresolver
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def LISTSP(murl): 
        urllist=['http://oneclickwatch.org/category/movies/','http://oneclickwatch.org/category/movies/page/2/','http://oneclickwatch.org/category/movies/page/3/','http://oneclickwatch.org/category/movies/page/4/','http://oneclickwatch.org/category/movies/page/5/','http://oneclickwatch.org/category/movies/page/6/','http://oneclickwatch.org/category/movies/page/7/','http://oneclickwatch.org/category/movies/page/8/','http://oneclickwatch.org/category/movies/page/9/','http://oneclickwatch.org/category/movies/page/10/','http://oneclickwatch.org/category/movies/page/11/','http://oneclickwatch.org/category/movies/page/12/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = 12
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for murl in urllist:
                link=main.OPENURL(murl)
                match=re.compile('<h2 class="pagetitle"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>\r\n\t\t\t\t<small>Posted: .+?<strong>.+?</strong> in <a href=".+?" title="View all posts in Movies" rel="category tag">Movies</a><br />\r\n\t\t\t\t</small>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="postcomments"><a href=".+?" title=".+?">0</a></div>\r\n\r\n\t\t\t\t<div class="entry">\r\n\t\t\t\t\t<p>(.+?) Plot:').findall(link)
                for url,sitename,mname in match:
                        match=re.compile('(.+?) / .+?').findall(mname)
                        for nname in match:
                                mname = nname
                        match=re.compile('(.+?) aka .+?').findall(mname)
                        for nname in match:
                                mname = nname
                        mname=mname.replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        namelen=len(mname)
                        if mname[-2:namelen-1] == ')':
                                nam= namelen- 6
                                year = mname[nam:namelen-2]
                                name= mname[0:namelen-7]
                        else:
                                nam= namelen- 5
                                year = mname[nam:namelen-1]
                                year2='('+year+')'
                                name= mname[0:namelen-6]
                        year=year.replace('(2 )','').replace(') ak','')
                        match=re.compile('720p BRRip').findall(sitename)
                        if (len(match) > 0):
                                year2 = '('+year+')'+'[COLOR red] 720p BRRip[/COLOR]'
                                main.addInfo(name+year2,url,26,'','',year)
                        match=re.compile('720p HDRip').findall(sitename)
                        if (len(match) > 0):
                                year2 = '('+year+')'+'[COLOR red] 720p HDRip[/COLOR]'
                                main.addInfo(name+year2,url,26,'','',year)
                        match=re.compile('720p WEBRip').findall(sitename)
                        if (len(match) > 0):
                                year2 = '('+year+')'+'[COLOR red] 720p WEBRip[/COLOR]'
                                main.addInfo(name+year2,url,26,'','',year)
                        match=re.compile('720p BluRay').findall(sitename)
                        if (len(match) > 0):
                                year2 = '('+year+')'+'[COLOR red] 720p BluRay[/COLOR]'
                                main.addInfo(name+year2,url,26,'','',year)
                        name=name.replace('-','').replace('&','').replace('acute;','')
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("HD","Oneclickwatch")


def LISTTV3(murl):
        urllist=['http://oneclickwatch.org/category/tv-shows/','http://oneclickwatch.org/category/tv-shows/page/2/','http://oneclickwatch.org/category/tv-shows/page/3/','http://oneclickwatch.org/category/tv-shows/page/4/','http://oneclickwatch.org/category/tv-shows/page/5/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = 5
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for murl in urllist:
                link=main.OPENURL(murl)
                match=re.compile('<a href="(.+?)" rel="bookmark" title="Permanent Link to .+?">(.+?)</a>').findall(link)
                for url,name in match:
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        main.addPlay(name,url,135,'')
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("TV","Oneclickwatch")


def LINKSP(name,url):
        link=main.OPENURL(url)
        putlocker=re.compile('<a href="(.+?)">putlocker.com</a><br />').findall(link)
        for url in putlocker:
                match=re.compile('http://pastebin.com/.+?').findall(url)
                if (len(match) > 0):
                        link=main.OPENURL(url)
                        main.addLink('If list is empty,means the links are downloadable only','','')
                else:
                        main.addPlayb(name,url,134,"%s/art/put.png"%selfAddon.getAddonInfo("path"),"%s/art/put.png"%selfAddon.getAddonInfo("path"))
        flashx=re.compile('<a href="(.+?)">flashx.tv</a><br />').findall(link)
        for url in flashx:
                main.addPlayb(name,url,134,"%s/art/flash.png"%selfAddon.getAddonInfo("path"),"%s/art/flash.png"%selfAddon.getAddonInfo("path"))
        nowvideo=re.compile('<a href="(.+?)">nowvideo.eu</a><br />').findall(link)
        for url in nowvideo:
                main.addPlayb(name,url,134,"%s/art/nov.png"%selfAddon.getAddonInfo("path"),"%s/art/nov.png"%selfAddon.getAddonInfo("path"))
        uploadc=re.compile('<a href="(.+?)">uploadc.com</a><br />').findall(link)
        for url in uploadc:
                main.addPlayb(name,url,134,"%s/art/uc.png"%selfAddon.getAddonInfo("path"),"%s/art/uc.png"%selfAddon.getAddonInfo("path"))
        vidxden=re.compile('<a href="(.+?)">vidxden.com</a><br />').findall(link)
        for url in vidxden:
                main.addPlayb(name,url,134,"%s/art/vidx.png"%selfAddon.getAddonInfo("path"),"%s/art/vidx.png"%selfAddon.getAddonInfo("path"))
        vidbux=re.compile('<a href="(.+?)">vidbux.com</a><br />').findall(link)
        for url in vidbux:
                main.addPlayb(name,url,134,"%s/art/vidb.png"%selfAddon.getAddonInfo("path"),"%s/art/vidb.png"%selfAddon.getAddonInfo("path"))


def PLAYOCW(name,murl):
        main.GA("OneclickwatchM","Watched")
        ok=True
        name=name.replace('[DVD]','').replace('[TS]','').replace('[TC]','').replace('[CAM]','').replace('[SCREENER]','').replace('[COLOR blue]','').replace('[COLOR red]','').replace('[/COLOR]','')
        name=name.replace(' : Putlocker','').replace(' : Sockshare','').replace(' : Nowvideo','').replace(' : 180upload','').replace(' : Filenuke','').replace(' : Flashx','').replace(' : Novamov','').replace(' : Uploadc','').replace(' : Xvidstage','').replace(' : Zooupload','').replace(' : Zalaa','').replace(' : Vidxden','').replace(' : Vidbux','')
        name=name.replace(' 720p BRRip','').replace(' 720p HDRip','').replace(' 720p WEBRip','').replace(' 720p BluRay','')
        namelen=len(name)
        if name[-2:namelen-1] == ')':
                nam= namelen- 6
                year = name[nam:namelen-2]
                name= name[0:namelen-7]
        else:
                nam= namelen- 5
                year = name[nam:namelen-1]
                name= name[0:namelen-6]
        infoLabels = main.GETMETAB(name,'',year,'')
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png",thumbnailImage=infoLabels['cover_url'])
        listitem.setInfo("Video", infoLabels = infoLabels)
        listitem.setProperty('mimetype', 'video/x-msvideo')
        listitem.setProperty('IsPlayable', 'true')
        media = urlresolver.HostedMediaFile(murl)
        source = media
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
        else:
              stream_url = False  
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok

def VIDEOLINKST3(mname,murl):
        sources = []
        main.GA("OneclickwatchT","Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,5000)")
        link=main.OPENURL(murl)
        ok=True
        match=re.compile('<a href="(.+?)">(.+?)</a><br />').findall(link)
        for url, host in match:
                
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
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
