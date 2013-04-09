import urllib,urllib2,re,cookielib,urlresolver
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def LISTDOC(murl):
    if murl=='doc1':
        main.GA("Documantary","DhHome")
        main.addDir('[COLOR red]Search[/COLOR]','search',89,'')
        main.addDir('[COLOR red]Popular[/COLOR]','http://documentaryheaven.com/popular/',89,'')
        main.addDir('[COLOR red]Recent[/COLOR]','http://documentaryheaven.com/all/',87,'')
        url='http://documentaryheaven.com/'
        link=main.OPENURL(url)
        match=re.compile('<li class=".+?"><a href="(.+?)" title=".+?">(.+?)</a> </li>').findall(link)
        for url, name in match:
            main.addDir(name,url,87,'')
    elif murl=='doc2':
        main.GA("Documantary","TDFHome")
        main.addDir('[COLOR red]Recent[/COLOR]','http://topdocumentaryfilms.com/all/',87,'')
        main.addDir('[COLOR red]Recommended[/COLOR]','rec',89,'')
        url='http://topdocumentaryfilms.com/'
        link=main.OPENURL(url)
        match=re.compile('href="(.+?)" title=".+?">(.+?)</a>.+?</li>').findall(link)
        for url, name in match:
            main.addDir(name,url,87,'')
    elif murl=='doc3':
        main.GA("Documantary","DLHome")
        main.addDir('[COLOR red]Latest[/COLOR]','http://www.documentary-log.com/',87,'')
        main.addDir("[COLOR red]Editor's Picks[/COLOR]",'http://www.documentary-log.com/category/editors-picks/',87,'')
        url='http://www.documentary-log.com/'
        link=main.OPENURL(url)
        match=re.compile('<li class="cat-item cat-item-.+?"><a href="(.+?)" title="(.+?)">(.+?)</a> ([^<]+)').findall(link)
        for url, desc, name, leng in match:
            main.addDir2(name+'  '+leng,url,87,'',desc)

