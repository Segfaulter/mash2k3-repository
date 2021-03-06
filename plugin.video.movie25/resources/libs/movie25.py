import urllib,urllib2,re,cookielib, urlresolver,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)



def FAVS():
        favpath=os.path.join(main.datapath,'Favourites')
        moviefav=os.path.join(favpath,'Movies')
        FavFile=os.path.join(moviefav,'Fav')
        if os.path.exists(FavFile):
                Favs=re.compile('url="(.+?)",name="(.+?)"').findall(open(FavFile,'r').read())
                for url,mname in Favs:
                        namelen=len(mname)
                        nam= namelen- 5
                        year = mname[nam:namelen-1]
                        name= mname[0:namelen-6]
                        name=name.replace('-','').replace('&','').replace('acute;','')

                        url=url.replace('(','').replace('[','')
                        if url[0]=='m':
                                url='http://movie25.com/'+url
                        link=main.OPENURL(url)
                        match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_blank">').findall(link)
                        for thumb in match:
                                main.addInfo(name+'('+year+')',url,3,thumb,'',year)
                
        else:
                xbmc.executebuiltin("XBMC.Notification([B][COLOR green]Mash Up[/COLOR][/B],[B]You Have No Saved Favourites[/B],5000,"")")
        main.GA("None","Movie25-Fav")
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()



