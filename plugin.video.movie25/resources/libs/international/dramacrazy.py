import urllib,urllib2,re,cookielib,urlresolver,os,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def LISTINT2(name,url):
        MainUrl = "http://www.dramacrazy.net"
        urllist=['http://www.dramacrazy.net/most-recent/','http://www.dramacrazy.net/most-recent/offset/15','http://www.dramacrazy.net/most-recent/offset/30','http://www.dramacrazy.net/most-recent/offset/45','http://www.dramacrazy.net/most-recent/offset/60'
                 ,'http://www.dramacrazy.net/most-recent/offset/75','http://www.dramacrazy.net/most-recent/offset/90','http://www.dramacrazy.net/most-recent/offset/105','http://www.dramacrazy.net/most-recent/offset/120','http://www.dramacrazy.net/most-recent/offset/135'
                 ,'http://www.dramacrazy.net/most-recent/offset/150','http://www.dramacrazy.net/most-recent/offset/165','http://www.dramacrazy.net/most-recent/offset/180','http://www.dramacrazy.net/most-recent/offset/195','http://www.dramacrazy.net/most-recent/offset/210']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for murl in urllist:
                link=main.OPENURL(murl)
                match=re.compile('href="(.+?)"><img src="(.+?)" width=".+?" alt=".+?" /></a>\r\n\t\t</div>\r\n\t\t<div class=".+?">\r\n\t\t<div class=".+?">\r\n\t\t\t<h1><a href=".+?">(.+?)</a></h1>').findall(link)
                for url,thumb,name in match:
                        match=re.compile('Movie').findall(name)
                        if (len(match)>0):
                                name = name.replace('xoxix','')
                                main.addDir(name,MainUrl+url,40,thumb)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        main.GA("INT","Dramacrazy")


def LINKINT2(name,murl):
        MainUrl = "http://www.dramacrazy.net"
        sources = []
        link=main.OPENURL(murl)
        match=re.compile('<a class=".+?" href="(.+?)">(.+?)</a>\r\n\t\t\t\t\t\t\t\t<p class=".+?">.+?</p>\r\n\t\t\t\t<div class=".+?"></div>\r\n\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\t\t<div class=".+?">\r\n\t\t\t\t\t\t<div class=".+?">').findall(link)
        for url, name in match:
                url =MainUrl+url
                link=main.OPENURL(url)
                link = ''.join(link.splitlines()).replace('\t','').replace('\'','"')

                streamingLinksModule=re.compile('<!-- Small Div alternate streaming mirros -->(.+?)<!--End of alternate streaming mirrors -->').findall(link)
                streamingLinks=re.compile('<div class="row">(.+?)<div class="clear"></div></div>').findall(streamingLinksModule[0])
                for stramingLinkRow in streamingLinks:
                        parts = re.compile('<a (.+?) onclick="return encLink\("/(.+?)"\);" (.+?)>').findall(stramingLinkRow.replace(')"',');"'))
                        streamingName = re.compile('Watch(.+?)\)').findall(stramingLinkRow)
                        streamingName= str(streamingName)
                        streamingName=streamingName.replace('with English Subs ','').replace("[' ","").replace("']","").replace("Speedy Joe","VideoDorm")   
                        streamTypeName = streamingName + ')'
                        linkname=streamTypeName.replace("(","").replace(")","")
                        imagename=str(linkname)
                        main.addLink('[COLOR blue]'+linkname+' Links[/COLOR]','',selfAddon.getAddonInfo("path")+'/art/'+imagename+'.png')
                        if re.search('\(Wat\)', streamTypeName):
                                continue
                
                        matchCount = len(parts)
                        if(matchCount > 1):
                                i = 0
                                playList = ''
                                for temp1, partLink, temp2 in parts:
                                        i = i + 1
                                        print ' - PART: '+str(i)+' PART link = '+partLink
                                        partName = streamTypeName + ' - PART: '+str(i)
                                        main.addPlay(name+'  '+partName,'http://www.dramacrazy.net/' + partLink,42,selfAddon.getAddonInfo("path")+'/art/'+imagename+'.png')

