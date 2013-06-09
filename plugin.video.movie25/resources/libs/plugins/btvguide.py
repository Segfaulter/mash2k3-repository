import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def MAINBTV():
        main.addDir('Search','s',558,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
        main.addDir('A-Z','s',560,"%s/art/wfs/az.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Todays Episodes','todays',555,"%s/art/wfs/toepi.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Popular Shows','http://www.btvguide.com/shows',562,"%s/art/wfs/popshow.png"%selfAddon.getAddonInfo("path"))
        main.addDir('New Shows','http://www.btvguide.com/shows/list-type/new_shows',564,"%s/art/wfs/newshow.png"%selfAddon.getAddonInfo("path"))
        main.addDir('New Episodes (Starting from yesterdays)','http://www.btvguide.com/shows/list-type/new_episodes',565,"%s/art/wfs/newepi.png"%selfAddon.getAddonInfo("path"))
        main.addDir('By Genre','genre',566,"%s/art/wfs/bygen.png"%selfAddon.getAddonInfo("path"))
        main.addDir('By Decade','decade',566,"%s/art/wfs/bydec.png"%selfAddon.getAddonInfo("path"))
        main.addDir('By Network','network',566,"%s/art/wfs/bynet.png"%selfAddon.getAddonInfo("path"))
        main.GA("Plugin","BTV-Guide")
        main.VIEWSB()
        
def AtoZBTV():
    main.addDir('0-9','http://www.btvguide.com/shows/list-type/a_z',561,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.btvguide.com/shows/sort/'+i.lower()+'/list-type/a_z',561,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
    main.GA("BTV-Guide","A-Z")
    main.VIEWSB()

def DECADEBTV(murl):
        url ='http://www.btvguide.com/shows/list-type/a_z'
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        if murl=='decade':
            match=re.compile('<li class="filter"><a  href="/shows/decade/(.+?)">(.+?)<em>(.+?)</em></a></li>').findall(link)
            thumb="%s/art/folder.png"%selfAddon.getAddonInfo("path")
            for url, name, length in match:
                main.addDir(name+' '+length,'http://www.btvguide.com/shows/decade/'+url,561,thumb)
        elif murl=='genre':
            match=re.compile('<li class="filter"><a  href="/shows/category/(.+?)">(.+?)<em>(.+?)</em></a></li>').findall(link)
            thumb="%s/art/folder.png"%selfAddon.getAddonInfo("path")
            for url, name, length in match:
                main.addDir(name+' '+length,'http://www.btvguide.com/shows/category/'+url,561,thumb)
        elif murl=='network':
            match=re.compile('<li class="filter"><a  href="/shows/network/(.+?)">(.+?)<em>(.+?)</em></a></li>').findall(link)
            thumb="%s/art/folder.png"%selfAddon.getAddonInfo("path")
            for url, name, length in match:
                main.addDir(name+' '+length,'http://www.btvguide.com/shows/network/'+url,561,thumb)

def SearchhistoryBTV():
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='btv'
            SEARCHBTV(url)
        else:
            main.addDir('Search','btv',557,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            main.addDir('Clear History',SeaFile,128,"%s/art/cleahis.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    main.addDir(seahis,url,557,thumb)
            
            
        
def SEARCHBTV(murl):
        seapath=os.path.join(main.datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'btv':
            keyb = xbmc.Keyboard('', 'Search Tv Shows')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://www.btvguide.com/searchresults/?q='+encode
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
                surl='http://www.btvguide.com/searchresults/?q='+encode
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<a class="_image_container" href="(.+?)"><img class="lazy" data-original="(.+?)"src=".+?"alt="(.+?)".+?/></a>').findall(link)
        for url,thumb,name in match:
                main.addDir(name,url,553,thumb)
        main.GA("BTV-Guide","Search")

            
def AllShowsBTV(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<li class="show"><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url, name in match:
            main.addDir(name,url,553,'')
        paginate = re.compile('<a href="([^<]+)">&gt;</a>').findall(link)
        if len(paginate)>0:
            main.addDir('Next','http://www.btvguide.com'+paginate[0],561,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

def LISTPopBTV(murl):
    if murl=='todays':
        url='http://www.btvguide.com/shows'
        link=main.OPENURL(url)
        match=re.compile('<a href="(.+?)" class=".+?" style=".+?">\r\n\t\t\t\t\t\t\t\t\t<span class=".+?">(.+?)</span>\r\n\t\t\t\t\t\t\t\t\t<span class=".+?">(.+?)\r\n\t\t\t\t\t\t\t\t\t(.+?)</span>').findall(link)
        for url, name, seep, epiname in match:
            main.addDir(name+'  '+seep+' [COLOR red]"'+epiname+'"[/COLOR]',url,559,'')

def LISTNEWEpiBTV(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<img .+?="h(.+?)" .+?/></a></div></div><div class=".+?"><h4><a href="([^<]+)" title="([^<]+)" style=".+?"  target=".+?">([^<]+)</a><div class=".+?" style=".+?">.+?</div></h4><div class=".+?" ><span class=\'_more_less\' style=".+?"><span style=".+?">([^<]+)</span>').findall(link)
        for thumb, url, epiname, name, seep in match:
            main.addDir(name+'  '+seep+' [COLOR red]"'+epiname+'"[/COLOR]',url,559,'h'+thumb)
        paginate = re.compile('<a href="([^<]+)">&gt;</a>').findall(link)
        if len(paginate)>0:
            main.addDir('Next','http://www.btvguide.com'+paginate[0],565,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

def LISTPOPShowsBTV(murl):
        desclist=[]
        i=0
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        descr=re.compile('<span class=\'_more_less\'>([^<]+)').findall(link)
        if len(descr)>0:
            for desc in descr:
                desclist.append(desc)
        match=re.compile('<a href="([^<]+)" title="([^<]+)"><img src="([^<]+)" alt=".+?" title=".+?" width=".+?" height=".+?" />').findall(link)
        for url, name, thumb in match:
            main.addDir2(name,url,553,thumb,desclist[i])
            i=i+1
        paginate = re.compile('<a href="([^<]+)">&gt;</a>').findall(link)
        if len(paginate)>0:
            main.addDir('Next','http://www.btvguide.com'+paginate[0],562,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

def LISTNEWShowsBTV(murl):
        desclist=[]
        i=0
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        descr=re.compile('<span class=\'_more_less\'>([^<]+)').findall(link)
        if len(descr)>0:
            for desc in descr:
                desclist.append(desc)
        match=re.compile('<a href="([^<]+)" title="([^<]+)"><img src="([^<]+)" alt=".+?" title=".+?" width=".+?" height=".+?" />').findall(link)
        for url, name, thumb in match:
            main.addDir2(name,url,553,thumb,desclist[i])
            i=i+1
        paginate = re.compile('<a href="([^<]+)">&gt;</a>').findall(link)
        if len(paginate)>0:
            main.addDir('Next','http://www.btvguide.com'+paginate[0],564,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

def LISTSeasonBTV(mname,murl):
        durl=murl+'/episodes'
        link=main.OPENURL(durl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a rel="nofollow" href=".+?"><strong>([^<]+)</strong>([^<]+)</a>').findall(link)
        for seaname, epilen in match:
                furl=seaname.replace(' ','+')
                main.addDir(seaname+epilen,murl+'/season-contents/'+furl,554,'')

def LISTEpilistBTV(mname,murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('"src="http://static0.btvguide.com/images/nocoverbig.png','').replace('|','')
        match=re.compile('<img class=.+?="(.+?)".+?="(.+?) BTVGuide".+?<a class="title" href="(.+?)"').findall(link)
        for thumb, name, url in match:
                main.addDir2(name,url,559,thumb,'')
                
def GETLINKBTV(murl):
    print "oob2 "+murl
    html = net().http_GET(murl).content
    next_url = re.compile('action="(.+?)" target="_blank">').findall(html)[0]
    token = re.compile('name="btvguide_csrf_token" value="(.+?)"').findall(html)[0]
    second = net().http_POST(next_url,{'submit':'','btvguide_csrf_token':token}).content
    match=re.compile('<title>GorillaVid - Just watch it!</title>').findall(second)
    if len(match)>0:
        match=re.compile('<input type="hidden" name="id" value="(.+?)">\n<input type="hidden"').findall(second)
        if len(match)>0:
            url='http://gorillavid.in/'+match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match2=re.compile('<title>DaClips - Just watch it!</title>').findall(second)
    if len(match2)>0:
        match=re.compile('<input type="hidden" name="id" value="(.+?)">\n<input type="hidden"').findall(second)
        if len(match)>0:
            url='http://daclips.in/'+match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match3=re.compile('<title>MovPod - Just watch it!</title>').findall(second)
    if len(match3)>0:
        match=re.compile('<input type="hidden" name="id" value="(.+?)">\n<input type="hidden"').findall(second)
        if len(match)>0:
            url='http://movpod.in/'+match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match4=re.compile('DivxStage').findall(second)
    if len(match4)>0:
        match=re.compile('type=".+?" value="(.+?)" id=".+?"').findall(second)
        if len(match)>0:
            url=match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match5=re.compile('<title>VidX Den').findall(second)
    if len(match5)>0:
        match=re.compile('<input name="id" type="hidden" value="(.+?)">').findall(second)
        if len(match)>0:
            url='http://www.vidxden.com/'+match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match6=re.compile('<title>VidBux').findall(second)
    if len(match6)>0:
        match=re.compile('<input name="id" type="hidden" value="(.+?)">').findall(second)
        if len(match)>0:
            url='http://www.vidbux.com/'+match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match7=re.compile('http://vidbull.com').findall(second)
    if len(match7)>0:
        match=re.compile('<input type="hidden" name="id" value="(.+?)">\n<input type="hidden"').findall(second)
        if len(match)>0:
            url='http://vidbull.com/'+match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match8=re.compile('http://flashx.tv/favicon.ico').findall(second)
    if len(match8)>0:
        match=re.compile('<meta property="og:video" content=\'(.+?)\'>').findall(second)
        if len(match)>0:
            url=match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match9=re.compile('filenuke.com').findall(second)
    if len(match9)>0:
        match=re.compile('</span> <a href="(.+?)">.+?</a>').findall(second)
        if len(match)>0:
            url=match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match10=re.compile('<title>NowVideo - Just watch it now!</title>').findall(second)
    if len(match10)>0:
        match=re.compile('type="text" value="(.+?)">').findall(second)
        if len(match)>0:
            url=match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''
    match11=re.compile('MovShare - Reliable video hosting</title>').findall(second)
    if len(match11)>0:
        match=re.compile('id="embedtext"  value="([^<]+)">').findall(second)
        if len(match)>0:
            url=match[0]
            return url
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Removed,3000)")
            return ''


def VIDEOLINKSBTV(mname,murl):
        main.GA("BTV-GUIDE","Watched")
        murl=murl+'/watch-online'
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','')
        match=re.compile('<a class="clickfreehoney" rel="nofollow" href="(.+?)"style=".+?">.+?</span>on&nbsp;(.+?)<br/>').findall(link)
        for url,host in match:
                gorillavid=re.compile('gorillavid').findall(host)
                if len(gorillavid) > 0:
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/gorillavid.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/gorillavid.png"%selfAddon.getAddonInfo("path"))
                daclips=re.compile('daclips').findall(host)
                if len(daclips) > 0: 
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/daclips.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/daclips.png"%selfAddon.getAddonInfo("path"))
                movpod=re.compile('movpod').findall(host)
                if len(movpod) > 0:
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/movpod.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movpod.png"%selfAddon.getAddonInfo("path"))
                divxstage=re.compile('divxstage').findall(host)
                if len(divxstage) > 0: 
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/divxstage.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/divxstage.png"%selfAddon.getAddonInfo("path"))
                nowvideo=re.compile('nowvideo').findall(host)
                if len(nowvideo) > 0:
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/nowvideo.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/nowvideo.png"%selfAddon.getAddonInfo("path"))
                movshare=re.compile('movshare').findall(host)
                if len(movshare) > 0: 
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/movshare.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/movshare.png"%selfAddon.getAddonInfo("path"))
                flashx=re.compile('flashx').findall(host)
                if len(flashx) > 0:
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/flashx.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/flashx.png"%selfAddon.getAddonInfo("path"))
                filenuke=re.compile('filenuke').findall(host)
                if len(filenuke) > 0:
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/filenuke.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/filenuke.png"%selfAddon.getAddonInfo("path"))               
                vidxden=re.compile('vidxden').findall(host)
                if len(vidxden) > 0:
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/vidxden.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/vidxden.png"%selfAddon.getAddonInfo("path"))
                vidbux=re.compile('vidbux').findall(host)
                if len(vidbux) > 0: 
                    main.addPlayb(mname+' '+host,url,563,"%s/art/hosts/vidbux.png"%selfAddon.getAddonInfo("path"),"%s/art/hosts/vidbux.png"%selfAddon.getAddonInfo("path"))

def PLAYBTV(mname,murl):
        furl=GETLINKBTV(murl)
        print "final url "+furl
        ok=True
        if furl=='':
            main.addDir('','','','')
        else:
            playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playlist.clear()
            listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png",thumbnailImage='')
            #listitem.setInfo("Video", infoLabels = infoLabels)
            #listitem.setProperty('mimetype', 'video/x-msvideo')
            #listitem.setProperty('IsPlayable', 'true')
            media = urlresolver.HostedMediaFile(furl)
            source = media
            if source:
                    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                    stream_url = source.resolve()
            else:
                  stream_url = False  
            playlist.add(str(stream_url),listitem)
            xbmcPlayer = xbmc.Player()
            xbmcPlayer.play(playlist)
        return ok
