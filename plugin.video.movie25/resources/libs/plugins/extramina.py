#-*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def MAINEXTRA():
        main.addDirb('Search','extra',535,"%s/art/wfs/searchex.png"%selfAddon.getAddonInfo("path"),"%s/art/blobfish.jpg"%selfAddon.getAddonInfo("path"))
        #main.addDirb('A-Z','http://seriesgate.tv/',538,"%s/art/wfs/azex.png"%selfAddon.getAddonInfo("path"),"%s/art/blobfish.jpg"%selfAddon.getAddonInfo("path"))
        main.addDirb('Recent Posts','http://www.extraminamovies.in/',532,"%s/art/wfs/recentex.png"%selfAddon.getAddonInfo("path"),"%s/art/blobfish.jpg"%selfAddon.getAddonInfo("path"))
        #main.addDirb('Latest Releases','latest',532,"%s/art/wfs/latestex.png"%selfAddon.getAddonInfo("path"),"%s/art/blobfish.jpg"%selfAddon.getAddonInfo("path"))
        main.addDirb('Genre','http://www.extraminamovies.in/',533,"%s/art/wfs/genreex.png"%selfAddon.getAddonInfo("path"),"%s/art/blobfish.jpg"%selfAddon.getAddonInfo("path"))
        main.GA("Plugin","Extramina")
        main.VIEWSB()
        
