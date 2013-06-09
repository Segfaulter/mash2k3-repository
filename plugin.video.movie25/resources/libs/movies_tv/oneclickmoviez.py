import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.movie25/art/hosts', ''))


def LISTSP4(murl):
        urllist=['http://oneclickmoviez.com/category/bluray/','http://oneclickmoviez.com/category/bluray/page/2/','http://oneclickmoviez.com/category/bluray/page/3/','http://oneclickmoviez.com/category/bluray/page/4/','http://oneclickmoviez.com/category/bluray/page/5/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for xurl in urllist:
                link=main.OPENURL(xurl)
                match=re.compile('href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>\n</div>\n<div class="cover">\n<div class="entry">\n\t\t\t\t\t<p style="text-align: center;"><img class="alignnone" title="poster" src="(.+?)" ').findall(link)
                for url,name, thumb in match:
                        main.addDir(name,url,56,thumb)   
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False    
        dialogWait.close()
        del dialogWait
        main.GA("HD","Oneclickmoviez")

def getlink(url):
        link=main.OPENURL(url)
        match=re.compile("TargetUrl = \'(.+?)\'").findall(link)
        for vlink in match:
               vid = vlink
        return vid

def LINKSP4(mname,murl):
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,3000)")
        link=main.OPENURL(murl)
        ok=True
        link= link.replace('href="http://oneclickmoviez.com/dws/MEGA','')
        main.addLink("[COLOR red]For Download Options, Bring up Context Menu Over Selected Link.[/COLOR]",'','')
        match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>.+?</p>').findall(link)
        for url, host in match:
                thumb=host.lower()
                thumb = thumb.replace('www.','').replace('.in','').replace('.net','').replace('.com','').replace('.to','').replace('.org','').replace('.ch','')
                vlink = getlink(url)
                match2=re.compile('rar').findall(vlink)
                if len(match2)==0:
                        hosted_media = urlresolver.HostedMediaFile(url=vlink, title=host)
                        match2=re.compile("{'url': '(.+?)', 'host': '(.+?)', 'media_id': '.+?'}").findall(str(hosted_media))
                        for murl,name in match2:
                                main.addDown2(mname+' [COLOR blue]'+host+'[/COLOR]',murl,211,art+thumb+".png",art+thumb+".png")

        
def LINKSP4B(mname,murl):
        main.GA("Oneclickmovies","Watched")
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
