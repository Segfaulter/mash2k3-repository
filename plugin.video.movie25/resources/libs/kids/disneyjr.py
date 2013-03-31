import urllib,urllib2,re,cookielib,string, urlparse,sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def DISJR():
        main.addDir('By Character','charac',108,"%s/art/disjr.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Full Episodes','full',108,"%s/art/disjr.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Short Videos','short',108,"%s/art/disjr.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Music Videos','music',108,"%s/art/disjr.png"%selfAddon.getAddonInfo("path"))
        
def DISJRList(murl):
        main.GA("DisneyJR","Category")
        if murl=='music':
            url ='http://disney.go.com/disneyjunior/data/tilePack?id=1815108&maxAmount=240'
            link=main.OPENURL(url)
            match = re.compile('<a href="(.+?)" ping=".+?"/>\n\t\t<img src="(.+?)" />\n\t\t<text class="title"><(.+?)>').findall(link)
            for url,thumb, name in match:
                name=name.replace('![CDATA[',' ').replace(']]',' ')
                main.addDir(name,url,110,thumb)

        elif murl=='full':
            url ='http://disney.go.com/disneyjunior/data/tilePack?id=1815106&maxAmount=240'
            link=main.OPENURL(url)
            match = re.compile('<a href="(.+?)" ping=".+?"/>\n\t\t<img src="(.+?)" />\n\t\t<text class="title"><(.+?)>').findall(link)
            for url,thumb, name in match:
                sname = re.compile('http://disney.go.com/disneyjunior/(.+?)/.+?').findall(url)
                sname = sname[0]
                sname=sname.replace('-',' ')
                name=name.replace('![CDATA[',' ').replace(']]',' ')
                sname=sname.upper()
                main.addDir(sname+'  [COLOR red]"'+name+'"[/COLOR]',url,110,thumb)

        elif murl=='short':
            url ='http://disney.go.com/disneyjunior/data/tilePack?id=1815107&maxAmount=240'
            link=main.OPENURL(url)
            match = re.compile('<a href="(.+?)" ping=".+?"/>\n\t\t<img src="(.+?)" />\n\t\t<text class="title"><(.+?)>').findall(link)
            for url,thumb, name in match:
                sname = re.compile('http://disney.go.com/disneyjunior/(.+?)/.+?/.+?').findall(url)
                sname = sname[0]
                sname=sname.replace('-',' ')
                name=name.replace('![CDATA[',' ').replace(']]',' ')
                sname=sname.upper()
                main.addDir(sname+'  [COLOR red]"'+name+'"[/COLOR]',url,110,thumb)

        elif murl=='charac':
            url ='http://disney.go.com/disneyjunior/data/tilePack?id=1815104&maxAmount=240'
            link=main.OPENURL(url)
            match = re.compile('<a href="(.+?)" target="_self" ping=".+?"></a>\n\t\t<img src="(.+?)" />\n\t\t<text class="title"><(.+?)]]>').findall(link)
            for url,thumb, name in match:
                name=name.replace('<font size="9">','').replace('<font size="10">','').replace('</font>','')
                name=name.replace('![CDATA[',' ').replace(']]',' ')
                main.addDir(name,url,109,thumb)
        
def DISJRList2(murl):
            main.GA("DisneyJR","DisJR-list")
            link=main.OPENURL(murl)
            match = re.compile('tileService: "http://disney.go.com/disneyjunior/data/tilePack.?id=(.+?)%26.+?" }').findall(link)
            url='http://disney.go.com/disneyjunior/data/tilePack?id='+match[0]+'&maxAmount=240'
            link2=main.OPENURL(url)
            match2 = re.compile('<a href="(.+?)" ping=".+?"/>\n\t\t<img src="(.+?)" />\n\t\t<text class="title"><(.+?)>').findall(link2)
            for url,thumb, name in match2:
                sname = re.compile('http://disney.go.com/disneyjunior/(.+?)/.+?').findall(url)
                sname = sname[0]
                sname=sname.replace('-',' ')
                name=name.replace('![CDATA[',' ').replace(']]',' ')
                sname=sname.upper()
                main.addPlay(sname+'  [COLOR red]"'+name+'"[/COLOR]',url,110,thumb)

def DISJRLink(mname,murl):
        main.GA("DisJR-list","Watched")
        link=main.OPENURL(murl)
        ok=True
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        vidID = re.compile('\'player-placeholder\', {entryId:\'(.+?)\',').findall(link)
        vurl='http://cdnapi.kaltura.com/p/628012/sp/628012/playManifest/entryId/'+vidID[0]+'/format/rtmp/protocol/rtmp/'
        link2=main.OPENURL(vurl)
        video = re.compile('<media url="(.+?)" bitrate=".+?" width=".+?" height=".+?"/>').findall(link2)
        stream_url = 'rtmp://videodolimgfs.fplive.net/videodolimg'
        if selfAddon.getSetting("disj-qua") == "0":
            playpath = video[len(video)-1]
        elif selfAddon.getSetting("disj-qua") == "1":
            playpath = video[len(video)-5]
        elif selfAddon.getSetting("disj-qua") == "2":
            playpath = video[0]  
        listitem = xbmcgui.ListItem(mname)
        listitem.setProperty('PlayPath', playpath);
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
