#-*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,string, urlparse
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urlresolver
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net as net
from metahandler import metahandlers
import datetime,time
from resources.libs import main, movie25


#Mash Up - by Mash2k3 2012.

Mainurl ='http://www.movie25.com/movies/'
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
grab = metahandlers.MetaData(preparezip = False)
addon = Addon(addon_id)


################################################################################ Source Imports ##########################################################################################################

from resources.libs import youtube

from resources.libs.documentaries import vice, documentary

from resources.libs.sports import wildtv, tsn, espn, foxsoccer, outdoorch, mmafighting

from resources.libs.kids import disneyjr, wbkids

from resources.libs.adventure import discovery, airaces, nationalgeo

from resources.libs.plugins import seriesgate, btvguide, watchseries, sceper, extramina, fma

from resources.libs.live import livestation, naviplaylists, ilive, castalba, desistreams, musicstreams, countries

from resources.libs.movies_tv import oneclickwatch, backuptv, rlsmix, newmyvideolinks, dailyflix, oneclickmoviez, starplay, iwatchonline, movie1k

from resources.libs.international import dramacrazy, einthusan, cinevip


################################################################################ Directories ##########################################################################################################

def AtoZ():
        main.addDir('0-9','http://www.movie25.com/movies/0-9/',1,"%s/art/09.png"%selfAddon.getAddonInfo("path"))
        for i in string.ascii_uppercase:
                main.addDir(i,'http://www.movie25.com/movies/'+i.lower()+'/',1,"%s/art/%s.png"%(selfAddon.getAddonInfo("path"),i.lower()))
        main.GA("None","A-Z")   