def LISTEXrecent(murl):     
        if murl=='latest':
            url='http://www.extraminamovies.in/'
            link=main.OPENURL(url)
            match= re.compile('custom menu-item-.+?"><a href="(.+?)">(.+?)</a></li>').findall(link)
            for url,name in match:
                main.addPlay(name,url,536,'')
        else:
            link=main.OPENURL(murl)
            link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
            match=re.compile('<a itemprop="url" href="(.+?)" rel=".+?" title="Permanent Link to (.+?)"><img itemprop="thumbnailUrl" alt=".+?" class="smallposter" src="(.+?)"></a>.+?<span itemprop="description">(.+?)</span>').findall(link)
            if len(match)==0:
                match = re.compile('<h1 class="post-title"><a href="([^<]+)" rel=".+?" title=".+?">([^<]+)</a></h1><img style=.+? src="(.+?)">(.+?)<div').findall(link)
            for url, name, thumb,desc in match:
                main.addSport(name,url,536,thumb,desc,'','')
            paginate = re.compile("<a href='([^<]+)' class='nextpostslink'>»</a>").findall(link)
            if len(paginate)>0:
                main.addDir('Next',paginate[0],532,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        main.GA("Extramina","Recent")

def LISTEXgenre(murl):     
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc2\xa0','')
        match = re.compile('title="Permanent Link to (.+?)">.+?</a></h1><a href="(.+?)" rel=".+?" title=".+?"><img alt=".+?" class=".+?" src="(.+?)"></a><a title=".+?" href=".+?" target=".+?" href=".+?" target=".+?" rel=".+?".+?</a><br/>(.+?)<div class="post-info">').findall(link)
        for  name,url, thumb,desc in match:
                main.addSport(name,url,536,thumb,desc,'','')
        paginate = re.compile("<a href='([^<]+)' class='nextpostslink'>»</a>").findall(link)
        if len(paginate)>0:
                main.addDir('Next',paginate[0],531,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        main.GA("Extramina","Recent")

def GENREEXTRA(murl):
        main.addDir('Action','http://www.extraminamovies.in/category/action-movies/',531,"%s/art/wfs/act.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Adventure','http://www.extraminamovies.in/category/adventure-movies/',531,"%s/art/wfs/adv.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Animation','http://www.extraminamovies.in/category/animation-movies/',531,"%s/art/wfs/ani.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Biography','http://www.extraminamovies.in/category/biography-movies/',531,"%s/art/wfs/bio.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Bollywood','http://www.extraminamovies.in/category/bollywood-movies/',531,"%s/art/wfs/bollyw.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Classics','http://www.extraminamovies.in/category/classic-movies/',531,"%s/art/wfs/class.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Comedy','http://www.extraminamovies.in/category/comedy-movies/',531,"%s/art/wfs/com.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Crime','http://www.extraminamovies.in/category/crime-movies/',531,"%s/art/wfs/cri.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Documentary','http://www.extraminamovies.in/category/documentary-movies/',531,"%s/art/wfs/doc.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Drama','http://www.extraminamovies.in/category/drama-movies/',531,"%s/art/wfs/dra.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Family','http://www.extraminamovies.in/category/family-movies/',531,"%s/art/wfs/fam.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Fantasy','http://www.extraminamovies.in/category/fantasy-movies/',531,"%s/art/wfs/fan.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Foreign','http://www.extraminamovies.in/category/foreign-movies/',531,"%s/art/wfs/foriegn.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Horror','http://www.extraminamovies.in/category/horror-movies/',531,"%s/art/wfs/hor.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Music','http://www.extraminamovies.in/category/music-movies/',531,"%s/art/wfs/mus.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Mystery','http://www.extraminamovies.in/category/mystery-movies/',531,"%s/art/wfs/mys.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Romance','http://www.extraminamovies.in/category/romance-movies/',531,"%s/art/wfs/rom.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Sci-Fi','http://www.extraminamovies.in/category/scifi-movies/',531,"%s/art/wfs/sci.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Sport','http://www.extraminamovies.in/category/sport-movies/',531,"%s/art/wfs/spo.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Thriller','http://www.extraminamovies.in/category/thriller-movies/',531,"%s/art/wfs/thr.png"%selfAddon.getAddonInfo("path"))
        main.addDir('War','http://www.extraminamovies.in/category/war-movies/',531,"%s/art/wfs/war.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Western','http://www.extraminamovies.in/category/western-movies/',531,"%s/art/wfs/wes.png"%selfAddon.getAddonInfo("path"))
        main.GA("Extramina","Genre")
        main.VIEWSB()

def AtoZEXTRA():
        main.addDir('#','http://www.extraminamovies.in/list-of-movies/?pgno=293#char_22',531,"%s/art/wfs/pound.png"%selfAddon.getAddonInfo("path"))
        main.addDir('0-9','http://www.extraminamovies.in/list-of-movies/?pgno=1#char_31',531,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
        main.addDir('A','http://www.extraminamovies.in/list-of-movies/?pgno=6#char_41',531,"%s/art/wfs/A.png"%selfAddon.getAddonInfo("path"))
        main.addDir('B','http://www.extraminamovies.in/list-of-movies/?pgno=24#char_42',531,"%s/art/wfs/B.png"%selfAddon.getAddonInfo("path"))
        main.addDir('C','http://www.extraminamovies.in/list-of-movies/?pgno=44#char_43',531,"%s/art/wfs/C.png"%selfAddon.getAddonInfo("path"))
        main.addDir('D','http://www.extraminamovies.in/list-of-movies/?pgno=60#char_44',531,"%s/art/wfs/D.png"%selfAddon.getAddonInfo("path"))
        main.addDir('E','http://www.extraminamovies.in/list-of-movies/?pgno=75#char_45',531,"%s/art/wfs/E.png"%selfAddon.getAddonInfo("path"))
        main.addDir('F','http://www.extraminamovies.in/list-of-movies/?pgno=81#char_46',531,"%s/art/wfs/F.png"%selfAddon.getAddonInfo("path"))
        main.addDir('G','http://www.extraminamovies.in/list-of-movies/?pgno=92#char_47',531,"%s/art/wfs/G.png"%selfAddon.getAddonInfo("path"))
        main.addDir('H','http://www.extraminamovies.in/list-of-movies/?pgno=99#char_48',531,"%s/art/wfs/H.png"%selfAddon.getAddonInfo("path"))
        main.addDir('I','http://www.extraminamovies.in/list-of-movies/?pgno=112#char_49',531,"%s/art/wfs/I.png"%selfAddon.getAddonInfo("path"))
        main.addDir('J','http://www.extraminamovies.in/list-of-movies/?pgno=120#char_4a',531,"%s/art/wfs/J.png"%selfAddon.getAddonInfo("path"))
        main.addDir('K','http://www.extraminamovies.in/list-of-movies/?pgno=125#char_4b',531,"%s/art/wfs/K.png"%selfAddon.getAddonInfo("path"))
        main.addDir('L','http://www.extraminamovies.in/list-of-movies/?pgno=130#char_4c',531,"%s/art/wfs/L.png"%selfAddon.getAddonInfo("path"))
        main.addDir('M','http://www.extraminamovies.in/list-of-movies/?pgno=141#char_4d',531,"%s/art/wfs/M.png"%selfAddon.getAddonInfo("path"))
        main.addDir('N','http://www.extraminamovies.in/list-of-movies/?pgno=156#char_4e',531,"%s/art/wfs/N.png"%selfAddon.getAddonInfo("path"))
        main.addDir('O','http://www.extraminamovies.in/list-of-movies/?pgno=162#char_4f',531,"%s/art/wfs/O.png"%selfAddon.getAddonInfo("path"))
        main.addDir('P','http://www.extraminamovies.in/list-of-movies/?pgno=166#char_50',531,"%s/art/wfs/P.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Q','http://www.extraminamovies.in/list-of-movies/?pgno=177#char_51',531,"%s/art/wfs/Q.png"%selfAddon.getAddonInfo("path"))
        main.addDir('R','http://www.extraminamovies.in/list-of-movies/?pgno=178#char_52',531,"%s/art/wfs/R.png"%selfAddon.getAddonInfo("path"))
        main.addDir('S','http://www.extraminamovies.in/list-of-movies/?pgno=188#char_53',531,"%s/art/wfs/S.png"%selfAddon.getAddonInfo("path"))
        main.addDir('T','http://www.extraminamovies.in/list-of-movies/?pgno=214#char_54',531,"%s/art/wfs/T.png"%selfAddon.getAddonInfo("path"))
        main.addDir('U','http://www.extraminamovies.in/list-of-movies/?pgno=273#char_55',531,"%s/art/wfs/U.png"%selfAddon.getAddonInfo("path"))
        main.addDir('V','http://www.extraminamovies.in/list-of-movies/?pgno=278#char_56',531,"%s/art/wfs/V.png"%selfAddon.getAddonInfo("path"))
        main.addDir('W','http://www.extraminamovies.in/list-of-movies/?pgno=279#char_57',531,"%s/art/wfs/W.png"%selfAddon.getAddonInfo("path"))
        main.addDir('X','http://www.extraminamovies.in/list-of-movies/?pgno=289#char_58',531,"%s/art/wfs/X.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Y','http://www.extraminamovies.in/list-of-movies/?pgno=289#char_59',531,"%s/art/wfs/Y.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Z','http://www.extraminamovies.in/list-of-movies/?pgno=291#char_5a',531,"%s/art/wfs/Z.png"%selfAddon.getAddonInfo("path"))
        main.GA("Extramina","AZ")
        main.VIEWSB()
        

def LISTEXAZ(mname,murl):
        if mname=='#':
            link=main.OPENURL(murl)
            match = re.compile('<li><a href="(.+?)"><span class="head">(.+?)</span></a></li>').findall(link)
            for url, name in match:
                if name[0]!='Z':
                    main.addPlay(name,url,536,'')
            paginate = re.compile('<a href="([^<]+)" title="Next page">').findall(link)
            if len(paginate)>0:
                main.addDir('Next',paginate[0],531,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        elif mname=='0-9' or mname=='Next >>':
            link=main.OPENURL(murl)
            match = re.compile('<li><a href="(.+?)"><span class="head">(.+?)</span></a></li>').findall(link)
            for url, name in match:
                    main.addPlay(name,url,536,'')
            paginate = re.compile('<a href="([^<]+)" title="Next page">').findall(link)
            if len(paginate)>0:
                main.addDir('Next >>',paginate[0],531,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        else:
            match2 = re.compile('(.+?)xoxc(.+?)xoxc').findall(murl)
            if len(match2)>0:
                for name,url in match2:
                    mname=name
                    murl=url
            link=main.OPENURL(murl)
            match = re.compile('<li><a href="(.+?)"><span class="head">(.+?)</span></a></li>').findall(link)
            for url, name in match:
                if name[0]==mname or name[0]==mname.lower():
                    main.addPlay(name,url,536,'')
            paginate = re.compile('<a href="([^<]+)" title="Next page">').findall(link)
            if len(paginate)>0 and name[0]==mname:
                main.addDir('Next',mname+'xoxc'+paginate[0]+'xoxc',531,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        main.GA("AZ","Movie-list")
def SearchhistoryEXTRA():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            url='extra'
            SEARCHEXTRA(url)
        else:
            main.addDir('Search','extra',534,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,534,thumb)
            
            
        
def SEARCHEXTRA(murl):
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
                    surl='http://www.extraminamovies.in/?s='+encode
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
                surl='http://www.extraminamovies.in/?s='+encode
        link=main.OPENURL(surl)
        link=link.replace('\xc2\xa0','').replace('\n','')
        match = re.compile('<a href="([^<]+)" rel=".+?" title=".+?">(.+?)</a>').findall(link)
        for url, name in match:
            main.addPlay(name,url,536,'')
        main.GA("Extramina","Search")
        
def VIDEOLINKSEXTRA(mname,murl):
        main.GA("Extramina","Watched")
        sources = []
        link=main.OPENURL(murl)
        ok=True
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,5000)")
        match=re.compile('class="autohyperlink" title="(.+?)" target="_blank"').findall(link)
        for url in match:
                match2=re.compile('http://(.+?)/.+?').findall(url)
                for host in match2:
                    host = host.replace('www.','')
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
                match3=re.compile('extraminamovies').findall(url)
                print len(match3)
                if len(match3)>0:
                    link2=main.OPENURL(url)
                    match = re.compile('<iframe src="(.+?)"').findall(link2)
                    for url in match:
                        match2=re.compile('http://(.+?)/.+?').findall(url)
                        for host in match2:
                            host = host.replace('www.','')
                            if host =='putlocker.com':
                                url=url.replace('embed','file')
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