def LISTDOC2(murl):
    match=re.compile('documentaryheaven').findall(murl)
    if (len(match)>0):
        main.GA("DhHome","Dh-List")
        link=main.OPENURL(murl)
        match=re.compile('<a href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        if (len(match)==0):
            match=re.compile('href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        for url,thumb,name,desc in match:
            #main.addDir(name,url,88,thumb)
            main.addSport(name,url,88,thumb,desc,'','')
        paginate=re.compile("class='page current'>1</span></li><li><a href='http://documentaryheaven.com/.+?/page/2/'").findall(link)
        if (len(paginate)>0):
            main.addDir('[COLOR blue]Page 2[/COLOR]',murl+'page/2/',87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        else:
                paginate=re.compile('http://documentaryheaven.com/(.+?)/page/(.+?)/').findall(murl)
                for section, page in paginate:
                        pg= int(page) +1
                        xurl = 'http://documentaryheaven.com/' + str(section) + '/page/'+ str (pg) + '/'
                main.addDir('[COLOR blue]Page '+ str(pg)+'[/COLOR]',xurl,87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

    match2=re.compile('topdocumentaryfilms').findall(murl)
    if (len(match2)>0):
        i=0
        main.GA("TDFHome","TDF-List")
        link=main.OPENURL(murl)
        link=link.replace('\n','')
        url=re.compile('href="([^<]+)">Watch now').findall(link)
        match=re.compile('href=".+?".+?src="(.+?)".+?alt="(.+?)"').findall(link)
        desc=re.compile('>([^<]+)</p><p><strong>').findall(link)
        for thumb,name in match:
            #main.addDir(name,url,88,thumb)
            main.addSport(name,url[i],88,thumb,desc[i],'','')
            i=i+1
        paginate=re.compile('</a>.+?href="([^<]+)">Next</a></div>').findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                main.addDir('[COLOR blue]Next[/COLOR]',purl,87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

    match3=re.compile('documentary-log').findall(murl)
    if (len(match3)>0):
        main.GA("DLHome","DL-List")
        i=0
        link=main.OPENURL(murl)
        match=re.compile('<img src="(.+?)" alt="(.+?)" class=".+?" />\n').findall(link)
        url=re.compile('<h2 class="title-1">\n      <a href="([^<]+)" title=').findall(link)
        desc=re.compile('<p>([^<]+)<').findall(link)
        for thumb,name in match:
            main.addPlay2(name,url[i],88,thumb,desc[i])
            i=i+1
        paginate=re.compile("<a href='([^<]+)' class='nextpostslink'>").findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                main.addDir('[COLOR blue]Next[/COLOR]',purl,87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

                  
def LISTDOCPOP(murl):
    if murl=='search':
        keyb = xbmc.Keyboard('', 'Search Documentaries')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://documentaryheaven.com/?s='+encode
                link=main.OPENURL(surl)
        match=re.compile('<a href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        if (len(match)==0):
            match=re.compile('href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        for url,thumb,name,desc in match:
            main.addSport(name,url,88,thumb,desc,'','')

        paginate=re.compile("<span class=\'page current\'>1</span></li><li><a href=\'http://documentaryheaven.com/page/2/.?s=.+?\'").findall(link)
        if (len(paginate)>0):
            main.addDir('[COLOR blue]Page 2[/COLOR]','http://documentaryheaven.com/page/2/?s='+encode,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
    elif murl=='rec':
        rurl='http://topdocumentaryfilms.com/'
        link=main.OPENURL(rurl)
        match=re.compile('href="([^<]+)">([^<]+)</a></li><li><a').findall(link)
        for url,name in match:
            main.addPlay(name,url,88,'')
    else:
        link=main.OPENURL(murl)
        match=re.compile("<li><a href='(.+?)'>(.+?)</a></li>").findall(link)
        for url,name in match:
            main.addPlay(name,url,88,'')


def LINKDOC(mname,murl):
    match=re.compile('documentaryheaven').findall(murl)
    if (len(match)>0):
        main.GA("DocumentaryHeaven","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.OPENURL(murl)
        match=re.compile('<div id="command"><a class="lightSwitcher" href="#">.+?</a></div>                      \n                     <div class=\'video\'><iframe.+?src="(.+?)"').findall(link)
        for url in match:
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
        if (len(match)==0):
            match=re.compile('<iframe\r\nwidth=".+?" height=".+?" src="(.+?)"').findall(link)
            print match[0]
            link2=main.OPENURL(match[0])
            match2=re.compile('href="/watch.?v=(.+?)"').findall(link2)
            url='http://www.youtube.com/watch?v='+match2[0]
        
        print "vlink " +url
        media = urlresolver.HostedMediaFile(str(url))
        source = media
        listitem = xbmcgui.ListItem(mname)
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False  
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok

    match2=re.compile('topdocumentaryfilms').findall(murl)
    if (len(match2)>0):
        sources=[]
        main.GA("TopDocumentaryFilms","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.OPENURL(murl)
        ok=True
        link=link.replace('src="http://cdn.tdfimg.com/wp-content/uploads','')
        match=re.compile('src="(.+?)"').findall(link)
        for url in match:
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
            match7=re.compile('google').findall(url)
            if (len(match7)>0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,link down,3000)")
                return
            match6=re.compile('youtube').findall(url)
            if (len(match6)>0):
                match=re.compile('http://www.youtube.com/embed/n_(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                if (len(match)>0):
                    url='http://www.youtube.com/watch?feature=player_embedded&v=n_'+match[0]
                else:
                    match=re.compile('http://www.youtube.com/embed/(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                    if (len(match)>0):
                        url='http://www.youtube.com/watch?feature=player_embedded&v='+match[0]
                    match2=re.compile('videoseries').findall(url)
                    if (len(match2)>0):
                        link2=main.OPENURL(url)
                        match2=re.compile('href="/watch.?v=(.+?)"').findall(link2)
                        match3=re.compile("http://www.youtube.com/embed/videoseries.?list=(.+?)&amp;iv_load_policy=3").findall(url)
                        print match3
                        url='http://www.youtube.com/watch?v='+match2[0]
                               
                    else:
                        url=url.replace('?rel=0','')
        """hosted_media = urlresolver.HostedMediaFile(url=url, title=host+' [COLOR red]'+lang+'[/COLOR]')
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)"""
        
        print "vlink " +str(url)
        media = urlresolver.HostedMediaFile(str(url))
        source = media
        listitem = xbmcgui.ListItem(mname)
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False
        
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok

    match3=re.compile('documentary-log.com').findall(murl)
    if (len(match3)>0):        

        main.GA("Documentary-Log","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.OPENURL(murl)
        link=link.replace('src="http://cdn.tdfimg.com/wp-content/uploads','')
        match=re.compile('src="(.+?)" .+?></iframe>').findall(link)
        if (len(match)==0):
            link=link.replace('src="http://www.documentary-log.com/wp-cont','')
            match=re.compile('src="(.+?)" .+?/>').findall(link)
        for url in match:
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
            match7=re.compile('google').findall(url)
            if (len(match7)>0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,link down,3000)")
                return
            match6=re.compile('youtube').findall(url)
            if (len(match6)>0):
                match=re.compile('http://www.youtube.com/embed/n_(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                if (len(match)>0):
                    url='http://www.youtube.com/watch?feature=player_embedded&v=n_'+match[0]
                else:
                    match=re.compile('http://www.youtube.com/embed/(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                    if (len(match)>0):
                        url='http://www.youtube.com/watch?feature=player_embedded&v='+match[0]
                    match2=re.compile('videoseries').findall(url)
                    if (len(match2)>0):
                        link2=main.OPENURL(url)
                        match2=re.compile('href="/watch.?v=(.+?)"').findall(link2)
                        match3=re.compile("http://www.youtube.com/embed/videoseries.?list=(.+?)&amp;iv_load_policy=3").findall(url)
                        print match3
                        url='http://www.youtube.com/watch?v='+match2[0]
                               
                    else:
                        url=url.replace('?rel=0','')
        
        print "vlink " +str(url)
        media = urlresolver.HostedMediaFile(str(url))
        source = media
        listitem = xbmcgui.ListItem(mname)
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False
        
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