def MAIN():
        mashup=126
        notified=os.path.join(main.datapath,str(mashup))
        if not os.path.exists(notified):
            open(notified,'w').write('version="%s",'%mashup)
            dialog = xbmcgui.Dialog()
            ok=dialog.ok('[B]Attention!!![/B]', 'I have been finding problems in the plugin', 'and no one reports it. Please report issues','at xbmchub.com or tweet @mashupxbmc')
            ok=dialog.ok('[B]VERSION 1.2.6[/B]', 'Please checkout the changes in the following sections','Live, Youtube Kids and BuiltIn Plugins.', 'Thanks and Enjoy the plugin')
            mashup=mashup-1
            notified=os.path.join(main.datapath,str(mashup))
            if  os.path.exists(notified):
                os.remove(notified)
        main.addDir('Search','http://www.movie25.com/',420,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
        main.addDir("My Fav's",'http://www.movie25.com/',10,"%s/art/fav.png"%selfAddon.getAddonInfo("path"))
        main.addDir('A-Z','http://www.movie25.com/',6,"%s/art/AZ.png"%selfAddon.getAddonInfo("path"))
        main.addDir('New Releases','http://www.movie25.com/movies/new-releases/',1,"%s/art/new.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Added','http://www.movie25.com/movies/latest-added/',1,"%s/art/latest.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Featured Movies','http://www.movie25.com/movies/featured-movies/',1,"%s/art/feat.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Most Viewed','http://www.movie25.com/movies/most-viewed/',1,"%s/art/view.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Most Voted','http://www.movie25.com/movies/most-voted/',1,"%s/art/vote.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Genre','http://www.movie25.com/',2,"%s/art/genre.png"%selfAddon.getAddonInfo("path"))
        main.addDir('By Year','http://www.movie25.com/',7,"%s/art/year.png"%selfAddon.getAddonInfo("path"))
        main.addDir('HD Movies','http://oneclickwatch.org/category/movies/',33,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('3D Movies','3D',34,"%s/art/3d.png"%selfAddon.getAddonInfo("path"))
        main.addDir('International','http://www.movie25.com/',36,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        main.addDir('TV Latest','http://www.movie25.com/',27,"%s/art/tv2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Live Streams','http://www.movie25.com/',115,"%s/art/live.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Built in Plugins','http://www.movie25.com/',500,"%s/art/plugins.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Sports','http://www.movie25.com/',43,"%s/art/sportsec2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Adventure','http://www.movie25.com/',63,"%s/art/adv2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Kids Zone','http://www.movie25.com/',76,"%s/art/kidzone2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Documentaries','http://www.movie25.com/',85,"%s/art/docsec2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Resolver Settings','http://www.movie25.com/',99,"%s/art/resset.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Need Help?','http://www.movie25.com/',100,"%s/art/xbmchub.png"%selfAddon.getAddonInfo("path"))
        main.addSpecial('Contact Mash2k3','http://www.movie25.com/',156,"%s/art/mash2k3info.png"%selfAddon.getAddonInfo("path"))
        main.VIEWSB()
        
def GENRE(url):
        main.addDir('Action','http://www.movie25.com/movies/action/',1,"%s/art/act.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Adventure','http://www.movie25.com/movies/adventure/',1,"%s/art/adv.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Animation','http://www.movie25.com/movies/animation/',1,"%s/art/ani.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Biography','http://www.movie25.com/movies/biography/',1,"%s/art/bio.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Comedy','http://www.movie25.com/movies/comedy/',1,"%s/art/com.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Crime','http://www.movie25.com/movies/crime/',1,"%s/art/cri.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Documentary','http://www.movie25.com/movies/documentary/',1,"%s/art/doc.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Drama','http://www.movie25.com/movies/drama/',1,"%s/art/dra.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Family','http://www.movie25.com/movies/family/',1,"%s/art/fam.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Fantasy','http://www.movie25.com/movies/fantasy/',1,"%s/art/fant.png"%selfAddon.getAddonInfo("path"))
        main.addDir('History','http://www.movie25.com/movies/history/',1,"%s/art/his.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Horror','http://www.movie25.com/movies/horror/',1,"%s/art/hor.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Music','http://www.movie25.com/movies/music/',1,"%s/art/mus.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Musical','http://www.movie25.com/movies/musical/',1,"%s/art/mucl.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Mystery','http://www.movie25.com/movies/mystery/',1,"%s/art/mys.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Romance','http://www.movie25.com/movies/romance/',1,"%s/art/rom.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Sci-Fi','http://www.movie25.com/movies/sci-fi/',1,"%s/art/sci.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Short','http://www.movie25.com/movies/short/',1,"%s/art/sho.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Sport','http://www.movie25.com/movies/sport/',1,"%s/art/sport.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Thriller','http://www.movie25.com/movies/thriller/',1,"%s/art/thr.png"%selfAddon.getAddonInfo("path"))
        main.addDir('War','http://www.movie25.com/movies/war/',1,"%s/art/war.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Western','http://www.movie25.com/movies/western/',1,"%s/art/west.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","Genre")
        main.VIEWSB()
        
def YEAR():
        main.addDir('2013','http://www.movie25.com/search.php?year=2013/',8,"%s/art/year.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2012','http://www.movie25.com/search.php?year=2012/',8,"%s/art/2012.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2011','http://www.movie25.com/search.php?year=2011/',8,"%s/art/2011.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2010','http://www.movie25.com/search.php?year=2010/',8,"%s/art/2010.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2009','http://www.movie25.com/search.php?year=2009/',8,"%s/art/2009.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2008','http://www.movie25.com/search.php?year=2008/',8,"%s/art/2008.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2007','http://www.movie25.com/search.php?year=2007/',8,"%s/art/2007.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2006','http://www.movie25.com/search.php?year=2006/',8,"%s/art/2006.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2005','http://www.movie25.com/search.php?year=2005/',8,"%s/art/2005.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2004','http://www.movie25.com/search.php?year=2004/',8,"%s/art/2004.png"%selfAddon.getAddonInfo("path"))
        main.addDir('2003','http://www.movie25.com/search.php?year=2003/',8,"%s/art/2003.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Enter Year','http://www.movie25.com',23,"%s/art/enteryear.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","Year")
        main.VIEWSB()


    
def TV():
        main.addDir('Latest Episodes (Newmyvideolinks) True HD','TV',34,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Episodes (Rlsmix)[COLOR red](Debrid Only)[/COLOR] True HD','TV',61,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Episodes (Sceper)[COLOR red](Debrid Only)[/COLOR] True HD','http://sceper.ws/home/category/tv-shows',545,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Episodes (iWatchonline)','http://www.iwatchonline.org/tv-show/latest-epsiodes?limit=18',28,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Episodes (Movie1k)','movintv',30,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Episodes (Oneclickwatch)','http://oneclickwatch.org',32,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.addLink('[COLOR red]Back Up Sources[/COLOR]','','')
        main.addDir('Latest 150 Episodes (ChannelCut)','http://www.channelcut.me/last-150',546,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest 100 Episodes (Tv4stream)','http://www.tv4stream.info/last-100-links/',546,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Episodes (Etowns) True HD [COLOR red] Clone Backup of Newmyvideolinks[/COLOR]','TV',548,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","TV-Latest")
        
def TVAll():
        #main.addDir('Watch-Free Series','TV',501,"%s/art/wfs/wsf.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Watchseries.it','TV',572,"%s/art/wfs/watchseries.png"%selfAddon.getAddonInfo("path"))
        main.addDir('BTV Guide','TV',551,"%s/art/wfs/btvguide.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Series Gate','TV',601,"%s/art/wfs/sg.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Extramina','TV',530,"%s/art/wfs/extramina.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Sceper [COLOR red](Debrid Only)[/COLOR]','TV',539,"%s/art/wfs/sceper.png"%selfAddon.getAddonInfo("path"))
        main.addDir('FMA','TV',567,"%s/art/wfs/fma.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","Plugin")

def HD():
        main.addDir('Latest HD Movies (Newmyvideolinks) True HD','http://newmyvideolinks.com',34,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest HD Movies (Dailyfix) True HD','HD',53,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest HD Movies (Starplay) Direct MP4 True HD','http://87.98.161.165/latest.php',57,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest HD Movies (Oneclickmovies)[COLOR red](Debrid Only)[/COLOR] True HD','www.scnsrc.me',55,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest HD Movies (Sceper)[COLOR red](Debrid Only)[/COLOR] True HD','http://sceper.ws/home/category/movies/movies-hdtv-720p',541,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest HD Movies (Oneclickwatch)','http://oneclickwatch.org/category/movies/',25,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        main.addLink('[COLOR red]Back Up Sources[/COLOR]','','')
        main.addDir('Latest HD Movies (Etowns) True HD  [COLOR red]Clone Backup of Newmyvideolinks[/COLOR]','http://go.etowns.net/category/movies/bluray/',548,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","HD")
def INT():
        main.addDir('Latest Indian Subtitled Movies (einthusan)','http://www.einthusan.com',37,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Indian Movies (Movie1k)','movin',30,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Indian Dubbed Movies (Movie1k)','movindub',30,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Asian Subtitled Movies (dramacrazy)','http://www.dramacrazy.net',39,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Latest Spanish Dubbed & Subtitled(ESP) Movies (cinevip)','http://www.cinevip.org/',66,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","INT")

def SPORTS():
        main.addDir('ESPN','http:/espn.com',44,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        main.addDir('TSN','http:/tsn.com',95,"%s/art/tsn.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Fox Soccer  [COLOR red](US ONLY)[/COLOR]','http:/tsn.com',124,"%s/art/foxsoc.png"%selfAddon.getAddonInfo("path"))
        main.addDir('All MMA','mma',537,"%s/art/mma.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Outdoor Channel','http://outdoorchannel.com/',50,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Wild TV','https://www.wildtv.ca/shows',92,"%s/art/wildtv.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","Sports")

def MMA():
        main.addDir('UFC','ufc',59,"%s/art/ufc.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Bellator','BellatorMMA',47,"%s/art/bellator.png"%selfAddon.getAddonInfo("path"))
        main.addDir('MMA Fighting.com','http://www.mmafighting.com/videos',113,"%s/art/mmafig.png"%selfAddon.getAddonInfo("path"))



def UFC():
        main.addDir('UFC.com','ufc',47,"%s/art/ufc.png"%selfAddon.getAddonInfo("path"))
        main.addDir('UFC(Movie25)','ufc',60,"%s/art/ufc.png"%selfAddon.getAddonInfo("path"))
        main.addDir('UFC(Newmyvideolinks)','ufc',103,"%s/art/ufc.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","UFC")

def ADVENTURE():
        main.addDir('Discovery Channel','discovery',631,"%s/art/disco.png"%selfAddon.getAddonInfo("path"))
        main.addDir('National Geographic','ng',70,"%s/art/natgeo.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Military Channel','discovery',80,"%s/art/milcha.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Science Channel','discovery',81,"%s/art/scicha.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Velocity Channel','discovery',82,"%s/art/velo.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Animal Planet','discovery',83,"%s/art/anip.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","Adventure")
        


def KIDZone(murl):
    main.addDir('Disney Jr.','djk',107,"%s/art/disjr.png"%selfAddon.getAddonInfo("path"))
    main.addDir('National Geographic Kids','ngk',71,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
    main.addDir('WB Kids','wbk',77,"%s/art/wb.png"%selfAddon.getAddonInfo("path"))
    main.addDir('Youtube Kids','wbk',84,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    main.GA("None","KidZone")
    main.VIEWSB()
    
def LiveStreams():
        livearea='live'
        notified=os.path.join(main.datapath,str(livearea))
        if not os.path.exists(notified):
            open(notified,'w').write('version="%s",'%livearea)
            dialog = xbmcgui.Dialog()
            ok=dialog.ok('[B]Attention!!![/B]', 'Please be carefull in this section','may have content unsuitable for children','please report at XBMCHUB if XXX content found.')
        main.addDir('Livestation News','http://mobile.livestation.com/',116,"%s/art/livestation.png"%selfAddon.getAddonInfo("path"))
        main.addDir('iLive Streams','ilive',119,"%s/art/ilive.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Desi Streams','desi',129,"%s/art/desistream.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Castalba Streams','castalgba',122,"%s/art/castalba.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Misc. Music Streams','music',127,"%s/art/miscmusic.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Playlists','navi',138,"%s/art/random.png"%selfAddon.getAddonInfo("path"))
        main.addDir('By Country','navi',143,"%s/art/country.png"%selfAddon.getAddonInfo("path"))
        main.GA("None","Live")

################################################################################ XBMCHUB Repo & Hub Maintenance Installer ##########################################################################################################


hubpath = xbmc.translatePath(os.path.join('special://home/addons', ''))
maintenance=os.path.join(hubpath, 'plugin.video.hubmaintenance')



def DownloaderClass(url,dest):
        dp = xbmcgui.DialogProgress()
        dp.create("XBMCHUB...Maintenance","Downloading & Copying File",'')
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
        try:
            percent = min((numblocks*blocksize*100)/filesize, 100)
            print 'Downloaded '+str(percent)+'%'
            dp.update(percent)
        except:
            percent = 100
            dp.update(percent)
        if (dp.iscanceled()): 
            print "DOWNLOAD CANCELLED" # need to get this part working
            return False
        dp.close()
        del dp

if os.path.exists(maintenance)==False: 
        dialog = xbmcgui.Dialog()
        dialog.ok("XBMCHUB TEAM", "This will Install Hub Maintenance Tool.","It is a requirement for Mash Up", "Will take effect after restart.")
        url = 'http://xbmc-hub-repo.googlecode.com/svn/addons/plugin.video.hubmaintenance/plugin.video.hubmaintenance-4.7b.zip'
        path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
        lib=os.path.join(path, 'plugin.video.hubmaintenance-4.7b.zip')
        DownloaderClass(url,lib)
        addonfolder = xbmc.translatePath(os.path.join('special://home/addons',''))
        time.sleep(2)
        xbmc.executebuiltin("XBMC.Extract(%s,%s)"%(lib,addonfolder))



################################################################################ XBMCHUB POPUP ##########################################################################################################


class HUB( xbmcgui.WindowXMLDialog ):
    def __init__( self, *args, **kwargs ):
        self.shut = kwargs['close_time'] 
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        xbmc.executebuiltin( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
                                       
    def onInit( self ):
        xbmc.Player().play('%s/resources/skins/DefaultSkin/media/xbmchub.mp3'%selfA.getAddonInfo('path'))# Music.
        while self.shut > 0:
            time.sleep(1)
            self.shut -= 1
        xbmc.Player().stop()
        self._close_dialog()
                
    def onFocus( self, controlID ): pass
    
    def onClick( self, controlID ): 
        if controlID == 12:
            xbmc.Player().stop()
            self._close_dialog()
        if controlID == 7:
            xbmc.Player().stop()
            self._close_dialog()

    def onAction( self, action ):
        if action in [ 5, 6, 7, 9, 10, 92, 117 ] or action.getButtonCode() in [ 275, 257, 261 ]:
            xbmc.Player().stop()
            self._close_dialog()

    def _close_dialog( self ):
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        time.sleep( .4 )
        self.close()
        
def pop():
    xbmc.Player().play('%s/resources/skins/DefaultSkin/media/xbmchub.mp3'%selfAddon.getAddonInfo('path'))
    if xbmc.getCondVisibility('system.platform.ios'):
        if not xbmc.getCondVisibility('system.platform.atv'):
            popup = HUB('hub1.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=11,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%AselfAddon.getAddonInfo('path'))
    if xbmc.getCondVisibility('system.platform.android'):
        popup = HUB('hub1.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=11,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%selfAddon.getAddonInfo('path'))
    else:
        popup = HUB('hub.xml',selfAddon.getAddonInfo('path'),'DefaultSkin',close_time=11,logo_path='%s/resources/skins/DefaultSkin/media/Logo/'%selfAddon.getAddonInfo('path'))
    popup.doModal()
    del popup

################################################################################ Message ##########################################################################################################

def Message():
    help = SHOWMessage()
    help.doModal()
    main.GA("None","Mash2k3Info")
    del help


class SHOWMessage(xbmcgui.Window):
    def __init__(self):
        self.addControl(xbmcgui.ControlImage(0,0,1280,720,"%s/art/infoposter.png"%selfAddon.getAddonInfo("path")))
    def onAction(self, action):
        if action == 92 or action == 10:
            xbmc.Player().stop()
            self.close()

################################################################################ Modes ##########################################################################################################


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
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        MAIN()
       
elif mode==1:
        print ""+url
        movie25.LISTMOVIES(url)
        
elif mode==2:
        print ""+url
        GENRE(url)

elif mode==4:
        print ""+url
        movie25.SEARCH(url)
        
elif mode==420:
        print ""+url
        movie25.Searchhistory()

elif mode==3:
        print ""+url
        movie25.VIDEOLINKS(name,url)

elif mode==5:
        print ""+url
        movie25.PLAY(name,url)

elif mode==6:
        AtoZ()

elif mode==7:
        YEAR()

elif mode==23:
        movie25.ENTYEAR()
        
elif mode==8:
        print ""+url
        movie25.YEARB(url)

elif mode==9:
        print ""+url
        movie25.NEXTPAGE(url)
        
elif mode==10:
        movie25.FAVS()

elif mode==11:
        print ""+url
        movie25.PUTLINKS(name,url)

elif mode==12:
        print ""+url
        movie25.OELINKS(name,url)

elif mode==13:
        print ""+url
        movie25.FNLINKS(name,url)

elif mode==14:
        print ""+url
        movie25.VIDLINKS(name,url)

elif mode==15:
        print ""+url
        movie25.FLALINKS(name,url)

elif mode==16:
        print ""+url
        movie25.NOVLINKS(name,url)

elif mode==17:
        print ""+url
        movie25.UPLINKS(name,url)

elif mode==18:
        print ""+url
        movie25.XVLINKS(name,url)

elif mode==19:
        print ""+url
        movie25.ZOOLINKS(name,url)

elif mode==20:
        print ""+url
        movie25.ZALINKS(name,url)

elif mode==21:
        print ""+url
        movie25.VIDXLINKS(name,url)

elif mode==22:
        print ""+url
        movie25.SOCKLINKS(name,url)

elif mode==24:
        print ""+url
        movie25.NOWLINKS(name,url)

elif mode==25:
        print ""+url
        oneclickwatch.LISTSP(url)

elif mode==26:
        print ""+url
        oneclickwatch.LINKSP(name,url)
        
elif mode==27:
        print ""+url
        TV()

elif mode==28:
        print ""+url
        iwatchonline.LISTTV(url)
        
elif mode==29:
        print ""+url
        iwatchonline.VIDEOLINKST(name,url)

elif mode==30:
        print ""+url
        movie1k.LISTTV2(url)

elif mode==31:
        print ""+url
        movie1k.VIDEOLINKST2(name,url)
        
elif mode==32:
        print ""+url
        oneclickwatch.LISTTV3(url)

elif mode==33:
        print ""+url
        HD()

elif mode==34:
        print ""+url
        newmyvideolinks.LISTSP2(url)

elif mode==35:
        print ""+url
        newmyvideolinks.LINKSP2(name,url)

elif mode==36:
        print ""+url
        INT()

elif mode==37:
        print ""+url
        einthusan.LISTINT(name,url)

elif mode==38:
        print ""+url
        einthusan.LINKINT(name,url)

elif mode==39:
        print ""+url
        dramacrazy.LISTINT2(name,url)

elif mode==40:
        print ""+url
        dramacrazy.LINKINT2(name,url)

elif mode==42:
        print ""+url
        dramacrazy.LOAD_AND_PLAY_VIDEO(url,name)
        
elif mode==43:
        print ""+url
        SPORTS()

elif mode==44:
        print ""+url
        espn.ESPN()
        
elif mode==45:
        print ""+url
        espn.ESPNList(url)

elif mode==46:
        print ""+url
        espn.ESPNLink(name,url)

elif mode==47:
        print ""+url
        youtube.YOUList(name,url)
        
elif mode==48:
        print ""+url
        youtube.YOULink(name,url)

elif mode==50:
        print ""+url
        outdoorch.OC()
        
elif mode==51:
        print ""+url
        outdoorch.OCList(url)

elif mode==52:
        print ""+url
        outdoorch.OCLink(name,url)

elif mode==53:
        print ""+url
        dailyflix.LISTSP3(url)

elif mode==54:
        print ""+url
        dailyflix.LINKSP3(name,url)

elif mode==55:
        print ""+url
        oneclickmoviez.LISTSP4(url)

elif mode==56:
        print ""+url
        oneclickmoviez.LINKSP4(name,url)

elif mode==57:
        print ""+url
        starplay.LISTSP5(url)

elif mode==58:
        print ""+url
        starplay.LINKSP5(name,url)
        
elif mode==59:
        print ""+url
        UFC()
        
elif mode==60:
        print ""+url
        movie25.UFCMOVIE25()

elif mode==61:
        print ""+url
        rlsmix.LISTTV4(url)

elif mode==62:
        print ""+url
        rlsmix.LINKTV4(name,url)

elif mode==63:
        print ""+url
        ADVENTURE()
        
elif mode==631:
        print ""+url
        discovery.DISC()

elif mode==64:
        print ""+url
        discovery.LISTDISC(name,url)

elif mode==65:
        print ""+url
        discovery.LINKDISC(name,url)

elif mode==66:
        print ""+url
        cinevip.LISTINT3(url)

elif mode==67:
        print ""+url
        cinevip.LINKINT3(name,url)

elif mode==68:
        print ""+url
        useme(url)

elif mode==69:
        print ""+url
        useMe(name,url)

elif mode==70:
        print ""+url
        nationalgeo.NG()

elif mode==71:
        print ""+url
        nationalgeo.NGDir(url)

elif mode==72:
        print ""+url
        nationalgeo.LISTNG(url)

elif mode==73:
        print ""+url
        nationalgeo.LISTNG2(url)

elif mode==74:
        print ""+url
        nationalgeo.LINKNG(name,url)

elif mode==75:
        print ""+url
        nationalgeo.LINKNG2(name,url)

elif mode==76:
        print ""+url
        KIDZone(url)
        
elif mode==77:
        print ""+url
        wbkids.WB()
        
elif mode==78:
        print ""+url
        wbkids.LISTWB(url)

elif mode==79:
        print ""+url
        wbkids.LINKWB(name,url)

elif mode==80:
        print ""+url
        discovery.MILIT()
        
elif mode==81:
        print ""+url
        discovery.SCI()

elif mode==82:
        print ""+url
        discovery.VELO()

elif mode==83:
        print ""+url
        discovery.ANIP()

elif mode==84:
        print ""+url
        youtube.YOUKIDS()

elif mode==85:
        print ""+url
        documentary.DOCS()        

elif mode==86:
        print ""+url
        documentary.LISTDOC(url)
        
elif mode==87:
        print ""+url
        documentary.LISTDOC2(url)

elif mode==88:
        print ""+url
        documentary.LINKDOC(name,url)
        
elif mode==89:
        print ""+url
        documentary.LISTDOCPOP(url)

elif mode==90:
        print ""+url
        airaces.LISTAA()

elif mode==91:
        print ""+url
        airaces.PLAYAA(name,url)

elif mode==92:
        print ""+url
        wildtv.WILDTV(url)        

elif mode==93:
        print ""+url
        wildtv.LISTWT(url)
        
elif mode==94:
        print ""+url
        wildtv.LINKWT(name,url)

elif mode==95:
        print ""+url
        tsn.TSNDIR()

elif mode==96:
        print ""+url
        tsn.TSNDIRLIST(url)        

elif mode==97:
        print ""+url
        tsn.TSNLIST(url)
        
elif mode==98:
        print ""+url
        tsn.TSNLINK(name,url)
        
elif mode==99:
        urlresolver.display_settings()
        
elif mode==100:
        pop()
        
elif mode==101:
        newmyvideolinks.SEARCHNEW(url)

elif mode==102:
        newmyvideolinks.SearchhistoryNEW(url)
        
elif mode==103:
        newmyvideolinks.UFCNEW()
        
elif mode==104:
        vice.Vice(url)
        
elif mode==105:
        vice.ViceList(url)

elif mode==106:        
        vice.ViceLink(name,url)        

elif mode==107:
        disneyjr.DISJR()
        
elif mode==108:
        disneyjr.DISJRList(url)

elif mode==109:
        disneyjr.DISJRList2(url)
        
elif mode==110:        
        disneyjr.DISJRLink(name,url)       
        
elif mode==111:
        StrikeFList(url)

elif mode==112:        
        StrikeFLink(name,url)   

elif mode==113:
        mmafighting.MMAFList(url)

elif mode==114:        
        mmafighting.MMAFLink(name,url)   
elif mode==115:
        LiveStreams()
elif mode==116:
        livestation.LivestationList(url)
elif mode==117:
        livestation.LivestationLink(name,url)
elif mode==118:
        livestation.LivestationLink2(name,url)

elif mode==119:
        ilive.iLive()
elif mode==120:
        ilive.iLiveList(url)
elif mode==121:
        ilive.iLiveLink(name,url)

elif mode==122:
        castalba.CastalbaList(url)
elif mode==123:
        castalba.CastalbaLink(name,url)

elif mode==124:
        foxsoccer.FOXSOC()
elif mode==125:
        foxsoccer.FOXSOCList(url)
elif mode==126:
        foxsoccer.FOXSOCLink(name,url)

elif mode==127:
        musicstreams.MUSICSTREAMS()
elif mode==128:
        main.Clearhistory(url)

elif mode==129:
        desistreams.DESISTREAMS()
elif mode==130:
        desistreams.DESISTREAMSList(url)
elif mode==131:
        desistreams.DESISTREAMSLink(name,url)
        
elif mode==132:
        movie1k.SearchhistoryMovie1k()
elif mode==133:
        movie1k.SEARCHMovie1k(url)
elif mode==134:
        oneclickwatch.PLAYOCW(name,url)

elif mode==135:
        oneclickwatch.VIDEOLINKST3(name,url)

elif mode==136:
        rlsmix.SearchhistoryRlsmix()

elif mode==137:
        rlsmix.SEARCHRlsmix(url)


elif mode==138:
       naviplaylists.playlists()

elif mode==139:
        naviplaylists.playlistList(url)

elif mode==140:
        naviplaylists.playlistList2(url)

elif mode==141:
        naviplaylists.playlistList3(url)

elif mode==142:
        naviplaylists.playlistList4(url)

elif mode==149:
        naviplaylists.playlistList5(url)


elif mode==143:
        countries.COUNTRIES()

elif mode==144:
        countries.COUNTRIESList(url)


elif mode==145:
        print ""+url
        movie25.MOVSHLINKS(name,url)

elif mode==146:
        print ""+url
        movie25.DIVXSLINKS(name,url)

elif mode==147:
        print ""+url
        movie25.SSIXLINKS(name,url)

elif mode==148:
        print ""+url
        movie25.GORLINKS(name,url)

elif mode==150:
        print ""+url
        movie25.MOVPLINKS(name,url)

elif mode==151:
        print ""+url
        movie25.DACLINKS(name,url)

elif mode==152:
        print ""+url
        movie25.VWEEDLINKS(name,url)

elif mode==153:
        print ""+url
        movie25.MOVDLINKS(name,url)

elif mode==154:
        print ""+url
        movie25.MOVRLINKS(name,url)

elif mode==155:
        print ""+url
        movie25.BUPLOADSLINKS(name,url)

elif mode==156:
        print ""+url
        Message()

elif mode==157:
        print ""+url
        movie25.PLAYEDLINKS(name,url)


        
elif mode==500:
        TVAll()        

elif mode==501:
        MAINWFS()
        
elif mode==528:
        print ""+url
        LISTEpi(url)

elif mode==506:
        print ""+url
        LISTShows(url)

elif mode==507:
        print ""+url
        LISTSeason(name,url)

elif mode==508:
        print ""+url
        LISTEpilist(name,url)

elif mode==511:
        print ""+url
        LISTPop(url)

elif mode==502:
        print ""+url
        GENREWFS(url)

elif mode==504:
        print ""+url
        SEARCHWFS(url)
        
elif mode==522:
        print ""+url
        Searchhistorywfs()

elif mode==503:
        print ""+url
        VIDEOLINKSWFS(name,url)

elif mode==505:
        print ""+url
        YEARWFS()
        
        
elif mode==510:
        print ""+url
        AtoZWFS()
        
elif mode==527:
        print ""+url
        GetMetAll()

elif mode==530:
        extramina.MAINEXTRA()

elif mode==531:
        print ""+url
        extramina.LISTEXAZ(name,url)

elif mode==532:
        print ""+url
        extramina.LISTEXrecent(url)


elif mode==533:
        print ""+url
        extramina.GENREEXTRA(url)

elif mode==534:
        print ""+url
        extramina.SEARCHEXTRA(url)
        
elif mode==535:
        print ""+url
        extramina.SearchhistoryEXTRA()

elif mode==536:
        print ""+url
        extramina.VIDEOLINKSEXTRA(name,url)
                
elif mode==538:
        print ""+url
        extramina.AtoZEXTRA()

elif mode==537:
        print ""+url
        MMA()        

elif mode==539:
        sceper.MAINSCEPER()
        
elif mode==540:
        sceper.MORTSCEPER(url)

elif mode==541:
        print ""+url
        sceper.LISTSCEPER(name,url)
        
elif mode==545:
        print ""+url
        sceper.LISTSCEPER2(name,url)

elif mode==542:
        print ""+url
        sceper.SEARCHSCEPER(url)
        
elif mode==543:
        print ""+url
        sceper.SearchhistorySCEPER()

elif mode==544:
        print ""+url
        sceper.VIDEOLINKSSCEPER(name,url)

elif mode==546:
        print ""+url
        backuptv.CHANNELCList(url)

elif mode==547:
        print ""+url
        backuptv.CHANNELCLink(name,url)

elif mode==548:
        print ""+url
        newmyvideolinks.LISTEtowns(url)

elif mode==549:
        newmyvideolinks.SEARCHEtowns(url)

elif mode==550:
        newmyvideolinks.SearchhistoryEtowns(url)

elif mode==551:
        btvguide.MAINBTV()

elif mode==552:
        print ""+url
        btvguide.LISTShowsBTV(url)

elif mode==553:
        print ""+url
        btvguide.LISTSeasonBTV(name,url)

elif mode==554:
        print ""+url
        btvguide.LISTEpilistBTV(name,url)

elif mode==555:
        print ""+url
        btvguide.LISTPopBTV(url)

elif mode==556:
        print ""+url
        btvguide.GENREBTV(url)

elif mode==557:
        print ""+url
        btvguide.SEARCHBTV(url)
        
elif mode==558:
        print ""+url
        btvguide.SearchhistoryBTV()

elif mode==559:
        print ""+url
        btvguide.VIDEOLINKSBTV(name,url)     
        
elif mode==560:
        print ""+url
        btvguide.AtoZBTV()
        
elif mode==561:
        print ""+url
        btvguide.AllShowsBTV(url)
elif mode==562:
        print ""+url
        btvguide.LISTPOPShowsBTV(url)

elif mode==563:
        print ""+url
        btvguide.PLAYBTV(name,url)
elif mode==564:
        print ""+url
        btvguide.LISTNEWShowsBTV(url)
elif mode==565:
        print ""+url
        btvguide.LISTNEWEpiBTV(url)

elif mode==566:
        print ""+url
        btvguide.DECADEBTV(url)
        

elif mode==567:
        print ""+url
        fma.MAINFMA()

elif mode==568:
        print ""+url
        fma.LISTFMA(url)
        
elif mode==569:
        print ""+url
        fma.LINKFMA(name,url)
        
elif mode==570:
        print ""+url
        fma.AtoZFMA()
        
elif mode==571:
        print ""+url
        fma.GENREFMA(url)

elif mode==572:
        print ""+url
        watchseries.MAINWATCHS()

elif mode==573:
        print ""+url
        watchseries.LISTWATCHS(url)

elif mode==574:
        print ""+url
        watchseries.LINKWATCHS(name,url)

elif mode==575:
        print ""+url
        watchseries.LISTHOST(name,url)

elif mode==576:
        print ""+url
        watchseries.LISTSHOWWATCHS(url)

elif mode==577:
        print ""+url
        watchseries.AtoZWATCHS()
        
elif mode==578:
        print ""+url
        watchseries.LISTWATCHSEASON(name, url)

elif mode==579:
        print ""+url
        watchseries.LISTWATCHEPISODE(name, url)
        
elif mode==580:
        print ""+url
        watchseries.POPULARWATCHS(url)

elif mode==581:
        print ""+url
        watchseries.SearchhistoryWS()
        
elif mode==582:
        print ""+url
        watchseries.SEARCHWS(url)

elif mode==583:
        print ""+url
        watchseries.GENREWATCHS()

        

elif mode==601:
        seriesgate.MAINSG()
        
elif mode==602:
        print ""+url
        seriesgate.LISTEpiSG(url)

elif mode==603:
        print ""+url
        seriesgate.LISTShowsSG(url)

elif mode==604:
        print ""+url
        seriesgate.LISTSeasonSG(name,url)

elif mode==605:
        print ""+url
        seriesgate.LISTEpilistSG(name,url)

elif mode==606:
        print ""+url
        seriesgate.LISTPopSG(url)

elif mode==607:
        print ""+url
        seriesgate.GENRESG(url)

elif mode==608:
        print ""+url
        seriesgate.SEARCHSG(url)
        
elif mode==612:
        print ""+url
        seriesgate.SearchhistorySG()

elif mode==609:
        print ""+url
        seriesgate.VIDEOLINKSSG(name,url)

     
        
elif mode==610:
        print ""+url
        seriesgate.AtoZSG()
        
elif mode==611:
        print ""+url
        seriesgate.AllShows(url)

        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
