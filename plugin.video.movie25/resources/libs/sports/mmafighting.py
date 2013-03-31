import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def MMAFList(murl):
        main.GA("MMA","MMA-Fighting")
        i=0
        if murl=='http://www.mmafighting.com/videos':
            
            thumblist=[]
            link=main.OPENURL(murl)
            thum = re.compile('load" data-original="(.+?)" src="').findall(link)
            for thumb in thum:
                thumblist.append(thumb)
            match = re.compile('      </div>\n      <h2>\n        <a href="([^<]+)">([^<]+)</a>').findall(link)
            for url, name in match:
                main.addPlay(name,url,114,thumblist[i])
                i=i+1
            main.addDir('Next','http://www.mmafighting.com/videos/archives',113,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        else:
            thumblist=[]
            link=main.OPENURL(murl)
            thum = re.compile('load" data-original="(.+?)" src="').findall(link)
            for thumb in thum:
                thumblist.append(thumb)
            match = re.compile('      </div>\n      <h2>\n        <a href="([^<]+)">([^<]+)</a>').findall(link)
            for url, name in match:
                main.addPlay(name,url,114,thumblist[i])
                i=i+1
            match2 = re.compile('<h3><a href="([^<]+)">([^<]+)</a></h3>').findall(link)
            for url, name in match2:
                main.addPlay(name,url,114,'http://cdn3.sbnation.com/uploads/branded_hub/sbnu_logo_minimal/395/large_mmafighting.com.minimal.png')
            paginate = re.compile('<a href="([^<]+)" rel="next">Next</a>').findall(link)
            if len(paginate)>0:
                main.addDir('Next',paginate[0],113,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        main.VIEWSB()

def MMAFLink(mname,murl):
    main.GA("MMA-Fighting","Watched")
    link=main.OPENURL(murl)
    ok=True
    match=re.compile('content="https://player.ooyala.com/tframe.html.?ec=(.+?)&pbid=.+?"').findall(link)
    if len(match)>0:
        desci=re.compile('<meta property="og:description" content="(.+?)" />').findall(link)
        if len(desci)>0:
            desc=desci[0]
        else:
            desc=''
        thumbi=re.compile('<meta property="og:image" content="(.+?)" />').findall(link)
        if len(thumbi)>0:
            thumb=thumbi[0]
        else:
            thumb=''
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        durl='http://player.ooyala.com/player/ipad/'+match[0]+'.m3u8'
        link2=main.OPENURL(durl)
        match=re.compile('http://(.+?).m3u8').findall(link2)
        if len(match)==0:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Played,5000)")
        else:
            if selfAddon.getSetting("vice-qua") == "0":
                try:
                    stream_url = 'http://'+match[len(match)-1]+'.m3u8'
                except:
                    stream_url = 'http://'+match[0]+'.m3u8'
            elif selfAddon.getSetting("vice-qua") == "1":
                try:
                    stream_url = 'http://'+match[0]+'.m3u8'
                except:
                    stream_url = 'http://'+match[2]+'.m3u8'
            else:
                try:
                    stream_url = 'http://'+match[2]+'.m3u8'
                except:
                    stream_url = 'http://'+match[0]+'.m3u8'
            listitem = xbmcgui.ListItem(mname, thumbnailImage= thumb)
            listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
            playlist.add(stream_url,listitem)
            xbmcPlayer = xbmc.Player()
            xbmcPlayer.play(playlist)
            return ok
    else:
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        match=re.compile('src="http://www.youtube.com/embed/(.+?)"').findall(link)
        if len(match)>0:
            url='http://www.youtube.com/watch?v='+match[0]
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
        
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Found,5000)")