def LOAD_AND_PLAY_VIDEO(url,name):
        main.GA("Dramacrazy","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        xbmc.executebuiltin("XBMC.Notification(PLease Wait!, Resolving Link,5000)")
        ok=True
        print url
        videoUrl = loadVideos(url,name,True,False)
        if videoUrl == None:
                d = xbmcgui.Dialog()
                d.ok('look',str(url),'Check other video links, This one is unplayable.')
                return False
        elif videoUrl == 'skip':
                return False				
        elif videoUrl == 'ERROR':
                return False
        listitem = xbmcgui.ListItem(name)
        playlist.add(videoUrl,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        
        return ok


def loadVideos(url,name,isRequestForURL,isRequestForPlaylist):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link = ''.join(link.splitlines()).replace('\t','').replace('\'','"')
        streamingPlayer = re.compile('document.write\(unescape\("(.+?)"\)\);').findall(link)
        #print streamingPlayer

        if(len(streamingPlayer) == 0):
        
                episodeContent = re.compile('<div class="episodeContent">(.+?)</div>').findall(link)[0]
                url = re.compile('src="(.+?)"').findall(episodeContent)[0]
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link = ''.join(link.splitlines()).replace('\t','').replace('\'','"')
                streamingPlayer = re.compile('document.write\(unescape\("(.+?)"\)\);').findall(link)
                if(len(streamingPlayer) == 0):
                        streamingPlayer = [ urllib.quote_plus(link) ]
                
        frame =  urllib.unquote_plus(streamingPlayer[0]).replace('\'','"').replace(' =','=').replace('= ','=')
        videoUrl = re.compile('config=(.+?)&amp;').findall(frame)
        if(len(videoUrl) == 0):
                videoUrl = re.compile('data="(.+?)"').findall(frame)
        if(len(videoUrl) == 0):
                videoUrl = re.compile('file=(.+?)&amp;autostart').findall(frame)
        if(len(videoUrl) == 0):
                videoUrl = re.compile('href="(.+?)"').findall(frame)
        if(len(videoUrl) == 0):
                videoUrl = re.compile('src="(.+?)"').findall(frame)
        url =  videoUrl[0] + '&AJ;'

                
                
        print 'VIDEO LINK = '+url
        #ANIMECRAZY
        try:
                match=re.compile('http://www.animecrazy.net/(.+?)&AJ;').findall(url)[0]
                req = urllib2.Request('http://www.animecrazy.net/'+match)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=urllib.unquote(response.read())
                response.close()
                link = ''.join(link.splitlines()).replace('\'','"')
                
                url = re.compile('<iframe src ="(.+?)"').findall(link)[0] + '&AJ;'
                print 'NEW url = '+url
        except: pass
        
        #DRAMACRAZY
        try:
                match=re.compile('http://www.dramacrazy.net/(.+?)&AJ;').findall(url)[0]
                req = urllib2.Request('http://www.dramacrazy.net/'+match)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=urllib.unquote(response.read())
                response.close()
                link = ''.join(link.splitlines()).replace('\'','"')
                
                url = re.compile('<iframe src ="(.+?)"').findall(link)[0] + '&AJ;'
                print 'in dramacrzy check'
                print 'NEW url = '+url
        except: pass

        #SAPO
        try:
                if not re.search('videos.sapo.pt', url):
                        raise     
                match=re.compile('/play\?file=(.+?)&AJ;').findall(url)
                newlink='http://videos.sapo.pt/playhtml?file=' + match[0]
                req = urllib2.Request(newlink)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                #print videoUrl
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link = ''.join(link.splitlines()).replace('\'','"')
                match1=re.compile('showEmbedHTML\("swfplayer", (.+?), "(.+?)"\);').findall(link)
                for time,token in match1:
                        videoUrl = match[0]+"?player=EXTERNO&time="+time+"&token="+token;
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]',videoUrl,imgUrl)
        except: pass 
        
        #Gamedorm
        try:
                
                match=re.compile('http://www.gamedorm.net/(.+?)&AJ;').findall(url)[0]
                req = urllib2.Request('http://www.gamedorm.net/'+match)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=urllib.unquote(response.read())
                response.close()
                link = ''.join(link.splitlines()).replace('\'','"')
                videoUrl = re.compile('playlist\:\[\{url: "(.+?)"').findall(link)[0]
                imgUrl = ''
                print 'gamedorm:' + videoUrl +' :end '
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]',videoUrl,imgUrl)
        except: pass
        
        #Gamedorm.org
        try:
                match=re.compile('videodorm.org/(.+?)&AJ;').findall(url)
                if(len(match) >= 1):
                        match=match[0]
                        req = urllib2.Request('http://www.videodorm.org/'+match)
                else:
                        match=re.compile('gamedorm.org/(.+?)&AJ;').findall(url)[0]
                        req = urllib2.Request('http://www.gamedorm.org/'+match)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=urllib.unquote(response.read())
                response.close()
                link = ''.join(link.splitlines()).replace('\'','"')
                #playlist = re.compile('playlist:\[(.+?)\]').findall(link)[0]
                print 'hellow'
                #playItems = re.compile('url: "(.+?)"').findall(playlist)
                videoUrl = re.compile('playlist\:\[\{url: "(.+?)"').findall(link)[0]
                print videoUrl
                
                if(isRequestForURL): 
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]',videoUrl,'')

        except: pass
        
        #Play File
        try:
                videoUrl = re.compile('play\?file\=(.+?)&AJ;').findall(url)[0]
                if(isRequestForURL): 
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]',videoUrl,'')
        except: pass
        
        #MP4
        try:
                match=re.compile('http://(.+?).mp4&AJ;').findall(url)
                videoUrl = 'http://'+match[0]+'.mp4'
                imgUrl = ''
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+name,videoUrl,imgUrl)
                
        except: pass
        
        #YOUTUBE
        try:
                
                match=re.compile('http://www.youtube.com/watch\?v=(.+?)&AJ;').findall(url)
                if(len(match) == 0):
                        match=re.compile('http://www.youtube.com/v/(.+?)&fs=1&AJ;').findall(url)
                code = match[0]
                linkImage = 'http://i1.ytimg.com/vi/'+code+'/sddefault.jpg'
                playVideo("youtube",code)
                return "skip"
        except: pass
        
        #GOOGLE VIDEO
        try:
                id=re.compile('docId=(.+?)&AJ;').findall(url)
                req = urllib2.Request('http://video.google.com/docinfo?%7B"docid":"' + id[0] + '"%7D')
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                print link
                link = ''.join(link.splitlines()).replace('\t','').replace('\'','"')
        
                videoTitle=re.compile('"Title":"(.+?)",').findall(link)[0]
                
                imgUrl=re.compile('"thumbnail_url":"(.+?)"').findall(link)[0].replace('\\u0026','&')
                videoUrl=re.compile('"streamer_url":"(.+?)"').findall(link)[0].replace('\\u0026','&')
                
                if(isRequestForURL): 
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
                
        except: pass
        
        
        #SATSUKAI
        try:
                match=re.compile('http://www.satsukai.com/(.+?)&AJ;').findall(url)[0]
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=urllib.unquote(response.read())
                response.close()
                link = ''.join(link.splitlines()).replace('\t','').replace('\'','"')
                imgUrl=re.compile('so.addVariable\("image","(.+?)"\);').findall(link)[0]
                videoUrl=re.compile('so.addVariable\("file","(.+?)"\);').findall(link)[0]
                videoTitle = name
                if(isRequestForURL): 
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
                
        except: pass
        
        
        #DRAMACRAZY
        try:
                match=re.compile('http://www.dramacrazy.net/(.+?)&AJ;').findall(url)[0]
                req = urllib2.Request('http://www.dramacrazy.net/'+match)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=urllib.unquote(response.read())
                response.close()
                link = ''.join(link.splitlines()).replace('\'','"')
                
                match = re.compile('<iframe src ="(.+?)"').findall(link)
                if len(match) > 0:
                        frameUrl = match[0]
                        req = urllib2.Request(frameUrl)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                        response = urllib2.urlopen(req)
                        link=urllib.unquote(response.read())
                        response.close()
                        link = ''.join(link.splitlines()).replace('\'','"')
                match = re.compile('"file": "(.+?)",').findall(link)
                if len(match) == 0:
                        match = re.compile('<file>(.+?)</file>').findall(link)
                videoUrl = match[0]
                imgUrl = ''
                videoTitle = name
                if(isRequestForURL): 
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem(videoTitle, thumbnailImage=imgUrl)
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        else:
                                return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
                
        except: pass
		  
        #DAILYMOTION
        try:
                match=re.compile('http://www.dailymotion.com/swf/(.+?)&AJ;').findall(url)
                if(len(match) == 0):
                        match=re.compile('http://www.dailymotion.com/video/(.+?)&AJ;').findall(url)
                link = 'http://www.dailymotion.com/video/'+str(match[0])
                req = urllib2.Request(link)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                sequence=re.compile('"sequence":"(.+?)"').findall(link)
                newseqeunce = urllib.unquote(sequence[0]).decode('utf8').replace('\\/','/')
                #print 'in dailymontion:' + str(newseqeunce)
                imgSrc=re.compile('"videoPreviewURL":"(.+?)"').findall(newseqeunce)
                print 'in dailymontion:' + str(imgSrc)
                if(len(imgSrc[0]) == 0):
                	imgSrc=re.compile('/jpeg" href="(.+?)"').findall(link)
                dm_low=re.compile('"sdURL":"(.+?)"').findall(newseqeunce)
                dm_high=re.compile('"hqURL":"(.+?)"').findall(newseqeunce)
                print 'in dailymontion vid:' + str(len(dm_high))
                if(isRequestForURL):
                        videoUrl = ''
                        if(len(dm_high) == 0):
                                videoUrl = dm_low[0]
                        else:
                                videoUrl = dm_high[0]
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        if(len(dm_low) > 0):
                                main.addLink ('PLAY Standard Quality ',dm_low[0],imgSrc[0])
                        if(len(dm_high) > 0):
                                main.addLink ('PLAY High Quality ',dm_high[0],imgSrc[0])
        except: pass
        
        
        #YAHOO
        try:
                id=re.compile('http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf\?id=(.+?)&AJ;').findall(url)
                req = urllib2.Request('http://cosmos.bcst.yahoo.com/up/yep/process/getPlaylistFOP.php?node_id='+id[0])
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link = ''.join(link.splitlines()).replace('\t','').replace('\'','"')
        
                server=re.compile('<STREAM APP="(.+?)"').findall(link)
                urlPath=re.compile('FULLPATH="(.+?)"').findall(link)
                videoUrl=(server[0]+urlPath[0]).replace('&amp;','&')
                imgInfo = re.compile('<THUMB TYPE="FULLSIZETHUMB"><\!\[CDATA\[(.+?)\]\]></THUMB>').findall(link)
                imgUrl = ''
                if(len(imgInfo) > 0):
                        imgUrl = imgInfo[0]
                videoTitle = name
                if(isRequestForURL): 
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem(videoTitle, thumbnailImage=imgUrl)
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        else:
                                return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
        except: pass
        
        #MOVSHARE
        try:
                p=re.compile('http://www.movshare.net/video/(.+?)&AJ;')
                match=p.findall(url)
                movUrl = 'http://www.movshare.net/video/'+match[0]
                req = urllib2.Request(movUrl)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link = ''.join(link.splitlines()).replace('\t','').replace('\'','"')
                if re.search('Video hosting is expensive. We need you to prove you"re human.',link):
                        values = {'wm': '1'}
                        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' }
                        data = urllib.urlencode(values)
                        req = urllib2.Request(movUrl, data, headers)
                        response = urllib2.urlopen(req)
                        link=response.read()
                        response.close()
                        link = ''.join(link.splitlines()).replace('\t','').replace('\'','"')
                
                match=re.compile('<param name="src" value="(.+?)" />').findall(link)
                if(len(match) == 0):
                        match=re.compile('flashvars.file="(.+?)"')
                imgUrl = ''
                videoUrl=match[0]
                videoTitle = name
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem(videoTitle, thumbnailImage=imgUrl)
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        else:
                                return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
        except: pass
        
        
        #VIDEOWEED
        try:
                p=re.compile('http://(.+?).videoweed(.+?)&AJ;')
                match=p.findall(url)
                link = match[0]
                req = urllib2.Request(url.replace('&AJ;',''))
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                imgUrl = ''
                file=re.compile('.file="(.+?)"').findall(link)[0]
                filekey=re.compile('.filekey="(.+?)"').findall(link)[0]
                newUrl = "http://www.videoweed.es/api/player.api.php?user=undefined&codes=undefined&pass=undefined&file=" + file + "&key=" + filekey
                req = urllib2.Request(newUrl)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                videoUrl = re.compile('url=(.+?)&').findall(link)[0]
                videoTitle = name
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
        except: pass
        
        
        #LOOMBO
        try:
                p=re.compile('http://loombo.com/(.+?)&AJ;')
                match=p.findall(url)
                link = match[0]
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link = ''.join(link.splitlines()).replace('\'','"')
                match=re.compile('s1.addVariable\("file","(.+?)"\);').findall(link)
                imgUrl = ''
                videoUrl=match[0]
                videoTitle = name
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem(videoTitle, thumbnailImage=imgUrl)
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        else:
                                return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
        except: pass
        
        
        #VIDEO BAM MP4
        try:
                p=re.compile('http://videobam.com/(.+?)&AJ;')
                match=p.findall(url)
                link = match[0]
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link = ''.join(link.splitlines()).replace('\'','"')
                match=re.compile('<source src="(.+?)"').findall(link)
                imgUrl = ''
                videoUrl=match[0]
                videoTitle = name
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem(videoTitle, thumbnailImage=imgUrl)
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        else:
                                return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
        except: pass
        
        
        #VIDBUX
        try:
                p=re.compile('http://www.vidbux.com/(.+?)&AJ;')
                match=p.findall(url)
                link = match[0]
                xbmc.executebuiltin("XBMC.Notification(SKIPPING...,Low Quality links are skipped,5000)")
                if(isRequestForURL and not isRequestForPlaylist):
                        return 'ERROR'
        except: pass
        
        
        #VIDEOBB
        try:
                p=re.compile('videobb.com/e/(.+?)&AJ;')
                match=p.findall(url)
                url='http://www.videobb.com/player_control/settings.php?v='+match[0]
                settingsObj = json.load(urllib.urlopen(url))['settings']
                imgUrl = str(settingsObj['config']['thumbnail'])
                videoUrl = str(base64.b64decode(settingsObj['config']['token1']))
                videoTitle = name
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                playlist.add(url=videoUrl, listitem=liz)
                        return videoUrl
                else:
                        main.addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
        except: pass
        
        
        #Z-SHARE
        try:
                id=re.compile('http://www.zshare.net/(.+?)&AJ;').findall(url)[0]
                url = 'http://www.zshare.net/'+id.replace(' ','%20')
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                videoUrl = re.compile('file: "(.+?)"').findall(link)[0]
                videoUrl = videoUrl.replace(' ','%20')+'|User-Agent='+urllib.quote_plus('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1) AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3'+'&Accept='+urllib.quote_plus('text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')+'&Accept_Encoding='+urllib.quote_plus('gzip, deflate'))
                
                if(isRequestForURL):
                        if(isRequestForPlaylist):
                                liz = xbmcgui.ListItem('EPISODE', thumbnailImage='')
                                xbmc.PlayList(xbmc.PLAYLIST_VIDEO).add(url = link, listitem=liz)
                        else:
                                return videoUrl
                else:
                        main.addLink ('PLAY High Quality Video',link,'')
        except: pass

        #Resolveurl
        try:
                sources = []
                #try:
                label=name
                hosted_media = urlresolver.HostedMediaFile(url=url.replace('&AJ;',""), title=label)
                sources.append(hosted_media)
                #except:
                print 'Error while trying to resolve %s' % url
                source = urlresolver.choose_source(sources)
                print "source info=" + str(source)
                if source:
                        videoUrl = source.resolve()
                else:
                        videoUrl =""
        
                if(videoUrl != ""):
                        if(isRequestForURL):
                                if(isRequestForPlaylist):
                                        liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
                                        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                                        playlist.add(url=videoUrl, listitem=liz)
                                return videoUrl
                        else:
                                main.addLink ('[B]PLAY VIDEO[/B]',videoUrl,"")
        except: pass
