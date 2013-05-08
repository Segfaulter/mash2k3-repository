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
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for murl in urllist:
                link=main.OPENURL(murl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\xc3\xaa','e').replace('\xc3\xa0','a')
                match=re.compile('<a href="([^<]+)" title="(.+?)".+? src="(.+?)" .+?/><br />(.+?)<br />Plot:(.+?)<.+?Genre</strong>: (.+?)<br />').findall(link)
                for url,sitename,thumb,name,desc,gen in match:
                        main.addSport(name,url,134,thumb,desc,'',gen)
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
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for murl in urllist:
                link=main.OPENURL(murl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('title=".+?">([^<]+)</a></h2>.+?href=".+?<a href="(.+?)" .+?href=".+?>.+?src="(.+?)"').findall(link)
                for name,url,thumb in match:
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        main.addPlay(name,url,134,thumb)
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("TV","Oneclickwatch")




def PLAYOCW(mname,murl):
        sources=[]
        main.GA("OneclickwatchM","Watched")
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting Hosts,5000)")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<br /><a href="(.+?)">(.+?)</a><br />').findall(link)
        desc=re.compile('<.+? />Plot:(.+?)<.+? />').findall(link)
        if len(desc)>0:
                descs=desc[0]
        else:
                descs=''
        thumb=re.compile('<img alt="" src="(.+?)"').findall(link)
        if len(thumb)>0:
                thumbs=thumb[0]
        else:
               thumbs=''
        for url,host in match:
                print url
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
                listitem = xbmcgui.ListItem(mname, thumbnailImage=thumbs)
                listitem.setInfo('video', {'Title': mname, 'Plot': descs} )         
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
