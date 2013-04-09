import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def iLive():
        main.addDir('General','general',120,'')
        main.addDir('Entertainment','entertainment',120,'')
        main.addDir('Sports','sports',120,'')
        main.addDir('News','news',120,'')
        main.addDir('Music','music',120,'')
        main.addDir('Animation','animation',120,'')
        main.GA("Live","iLive")
        
def iLiveList(murl):
        if murl=='general':
            try:
                urllist=['http://www.ilive.to/channels/General','http://www.ilive.to/channels/General?p=2']
            except:
                urllist=['http://www.ilive.to/channels/General']
        if murl=='entertainment':
            try:
                urllist=['http://www.ilive.to/channels/Entertainment','http://www.ilive.to/channels/Entertainment?p=2','http://www.ilive.to/channels/Entertainment?p=3','http://www.ilive.to/channels/Entertainment?p=4','http://www.ilive.to/channels/Entertainment?p=5','http://www.ilive.to/channels/Entertainment?p=6']
            except:
                urllist=['http://www.ilive.to/channels/Entertainment','http://www.ilive.to/channels/Entertainment?p=2','http://www.ilive.to/channels/Entertainment?p=3','http://www.ilive.to/channels/Entertainment?p=4','http://www.ilive.to/channels/Entertainment?p=5']
        if murl=='sports':
            try:
                urllist=['http://www.ilive.to/channels/Sport','http://www.ilive.to/channels/Sport?p=2','http://www.ilive.to/channels/Sport?p=3','http://www.ilive.to/channels/Sport?p=4']
            except:
                urllist=['http://www.ilive.to/channels/Sport','http://www.ilive.to/channels/Sport?p=2','http://www.ilive.to/channels/Sport?p=3']
        if murl=='news':
            try:
                urllist=['http://www.ilive.to/channels/News']
            except:
                urllist=['http://www.ilive.to/channels/News']
        if murl=='music':
            try:
                urllist=['http://www.ilive.to/channels/Music']
            except:
                urllist=['http://www.ilive.to/channels/Music']
        if murl=='animation':
            try:
                urllist=['http://www.ilive.to/channels/Animation']
            except:
                urllist=['http://www.ilive.to/channels/Animation']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until channel list is loaded.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading.....[/B]',remaining_display)
        for durl in urllist:
                link=main.OPENURL(durl)
                link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                match=re.compile('<img width=".+?" height=".+?" src="([^<]+)" alt=""/></noscript></a><a href="(.+?)"><strong>(.+?)</strong></a>').findall(link)
                for thumb,url,name in match:
                    if name != 'Playboy TV'or name != 'Hongkong Cat III channel 2':
                        main.addPlay(name,url,121,thumb)
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading.....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("iLive","List") 

def iLiveLink(mname,murl):
        main.GA("iLive","Watched")
        link=main.OPENURL(murl)
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('http://www.ilive.to/embed/(.+?)&width=(.+?)&height=(.+?)&autoplay=true').findall(link)
        for fid,wid,hei in match:
            pageUrl='http://www.ilive.to/embedplayer.php?width='+wid+'&height='+hei+'&channel='+fid+'&autoplay=true'
        link=main.OPENURL(pageUrl)
        playpath=re.compile("file\': \'(.+?).flv").findall(link)
        for playPath in playpath:
            stream_url = 'rtmp://142.4.216.176/edge playpath=' + playPath + " swfUrl=http://static.ilive.to/jwplayer/player_embed.swf pageUrl="+pageUrl+"live=1"
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
