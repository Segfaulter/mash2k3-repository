import urllib,urllib2,re,cookielib,string
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from t0mm0.common.addon import Addon
import datetime
import time

Mainurl ='http://dsc.discovery.com'
addon_id = 'plugin.video.discovery'
selfAddon = xbmcaddon.Addon(id=addon_id)

if selfAddon.getSetting('ga_visitor')=='':
    from random import randint
    selfAddon.setSetting('ga_visitor',str(randint(0, 0x7fffffff)))

VERSION = "4.2i"
PATH = "Discovery"            
UATRACK="UA-38312513-4" 


def OPENURL(url):
        print "openurl = " + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def VIEWSB():
        if selfAddon.getSetting("auto-view") == "true":
                        if selfAddon.getSetting("home-view") == "0":
                                xbmc.executebuiltin("Container.SetViewMode(50)")
                        elif selfAddon.getSetting("home-view") == "1":
                                xbmc.executebuiltin("Container.SetViewMode(500)")

                        return


def DISC():
        dialog = xbmcgui.Dialog()
        ok=dialog.ok('[B]Devices[/B]', 'Make sure you go to settings and set your device type.', 'Videos in this plugin can go up to 3500k in quality.','Will not work well on older or phone/tablet devices.')
        addDir('AFRICA','http://dsc.discovery.com/services/taxonomy/Africa%20the%20Series/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/africa-show-carousel-badge-130x97.jpg')
        addDir('ALASKA: THE LAST FRONTIER','http://dsc.discovery.com/services/taxonomy/ALASKA:%20THE%20LAST%20FRONTIER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/alaska_badge_130x97.jpg')
        addDir('AMERICAN CHOPPER','http://dsc.discovery.com/services/taxonomy/AMERICAN%20CHOPPER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/american-chopper-badge.jpg')
        addDir('AMERICAN GUNS','http://dsc.discovery.com/services/taxonomy/AMERICAN%20GUNS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/american-guns-show-carousel-badge.jpg')
        addDir('AMISH MAFIA','http://dsc.discovery.com/services/taxonomy/AMISH%20MAFIA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/amish-mafia-show-carousel-badge-130x97.jpg')
        addDir('AUCTION KINGS','http://dsc.discovery.com/services/taxonomy/AUCTION%20KINGS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/auction-kings-show-carousel-badge.jpg')
        addDir('BERING SEA GOLD','http://dsc.discovery.com/services/taxonomy/BERING%20SEA%20GOLD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/bsg-full-ep.jpg')
        addDir('BERING SEA GOLD: UNDER THE ICE','http://dsc.discovery.com/services/taxonomy/BERING%20SEA%20GOLD%20UNDER%20THE%20ICE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/new-bsg-under-the-ice-show-carousel-badge.jpg')
        addDir('BREAKING MAGIC','http://dsc.discovery.com/services/taxonomy/BREAKING%20MAGIC/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/breaking-magic-badge.jpg')
        addDir('CASH CAB','http://dsc.discovery.com/services/taxonomy/CASH%20CAB/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/cash-cab-show-carousel-badge.jpg')
        addDir('CURIOSITY','http://dsc.discovery.com/services/taxonomy/CURIOSITY/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/curiosity-show-carousel-badge.jpg')
        addDir('DEADLIEST CATCH','http://dsc.discovery.com/services/taxonomy/DEADLIeST%20CATCH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/deadliest-catch-show-carousel-badge.jpg')
        addDir('DIRTY JOBS','http://dsc.discovery.com/services/taxonomy/DIRTY%20JOBS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/dirty-jobs-show-carousel-badge.jpg')
        addDir('DUAL SURVIVAL','http://dsc.discovery.com/services/taxonomy/DUAL%20SURVIVAL/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/dual-survivor-130x97.jpg')
        addDir('FAST N LOUD',"http://dsc.discovery.com/services/taxonomy/FAST%20N'%20LOUD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",1,'http://static.ddmcdn.com/gif/fast-n-loud-show-carousel-badge.jpg')
        addDir('FLYING WILD ALASKA ','http://dsc.discovery.com/services/taxonomy/FLYING%20WILD%20ALASKA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/flying-wild-alaska-show-carousel-badge.jpg')
        addDir('FROZEN PLANET','http://dsc.discovery.com/services/taxonomy/FROZEN%20PLANET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/frozen-planet-show-carousel-badge.jpg')
        addDir('GOLD RUSH','http://dsc.discovery.com/services/taxonomy/GOLD%20RUSH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/gold-rush-show-carousel-badge.jpg')
        addDir('HOW BOOZE BUILT AMERICA','http://dsc.discovery.com/services/taxonomy/HOW%20BOOZE%20BUILT%20AMERICA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/hbba-show-carousel-badge-130x97.jpg')
        addDir('JESSE JAMES: OUTLAW GARAGE','http://dsc.discovery.com/services/taxonomy/OUTLAW%20GARAGE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/outlawgarage_130x97.jpg')
        addDir('JUNGLE GOLD','http://dsc.discovery.com/services/taxonomy/JUNGLE%20GOLD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/jungle-gold-show-carousel-badge.jpg')
        addDir("KURT SUTTER'S OUTLAW EMPIRES","http://dsc.discovery.com/services/taxonomy/KURT%20SUTTER'S%20OUTLAW%20EMPIRES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",1,'http://static.ddmcdn.com/gif/outlaw-empires-show-carousel-badge.jpg')
        addDir('LIFE','http://dsc.discovery.com/services/taxonomy/LIFE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/life-show-carousel-badge.jpg')
        addDir('MAN VS. WILD','http://dsc.discovery.com/services/taxonomy/MAN%20VS%20WILD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/man-vs-wild-show-carousel-badge.jpg')
        addDir('MAYAN DOOMSDAY PROPHECY','http://dsc.discovery.com/services/taxonomy/Mayan%20Doomsday%20Prophecy%20Videos/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/mayan-doomsday-130x97.jpg')
        addDir('MOONSHINERS','http://dsc.discovery.com/services/taxonomy/MOONSHINERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/moonshiners-full-episodes.jpg')
        addDir('MYTHBUSTERS','http://dsc.discovery.com/services/taxonomy/MYTHBUSTERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/mythbusters-show-carousel-badge.jpg')
        addDir('ONE CAR TOO FAR)','http://dsc.discovery.com/services/taxonomy/ONE%20CAR%20TOO%20FAR/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/one-car-too-far-show-carousel-badge.jpg')
        addDir('PLANET EARTH','http://dsc.discovery.com/services/taxonomy/PLANET%20EARTH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/show-badge-planet-earth.jpg')
        addDir('PROPERTY WARS','http://dsc.discovery.com/services/taxonomy/PROPERTY%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/show-badge-property-wars-130x97.jpg')
        addDir('SHARK WEEK','http://dsc.discovery.com/services/taxonomy/SHARK%20WEEK/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/show-badge-sharkweek-130x97.jpg')
        addDir('SHIPWRECK MEN','http://dsc.discovery.com/services/taxonomy/SHIPWRECK%20MEN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/badge_130x97_full2.jpg')
        addDir('SONS OF GUNS','http://dsc.discovery.com/services/taxonomy/SONS%20OF%20GUNS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/sons-of-guns-show-carousel-badge.jpg')
        addDir('STORM CHASERS','http://dsc.discovery.com/services/taxonomy/STORM%20CHASERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/storm-chasers-show-carousel-badge.jpg')
        addDir('SURVIVORMAN','http://dsc.discovery.com/services/taxonomy/SURVIVORMAN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/survivorman-130x97.jpg')
        addDir('TEXAS CAR WARS','http://dsc.discovery.com/services/taxonomy/TEXAS%20CAR%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/texas-car-wars-show-carousel-badge.jpg')
        addDir('THE DEVILS RIDE','http://dsc.discovery.com/services/taxonomy/THE%20DEVILS%20RIDE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/devils-ride-show-carousel-badge.jpg')
        addDir('WINGED PLANET','http://dsc.discovery.com/services/taxonomy/WINGED%20PLANET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/winged-planet-130x97.jpg')
        addDir('YUKON MEN','http://dsc.discovery.com/services/taxonomy/YUKON%20MEN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',1,'http://static.ddmcdn.com/gif/yukon-men-130-97.jpg')
        VIEWSB()


