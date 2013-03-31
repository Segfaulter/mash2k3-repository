import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def LISTTV2(murl):
        if murl=='movintv':
            main.addDir('Search Movie1k','www.movie1k.org',132,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            urllist=['http://www.movie1k.org/category/tv-show/','http://www.movie1k.org/category/tv-show/page/2/','http://www.movie1k.org/category/tv-show/page/3/','http://www.movie1k.org/category/tv-show/page/4/','http://www.movie1k.org/category/tv-show/page/5/']
        elif murl=='movin':
            urllist=['http://www.movie1k.org/category/hindi-movies/','http://www.movie1k.org/category/hindi-movies/page/2/','http://www.movie1k.org/category/hindi-movies/page/3/','http://www.movie1k.org/category/hindi-movies/page/4/','http://www.movie1k.org/category/hindi-movies/page/5/','http://www.movie1k.org/category/hindi-movies/page/6/','http://www.movie1k.org/category/hindi-movies/page/7/']
        elif murl=='movindub':
            urllist=['http://www.movie1k.org/category/hindi-dubbed-movies/','http://www.movie1k.org/category/hindi-dubbed-movies/page/2/','http://www.movie1k.org/category/hindi-dubbed-movies/page/3/','http://www.movie1k.org/category/hindi-dubbed-movies/page/4/','http://www.movie1k.org/category/hindi-dubbed-movies/page/5/','http://www.movie1k.org/category/hindi-dubbed-movies/page/6/','http://www.movie1k.org/category/hindi-dubbed-movies/page/7/']
            murl=murl
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for murl in urllist:
                link=main.OPENURL(murl)
                match=re.compile('href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" class=".+?" alt="Watch.+?" title="(.+?)" />').findall(link)
                for url,thumb,name in match:
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        main.addPlay(name,url,31,thumb)
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("TV-INT","Movie1k")


def SearchhistoryMovie1k():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='M1k'
            SEARCHMovie1k(url)
        else:
            main.addDir('Search','M1k',133,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,133,thumb)
            
            
    


def SEARCHMovie1k(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'M1k':
                keyb = xbmc.Keyboard('', 'Search For Shows or Movies')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        surl='http://www.movie1k.org/?s='+encode
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
                surl='http://www.movie1k.org/?s='+encode
        req = urllib2.Request(surl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" class=".+?" alt="Watch.+?" title="(.+?)" />').findall(link)
        for url,thumb,name in match:
                    main.addPlay(name,url,31,thumb)
        main.GA("Movie1k","Search")

def VIDEOLINKST2(mname,murl):
        sources = []
        main.GA("Movie1k","Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,5000)")
        link=main.OPENURL(murl)
        ok=True
        match=re.compile('<a href="(.+?)">(.+?)</a><br />').findall(link)
        for url, host in match:
                
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
                
        match2=re.compile(': (.+?)</strong></p>\n<p><a href=".+?watch.php.?idl=(.+?)"').findall(link)
        for host, url in match2:
                matchx=re.compile('sockshare.com').findall(url)
                if (len(matchx)>0):
                    url=url.replace('embed','file')
                matchy=re.compile('putlocker.com').findall(url)
                if (len(matchy)>0):
                    url=url.replace('embed','file')
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
                match4=re.compile('linkembed').findall(url)
                if len(match4)>0:
                    link2=main.OPENURL(url)
                    match3=re.compile('<iframe.+?src="(.+?)"').findall(link2)
                    if len(match3)==0:
                        match3=re.compile('<IFRAME SRC="(.+?)"').findall(link2)
                    for url2 in match3:
                        matchx=re.compile('sockshare.com').findall(url2)
                        if (len(matchx)>0):
                            url2=url2.replace('embed','file')
                        matchy=re.compile('putlocker.com').findall(url2)
                        if (len(matchy)>0):
                            url2=url2.replace('embed','file')
                        hosted_media = urlresolver.HostedMediaFile(url=url2, title=host)
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
