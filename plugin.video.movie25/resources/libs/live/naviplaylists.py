import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)



def playlists():
        link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/playlistDir.xml')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        thumb="%s/art/folder.png"%selfAddon.getAddonInfo("path")
        match=re.compile('<name>(.+?)</name><link>(.+?)</link><thumbnail>.+?</thumbnail><mode>(.+?)</mode>').findall(link)
        for name,url,mode in match:
            main.addDir(name,url,int(mode),thumb)
        """main.addDir('Max Powers Sports','https://nkjtvt.googlecode.com/svn/trunk/playlists/maxpowers.xml',139,'')
        main.addDir('Max Powers Streams','https://nkjtvt.googlecode.com/svn/trunk/playlists/maxpowers_all.xml',141,'')
        main.addDir('Live Tv Channels','https://nkjtvt.googlecode.com/svn/trunk/playlists/generallivetv.xml',139,'')
        main.addDir('Live Tv Channels 2','https://nkjtvt.googlecode.com/svn/trunk/playlists/generallivetv2.xml',149,'')
        main.addDir('Sky Sports Channels','https://nkjtvt.googlecode.com/svn/trunk/playlists/skysports.xml',140,'')
        main.addDir('Live UK TV Channels','https://nkjtvt.googlecode.com/svn/trunk/playlists/liveuktv.xml',141,'')
        main.addDir('Live US TV by:TNT','http://www.navixtreme.com/wiilist/100232/_live_usa_tv_(tnt)_now_includes_25_live_sports_streams_.plx',142,'')
        main.addDir('XBMC TV','https://nkjtvt.googlecode.com/svn/trunk/playlists/xbmctv.xml',142,'')"""
        main.GA("Live","Playlists")

        

def playlistList(murl):
        main.GA("Playlists","Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('name=(.+?)thumb=(.+?)date=.+?URL=(.+?)#').findall(link)
        for name,thumb,url in match:
                match2=re.compile('http://(.+?)URL').findall(thumb)
                if len(match2)>0:
                        thumb ='http://'+match2[0]
                url=url.replace('player=defaultrating=-1.00','').replace('%20',' ').replace('player=default','').replace(' conn=S:OK --live','').replace(' conn=S:OK','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,thumb)
        main.VIEWSB()
def playlistList2(murl):
        main.GA("Playlists","Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('name=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=[COLOR=FFFFD700] Sky Sports Channels Live HD [/COLOR] [COLOR=FF00FFFF]','').replace('thumb=http://coloradorushrfc.org/home/wp-content/uploads/2010/11/foxsoccer_logo.jpg','')
        match=re.compile('name=(.+?)date.+?URL=(.+?)#').findall(link)
        for name,url in match[0:9]:
                url=url.replace('player=defaultrating=-1.00','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,'')
        main.VIEWSB()
def playlistList3(murl):
        main.GA("Playlists","Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('name=(.+?)thumb=(.+?)date=.+?URL=(.+?)#').findall(link)
        for name,thumb,url in match:
                match2=re.compile('http://(.+?)URL').findall(thumb)
                if len(match2)>0:
                        thumb ='http://'+match2[0]
                url=url.replace('player=defaultrating=-1.00','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,thumb)
        match=re.compile('name=(.+?)thumb=(.+?)URL=(.+?)#').findall(link)
        for name,thumb,url in match:
                match2=re.compile('http://(.+?)URL').findall(thumb)
                if len(match2)>0:
                        thumb ='http://'+match2[0]
                url=url.replace('player=defaultrating=-1.00','').replace('%20',' ').replace('player=default','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,thumb)
        main.VIEWSB()
def playlistList4(murl):
        main.GA("Playlists","Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('name=(.+?)thumb=(.+?)URL=(.+?)#').findall(link)
        for name,thumb,url in match:
                match2=re.compile('http://(.+?)URL').findall(thumb)
                if len(match2)>0:
                        thumb ='http://'+match2[0]
                url=url.replace('player=defaultrating=-1.00','').replace('%20',' ').replace('player=default','').replace(' conn=S:OK --live','').replace(' conn=S:OK','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,thumb)
        main.VIEWSB()
def playlistList5(murl):
        main.GA("Playlists","Watched")
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('date=',' ').replace('\t','').replace('&nbsp;','').replace('name=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=[COLOR=FFFFD700] Sky Sports Channels Live HD [/COLOR] [COLOR=FF00FFFF]','').replace('thumb=http://coloradorushrfc.org/home/wp-content/uploads/2010/11/foxsoccer_logo.jpg','')
        match=re.compile('name=(.+?)URL=(.+?)#').findall(link)
        for name,url in sorted(match):
                url=url.replace('player=defaultrating=-1.00','')
                match3=re.compile('rtmp').findall(url)
                match4=re.compile('timeout').findall(url)
                if len(match3)>0 and len(match4)==0:
                        url=url+' timeout=15'
                main.addLink(name,url,'')
        main.VIEWSB()
