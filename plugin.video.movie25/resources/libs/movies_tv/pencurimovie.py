import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def unescape(text):
        try:            
            rep = {"&nbsp;": " ",
                   "\n": "",
                   "\t": "",   
                   "%3a": ":",
                   "%3A":":",
                   "%2f":"/",
                   "%2F":"/",
                   "%3f":"?",
                   "%3F":"?",
                   "%26":"&",
                   "%3d":"=",
                   "%3D":"=",
                   "%2C":",",
                   "%2c":","
                   }
            for s, r in rep.items():
                text = text.replace(s, r)
				
            # remove html comments
            text = re.sub(r"<!--.+?-->", "", text)    
				
        except TypeError:
            pass

        return text

def LIST(murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile("""<title type='text'>([^<]+)</title><.+?>.+?div class=".+?" style=".+?".+?href="(.+?)" imageanchor=".+?" .+?href='.+?'.+?href='([^<]+).html' title='.+?'/><author>""").findall(link)
        for name,thumb,url in match:
                main.addPlay(name,url+'.html',216,thumb)
        main.GA("HD","Pencurimovie")

def LINK(mname,url):
        main.GA("Pencurimovie","Watched")
        ok=True
        namelist=[]
        urllist=[]
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        docUrl= re.compile('<iframe height=".+?" src="(.+?)" width=".+?"></iframe>').findall(link)
        if docUrl:
            link2=main.OPENURL(docUrl[0])
            match= re.compile('url_encoded_fmt_stream_map\":\"(.+?),\"').findall(link2)
            if match:
                streams_map = str(match)
                stream= re.compile('url=(.+?)&type=.+?&quality=(.+?)[,\"]{1}').findall(streams_map)
                for group1,group2 in stream:#Thanks to the-one for google-doc resolver
                    stream_url = str(group1)
                    stream_url = unescape(stream_url)
                    urllist.append(stream_url)
                    stream_qlty = str(group2.upper())
                    if (stream_qlty == 'HD720'):
                        stream_qlty = 'HD-720p'
                    elif (stream_qlty == 'LARGE'):
                        stream_qlty = 'SD-480p'
                    elif (stream_qlty == 'MEDIUM'):
                        stream_qlty = 'SD-360p'
                    namelist.append(stream_qlty)
                dialog = xbmcgui.Dialog()
                answer =dialog.select("Quality Select", namelist)
                if answer != -1:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,3000)")
                        stream_url2 = urllist[int(answer)]
                        listitem = xbmcgui.ListItem(mname)
                        playlist.add(stream_url2,listitem)
                        xbmcPlayer = xbmc.Player()
                        xbmcPlayer.play(playlist)
                return ok
        vidmUrl= re.compile('<iframe frameborder=".+?" height=".+?" scrolling=".+?" src="(.+?)" width=".+?"></iframe>').findall(link)
        if vidmUrl:
                link2=main.OPENURL(vidmUrl[0])
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,3000)")
                encodedurl=re.compile('unescape.+?"(.+?)"').findall(link2)#Thanks to j0anita for vidmega resolver
                teste=urllib.unquote(encodedurl[0])
                mega=re.compile('file: "(.+?)"').findall(teste)
                for url in mega:
                        stream_url2 = url
                        listitem = xbmcgui.ListItem(mname)
                        playlist.add(stream_url2,listitem)
                        xbmcPlayer = xbmc.Player()
                        xbmcPlayer.play(playlist)
        
        else:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Not Available,3000)")

