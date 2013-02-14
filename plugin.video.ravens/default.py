import urllib,urllib2,re
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urlresolver

#Baltimore Ravens - by Mash2k3 2012.

Mainurl =''
addon_id = 'plugin.video.ravens'
selfAddon = xbmcaddon.Addon(id=addon_id)
def MAIN():
        addDir( 'Recent','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'Ray Lewis','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Ray+Lewis&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'NFL Network','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=NFL+Network&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'Super Bowl XLVII','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Super+Bowl+XLVII&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'Gameday','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Gameday&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( '2 Minute Drill','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=2+Minute+Drill&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'CSN','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=CSN&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( '1 Winning Drive','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Rave+TV+-+1+Winning+Drive&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'Ravens One-On-One','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Rave+TV+-+Ravens+One-on-One&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'Game Plan','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Rave+TV+-+Game+Plan&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'Ravens Report','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Rave+TV+-+Ravens+Report&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'Purple Passion','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Rave+TV+-+Purple+Passion&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        addDir( 'Press Conferences','http://www.baltimoreravens.com/cda-web/audio-video-channel.htm?type=VIDEO&channelKey=Press+Conferences&month=&year=',1,"%s/art/rav.png"%selfAddon.getAddonInfo("path"))
        VIEWSB()
 
        
def LISTVID(murl):
        link=OPENURL(murl)
        match=re.compile('{"id":"(.+?)","title":"(.+?)","description":"(.+?)","thumb":"(.+?)","date":"(.+?) .+?').findall(link)
        for url,name,desc,thumb,date in match:
                addInfo(name,url,thumb,3,desc,date)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
        VIEWS()

def OPENURL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def VIDEOLINKS(name,url):
        url='http://www.baltimoreravens.com/videos/videos/Watch-The-Ravens-Parade-Through-Baltimore/'+url
        print url
        link=OPENURL(url)
        match=re.compile('<meta itemprop="thumbnailUrl" content="(.+?)" />\n        <meta itemprop="contentURL" content="(.+?)"/>\n').findall(link)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        for thumb, vidlink in match:
                match=re.compile('http://video.nfl.com/films/').findall(vidlink)
                if len(match)>0:
                        vidlink=vidlink.replace('http://prod.video.ravens.clubs.nfl.com/','')
                listitem = xbmcgui.ListItem(name)
                listitem.setThumbnailImage(thumb)
                playlist.add(vidlink, listitem)
                player = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
                GA()
                player.play(playlist)
                
                addDir('','','','')

def VIEWS():
        if selfAddon.getSetting("auto-view") == "true":
                if selfAddon.getSetting("choose-skin") == "true":
                        if selfAddon.getSetting("con-view") == "0":
                                xbmc.executebuiltin("Container.SetViewMode(50)")
                        elif selfAddon.getSetting("con-view") == "1":
                                xbmc.executebuiltin("Container.SetViewMode(51)")
                        elif selfAddon.getSetting("con-view") == "2":
                                xbmc.executebuiltin("Container.SetViewMode(500)")
                        elif selfAddon.getSetting("con-view") == "3":
                                xbmc.executebuiltin("Container.SetViewMode(503)")
                        elif selfAddon.getSetting("con-view") == "4":
                                xbmc.executebuiltin("Container.SetViewMode(515)")
                        return
                elif selfAddon.getSetting("choose-skin") == "false":
                        if selfAddon.getSetting("xpr-view") == "0":
                                xbmc.executebuiltin("Container.SetViewMode(50)")
                        elif selfAddon.getSetting("xpr-view") == "1":
                                xbmc.executebuiltin("Container.SetViewMode(500)")
                        elif selfAddon.getSetting("xpr-view") == "2":
                                xbmc.executebuiltin("Container.SetViewMode(54)")
                        elif selfAddon.getSetting("xpr-view") == "3":
                                xbmc.executebuiltin("Container.SetViewMode(60)")
                        return
        else:
                return
def VIEWSB():
        if selfAddon.getSetting("auto-view") == "true":
                        if selfAddon.getSetting("home-view") == "0":
                                xbmc.executebuiltin("Container.SetViewMode(50)")
                        elif selfAddon.getSetting("home-view") == "1":
                                xbmc.executebuiltin("Container.SetViewMode(500)")

                        return                



def GA():
    from random import randint
    from urllib import urlencode
    from urllib2 import urlopen
    from urlparse import urlunparse
    from hashlib import sha1
    from os import environ
    PROPERTY_ID = environ.get("GA_PROPERTY_ID", "UA-38312513-3")

    # Generate the visitor identifier somehow. I get it from the
    # environment, calculate the SHA1 sum of it, convert this from base 16
    # to base 10 and get first 10 digits of this number.
    VISITOR = environ.get("GA_VISITOR", "xxxxx")
    VISITOR = str(int("0x%s" % sha1(VISITOR).hexdigest(), 0))[:10]

    # The path to visit
    PATH = "XBMC_Rav"

    # Collect everything in a dictionary
    DATA = {"utmwv": "4.2.8-FRODO",
            "utmn": str(randint(1, 9999999999)),
            "utmp": PATH,
            "utmac": PROPERTY_ID,
            "utmcc": "__utma=%s;" % ".".join(["1", VISITOR, "1", "1", "1", "1"])}

    # Encode this data and generate the final URL
    URL = urlunparse(("http",
                      "www.google-analytics.com",
                      "/__utm.gif",
                      "",
                      urlencode(DATA),
                      ""))
  
    urlopen(URL).info()        
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param




def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image',"%s/art/fanart.png"%selfAddon.getAddonInfo("path"))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addInfo(name,url,iconimage,mode,desc,date):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc,"Date": date} )
        liz.setProperty('fanart_image',"%s/art/fanart.png"%selfAddon.getAddonInfo("path"))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        MAIN()
       
elif mode==1:
        print ""+url
        LISTVID(url)
        
elif mode==2:
        print ""+url
        GENRE(url)

elif mode==4:
        print ""+url
        SEARCH()

elif mode==3:
        print ""+url
        VIDEOLINKS(name,url)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