def LISTMOVIES(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class="movie_pic"><a href="(.+?)" ><img src="(.+?)" width=".+?" height=".+?" alt=".+?" /></a></div>  <div class=".+?">    <div class=".+?">      <h1><a href=".+?" >(.+?)</a></h1>      <div class=".+?">Genre:      <a href=".+?" title=\'.+?\'>(.+?)</a>.+?Release:.+?<br/>      Views: <span>(.+?)</span>.+?<span>(.+?)</span> votes.+?<div id=".+?">score:<span id=Rate_.+?>(.+?)</span></div>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,mname,genre,views,votes,rating in match:
                namelen=len(mname)
                if mname[-2:namelen-1] == ')':
                        nam= namelen- 6
                        year = mname[nam:namelen-2]
                        name= mname[0:namelen-7]
                elif mname[-1:namelen] == ')':
                        nam= namelen- 5
                        year = mname[nam:namelen-1]
                        name= mname[0:namelen-6]
                else:
                        name = mname
                        year = ''
                name=name.replace('-','').replace('&','').replace('acute;','')
                main.addInfo(name+'('+year+')[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'[/COLOR]',url,3,thumb,genre,year)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        
        main.GA("None","Movie25-list")
        paginate=re.compile('http://www.movie25.com/movies/.+?/index-(.+?).html').findall(murl)
       
        if (len(paginate) == 0):
                purl = murl + 'index-2.html'
                main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,207,"%s/art/gotopage.png"%selfAddon.getAddonInfo("path"))
                main.addDir('[COLOR blue]Page 2[/COLOR]',purl,1,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        else:
                paginate=re.compile('http://www.movie25.com/movies/(.+?)/index-(.+?).html').findall(murl)
                for section, page in paginate:
                        pg= int(page) +1
                        xurl = main.Mainurl + str(section) + '/' + 'index-'+ str (pg) + '.html'
                main.addDir('[COLOR red]Home[/COLOR]','',0,"%s/art/home.png"%selfAddon.getAddonInfo("path"))
                main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,207,"%s/art/gotopage.png"%selfAddon.getAddonInfo("path"))
                main.addDir('[COLOR blue]Page '+ str(pg)+'[/COLOR]',xurl,1,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()


def UFCMOVIE25():
                surl='http://www.movie25.com/search.php?key=ufc&submit='
                link=main.OPENURL(surl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<div class="movie_pic"><a href="(.+?)" target=".+?">                            <img src="(.+?)" width=".+?" height=".+?" />                            </a></div>            <div class=".+?">              <div class=".+?">                <h1><a href=".+?" target=".+?">                  (.+?)                  </a></h1>                <div class=".+?">Genre:                  <a href=".+?" target=\'.+?\'>(.+?)</a>.+?Release:.+?Views: <span>                (.+?)                </span>.+?<span id=RateCount.+?>                (.+?)                </span> votes.+?<div id=".+?">score:<span id=Rate_.+?>(.+?)</span>').findall(link)
                dialogWait = xbmcgui.DialogProgress()
                ret = dialogWait.create('Please wait until Movie list is cached.')
                totalLinks = len(match)
                loadedLinks = 0
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
                for url,thumb,mname,genre,views,votes,rating in match:
                        namelen=len(mname)
                        if mname[-4:namelen-3] == ')':
                                nam= namelen- 8
                                year = mname[nam:namelen-4]
                                name= mname[0:namelen-9]
                        elif mname[-3:namelen-2] == ')':
                                nam= namelen- 7
                                year = mname[nam:namelen-3]
                                name= mname[0:namelen-8]
                        else:
                                name = mname
                                year = ''
                        name=name.replace('-','').replace('&','').replace('acute;','')
                        furl= 'http://movie25.com/'+url
                        main.addInfo(name+'('+year+')[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'[/COLOR]',furl,3,thumb,genre,year)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False 
                dialogWait.close()
                del dialogWait
                main.addDir('[COLOR blue]Page 2[/COLOR]','http://www.movie25.com/search.php?page=2&key=ufc',9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
                main.GA("UFC","UFC_Movie25-List")

def Searchhistory():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            url='m25'
            SEARCH(url)
        else:
            main.addDir('Search','m25',4,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,4,thumb)

def SEARCH(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'm25':
                keyb = xbmc.Keyboard('', 'Search Movies')
                keyb.doModal()
                if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://www.movie25.com/search.php?key='+encode+'&submit='
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
                        return
        else:
                encode = murl
                surl='http://www.movie25.com/search.php?key='+encode+'&submit='
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class="movie_pic"><a href="(.+?)" target=".+?">                            <img src="(.+?)" width=".+?" height=".+?" />                            </a></div>            <div class=".+?">              <div class=".+?">                <h1><a href=".+?" target=".+?">                  (.+?)                  </a></h1>                <div class=".+?">Genre:                  <a href=".+?" target=\'.+?\'>(.+?)</a>.+?Release:.+?Views: <span>                (.+?)                </span>.+?<span id=RateCount.+?>                (.+?)                </span> votes.+?<div id=".+?">score:<span id=Rate_.+?>(.+?)</span>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,mname,genre,views,votes,rating in match:
                namelen=len(mname)
                if mname[-4:namelen-3] == ')':
                        nam= namelen- 8
                        year = mname[nam:namelen-4]
                        name= mname[0:namelen-9]
                elif mname[-3:namelen-2] == ')':
                        nam= namelen- 7
                        year = mname[nam:namelen-3]
                        name= mname[0:namelen-8]
                else:
                        name = mname
                        year = ''
                name=name.replace('-','').replace('&','').replace('acute;','')
                furl= 'http://movie25.com/'+url
                main.addInfo(name+'('+year+')[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'[/COLOR]',furl,3,thumb,genre,year)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False 
        dialogWait.close()
        del dialogWait
        main.addDir('[COLOR blue]Page 2[/COLOR]','http://www.movie25.com/search.php?page=2&key='+encode,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","Movie25-Search")


def ENTYEAR():
        dialog = xbmcgui.Dialog()
        d = dialog.numeric(0, 'Enter Year')
        if d:
                encode=urllib.quote(d)
                if encode < '2014' and encode > '1900':
                     surl='http://www.movie25.com/search.php?year='+encode+'/'
                     YEARB(surl)
                else:
                    dialog = xbmcgui.Dialog()
                    ret = dialog.ok('Wrong Entry', 'Must enter year in four digit format like 1999','Enrty must be between 1900 and 2014')
        
def GotoPage(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        r = re.findall('Next</a><a href="index-(.+?).html"  title="Last" >Last</a>',link)
        dialog = xbmcgui.Dialog()
        d = dialog.numeric(0, 'Section Last Page = '+r[0])
        if d:
                pagelimit=int(r[0])
                if int(d) <= pagelimit:
                     encode=urllib.quote(d)
                     url  = url.split('index-')[0]
                     surl=url+'index-'+encode+'.html'
                     LISTMOVIES(surl)
                else:
                    dialog = xbmcgui.Dialog()
                    ret = dialog.ok('Wrong Entry', 'The page number you entered does not exist.',' This sections page limit is '+str(pagelimit) )

def GotoPageB(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        r = re.findall('>Next</a><a href=\'search.php.?page=(.+?)&year=.+?\'>Last</a>',link)
        dialog = xbmcgui.Dialog()
        d = dialog.numeric(0, 'Section Last Page = '+r[0])
        if d:
                pagelimit=int(r[0])
                if int(d) <= pagelimit:
                     encode=urllib.quote(d)
                     year  = url.split('year=')
                     url  = url.split('year=')
                     url  = url[0].split('page=')
                     
                     
                     surl=url[0]+'page='+encode+'&year='+year[1]
                     NEXTPAGE(surl)
                else:
                    dialog = xbmcgui.Dialog()
                    ret = dialog.ok('Wrong Entry', 'The page number you entered does not exist.',' This sections page limit is '+str(pagelimit) )

def YEARB(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class="movie_pic"><a href="(.+?)" target=".+?">                            <img src="(.+?)" width=".+?" height=".+?" />                            </a></div>            <div class=".+?">              <div class=".+?">                <h1><a href=".+?" target=".+?">                  (.+?)                  </a></h1>                <div class=".+?">Genre:                  <a href=".+?" target=\'.+?\'>(.+?)</a>.+?Release:.+?Views: <span>                (.+?)                </span>.+?<span id=RateCount.+?>                (.+?)                </span> votes.+?<div id=".+?">score:<span id=Rate_.+?>(.+?)</span>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,mname,genre,views,votes,rating in match:
                namelen=len(mname)
                if mname[-4:namelen-3] == ')':
                        nam= namelen- 8
                        year = mname[nam:namelen-4]
                        name= mname[0:namelen-9]
                elif mname[-3:namelen-2] == ')':
                        nam= namelen- 7
                        year = mname[nam:namelen-3]
                        name= mname[0:namelen-8]
                else:
                        name = mname
                        year = ''
                name=name.replace('-','').replace('&','').replace('acute;','')
                furl= 'http://movie25.com/'+url
                main.addInfo(name+'('+year+')[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'[/COLOR]',furl,3,thumb,genre,year)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False 
        dialogWait.close()
        del dialogWait
        ye = murl[39:44]
        main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,208,"%s/art/gotopage.png"%selfAddon.getAddonInfo("path"))
        main.addDir('[COLOR blue]Page 2[/COLOR]','http://www.movie25.com/search.php?page=2&year='+str(ye),9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()
        
def NEXTPAGE(murl):
    match=re.compile('documentaryheaven').findall(murl)
    if (len(match)>0):
        link=main.OPENURL(murl)
        match=re.compile('<a href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        if (len(match)==0):
            match=re.compile('href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        for url,thumb,name,desc in match:
            addSport(name,url,88,thumb,desc,'','')
        paginate=re.compile('http://documentaryheaven.com/page/(.+?)/.?s=(.+?)').findall(murl)
        for page, search in paginate:
            pgs = int(page)+1
            jurl='http://documentaryheaven.com/page/'+str(pgs)+'/?s='+str(search)
        main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,208,"%s/art/gotopage.png"%selfAddon.getAddonInfo("path"))
        main.addDir('[COLOR blue]Page '+str(pgs)+'[/COLOR]',jurl,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

    else:
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class="movie_pic"><a href="(.+?)" target=".+?">                            <img src="(.+?)" width=".+?" height=".+?" />                            </a></div>            <div class=".+?">              <div class=".+?">                <h1><a href=".+?" target=".+?">                  (.+?)                  </a></h1>                <div class=".+?">Genre:                  <a href=".+?" target=\'.+?\'>(.+?)</a>.+?Release:.+?Views: <span>                (.+?)                </span>.+?<span id=RateCount.+?>                (.+?)                </span> votes.+?<div id=".+?">score:<span id=Rate_.+?>(.+?)</span>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,mname,genre,views,votes,rating in match:
                namelen=len(mname)
                if mname[-4:namelen-3] == ')':
                        nam= namelen- 8
                        year = mname[nam:namelen-4]
                        name= mname[0:namelen-9]
                elif mname[-3:namelen-2] == ')':
                        nam= namelen- 7
                        year = mname[nam:namelen-3]
                        name= mname[0:namelen-8]
                else:
                        name = mname
                        year = ''
                name=name.replace('-','').replace('&','').replace('acute;','')
                furl= 'http://movie25.com/'+url
                main.addInfo(name+'('+year+')[COLOR blue] Views: '+views+'[/COLOR] [COLOR red]Votes: '+votes+'[/COLOR] [COLOR green]Rating: '+rating+'[/COLOR]',furl,3,thumb,genre,year)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False
        dialogWait.close()
        del dialogWait
        matchx=re.compile('http://www.movie25.com/search.php.+?page=(.+?)&year=(.+?)').findall(murl)
        if len(matchx)>0:
                durl = murl + '/'
                paginate=re.compile('http://www.movie25.com/search.php.+?page=(.+?)&year=(.+?)/').findall(durl)
                for page, yearb in paginate:
                        pgs = int(page)+1
                        jurl='http://www.movie25.com/search.php?page='+str(pgs)+'&year='+str(yearb)
                main.addDir('[COLOR red]Home[/COLOR]','',0,"%s/art/home.png"%selfAddon.getAddonInfo("path"))
                main.addDir('[COLOR red]Enter Page #[/COLOR]',murl,208,"%s/art/gotopage.png"%selfAddon.getAddonInfo("path"))
                main.addDir('[COLOR blue]Page '+str(pgs)+'[/COLOR]',jurl,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
                xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
                main.VIEWS()                
        else:
                durl = murl + '/'
                paginate=re.compile('http://www.movie25.com/search.php.+?page=(.+?)&key=(.+?)/').findall(durl)
                for page, search in paginate:
                        pgs = int(page)+1
                        jurl='http://www.movie25.com/search.php?page='+str(pgs)+'&key='+str(search)
                main.addDir('[COLOR red]Home[/COLOR]','',0,"%s/art/home.png"%selfAddon.getAddonInfo("path"))
                main.addDir('[COLOR blue]Page '+str(pgs)+'[/COLOR]',jurl,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        




def VIDEOLINKS(name,url):
        link=main.OPENURL(url)
        qual = re.compile('<h1 >Links - Quality\n              \n              (.+?) <a name="link"></a> </h1>').findall(link)
        quality=str(qual)
        quality=quality.replace("'","")
        name  = name.split(' Views:')[0]
        putlocker=re.compile('<li class=link_name>putlocker</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(putlocker) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Putlocker[/COLOR]",url,11,"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"))
        if len(putlocker) == 0:
                putlocker=re.compile("javascript:window.open.+?'http://movie25.com/redirect.php.?url=http://www.putlocker.com/file/.+?',").findall(link)
                if len(putlocker) > 0:
                        main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Putlocker[/COLOR]",url,11,"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"))
        sockshare=re.compile('<li class=link_name>sockshare</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(sockshare) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Sockshare[/COLOR]",url,22,"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"))
        if len(sockshare) == 0:
                sockshare=re.compile("javascript:window.open.+?'http://movie25.com/redirect.php.?url=http://www.sockshare.com/file/.+?',").findall(link)
                if len(sockshare) > 0:
                        main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Sockshare[/COLOR]",url,22,"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"))
        nowvideo=re.compile('<li class=link_name>nowvideo</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(nowvideo) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Nowvideo[/COLOR]",url,24,"%s/art/hosts/nowvideo.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/nowvideo.png"%selfAddon.getAddonInfo("path"))
        oeupload=re.compile('<li class=link_name>180upload</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(oeupload) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : 180upload[/COLOR]",url,12,"%s/art/hosts/180upload.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/180upload.png"%selfAddon.getAddonInfo("path"))
        filenuke=re.compile('<li class=link_name>filenuke</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(filenuke) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Filenuke[/COLOR]",url,13,"%s/art/hosts/filenuke.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/filenuke.png"%selfAddon.getAddonInfo("path"))
        flashx=re.compile('<li class=link_name>flashx</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(flashx) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Flashx[/COLOR]",url,15,"%s/art/hosts/flashx.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/flashx.png"%selfAddon.getAddonInfo("path"))
        novamov=re.compile('<li class=link_name>novamov</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(novamov) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Novamov[/COLOR]",url,16,"%s/art/hosts/novamov.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/novamov.png"%selfAddon.getAddonInfo("path"))
        gorillavid=re.compile('<li class=link_name>gorillavid</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(gorillavid) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Gorillavid[/COLOR]",url,148,"%s/art/hosts/gorillavid.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/gorillavid.png"%selfAddon.getAddonInfo("path"))
        divxstage=re.compile('<li class=link_name>divxstage</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(divxstage) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Divxstage[/COLOR]",url,146,"%s/art/hosts/divxstage.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/divxstage.png"%selfAddon.getAddonInfo("path"))
        movshare=re.compile('<li class=link_name>movshare</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(movshare) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Movshare[/COLOR]",url,145,"%s/art/hosts/movshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movshare.png"%selfAddon.getAddonInfo("path"))
        sharesix=re.compile('<li class=link_name>sharesix</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(sharesix) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Sharesix[/COLOR]",url,147,"%s/art/hosts/sharesix.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/sharesix.png"%selfAddon.getAddonInfo("path"))
        movpod=re.compile('<li class=link_name>movpod</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(movpod) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Movpod[/COLOR]",url,150,"%s/art/hosts/movpod.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movpod.png"%selfAddon.getAddonInfo("path"))
        daclips=re.compile('<li class=link_name>daclips</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(daclips) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Daclips[/COLOR]",url,151,"%s/art/hosts/daclips.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/daclips.png"%selfAddon.getAddonInfo("path"))
        videoweed=re.compile('<li class=link_name>videoweed</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(videoweed) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Videoweed[/COLOR]",url,152,"%s/art/hosts/videoweed.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/videoweed.png"%selfAddon.getAddonInfo("path"))
        played=re.compile('<li class=link_name>played</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(played) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Played[/COLOR]",url,157,"%s/art/hosts/played.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/played.png"%selfAddon.getAddonInfo("path"))
        movdivx=re.compile('<li class=link_name>movdivx</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(movdivx) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : MovDivx[/COLOR]",url,153,"%s/art/hosts/movdivx.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movdivx.png"%selfAddon.getAddonInfo("path"))
        movreel=re.compile('<li class=link_name>movreel</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(movreel) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Movreel[/COLOR]",url,154,"%s/art/hosts/movreel.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movreel.png"%selfAddon.getAddonInfo("path"))
        billionuploads=re.compile('<li class=link_name>billionuploads</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(billionuploads) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : BillionUploads[/COLOR]",url,155,"%s/art/hosts/billionuploads.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/billionuploads.png"%selfAddon.getAddonInfo("path"))
        uploadc=re.compile('<li class=link_name>uploadc</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(uploadc) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Uploadc[/COLOR]",url,17,"%s/art/hosts/uploadc.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/uploadc.png"%selfAddon.getAddonInfo("path"))
        xvidstage=re.compile('<li class=link_name>xvidstage</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(xvidstage) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Xvidstage[/COLOR]",url,18,"%s/art/hosts/xvidstage.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/xvidstage.png"%selfAddon.getAddonInfo("path"))        
        zooupload=re.compile('<li class=link_name>zooupload</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(zooupload) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Zooupload[/COLOR]",url,19,"%s/art/hosts/zooupload.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/zooupload.png"%selfAddon.getAddonInfo("path"))
        zalaa=re.compile('<li class=link_name>zalaa</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(zalaa) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Zalaa[/COLOR]",url,20,"%s/art/hosts/zalaa.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/zalaa.png"%selfAddon.getAddonInfo("path"))
        vidxden=re.compile('<li class=link_name>vidxden</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(vidxden) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Vidxden[/COLOR]",url,21,"%s/art/hosts/vidxden.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/vidxden.png"%selfAddon.getAddonInfo("path"))
        vidbux=re.compile('<li class=link_name>vidbux</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        if len(vidbux) > 0:
                main.addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Vidbux[/COLOR]",url,14,"%s/art/hosts/vidbux.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/vidbux.png"%selfAddon.getAddonInfo("path"))

def PUTLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        putlocker=re.compile('<li class=link_name>putlocker</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in putlocker:
                main.addDown(name,url,5,"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"))
        if len(putlocker) == 0:
                putlocker=re.compile("""javascript:window.open.+?'http://movie25.com/redirect.php.?url=(.+?)','.+?',.+?>(.+?)</a></span>""").findall(link)
                for url,part in putlocker:
                        match=re.compile("putlocker").findall(url)
                        if len(match) > 0:
                                main.addDown(name+"  [COLOR red]Part:"+part+"[/COLOR]",url,171,"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"))
def SOCKLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        sockshare=re.compile('<li class=link_name>sockshare</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in sockshare:
                main.addDown(name,url,5,"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"))
        if len(sockshare) == 0:
                sockshare=re.compile("""javascript:window.open.+?'http://movie25.com/redirect.php.?url=(.+?)','.+?',.+?>(.+?)</a></span>""").findall(link)
                for url,part in sockshare:
                        match=re.compile("sockshare").findall(url)
                        if len(match) > 0:
                                main.addDown(name+"  [COLOR red]Part:"+part+"[/COLOR]",url,171,"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"))
def NOWLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        nowvideo=re.compile('<li class=link_name>nowvideo</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in nowvideo:
                main.addDown(name,url,5,"%s/art/nowvideo.png"%selfAddon.getAddonInfo("path"),"%s/art/nowvideo.png"%selfAddon.getAddonInfo("path"))

def OELINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        oeupload=re.compile('<li class=link_name>180upload</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in oeupload:
                main.addDown(name,url,5,"%s/art/hosts/180upload.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/180upload.png"%selfAddon.getAddonInfo("path"))
def FNLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        filenuke=re.compile('<li class=link_name>filenuke</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in filenuke:
                main.addDown(name,url,5,"%s/art/hosts/filenuke.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/filenuke.png"%selfAddon.getAddonInfo("path"))
def FLALINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        flashx=re.compile('<li class=link_name>flashx</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in flashx:
                main.addDown(name,url,5,"%s/art/hosts/flashx.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/flashx.png"%selfAddon.getAddonInfo("path"))
def VIDLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        vidbux=re.compile('<li class=link_name>vidbux</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in vidbux:
                main.addDown(name,url,5,"%s/art/hosts/vidbux.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/vidbux.png"%selfAddon.getAddonInfo("path"))
def NOVLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        novamov=re.compile('<li class=link_name>novamov</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in novamov:
                main.addDown(name,url,5,"%s/art/hosts/novamov.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/novamov.png"%selfAddon.getAddonInfo("path"))
def UPLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        uploadc=re.compile('<li class=link_name>uploadc</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in uploadc:
                main.addDown(name,url,5,"%s/art/hosts/uploadc.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/uploadc.png"%selfAddon.getAddonInfo("path"))
def XVLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        xvidstage=re.compile('<li class=link_name>xvidstage</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in xvidstage:
                main.addDown(name,url,5,"%s/art/hosts/xvidstage.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/xvidstage.png"%selfAddon.getAddonInfo("path"))
def ZOOLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        zooupload=re.compile('<li class=link_name>zooupload</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in zooupload:
                main.addDown(name,url,5,"%s/art/hosts/zooupload.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/zooupload.png"%selfAddon.getAddonInfo("path"))
def ZALINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        zalaa=re.compile('<li class=link_name>zalaa</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in zalaa:
                main.addDown(name,url,5,"%s/art/hosts/zalaa.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/zalaa.png"%selfAddon.getAddonInfo("path"))
def VIDXLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        vidxden=re.compile('<li class=link_name>vidxden</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in vidxden:
                main.addDown(name,url,5,"%s/art/hosts/vidxden.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/vidxden.png"%selfAddon.getAddonInfo("path"))

def PLAYEDLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        played=re.compile('<li class=link_name>played</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in played:
                main.addDown(name,url,5,"%s/art/hosts/played.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/played.png"%selfAddon.getAddonInfo("path"))

def MOVSHLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        moveshare=re.compile('<li class=link_name>moveshare</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in moveshare:
                main.addDown(name,url,5,"%s/art/hosts/moveshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/moveshare.png"%selfAddon.getAddonInfo("path"))
def DIVXSLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        divxstage=re.compile('<li class=link_name>divxstage</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in divxstage:
                main.addDown(name,url,5,"%s/art/divxstage.png"%selfAddon.getAddonInfo("path"),"%s/art/divxstage.png"%selfAddon.getAddonInfo("path"))
def SSIXLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        sharesix=re.compile('<li class=link_name>sharesix</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in sharesix:
                main.addDown(name,url,5,"%s/art/hosts/sharesix.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/sharesix.png"%selfAddon.getAddonInfo("path"))
def GORLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        gorillavid=re.compile('<li class=link_name>gorillavid</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in gorillavid:
                main.addDown(name,url,5,"%s/art/hosts/gorillavid.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/gorillavid.png"%selfAddon.getAddonInfo("path"))
def MOVPLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        movpod=re.compile('<li class=link_name>movpod</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in movpod:
                main.addDown(name,url,5,"%s/art/hosts/movpod.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movpod.png"%selfAddon.getAddonInfo("path"))
def DACLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        daclips=re.compile('<li class=link_name>daclips</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in daclips:
                main.addDown(name,url,5,"%s/art/hosts/daclips.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/daclips.png"%selfAddon.getAddonInfo("path"))
def VWEEDLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        videoweed=re.compile('<li class=link_name>videoweed</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in videoweed:
                main.addDown(name,url,5,"%s/art/hosts/Videoweed.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/Videoweed.png"%selfAddon.getAddonInfo("path"))
def MOVDLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        movdivx=re.compile('<li class=link_name>movdivx</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in movdivx:
                main.addDown(name,url,5,"%s/art/hosts/movdivx.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movdivx.png"%selfAddon.getAddonInfo("path"))
def MOVRLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        movreel=re.compile('<li class=link_name>movreel</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in movreel:
                main.addDown(name,url,5,"%s/art/hosts/movreel.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movreel.png"%selfAddon.getAddonInfo("path"))
def BUPLOADSLINKS(name,url):
        link=main.OPENURL(url)
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        billionuploads=re.compile('<li class=link_name>billionuploads</li><li class=".+?"><span><a href=(.+?) target=".+?">').findall(link)
        for url in billionuploads:
                main.addDown(name,url,5,"%s/art/hosts/billionuploads.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/billionuploads.png"%selfAddon.getAddonInfo("path"))




def PLAY(name,murl):
        main.GA("Movie25-Movie","Watched")
        ok=True
        name=name.replace('[DVD]','').replace('[TS]','').replace('[TC]','').replace('[CAM]','').replace('[SCREENER]','').replace('[COLOR blue]','').replace('[COLOR red]','').replace('[/COLOR]','')
        name=name.replace(' : Gorillavid','').replace(' : Divxstage','').replace(' : Movshare','').replace(' : Sharesix','').replace(' : Movpod','').replace(' : Daclips','').replace(' : Videoweed','')
        name=name.replace(' : Played','').replace(' : MovDivx','').replace(' : Movreel','').replace(' : BillionUploads','').replace(' : Putlocker','').replace(' : Sockshare','').replace(' : Nowvideo','').replace(' : 180upload','').replace(' : Filenuke','').replace(' : Flashx','').replace(' : Novamov','').replace(' : Uploadc','').replace(' : Xvidstage','').replace(' : Zooupload','').replace(' : Zalaa','').replace(' : Vidxden','').replace(' : Vidbux','')
        name=name.replace(' 720p BRRip','').replace(' 720p HDRip','').replace(' 720p WEBRip','').replace(' 720p BluRay','')
        name=name.replace('  Part:1','')
        name  = name.split(' Views:')[0]
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
        link=main.OPENURL(murl)
        match=re.compile("Javascript:location.?href=.+?'(.+?)\'").findall(link)
        for murl in match:
            print murl
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

def PLAYB(name,murl):
        main.GA("Movie25-Movie","Watched")
        ok=True
        name=name.replace('[DVD]','').replace('[TS]','').replace('[TC]','').replace('[CAM]','').replace('[SCREENER]','').replace('[COLOR blue]','').replace('[COLOR red]','').replace('[/COLOR]','')
        name=name.replace(' : Gorillavid','').replace(' : Divxstage','').replace(' : Movshare','').replace(' : Sharesix','').replace(' : Movpod','').replace(' : Daclips','').replace(' : Videoweed','')
        name=name.replace(' : Played','').replace(' : MovDivx','').replace(' : Movreel','').replace(' : BillionUploads','').replace(' : Putlocker','').replace(' : Sockshare','').replace(' : Nowvideo','').replace(' : 180upload','').replace(' : Filenuke','').replace(' : Flashx','').replace(' : Novamov','').replace(' : Uploadc','').replace(' : Xvidstage','').replace(' : Zooupload','').replace(' : Zalaa','').replace(' : Vidxden','').replace(' : Vidbux','')
        name=name.replace(' 720p BRRip','').replace(' 720p HDRip','').replace(' 720p WEBRip','').replace(' 720p BluRay','')
        name=name.replace('  Part:1','').replace('  Part:2','').replace('  Part:3','').replace('  Part:4','')
        namelen=len(name)
        name  = name.split(' Views:')[0]
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
