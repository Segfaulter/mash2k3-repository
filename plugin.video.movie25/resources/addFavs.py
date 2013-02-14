import urllib,urllib2,re,cookielib,sys,xbmcplugin,xbmcgui,xbmcaddon,time,socket,string,os,shutil,stat

#SET DIRECTORIES
selfAddon=xbmcaddon.Addon(id='plugin.video.movie25')

def addFAVS(url,name):
    if open("%s/resources/Favs"%selfAddon.getAddonInfo('path'),'r').read().find(name)>0:
        xbmc.executebuiltin("XBMC.Notification([B][COLOR green]"+name+"[/COLOR][/B],[B]Already added to Favourites[/B],1000,"")")
    else:    
        open("%s/resources/Favs"%selfAddon.getAddonInfo('path'),'a').write('url="%s",name="%s",'%(url,name))
        xbmc.executebuiltin("XBMC.Notification([B][COLOR green]"+name+"[/COLOR][/B],[B]Added to Favourites[/B],1000,"")")
    
bits = sys.argv[1].split(',')
print "BaseUrl= "+sys.argv[0]
url = bits[0].replace("[(u'",'').replace("'",'')
print "Url= "+url
name = bits[1].replace("'[B][COLOR green]",'').replace("[/COLOR][/B]')]",'').replace("'",'').replace(')]','').strip()
print "name= "+name

if not os.path.exists("%s/resources/Favs"%selfAddon.getAddonInfo('path')):
    open("%s/resources/Favs"%selfAddon.getAddonInfo('path'),'w').write('url="%s",name="%s",'%(url,name))
    xbmc.executebuiltin("XBMC.Notification([B][COLOR green]"+name+"[/COLOR][/B],[B]Favourites file Created.[/B],1000,"")")
else:
    addFAVS(url,name)
