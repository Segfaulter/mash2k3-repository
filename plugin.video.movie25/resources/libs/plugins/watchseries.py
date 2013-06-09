import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def MAINWATCHS():
        main.addDir('Search','s',581,"%s/art/wfs/searchws.png"%selfAddon.getAddonInfo("path"))
        main.addDir('A-Z','s',577,"%s/art/wfs/azws.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Yesterdays Episodes','http://watchseries.lt/tvschedule/-2',573,"%s/art/wfs/yesepi.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Todays Episodes','http://watchseries.lt/tvschedule/-1',573,"%s/art/wfs/toepi2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Popular Shows','http://watchseries.lt/',580,"%s/art/wfs/popshowsws.png"%selfAddon.getAddonInfo("path"))
        main.addDir('This Weeks Popular Episodes','http://watchseries.lt/new',573,"%s/art/wfs/thisweek.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Newest Episodes Added','http://watchseries.lt/latest',573,"%s/art/wfs/newadd.png"%selfAddon.getAddonInfo("path"))
        main.addDir('By Genre','genre',583,"%s/art/wfs/genrews.png"%selfAddon.getAddonInfo("path"))
        main.GA("Plugin","Watchseries")
        main.VIEWSB()

def POPULARWATCHS(murl):
        main.GA("Watchseries","PopularShows")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<span style=".+?">.+?;</span><a href="([^<]+)" title=".+?">(.+?)</a><br/>').findall(link)
        main.addLink('[COLOR red]Most Popular Series[/COLOR]','','')
        for url, name in match[0:12]:
            main.addDir(name,'http://watchseries.lt'+url,578,'')
        main.addLink('[COLOR red]Most Popular Cartoons[/COLOR]','','')
        for url, name in match[12:24]:
            main.addDir(name,'http://watchseries.lt'+url,578,'')
        main.addLink('[COLOR red]Most Popular Documentaries[/COLOR]','','')
        for url, name in match[24:36]:
            main.addDir(name,'http://watchseries.lt'+url,578,'')
        main.addLink('[COLOR red]Most Popular Shows[/COLOR]','','')
        for url, name in match[36:48]:
            main.addDir(name,'http://watchseries.lt'+url,578,'')
        main.addLink('[COLOR red]Most Popular Sports[/COLOR]','','')
        for url, name in match[48:60]:
            main.addDir(name,'http://watchseries.lt'+url,578,'')

            
def GENREWATCHS():
        main.addDir('Action','http://watchseries.lt/genres/action',576,"%s/art/wfs/act.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Adventure','http://watchseries.lt/genres/adventure',576,"%s/art/wfs/adv.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Animation','http://watchseries.lt/genres/animation',576,"%s/art/wfs/ani.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Comedy','http://watchseries.lt/genres/comedy',576,"%s/art/wfs/com.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Crime','http://watchseries.lt/genres/crime',576,"%s/art/wfs/cri.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Documentary','http://watchseries.lt/genres/documentary',576,"%s/art/wfs/doc.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Drama','http://watchseries.lt/genres/drama',576,"%s/art/wfs/dra.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Family','http://watchseries.lt/genres/family',576,"%s/art/wfs/fam.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Fantasy','http://watchseries.lt/genres/fantasy',576,"%s/art/wfs/fan.png"%selfAddon.getAddonInfo("path"))
        main.addDir('History','http://watchseries.lt/genres/history',576,"%s/art/wfs/his.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Horror','http://watchseries.lt/genres/horror',576,"%s/art/wfs/hor.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Music','http://watchseries.lt/genres/music',576,"%s/art/wfs/mus.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Mystery','http://watchseries.lt/genres/mystery',576,"%s/art/wfs/mys.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Reality','http://watchseries.lt/genres/reality-tv',576,"%s/art/wfs/rea.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Sci-Fi','http://watchseries.lt/genres/sci-fi',576,"%s/art/wfs/sci.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Sport','http://watchseries.lt/genres/sport',576,"%s/art/wfs/spo.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Talk Show','http://watchseries.lt/genres/talk-show',576,"%s/art/wfs/tals.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Thriller','http://watchseries.lt/genres/thriller',576,"%s/art/wfs/thr.png"%selfAddon.getAddonInfo("path"))
        main.addDir('War','http://watchseries.lt/genres/war',576,"%s/art/wfs/war.png"%selfAddon.getAddonInfo("path"))
        main.GA("Watchseries","Genre")
        main.VIEWSB()

def AtoZWATCHS():
    main.addDir('0-9','http://watchseries.lt/letters/09',576,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
    for i in string.ascii_uppercase:
            main.addDir(i,'http://watchseries.lt/letters/'+i.lower()+'/list-type/a_z',576,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
    main.GA("Watchseries","A-Z")
    main.VIEWSB()

def LISTWATCHS(murl):
        main.GA("Watchseries","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a title=".+?" href="(.+?)">(.+?)</a>').findall(link)
        for url, name in match:
            main.addDir(name,'http://watchseries.lt'+url,575,'')

def LISTSHOWWATCHS(murl):
        main.GA("Watchseries","List")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a title="(.+?)" href="(.+?)">.+?<span class="epnum">(.+?)</span></a>').findall(link)
        for name, url, year in match:
            main.addDir(name,'http://watchseries.lt'+url,578,'')

def LISTWATCHSEASON(mname, murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        thumb="%s/art/folder.png"%selfAddon.getAddonInfo("path")
        match=re.compile('<a class="null" href="(.+?)">(.+?)</a>').findall(link)
        for url, name in reversed(match):
            main.addDir(mname+'   [COLOR red]'+name+'[/COLOR]','http://watchseries.lt'+url,579,thumb)


def LISTWATCHEPISODE(mname, murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace("&nbsp;&nbsp;&nbsp;"," ")
        match=re.compile('<a href="([^<]+)"><span class="" >([^<]+)</span>').findall(link)
        for url, name in reversed(match):
            main.addDir(mname+' [COLOR red]'+name+'[/COLOR]','http://watchseries.lt'+url,575,'')


def SearchhistoryWS():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='ws'
            SEARCHWS(url)
        else:
            main.addDir('Search','ws',582,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,582,thumb)
            
            


def SEARCHWS(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'ws':
            keyb = xbmc.Keyboard('', 'Search For Shows or Episodes')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://watchseries.lt/search/'+encode
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
            surl='http://watchseries.lt/search/'+encode
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('</a></td><td valign=".+?">    <a title="watch serie (.+?)" href="(.+?)">').findall(link)
        for name,url in match:
                main.addDir(name,'http://watchseries.lt'+url,578,'')
        main.GA("Watchseries","Search")


def LISTHOST(name,murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        putlocker=re.compile('<span>putlocker.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(putlocker) > 0:
            for url in putlocker:
                main.addDown2(name+"[COLOR blue] : Putlocker[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/putlocker.png"%selfAddon.getAddonInfo("path"))
        sockshare=re.compile('<span>sockshare.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(sockshare) > 0:
            for url in sockshare:
                main.addDown2(name+"[COLOR blue] : Sockshare[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/sockshare.png"%selfAddon.getAddonInfo("path"))
        nowvideo=re.compile('<span>nowvideo.co</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(nowvideo) > 0:
            for url in nowvideo:
                main.addDown2(name+"[COLOR blue] : Nowvideo[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/nowvideo.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/nowvideo.png"%selfAddon.getAddonInfo("path"))
        oeupload=re.compile('<span>180upload.com/span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(oeupload) > 0:
            for url in oeupload:
                main.addDown2(name+"[COLOR blue] : 180upload[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/180upload.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/180upload.png"%selfAddon.getAddonInfo("path"))
        filenuke=re.compile('<span>filenuke.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(filenuke) > 0:
            for url in filenuke:
                main.addDown2(name+"[COLOR blue] : Filenuke[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/filenuke.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/filenuke.png"%selfAddon.getAddonInfo("path"))
        flashx=re.compile('<span>flashx.tv</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(flashx) > 0:
            for url in flashx:
                main.addDown2(name+"[COLOR blue] : Flashx[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/flashx.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/flashx.png"%selfAddon.getAddonInfo("path"))
        novamov=re.compile('<span>novamov.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(novamov) > 0:
            for url in novamov:
                main.addDown2(name+"[COLOR blue] : Novamov[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/novamov.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/novamov.png"%selfAddon.getAddonInfo("path"))
        uploadc=re.compile('<span>uploadc.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(uploadc) > 0:
            for url in uploadc:
                main.addDown2(name+"[COLOR blue] : Uploadc[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/uploadc.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/uploadc.png"%selfAddon.getAddonInfo("path"))
        xvidstage=re.compile('<span>xvidstage.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(xvidstage) > 0:
            for url in xvidstage:
                main.addDown2(name+"[COLOR blue] : Xvidstage[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/xvidstage.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/xvidstage.png"%selfAddon.getAddonInfo("path"))
        stagevu=re.compile('<span>stagevu.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(stagevu) > 0:
            for url in stagevu:
                main.addDown2(name+"[COLOR blue] : StageVu[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/stagevu.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/stagevu.png"%selfAddon.getAddonInfo("path"))        
        gorillavid=re.compile('<span>gorillavid.in</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(gorillavid)==0:
                gorillavid=re.compile('<span>gorillavid.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(gorillavid) > 0:
            for url in gorillavid:
                main.addDown2(name+"[COLOR blue] : Gorillavid[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/gorillavid.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/gorillavid.png"%selfAddon.getAddonInfo("path"))
        divxstage=re.compile('<span>divxstage.eu</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(divxstage) > 0:
            for url in divxstage:
                main.addDown2(name+"[COLOR blue] : Divxstage[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/divxstage.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/divxstage.png"%selfAddon.getAddonInfo("path"))
        moveshare=re.compile('<span>moveshare.net</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(moveshare) > 0:
            for url in moveshare:
                main.addDown2(name+"[COLOR blue] : Moveshare[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/moveshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/moveshare.png"%selfAddon.getAddonInfo("path"))
        sharesix=re.compile('<span>sharesix.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(sharesix) > 0:
            for url in sharesix:
                main.addDown2(name+"[COLOR blue] : Sharesix[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/sharesix.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/sharesix.png"%selfAddon.getAddonInfo("path"))
        movpod=re.compile('<span>movpod.in</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(movpod)==0:
                movpod=re.compile('<span>movpod.net</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(movpod) > 0:
            for url in movpod:
                main.addDown2(name+"[COLOR blue] : Movpod[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/movpod.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movpod.png"%selfAddon.getAddonInfo("path"))
        daclips=re.compile('<span>daclips.in</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(daclips)==0:
                daclips=re.compile('<span>daclips.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(daclips) > 0:
            for url in daclips:
                main.addDown2(name+"[COLOR blue] : Daclips[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/daclips.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/daclips.png"%selfAddon.getAddonInfo("path"))
        videoweed=re.compile('<span>videoweed.es</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(videoweed) > 0:
            for url in videoweed:
                main.addDown2(name+"[COLOR blue] : Videoweed[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/videoweed.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/videoweed.png"%selfAddon.getAddonInfo("path"))        
        zooupload=re.compile('<span>zooupload.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(zooupload) > 0:
            for url in zooupload:
                main.addDown2(name+"[COLOR blue] : Zooupload[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/zooupload.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/zooupload.png"%selfAddon.getAddonInfo("path"))
        zalaa=re.compile('<span>zalaa.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(zalaa) > 0:
            for url in zalaa:
                main.addDown2(name+"[COLOR blue] : Zalaa[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/zalaa.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/zalaa.png"%selfAddon.getAddonInfo("path"))
        vidxden=re.compile('<span>vidxden.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(vidxden) > 0:
            for url in vidxden:
                main.addDown2(name+"[COLOR blue] : Vidxden[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/vidxden.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/vidxden.png"%selfAddon.getAddonInfo("path"))
        vidbux=re.compile('<span>vidbux.com</span></td><td> <a target=".+?" href="(.+?)"').findall(link)
        if len(vidbux) > 0:
            for url in vidbux:
                main.addDown2(name+"[COLOR blue] : Vidbux[/COLOR]",url+'xocx'+murl+'xocx',574,"%s/art/hosts/vidbux.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/vidbux.png"%selfAddon.getAddonInfo("path"))

def geturl(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a class="myButton" href="(.+?)">Click Here to Play</a>').findall(link)
        if len(match)==0:
                match=re.compile('<a class="myButton" href="(.+?)">Click Here to Play Part1</a><a class="myButton" href="(.+?)">Click Here to Play Part2</a>').findall(link)
                return match[0]
        else:
                return match[0]

def LINKWATCHS(mname,murl):
        main.GA("Watchseries","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        match=re.compile('(.+?)xocx(.+?)xocx').findall(murl)
        for hurl, durl in match:
                furl=geturl('http://watchseries.lt'+hurl)
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Checking Link,1500)")
        link=main.OPENURL(durl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match2=re.compile('<h1 class=".+?"><a href=".+?">.+?</a> - <a href="(.+?)" title=".+?">.+?</a>').findall(link)
        for xurl in match2:
                link2=main.OPENURL('http://watchseries.lt'+xurl)
                link2=link2.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        descr=re.compile('<b>Description :</b>(.+?)<').findall(link2)
        if len(descr)>0:
                desc=descr[0]
        else:
                desc=''
        thumbs=re.compile('<td style=".+?"><a href=".+?"><img src="(.+?)"').findall(link2)
        if len(thumbs)>0:
                thumb=thumbs[0]
        else:
                thumb=''
        genres=re.compile('<b>Genre: <a href=.+?>(.+?)</a>').findall(link2)
        if len(genres)>0:
                genre=genres[0]
        else:
                genre=''
        listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png",thumbnailImage=thumb)
        listitem.setInfo('video', {'Title': mname, 'Plot': desc, 'Genre': genre} )
        #listitem.setProperty('mimetype', 'video/x-msvideo')
        #listitem.setProperty('IsPlayable', 'true')
        media = urlresolver.HostedMediaFile(furl)
        source = media
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,4000)")
                stream_url = source.resolve()
        else:
                stream_url = False  
        playlist.add(str(stream_url),listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
