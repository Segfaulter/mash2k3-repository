# -*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.movie25/art/hosts', ''))


def LISTTV4(murl):
        main.addDir('Search Rlsmix','rlsmix',136,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
        main.addLink('[COLOR red]First turbobit Link could be HD[/COLOR]','',"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        urllist=['http://www.rlsmix.net/category/tv-shows/','http://www.rlsmix.net/category/tv-shows/page/2/','http://www.rlsmix.net/category/tv-shows/page/3/','http://www.rlsmix.net/category/tv-shows/page/4/','http://www.rlsmix.net/category/tv-shows/page/5/','http://www.rlsmix.net/category/tv-shows/page/6/','http://www.rlsmix.net/category/tv-shows/page/7/','http://www.rlsmix.net/category/tv-shows/page/8/','http://www.rlsmix.net/category/tv-shows/page/9/','http://www.rlsmix.net/category/tv-shows/page/10/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = 10
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for murl in urllist:
                link=main.OPENURL(murl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<h1 class="titles"><a href="(.+?)" title="Permanent Link to (.+?)">.+?src="http://uppix.net/(.+?)"').findall(link)
                for url,name,thumb in match:
                        match2=re.compile('TV Round Up').findall(name)
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        if len(match2)==0:
                            main.addDir(name,url,62,'http://uppix.net/'+thumb)
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("TV","Rlsmix")

def LINKTV4(mname,url):
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,3000)")
        link=main.OPENURL(url)
        link= link.replace('TV Rage','').replace('Homepage','').replace('href="http://www.tvrage.com','').replace('href="http://www.cbs.com','').replace('Torrent Search','').replace('Season Download','').replace('href="http://uppix.net','').replace('href="http://www.torrentz.com','').replace('href="http://directdownload.tv','')
        ok=True
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(link)
        print len(match)
        for url, host in match:
                thumb=host.lower()
                match5=re.compile('Part').findall(host)
                if len(match5)>0:
                        match6=re.compile('http://(.+?)/.+?').findall(url)
                        for url2 in match6:
                            host2 = url2.replace('www.','').replace('.in','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','')
                        thumb=host2.lower()
                match3=re.compile('720p').findall(url)
                match4=re.compile('mp4').findall(url)
                
                
                if len(match3)>0:
                    host =host+' [COLOR red]HD[/COLOR]'
                elif len(match4)>0:
                    host =host+' [COLOR green]SD MP4[/COLOR]'
                else:
                    host =host+' [COLOR blue]SD[/COLOR]'
                match2=re.compile('rar').findall(url)
                if len(match2)==0:
                        hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                        match2=re.compile("{'url': '(.+?)', 'host': '(.+?)', 'media_id': '.+?'}").findall(str(hosted_media))
                        for murl,name in match2:
                                main.addDown2(mname+' [COLOR blue]'+host+'[/COLOR]',murl,210,art+thumb+".png",art+thumb+".png")

        
def LINKTV4B(mname,murl):
        main.GA("RlsmixTV","Watched")
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

def SearchhistoryRlsmix():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='rlsmix'
            SEARCHRlsmix(url)
        else:
            main.addDir('Search','rlsmix',137,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,137,thumb)
            
            
    


def SEARCHRlsmix(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'rlsmix':
                keyb = xbmc.Keyboard('', 'Search For Shows or Movies')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        urllist=['http://www.rlsmix.net/?s='+encode,'http://www.rlsmix.net/page/2/?s='+encode,'http://www.rlsmix.net/page/3/?s='+encode]
                        for surl in urllist:
                            link=main.OPENURL(surl)
                            link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                            match=re.compile('<h1 class="titles"><a href="(.+?)" title="Permanent Link to (.+?)">.+?src="http://uppix.net/(.+?)"').findall(link)
                            for url,name,thumb in match:
                                match2=re.compile('TV Round Up').findall(name)
                                name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                                if len(match2)==0:
                                    main.addPlay(name,url,62,'http://uppix.net/'+thumb)
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
                urllist=['http://www.rlsmix.net/?s='+encode,'http://www.rlsmix.net/page/2/?s='+encode,'http://www.rlsmix.net/page/3/?s='+encode]
                for surl in urllist:
                    link=main.OPENURL(surl)
                    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                    match=re.compile('<h1 class="titles"><a href="(.+?)" title="Permanent Link to (.+?)">.+?src="http://uppix.net/(.+?)"').findall(link)
                    for url,name,thumb in match:
                        match2=re.compile('TV Round Up').findall(name)
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        if len(match2)==0:
                            main.addDir(name,url,62,'http://uppix.net/'+thumb)
        main.GA("Movie1k","Search")