def LISTDISC(mname,murl):
        thumbList=[]
        link=OPENURL(murl)
        Thumb=re.compile('<img src="(.+?)" />').findall(link)
        for thumb in Thumb:
                thumbList.append(thumb)
         
        match=re.compile('<a href="(.+?)" class=".+?" data-track-rule=".+?"  data-module-name=".+?" data-module-location=".+?" data-link-position=".+?" data-track-more=".+?">(.+?)</a></h4>\n                        <p class="clip-count-all">(.+?)</p>\n').findall(link)
        i=0
        for url, name, view in match:
                Full=re.compile('<img src="(.+?)" />\n                                \n                                <span class="full-episode-flag">FULL EPISODE</span>').findall(link)
                for ind in Full:
                        if ind == thumbList[i]:
                                name= name + '  [COLOR red]Full Episode[/COLOR]'
                name=name.replace('&#39;',"'").replace('&quot;','"').replace('&amp;',"&")
                addDir(name+'  [COLOR blue]'+view+'[/COLOR]',url,2,thumbList[i])
                i=i+1
        GA("None",mname+"-list")
def LINKDISC(name,url):
        idlist1=[]
        idlist2=[]
        idlist3=[]
        qualitylist=[]
        ETitleList=[]
        thumbList=[]
        plotList=[]
        #GA("Discovery","Watched")
        MainUrl= 'http://dsc.discovery.com'
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        url = MainUrl+url
        link=OPENURL(url)
        Title=re.compile('"name": "(.+?)",').findall(link)
        for title in Title:
            mtitle = title
        Thumb=re.compile('"thumbnailURL": "(.+?)",').findall(link)
        for thumb in Thumb:
            thumbList.append(thumb)
        Plot=re.compile('"videoCaption": "(.+?)",').findall(link)
        for plot in Plot:
            plotList.append(plot)
        ETitle=re.compile('"episodeTitle": "(.+?)",').findall(link)
        for etitle in ETitle:
            ETitleList.append(etitle)
        match=re.compile('"m3u8": "http://discidevflash-f.akamaihd.net/i/digmed/hdnet/(.+?)/(.+?)/(.+?)-(.+?).mp4').findall(link)
        for id1, id2, id3, quality in match:
                idlist1.append(id1)
                idlist2.append(id2)
                idlist3.append(id3)
                qualitylist.append(quality)
        i=0
        for i in range(len(match)):
                match1=re.compile('3500k').findall(qualitylist[i])
                match2=re.compile('1500k').findall(qualitylist[i])
                if selfAddon.getSetting("device-type") == "0" or selfAddon.getSetting("device-type") == "1":
                    if (len(match1)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-3500k.mp4?seek=5'
                    elif (len(match1)==0) and (len(match2)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-1500k.mp4?seek=5'
                    else:
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-600k.mp4?seek=5'    
                else:
                    if (len(match2)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-1500k.mp4?seek=5'
                    else:
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-600k.mp4?seek=5'
                match2=re.compile('1500k').findall(quality)
                listitem = xbmcgui.ListItem('',thumbnailImage=thumbList[i])
                tot = i + 1
                listitem.setInfo('video', {'Title':mtitle+'  [COLOR blue]'+ETitleList[i]+'[/COLOR]','Plot': plotList[i],'Genre': '[B]Clip '+str(tot)+'/'+str(len(match))+' on playlist[/B]'} )
                #ListItem.Tagline
                print "llll "+ ETitleList[i]
                playlist.add(final,listitem)
                i=i+1
                
        
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        if idlist3[0][0:7]==idlist3[1][0:7]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
        elif idlist3[0][6:13]==idlist3[1][6:13]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
        elif idlist3[1][6:13]==idlist3[2][6:13]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
        else:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],Related clips loaded to playlist,10000)")
        addDir('','','','')

        GA(mtitle,"Watching")

def parseDate(dateString):
    try:
        return datetime.datetime.fromtimestamp(time.mktime(time.strptime(dateString.encode('utf-8', 'replace'), "%Y-%m-%d %H:%M:%S")))
    except:
        return datetime.datetime.today() - datetime.timedelta(days = 1) #force update


def checkGA():

    secsInHour = 60 * 60
    threshold  = 2 * secsInHour

    now   = datetime.datetime.today()
    prev  = parseDate(selfAddon.getSetting('ga_time'))
    delta = now - prev
    nDays = delta.days
    nSecs = delta.seconds

    doUpdate = (nDays > 0) or (nSecs > threshold)
    if not doUpdate:
        return

    selfAddon.setSetting('ga_time', str(now).split('.')[0])
    APP_LAUNCH()
    
    
    
                    
def send_request_to_google_analytics(utm_url):
    ua='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    import urllib2
    try:
        req = urllib2.Request(utm_url, None,
                                    {'User-Agent':ua}
                                     )
        response = urllib2.urlopen(req).read()
    except:
        print ("GA fail: %s" % utm_url)         
    return response
       
def GA(group,name):
        try:
            try:
                from hashlib import md5
            except:
                from md5 import md5
            from random import randint
            import time
            from urllib import unquote, quote
            from os import environ
            from hashlib import sha1
            VISITOR = selfAddon.getSetting('ga_visitor')
            utm_gif_location = "http://www.google-analytics.com/__utm.gif"
            if not group=="None":
                    utm_track = utm_gif_location + "?" + \
                            "utmwv=" + VERSION + \
                            "&utmn=" + str(randint(0, 0x7fffffff)) + \
                            "&utmt=" + "event" + \
                            "&utme="+ quote("5("+PATH+"*"+group+"*"+name+")")+\
                            "&utmp=" + quote(PATH) + \
                            "&utmac=" + UATRACK + \
                            "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR,VISITOR,"2"])
                    try:
                        print "============================ POSTING TRACK EVENT ============================"
                        send_request_to_google_analytics(utm_track)
                    except:
                        print "============================  CANNOT POST TRACK EVENT ============================" 
            if name=="None":
                    utm_url = utm_gif_location + "?" + \
                            "utmwv=" + VERSION + \
                            "&utmn=" + str(randint(0, 0x7fffffff)) + \
                            "&utmp=" + quote(PATH) + \
                            "&utmac=" + UATRACK + \
                            "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
            else:
                if group=="None":
                       utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmp=" + quote(PATH+"/"+name) + \
                                "&utmac=" + UATRACK + \
                                "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
                else:
                       utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmp=" + quote(PATH+"/"+group+"/"+name) + \
                                "&utmac=" + UATRACK + \
                                "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
                                
            print "============================ POSTING ANALYTICS ============================"
            send_request_to_google_analytics(utm_url)
            
        except:
            print "================  CANNOT POST TO ANALYTICS  ================" 
            
            
def APP_LAUNCH():
        try:
            try:
                from hashlib import md5
            except:
                from md5 import md5
            from random import randint
            import time
            from urllib import unquote, quote
            from os import environ
            from hashlib import sha1
            import platform
            VISITOR = selfAddon.getSetting('ga_visitor')
            if re.search('12.',xbmc.getInfoLabel( "System.BuildVersion"),re.IGNORECASE): 
                build="Frodo" 
            if re.search('11.',xbmc.getInfoLabel( "System.BuildVersion"),re.IGNORECASE): 
                build="Eden" 
            if re.search('13.',xbmc.getInfoLabel( "System.BuildVersion"),re.IGNORECASE): 
                build="Gotham" 
            try: 
                PLATFORM=platform.system()+' '+platform.release()+" "+platform.machine()
            except: 
                PLATFORM='Unknown'
            utm_gif_location = "http://www.google-analytics.com/__utm.gif"
            utm_track = utm_gif_location + "?" + \
                    "utmwv=" + VERSION + \
                    "&utmn=" + str(randint(0, 0x7fffffff)) + \
                    "&utmt=" + "event" + \
                    "&utme="+ quote("5("+PATH+"*LAUNCH-"+build+"-"+VERSION+"*"+PLATFORM+"-"+VERSION+")")+\
                    "&utmp=" + quote(PATH) + \
                    "&utmac=" + UATRACK + \
                    "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR,VISITOR,"2"])
            try:
                print "============================ POSTING APP LAUNCH TRACK EVENT ============================"
                send_request_to_google_analytics(utm_track)
            except:
                print "============================  CANNOT POST APP LAUNCH TRACK EVENT ============================" 
            
        except:
            print "================  CANNOT POST TO ANALYTICS  ================" 
checkGA()


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
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addInfo(name,url,iconimage,mode,plot,rate,mpaas,gen,yr,fan):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": plot, "Rating": rate,"mpaa": mpaas, "Genre": gen,"Year": yr } )
        liz.setProperty('fanart_image', fan)
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
        DISC()
       
elif mode==1:
        print ""+url
        LISTDISC(name,url)
        
elif mode==2:
        print ""+url
        LINKDISC(name,url)




xbmcplugin.endOfDirectory(int(sys.argv[1]))

