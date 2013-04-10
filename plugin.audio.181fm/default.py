import urllib,urllib2,re,cookielib,string
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from t0mm0.common.addon import Addon


addon_id = 'plugin.audio.181fm'
selfAddon = xbmcaddon.Addon(id=addon_id)

def OPENURL(url):
        print "openurl = " + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=link.replace('&#39;',"'").replace('&quot;','"').replace('&amp;',"&").replace("&#39;","'").replace('&lt;i&gt;','').replace("#8211;","-").replace('&lt;/i&gt;','').replace("&#8217;","'").replace('&amp;quot;','"').replace('&#215;','').replace('&#038;','').replace('&#8216;','').replace('&#8211;','').replace('&#8220;','').replace('&#8221;','').replace('&#8212;','')
        link=link.replace('%3A',':').replace('%2F','/')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        return link


def MAIN():
        link=OPENURL('http://www.181.fm/channellistmini.php')
        newchannel = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>New Channels</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Oldies</font></td>''').findall(link)
        oldies = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Oldies</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>80's Decade</font></td>''').findall(link)
        eightys = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>80's Decade</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>90's Decade</font></td>''').findall(link)
        nintys = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>90's Decade</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Pop</font></td>''').findall(link)
        pop = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Pop</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Rock Channels</font></td>''').findall(link)
        rock = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Rock Channels</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Country</font></td>''').findall(link)
        country = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Country</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Urban</font></td>''').findall(link)
        urban = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Urban</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Dance / Techno</font></td>''').findall(link)
        techno = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Dance / Techno</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Easy Listening</font></td>''').findall(link)
        easy = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Easy Listening</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Latin / Tropical</font></td>''').findall(link)
        latin = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Latin / Tropical</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Talk Radio</font></td>''').findall(link)
        talk = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Talk Radio</font></td>(.+?)<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Christmas</font></td>''').findall(link)
        chris = re.compile('''<td align="center" valign="middle" class="menu_left_title"><font face="Tahoma" style="font-size: 8pt; font-weight: 700"><br>Christmas</font></td>(.+?)<td align="left" valign="top">''').findall(link)

        addDir('New Channels',newchannel[0],1,"%s/resources/art/New Channels.png"%selfAddon.getAddonInfo("path"))
        addDir('Oldies',oldies[0],1,"%s/resources/art/Oldies.png"%selfAddon.getAddonInfo("path"))
        addDir("80's Decade",eightys[0],1,"%s/resources/art/80's Decade.png"%selfAddon.getAddonInfo("path"))
        addDir("90's Decade",nintys[0],1,"%s/resources/art/90's Decade.png"%selfAddon.getAddonInfo("path"))
        addDir('Pop',pop[0],1,"%s/resources/art/Pop.png"%selfAddon.getAddonInfo("path"))
        addDir('Rock Channels',rock[0],1,"%s/resources/art/Rock Channels.png"%selfAddon.getAddonInfo("path"))
        addDir('Country',country[0],1,"%s/resources/art/Country.png"%selfAddon.getAddonInfo("path"))
        addDir('Urban',urban[0],1,"%s/resources/art/Urban.png"%selfAddon.getAddonInfo("path"))
        addDir('Dance & Techno',techno[0],1,"%s/resources/art/Dance & Techno.png"%selfAddon.getAddonInfo("path"))
        addDir('Easy Listening',easy[0],1,"%s/resources/art/Easy Listening.png"%selfAddon.getAddonInfo("path"))
        addDir('Latin & Tropical',latin[0],1,"%s/resources/art/Latin & Tropical.png"%selfAddon.getAddonInfo("path"))
        addDir('Talk Radio',talk[0],1,"%s/resources/art/Talk Radio.png"%selfAddon.getAddonInfo("path"))
        addDir('Christmas',chris[0],1,"%s/resources/art/Christmas.png"%selfAddon.getAddonInfo("path"))
    

def LIST(mname,murl):
        thumb="%s/resources/art/%s.png"%(selfAddon.getAddonInfo("path"),mname)
        print "kk "+thumb
        match = re.compile('<a STYLE="text-decoration:none" href="(.+?)" class="left_link">(.+?)</a></font></td>').findall(murl)
        for url,name in match:
            addPlay(name,url,2,thumb)


def LINK(name,url):
        #xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Stream,3000)")
        link=OPENURL(url)
        source = re.compile('<REF HREF="(.+?)"/>').findall(link)
        for stream_url in source:
                match = re.compile('relay').findall(stream_url)
                if len(match)>0:
                        stream=stream_url
        pl = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
        pl.clear()    
        pl.add(stream)
        xbmc.Player().play(pl)
        

def addPlay(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage='', thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image',"%s/resources/art/fanart.jpg"%selfAddon.getAddonInfo("path"))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage='', thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image',"%s/resources/art/fanart.jpg"%selfAddon.getAddonInfo("path"))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




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
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        MAIN()
       
elif mode==1:
        LIST(name,url)
        
elif mode==2:
        LINK(name,url)

        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
