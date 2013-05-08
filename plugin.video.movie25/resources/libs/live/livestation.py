import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def LivestationList(murl):
        main.GA("Live","Livestation")
        link=main.OPENURL(murl)
        main.addLink('BBC News','http://akamedia2.lsops.net/live/bbcworld1_en.smil/playlist.m3u8','http://beta.cdn.livestation.com/uploads/channel/ident/10/medium_bbcworld_en.jpg')
        main.addLink('CNN News','http://akamedia2.lsops.net/live/cnn_en.smil/playlist.m3u8','http://beta.cdn.livestation.com/uploads/channel/ident/84/medium_cnn.jpeg')
        main.addLink('Euronews English','http://akamedia10.lsops.net/live/smil:euronews_en.smil/playlist.m3u8','http://beta.cdn.livestation.com/uploads/channel/ident/1/medium_euronews.jpg')
        main.addLink('Euronews Arabic','http://akamedia10.lsops.net/live/smil:euronews_ar.smil/playlist.m3u8','http://beta.cdn.livestation.com/uploads/channel/ident/1/medium_euronews.jpg')
        match=re.compile('<a href="(.+?)"><img alt=".+?" src="(.+?)" /></a>\n</div>\n<h3>\n<a href=".+?">(.+?)</a>').findall(link)
        for url,thumb,name in match:
                if name=='FRANCE 24' or name=='RT':
                         main.addDir(name,'http://mobile.livestation.com'+url,117,thumb)
                        
                else:
                        main.addPlay(name,'http://mobile.livestation.com'+url,117,thumb)
                       


def LivestationLink(mname,murl):
        link=main.OPENURL(murl)
        link=link.replace('href="/en/sessions/new','').replace('href="/en/contacts/new">','').replace('href="/redirect?locale=en">','')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        if len(match)>1:
            for url, name in match:
                main.addPlay(name,'http://mobile.livestation.com'+url,118,'')
        else:
            LivestationLink2(mname,murl)
            
def LivestationLink2(mname,murl):
        main.GA("Livestation-"+mname,"Watched")
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Playing Link,4000)")
        link=main.OPENURL(murl)
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        rtmp= re.compile('"streamer":"(.+?)"').findall(link)
        match= re.compile('"file":".+?".+?"file":"([^<]+)high.sdp"').findall(link)
        if len(match)>0 and len(rtmp)>0:
            for fid in match[0:1]:
                stream_url = rtmp[0]+' playpath='+fid+'high.sdp swfUrl=http://beta.cdn.livestation.com/player/5.10/livestation-player.swf pageUrl='+murl
        else:
            match3= re.compile('<source src="(.+?)" type="video/mp4"/>').findall(link)
            if len(match3)>0:
                for vid in match3:
                    match2= re.compile('akamedia').findall(vid)
                    if len(match2)>0:
                        stream_url =vid
                    else:
                        stream_url =vid
            else:
                fid= re.compile('"file":"(.+?).sdp"').findall(link)
                stream_url = rtmp[0]+' playpath='+fid[0]+'.sdp swfUrl=http://beta.cdn.livestation.com/player/5.10/livestation-player.swf pageUrl='+murl      
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
