import urllib,urllib2,re,cookielib,string
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


def MAINBB():
    main.GA("Sports","BodyBuilding")   
    main.addDir('Abdominals','http://www.bodybuilding.com/exercises/list/muscle/selected/abdominals',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Abductors','http://www.bodybuilding.com/exercises/list/muscle/selected/abductors',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Adductors','http://www.bodybuilding.com/exercises/list/muscle/selected/adductors',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Biceps','http://www.bodybuilding.com/exercises/list/muscle/selected/biceps',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Calves','http://www.bodybuilding.com/exercises/list/muscle/selected/calves',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Chest','http://www.bodybuilding.com/exercises/list/muscle/selected/chest',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Forearms','http://www.bodybuilding.com/exercises/list/muscle/selected/forearms',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Glutes','http://www.bodybuilding.com/exercises/list/muscle/selected/glutes',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Hamstrings','http://www.bodybuilding.com/exercises/list/muscle/selected/hamstrings',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Lats','http://www.bodybuilding.com/exercises/list/muscle/selected/lats',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Lower Back','http://www.bodybuilding.com/exercises/list/muscle/selected/lower-back',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Middle Back','http://www.bodybuilding.com/exercises/list/muscle/selected/middle-back',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Neck','http://www.bodybuilding.com/exercises/list/muscle/selected/neck',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Quadriceps','http://www.bodybuilding.com/exercises/list/muscle/selected/quadriceps',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Shoulders','http://www.bodybuilding.com/exercises/list/muscle/selected/shoulders',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Traps','http://www.bodybuilding.com/exercises/list/muscle/selected/traps',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Triceps','http://www.bodybuilding.com/exercises/list/muscle/selected/triceps',196,"%s/art/bodybuilding.png"%selfAddon.getAddonInfo("path"))

def LISTBB(murl):
    main.GA("BodyBuilding","List")   
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('img src="http://assets.bodybuilding.com','')
    match=re.compile('''img src="(.+?)".+? title="(.+?)" /></a>.+?<h3>.+?<a href=\'(.+?)'> .+? </a>.+?Muscle Targeted:.+?> (.+?) </a>''').findall(link)
    for thumb,name,url,body in match:    
        main.addPlay(name+"   [COLOR red]"+body+"[/COLOR]",url,197,thumb)


def LINKBB(mname,murl):
    main.GA("BodyBuilding","Watched")
    ok=True
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    namelist=[]
    urllist=[]
    thumblist=[]
    link=main.OPENURL(murl)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('img src="http://assets.bodybuilding.com','')
    match=re.compile('<div id=".+?" style="display:.+?">                <div id="(.+?)Video">                    <div class="BBCOMVideoEmbed" data-video-id="(.+?)" data-thumbnail-url="(.+?)"').findall(link)
    for gender,vidid,thumb in match:
        namelist.append(gender)
        urllist.append(vidid)
        thumblist.append(thumb)
    dialog = xbmcgui.Dialog()
    answer =dialog.select("Playlist", namelist)
    listitem = xbmcgui.ListItem(mname, thumbnailImage=thumblist[int(answer)])
    stream_url = "http://videocdn.bodybuilding.com/video/mp4/"+urllist[int(answer)]+"m.mp4"
    playlist.add(stream_url,listitem)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(playlist)
    return ok
