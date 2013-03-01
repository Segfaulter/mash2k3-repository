#-*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib,string
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urlresolver
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net as net
from metahandler import metahandlers
import datetime,time

#Movie25.com - by Mash2k3 2012.

Mainurl ='http://www.movie25.com/movies/'
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
grab = metahandlers.MetaData(preparezip = False)
addon = Addon(addon_id)
datapath = addon.get_profile()
#datapath = os.path.join(xbmc.translatePath('special://profile/addon_data/' + addon_id), '')
if selfAddon.getSetting('visitor_ga')=='':
    from random import randint
    selfAddon.setSetting('visitor_ga',str(randint(0, 0x7fffffff)))

VERSION = "1.2.0"
PATH = "Movie25-"            
UATRACK="UA-38312513-1" 


def OPENURL(url):
        print "openurl = " + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def FAVS():
        favpath=os.path.join(datapath,'Favourites')
        moviefav=os.path.join(favpath,'Movies')
        FavFile=os.path.join(moviefav,'Fav')
        if os.path.exists(FavFile):
                Favs=re.compile('url="(.+?)",name="(.+?)"').findall(open(FavFile,'r').read())
                for url,mname in Favs:
                        namelen=len(mname)
                        nam= namelen- 5
                        year = mname[nam:namelen-1]
                        name= mname[0:namelen-6]
                        name=name.replace('-','').replace('&','').replace('acute;','')

                        url=url.replace('(','').replace('[','')
                        if url[0]=='m':
                                url='http://movie25.com/'+url
                        link=OPENURL(url)
                        match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_blank">').findall(link)
                        for thumb in match:
                                addInfo(name+'('+year+')',url,3,thumb,'',year)
                xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
                VIEWS()
        else: xbmc.executebuiltin("XBMC.Notification([B][COLOR green]Movies25[/COLOR][/B],[B]You Have No Saved Favourites[/B],5000,"")")
        GA("None","Fav")

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
                                xbmc.executebuiltin("Container.SetViewMode(501)")
                        elif selfAddon.getSetting("con-view") == "4":
                                xbmc.executebuiltin("Container.SetViewMode(508)")
                        elif selfAddon.getSetting("con-view") == "5":
                                xbmc.executebuiltin("Container.SetViewMode(504)")
                        elif selfAddon.getSetting("con-view") == "6":
                                xbmc.executebuiltin("Container.SetViewMode(503)")
                        elif selfAddon.getSetting("con-view") == "7":
                                xbmc.executebuiltin("Container.SetViewMode(515)")
                        return
                elif selfAddon.getSetting("choose-skin") == "false":
                        if selfAddon.getSetting("xpr-view") == "0":
                                xbmc.executebuiltin("Container.SetViewMode(50)")
                        elif selfAddon.getSetting("xpr-view") == "1":
                                xbmc.executebuiltin("Container.SetViewMode(52)")
                        elif selfAddon.getSetting("xpr-view") == "2":
                                xbmc.executebuiltin("Container.SetViewMode(501)")
                        elif selfAddon.getSetting("xpr-view") == "3":
                                xbmc.executebuiltin("Container.SetViewMode(55)")
                        elif selfAddon.getSetting("xpr-view") == "4":
                                xbmc.executebuiltin("Container.SetViewMode(54)")
                        elif selfAddon.getSetting("xpr-view") == "5":
                                xbmc.executebuiltin("Container.SetViewMode(60)")
                        elif selfAddon.getSetting("xpr-view") == "6":
                                xbmc.executebuiltin("Container.SetViewMode(53)")
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
        
def AtoZ():
        addDir('0-9','http://www.movie25.com/movies/0-9/',1,"%s/art/09.png"%selfAddon.getAddonInfo("path"))
        for i in string.ascii_uppercase:
                addDir(i,'http://www.movie25.com/movies/'+i.lower()+'/',1,"%s/art/%s.png"%(selfAddon.getAddonInfo("path"),i.lower()))
        GA("None","A-Z")   
def MAIN():
        addDir('Search','http://www.movie25.com/',420,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
        addDir("My Fav's",'http://www.movie25.com/',10,"%s/art/fav.png"%selfAddon.getAddonInfo("path"))
        addDir('A-Z','http://www.movie25.com/',6,"%s/art/AZ.png"%selfAddon.getAddonInfo("path"))
        addDir('New Releases','http://www.movie25.com/movies/new-releases/',1,"%s/art/new.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Added','http://www.movie25.com/movies/latest-added/',1,"%s/art/latest.png"%selfAddon.getAddonInfo("path"))
        addDir('Featured Movies','http://www.movie25.com/movies/featured-movies/',1,"%s/art/feat.png"%selfAddon.getAddonInfo("path"))
        addDir('Most Viewed','http://www.movie25.com/movies/most-viewed/',1,"%s/art/view.png"%selfAddon.getAddonInfo("path"))
        addDir('Most Voted','http://www.movie25.com/movies/most-voted/',1,"%s/art/vote.png"%selfAddon.getAddonInfo("path"))
        addDir('Genre','http://www.movie25.com/',2,"%s/art/genre.png"%selfAddon.getAddonInfo("path"))
        addDir('By Year','http://www.movie25.com/',7,"%s/art/year.png"%selfAddon.getAddonInfo("path"))
        addDir('HD Movies','http://oneclickwatch.org/category/movies/',33,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        addDir('3D Movies','3D',34,"%s/art/3d.png"%selfAddon.getAddonInfo("path"))
        addDir('International','http://www.movie25.com/',36,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        addDir('TV Latest','http://www.movie25.com/',27,"%s/art/tv2.png"%selfAddon.getAddonInfo("path"))
        addDir('Built in Plugins','http://www.movie25.com/',500,"%s/art/plugins.png"%selfAddon.getAddonInfo("path"))
        addDir('Sports','http://www.movie25.com/',43,"%s/art/sportsec2.png"%selfAddon.getAddonInfo("path"))
        addDir('Adventure','http://www.movie25.com/',63,"%s/art/adv2.png"%selfAddon.getAddonInfo("path"))
        addDir('Kids Zone','http://www.movie25.com/',76,"%s/art/kidzone2.png"%selfAddon.getAddonInfo("path"))
        addDir('Documentaries','http://www.movie25.com/',85,"%s/art/docsec2.png"%selfAddon.getAddonInfo("path"))
        addDir('Resolver Settings','http://www.movie25.com/',99,"%s/art/resset.png"%selfAddon.getAddonInfo("path"))
        addDir('Need Help?','http://www.movie25.com/',100,"%s/art/xbmchub.png"%selfAddon.getAddonInfo("path"))
        VIEWSB()
        
def GENRE(url):
        addDir('Action','http://www.movie25.com/movies/action/',1,"%s/art/act.png"%selfAddon.getAddonInfo("path"))
        addDir('Adventure','http://www.movie25.com/movies/adventure/',1,"%s/art/adv.png"%selfAddon.getAddonInfo("path"))
        addDir('Animation','http://www.movie25.com/movies/animation/',1,"%s/art/ani.png"%selfAddon.getAddonInfo("path"))
        addDir('Biography','http://www.movie25.com/movies/biography/',1,"%s/art/bio.png"%selfAddon.getAddonInfo("path"))
        addDir('Comedy','http://www.movie25.com/movies/comedy/',1,"%s/art/com.png"%selfAddon.getAddonInfo("path"))
        addDir('Crime','http://www.movie25.com/movies/crime/',1,"%s/art/cri.png"%selfAddon.getAddonInfo("path"))
        addDir('Documentary','http://www.movie25.com/movies/documentary/',1,"%s/art/doc.png"%selfAddon.getAddonInfo("path"))
        addDir('Drama','http://www.movie25.com/movies/drama/',1,"%s/art/dra.png"%selfAddon.getAddonInfo("path"))
        addDir('Family','http://www.movie25.com/movies/family/',1,"%s/art/fam.png"%selfAddon.getAddonInfo("path"))
        addDir('Fantasy','http://www.movie25.com/movies/fantasy/',1,"%s/art/fant.png"%selfAddon.getAddonInfo("path"))
        addDir('History','http://www.movie25.com/movies/history/',1,"%s/art/his.png"%selfAddon.getAddonInfo("path"))
        addDir('Horror','http://www.movie25.com/movies/horror/',1,"%s/art/hor.png"%selfAddon.getAddonInfo("path"))
        addDir('Music','http://www.movie25.com/movies/music/',1,"%s/art/mus.png"%selfAddon.getAddonInfo("path"))
        addDir('Musical','http://www.movie25.com/movies/musical/',1,"%s/art/mucl.png"%selfAddon.getAddonInfo("path"))
        addDir('Mystery','http://www.movie25.com/movies/mystery/',1,"%s/art/mys.png"%selfAddon.getAddonInfo("path"))
        addDir('Romance','http://www.movie25.com/movies/romance/',1,"%s/art/rom.png"%selfAddon.getAddonInfo("path"))
        addDir('Sci-Fi','http://www.movie25.com/movies/sci-fi/',1,"%s/art/sci.png"%selfAddon.getAddonInfo("path"))
        addDir('Short','http://www.movie25.com/movies/short/',1,"%s/art/sho.png"%selfAddon.getAddonInfo("path"))
        addDir('Sport','http://www.movie25.com/movies/sport/',1,"%s/art/sport.png"%selfAddon.getAddonInfo("path"))
        addDir('Thriller','http://www.movie25.com/movies/thriller/',1,"%s/art/thr.png"%selfAddon.getAddonInfo("path"))
        addDir('War','http://www.movie25.com/movies/war/',1,"%s/art/war.png"%selfAddon.getAddonInfo("path"))
        addDir('Western','http://www.movie25.com/movies/western/',1,"%s/art/west.png"%selfAddon.getAddonInfo("path"))
        GA("None","Genre")
        VIEWSB()
def YEAR():
        addDir('2013','http://www.movie25.com/search.php?year=2013/',8,"%s/art/year.png"%selfAddon.getAddonInfo("path"))
        addDir('2012','http://www.movie25.com/search.php?year=2012/',8,"%s/art/2012.png"%selfAddon.getAddonInfo("path"))
        addDir('2011','http://www.movie25.com/search.php?year=2011/',8,"%s/art/2011.png"%selfAddon.getAddonInfo("path"))
        addDir('2010','http://www.movie25.com/search.php?year=2010/',8,"%s/art/2010.png"%selfAddon.getAddonInfo("path"))
        addDir('2009','http://www.movie25.com/search.php?year=2009/',8,"%s/art/2009.png"%selfAddon.getAddonInfo("path"))
        addDir('2008','http://www.movie25.com/search.php?year=2008/',8,"%s/art/2008.png"%selfAddon.getAddonInfo("path"))
        addDir('2007','http://www.movie25.com/search.php?year=2007/',8,"%s/art/2007.png"%selfAddon.getAddonInfo("path"))
        addDir('2006','http://www.movie25.com/search.php?year=2006/',8,"%s/art/2006.png"%selfAddon.getAddonInfo("path"))
        addDir('2005','http://www.movie25.com/search.php?year=2005/',8,"%s/art/2005.png"%selfAddon.getAddonInfo("path"))
        addDir('2004','http://www.movie25.com/search.php?year=2004/',8,"%s/art/2004.png"%selfAddon.getAddonInfo("path"))
        addDir('2003','http://www.movie25.com/search.php?year=2003/',8,"%s/art/2003.png"%selfAddon.getAddonInfo("path"))
        addDir('Enter Year','http://www.movie25.com',23,"%s/art/enteryear.png"%selfAddon.getAddonInfo("path"))
        GA("None","Year")
        VIEWSB()

def ENTYEAR():
        keyb = xbmc.Keyboard('', 'Search Movies')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                if encode < '2014' and encode > '1900':
                     surl='http://www.movie25.com/search.php?year='+encode+'/'
                     YEARB(surl)
                else:
                    dialog = xbmcgui.Dialog()
                    ret = dialog.ok('Wrong Entry', 'Must enter year in four digit format like 1999','Enrty must be between 1900 and 2014')
    
def TV():
        addDir('Latest Episodes (Newmyvideolinks) True HD','TV',34,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Episodes (Rlsmix)[COLOR red](Real Debrid Only)[/COLOR] True HD','TV',61,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Episodes (iWatchonline)','http://www.iwatchonline.org/tv-show/latest-epsiodes?limit=18',28,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Episodes (Movie1k)','http://www.movie1k.org',30,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Episodes (Oneclickwatch)','http://oneclickwatch.org',32,"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        GA("None","TV-Latest")
        
def TVAll():
        addDir('Watch-Free Series','TV',501,"%s/art/wfs/wsf.png"%selfAddon.getAddonInfo("path"))
        addDir('Series Gate','TV',601,"%s/art/wfs/sg.png"%selfAddon.getAddonInfo("path"))
        GA("None","Plugin")

def HD():
        addDir('Latest HD Movies (Newmyvideolinks) True HD','http://newmyvideolinks.com/category/movies/bluray/',34,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest HD Movies (Dailyfix) True HD','HD',53,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest HD Movies (Starplay) Direct MP4 True HD','http://87.98.161.165/latest.php',57,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest HD Movies (Oneclickmovies)[COLOR red](Real Debrid Only)[/COLOR] True HD','www.scnsrc.me',55,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest HD Movies (Oneclickwatch)','http://oneclickwatch.org/category/movies/',25,"%s/art/hd2.png"%selfAddon.getAddonInfo("path"))
        GA("None","HD")
def INT():
        addDir('Latest Indian Subtitled Movies (einthusan)','http://www.einthusan.com',37,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Asian Subtitled Movies (dramacrazy)','http://www.dramacrazy.net',39,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Spanish Dubbed & Subtitled(ESP) Movies (cinevip)','http://www.cinevip.org/',66,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Russian Dubbed Movies (Kino-live)','http://kino-live.org/hq/',68,"%s/art/intl.png"%selfAddon.getAddonInfo("path"))
        GA("None","INT")

def SPORTS():
        addDir('ESPN','http:/espn.com',44,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('UFC','ufc',59,"%s/art/ufc.png"%selfAddon.getAddonInfo("path"))
        addDir('Outdoor Channel','http://outdoorchannel.com/',50,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        GA("None","Sports")

def ESPN():
        addDir('NFL','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=3520083',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('NBA','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=3631756',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('NCAAM','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=3707293',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('NCAAF','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=3573504',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('TENNIS','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=4830039',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('MLB','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=3573503',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('MMA','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=3685710',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('BOXING','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=4117562',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('NHL','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=3631758',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('GOLF','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=4331063',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        addDir('MOTORSPORTS','http://m.espn.go.com/mobilecache/general/apps/videohub/moreVideos?xhr=1&pageNum=1&numResults=100&trackingPage=espntablet%3Ageneral%3Avideo&format=json&cid=3879997',45,"%s/art/espn.png"%selfAddon.getAddonInfo("path"))
        GA("Sports","ESPN")

def OC():
        addDir('All Videos','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        addDir('Hunting','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Hunting',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        addDir('Fishing','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Fishing',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        addDir('Shooting','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Shooting',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        addDir('Off Road','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Off-Road',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        addDir('Adventure','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Adventure',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        addDir('Conservation','http://feed.theplatform.com/f/MTQ3NTE2MjMwOA/swTdEQGW9CKd?byCategories=Outdoor%20Channel/Conservation',51,"%s/art/OC.png"%selfAddon.getAddonInfo("path"))
        GA("Sports","OutChannel")


def UFC():
        addDir('UFC.com','ufc',47,"%s/art/ufc.png"%selfAddon.getAddonInfo("path"))
        addDir('UFC(Movie25)','ufc',60,"%s/art/ufc.png"%selfAddon.getAddonInfo("path"))
        addDir('UFC(Newmyvideolinks)','ufc',103,"%s/art/ufc.png"%selfAddon.getAddonInfo("path"))
        GA("None","UFC")

def ADVENTURE():
        addDir('Discovery Channel','discovery',631,"%s/art/disco.png"%selfAddon.getAddonInfo("path"))
        addDir('National Geographic','ng',70,"%s/art/natgeo.png"%selfAddon.getAddonInfo("path"))
        addDir('Military Channel','discovery',80,"%s/art/milcha.png"%selfAddon.getAddonInfo("path"))
        addDir('Science Channel','discovery',81,"%s/art/scicha.png"%selfAddon.getAddonInfo("path"))
        addDir('Velocity Channel','discovery',82,"%s/art/velo.png"%selfAddon.getAddonInfo("path"))
        addDir('Animal Planet','discovery',83,"%s/art/anip.png"%selfAddon.getAddonInfo("path"))
        GA("None","Adventure")
        
def DISC():
        addDir('AFRICA','http://dsc.discovery.com/services/taxonomy/Africa%20the%20Series/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/africa-show-carousel-badge-130x97.jpg')
        addDir('ALASKA: THE LAST FRONTIER','http://dsc.discovery.com/services/taxonomy/ALASKA:%20THE%20LAST%20FRONTIER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/alaska_badge_130x97.jpg')
        addDir('AMERICAN CHOPPER','http://dsc.discovery.com/services/taxonomy/AMERICAN%20CHOPPER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/american-chopper-badge.jpg')
        addDir('AMERICAN GUNS','http://dsc.discovery.com/services/taxonomy/AMERICAN%20GUNS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/american-guns-show-carousel-badge.jpg')
        addDir('AMISH MAFIA','http://dsc.discovery.com/services/taxonomy/AMISH%20MAFIA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/amish-mafia-show-carousel-badge-130x97.jpg')
        addDir('AUCTION KINGS','http://dsc.discovery.com/services/taxonomy/AUCTION%20KINGS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/auction-kings-show-carousel-badge.jpg')
        addDir('BERING SEA GOLD','http://dsc.discovery.com/services/taxonomy/BERING%20SEA%20GOLD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/bsg-full-ep.jpg')
        addDir('BERING SEA GOLD: UNDER THE ICE','http://dsc.discovery.com/services/taxonomy/BERING%20SEA%20GOLD%20UNDER%20THE%20ICE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/new-bsg-under-the-ice-show-carousel-badge.jpg')
        addDir('BREAKING MAGIC','http://dsc.discovery.com/services/taxonomy/BREAKING%20MAGIC/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/breaking-magic-badge.jpg')
        addDir('CASH CAB','http://dsc.discovery.com/services/taxonomy/CASH%20CAB/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/cash-cab-show-carousel-badge.jpg')
        addDir('CURIOSITY','http://dsc.discovery.com/services/taxonomy/CURIOSITY/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/curiosity-show-carousel-badge.jpg')
        addDir('DEADLIEST CATCH','http://dsc.discovery.com/services/taxonomy/DEADLIeST%20CATCH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/deadliest-catch-show-carousel-badge.jpg')
        addDir('DIRTY JOBS','http://dsc.discovery.com/services/taxonomy/DIRTY%20JOBS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/dirty-jobs-show-carousel-badge.jpg')
        addDir('DUAL SURVIVAL','http://dsc.discovery.com/services/taxonomy/DUAL%20SURVIVAL/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/dual-survivor-130x97.jpg')
        addDir('FAST N LOUD',"http://dsc.discovery.com/services/taxonomy/FAST%20N'%20LOUD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/fast-n-loud-show-carousel-badge.jpg')
        addDir('FLYING WILD ALASKA ','http://dsc.discovery.com/services/taxonomy/FLYING%20WILD%20ALASKA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/flying-wild-alaska-show-carousel-badge.jpg')
        addDir('FROZEN PLANET','http://dsc.discovery.com/services/taxonomy/FROZEN%20PLANET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/frozen-planet-show-carousel-badge.jpg')
        addDir('GOLD RUSH','http://dsc.discovery.com/services/taxonomy/GOLD%20RUSH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/gold-rush-show-carousel-badge.jpg')
        addDir('HOW BOOZE BUILT AMERICA','http://dsc.discovery.com/services/taxonomy/HOW%20BOOZE%20BUILT%20AMERICA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/hbba-show-carousel-badge-130x97.jpg')
        addDir('JESSE JAMES: OUTLAW GARAGE','http://dsc.discovery.com/services/taxonomy/OUTLAW%20GARAGE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/outlawgarage_130x97.jpg')
        addDir('JUNGLE GOLD','http://dsc.discovery.com/services/taxonomy/JUNGLE%20GOLD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/jungle-gold-show-carousel-badge.jpg')
        addDir("KURT SUTTER'S OUTLAW EMPIRES","http://dsc.discovery.com/services/taxonomy/KURT%20SUTTER'S%20OUTLAW%20EMPIRES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/outlaw-empires-show-carousel-badge.jpg')
        addDir('LIFE','http://dsc.discovery.com/services/taxonomy/LIFE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/life-show-carousel-badge.jpg')
        addDir('MAN VS. WILD','http://dsc.discovery.com/services/taxonomy/MAN%20VS%20WILD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/man-vs-wild-show-carousel-badge.jpg')
        addDir('MAYAN DOOMSDAY PROPHECY','http://dsc.discovery.com/services/taxonomy/Mayan%20Doomsday%20Prophecy%20Videos/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mayan-doomsday-130x97.jpg')
        addDir('MOONSHINERS','http://dsc.discovery.com/services/taxonomy/MOONSHINERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/moonshiners-full-episodes.jpg')
        addDir('MYTHBUSTERS','http://dsc.discovery.com/services/taxonomy/MYTHBUSTERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mythbusters-show-carousel-badge.jpg')
        addDir('ONE CAR TOO FAR)','http://dsc.discovery.com/services/taxonomy/ONE%20CAR%20TOO%20FAR/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/one-car-too-far-show-carousel-badge.jpg')
        addDir('PLANET EARTH','http://dsc.discovery.com/services/taxonomy/PLANET%20EARTH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/show-badge-planet-earth.jpg')
        addDir('PROPERTY WARS','http://dsc.discovery.com/services/taxonomy/PROPERTY%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/show-badge-property-wars-130x97.jpg')
        addDir('SHARK WEEK','http://dsc.discovery.com/services/taxonomy/SHARK%20WEEK/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/show-badge-sharkweek-130x97.jpg')
        addDir('SHIPWRECK MEN','http://dsc.discovery.com/services/taxonomy/SHIPWRECK%20MEN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge_130x97_full2.jpg')
        addDir('SONS OF GUNS','http://dsc.discovery.com/services/taxonomy/SONS%20OF%20GUNS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sons-of-guns-show-carousel-badge.jpg')
        addDir('STORM CHASERS','http://dsc.discovery.com/services/taxonomy/STORM%20CHASERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/storm-chasers-show-carousel-badge.jpg')
        addDir('SURVIVORMAN','http://dsc.discovery.com/services/taxonomy/SURVIVORMAN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/survivorman-130x97.jpg')
        addDir('TEXAS CAR WARS','http://dsc.discovery.com/services/taxonomy/TEXAS%20CAR%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/texas-car-wars-show-carousel-badge.jpg')
        addDir('THE DEVILS RIDE','http://dsc.discovery.com/services/taxonomy/THE%20DEVILS%20RIDE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/devils-ride-show-carousel-badge.jpg')
        addDir('WINGED PLANET','http://dsc.discovery.com/services/taxonomy/WINGED%20PLANET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/winged-planet-130x97.jpg')
        addDir('YUKON MEN','http://dsc.discovery.com/services/taxonomy/YUKON%20MEN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/yukon-men-130-97.jpg')
        GA("Adventure","Discovery")
        VIEWSB()

def ANIP():
        addDir("AMERICA'S CUTEST PET","http://animal.discovery.com/services/taxonomy/AMERICA'S%20CUTEST%20PET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/americascutestpet-130x97.jpg')
        addDir('AMERICAN STUFFERS','http://animal.discovery.com/services/taxonomy/AMERICAN%20STUFFERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/americanstuffers-130x97.jpg')
        addDir('ANIMAL COPS','http://animal.discovery.com/services/taxonomy/ANIMAL%20COPS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/animalcops-130x97.jpg')
        addDir('BAD DOG','http://animal.discovery.com/services/taxonomy/BAD%20DOG!/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/baddog-130x97.jpg')
        addDir('BATTLEGROUND: RHINO WARS','http://animal.discovery.com/services/taxonomy/BATTLEGROUND:%20RHINO%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/rhino-wars-130x97.jpg')
        addDir('CALL OF THE WILDMAN','http://animal.discovery.com/services/taxonomy/CALL%20OF%20THE%20WILDMAN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/call-of-the-wildman-130x97.jpg')
        addDir('CATS 101','http://animal.discovery.com/services/taxonomy/CATS%20101/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/cats101-130x97.jpg')
        addDir('CONFESSIONS: ANIMAL HOARDING','http://animal.discovery.com/services/taxonomy/CONFESSIONS:%20ANIMAL%20HOARDING/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/confessionsanimalhoarding-130x97.jpg')
        addDir('DOGS 101','http://animal.discovery.com/services/taxonomy/DOGS%20101/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/dogs101-130x97.jpg')
        addDir('EATING GIANTS','http://animal.discovery.com/services/taxonomy/WILD%20ANIMAL%20VIDEOS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/eating-giants.jpg')
        addDir('FATAL ATTRACTIONS','http://animal.discovery.com/services/taxonomy/FATAL%20ATTRACTIONS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/fatalattractions-130x97.jpg')
        addDir('FINDING BIGFOOT','http://animal.discovery.com/services/taxonomy/FINDING%20BIGFOOT/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/findingbigfoot-130x97.jpg')
        addDir('GATOR BOYS','http://animal.discovery.com/services/taxonomy/GATOR%20BOYS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/gatorboys-130x97.jpg')
        addDir('GLORY HOUNDS',"http://animal.discovery.com/services/taxonomy/GLORY%20HOUNDS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/glory-hounds-130x97.jpg')
        addDir('THE HAUNTED','http://animal.discovery.com/services/taxonomy/THE%20HAUNTED/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/thehaunted-130x97.jpg')
        addDir('HILLBILLY HANDFISHIN',"http://animal.discovery.com/services/taxonomy/HILLBILLY%20HANDFISHIN'/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/hillbillyhandfishin-130x97.jpg')
        addDir("I SHOULDN'T BE ALIVE VIDEOS","http://animal.discovery.com/services/taxonomy/I%20SHOULDN'T%20BE%20ALIVE%20VIDEOS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/ishouldntbealive130x97.jpg')
        addDir('INFESTED!','http://animal.discovery.com/services/taxonomy/INFESTED/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/infested-130x97.jpg')
        addDir("IT'S ME OR THE DOG","http://animal.discovery.com/services/taxonomy/IT'S%20ME%20OR%20THE%20DOG/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/itsmeorthedog-130x97.jpg')
        addDir('LAW ON THE BORDER','http://animal.discovery.com/services/taxonomy/LAW%20ON%20THE%20BORDER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/law-on-the-border-130x97.jpg')
        addDir('LOST TAPES','http://animal.discovery.com/services/taxonomy/LOST%20TAPES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/lost-tapes-130x97.jpg')
        addDir('LOUSIANA LOCKDOWN','http://dsc.discovery.com/services/taxonomy/Mayan%20Doomsday%20Prophecy%20Videos/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/louisiana-lockdown-130x97.jpg')
        addDir('MERMAIDS','http://animal.discovery.com/services/taxonomy/MERMAIDS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mermaids-130x97.jpg')
        addDir('MONSTERS INSIDE ME','http://animal.discovery.com/services/taxonomy/MONSTERS%20INSIDE%20ME/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/monstersinsideme-130x97.jpg')
        addDir('MUST LOVE CATS','http://animal.discovery.com/services/taxonomy/MUST%20LOVE%20CATS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mustlovecats-130x97.jpg')
        addDir('MY CAT FROM HELL','http://animal.discovery.com/services/taxonomy/MY%20CAT%20FROM%20HELL/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mycatfromhell-130x97.jpg')
        addDir('MY EXTREME ANIMAL PHOBIA','http://animal.discovery.com/services/taxonomy/MY%20EXTREME%20ANIMAL%20PHOBIA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/myextremeanimalphobia-130x97.jpg')
        addDir('NORTH WOODS LAW','http://animal.discovery.com/services/taxonomy/NORTH%20WOODS%20LAW/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/north-woods-law-130x97.jpg')
        addDir('OFF THE HOOK','http://animal.discovery.com/services/taxonomy/OFF%20THE%20HOOK/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/off-the-hook-badge.jpg')
        addDir('PIT BOSS','http://animal.discovery.com/services/taxonomy/PIT%20BOSS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/pitboss-130x97.jpg')
        addDir('PIT BULLS AND PAROLEES','http://animal.discovery.com/services/taxonomy/PIT%20BULLS%20AND%20PAROLEES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/pitbulls-and-parolees-130x97.jpg')
        addDir('PUPPY BOWL','http://animal.discovery.com/services/taxonomy/PUPPY%20BOWL/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/puppy-bowl9-130x97.jpg')
        addDir('RAISED WILD','http://animal.discovery.com/services/taxonomy/RAISED%20WILD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/raised-wild-130x97.jpg')
        addDir('RATTLESNAKE REPUBLIC','http://animal.discovery.com/services/taxonomy/RATTLESNAKE%20REPUBLIC/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/rattlesnakerepublic-130x97.jpg')
        addDir('RIVER MONSTERS','http://animal.discovery.com/services/taxonomy/RIVER%20MONSTERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/river-monsters-130x97.jpg')
        addDir('SWAMP WARS','http://animal.discovery.com/services/taxonomy/SWAMP%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/swampwars-130x97.jpg')
        addDir('TANKED','http://animal.discovery.com/services/taxonomy/TANKED/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/tanked-130x97.jpg')
        addDir('TOO CUTE','http://animal.discovery.com/services/taxonomy/TOO%20CUTE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/toocute-130x97.jpg')
        addDir('UNTAMED & UNCUT','http://animal.discovery.com/services/taxonomy/UNTAMED%20AND%20UNCUT/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/untamedanduncut-130x97.jpg')
        addDir('WEIRD, TRUE AND FREAKY','http://dsc.discovery.com/services/taxonomy/YUKON%20MEN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/weirdtrueandfreaky-130x97.jpg')
        addDir('WHALE WARS','http://animal.discovery.com/services/taxonomy/WHALE%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/whalewars-130x97.jpg')
        addDir('WHALE WARS VIKING SHORES','http://animal.discovery.com/services/taxonomy/WHALE%20WARS%20VIKING%20SHORES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/whale-wars-viking-shores-130x97.jpg')
        GA("Adventure","AnimalPlanet")
        VIEWSB()
        
def MILIT():
        addDir('AN OFFICER AND A MOVIE','http://military.discovery.com/services/taxonomy/AN%20OFFICER%20AND%20A%20MOVIE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/oam.jpg')
        addDir('BLACK OPS','http://military.discovery.com/services/taxonomy/BLACK%20OPS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/black_ops.jpg')
        addDir('COMBAT COUNTDOWN','http://military.discovery.com/services/taxonomy/COMBAT%20COUNTDOWN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/combat-countdown.jpg')
        addDir('COMBAT TECH','http://military.discovery.com/services/taxonomy/COMBAT%20TECH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/combat-tech-130.jpg')
        addDir('COMMANDER IN CHIEF','http://military.discovery.com/services/taxonomy/COMMANDER%20IN%20CHIEF/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/commanderinchief.jpg')
        addDir('GREAT PLANES','http://military.discovery.com/services/taxonomy/GREAT%20PLANES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/great-planes.jpg')
        addDir('GREATEST TANK BATTLES','http://military.discovery.com/services/taxonomy/GREATEST%20TANK%20BATTLES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/greatest-tank-battles.jpg')
        addDir('RETURN SALUTE','http://military.discovery.com/services/taxonomy/RETURN%20SALUTE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/returnsalute.jpg')
        addDir('SECRETS OF','http://military.discovery.com/services/taxonomy/SECRETS%20OF/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/secrets-of.jpg')
        addDir('TOP SECRET WEAPONS REVEALED','http://military.discovery.com/services/taxonomy/TOP%20SECRET%20WEAPONS%20REVEALED/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/top-secret-weapons-revealed.jpg')
        addDir('TRIGGERS','http://military.discovery.com/services/taxonomy/TRIGGERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/triggers.jpg')
        addDir('ULTIMATE WARFARE','http://military.discovery.com/services/taxonomy/ULTIMATE%20WARFARE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/ultimate-warfare.jpg')
        addDir('ULTIMATE WEAPONS','http://military.discovery.com/services/taxonomy/ULTIMATE%20WEAPONS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/ultimate-weapons.jpg')
        addDir('WARPLANE','http://military.discovery.com/services/taxonomy/WARPLANE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mc-show-thumb-warplane-130x97.jpg')
        addDir('WORLD WAR II IN COLOR','http://military.discovery.com/services/taxonomy/WORLD%20WAR%20II%20IN%20COLOR/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mc-show-thumb-ww2-color-130x97.jpg')        
        GA("Adventure","Military")
        VIEWSB()

def SCI():
        addDir('AN IDIOT ABROAD','http://science.discovery.com/services/taxonomy/AN%20IDIOT%20ABROAD%20VIDEOS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/anidiotabroad_badge_130x97_v2.jpg')
        addDir('ARE WE ALONE','http://science.discovery.com/services/taxonomy/ARE%20WE%20ALONE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_are-we-alone.jpg')
        addDir('BIG BIGGER BIGGEST','http://science.discovery.com/services/taxonomy/BIG%20BIGGER%20BIGGEST/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/bigbiggerbiggest-130x97.jpg')
        addDir('BUILD IT BIGGER','http://science.discovery.com/services/taxonomy/BUILD%20IT%20BIGGER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/builditbigger-130x97.jpg')
        addDir('DARK MATTERS: TWISTED BUT TRUE','http://science.discovery.com/services/taxonomy/DARK%20MATTERS:%20TWISTED%20BUT%20TRUE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_dark-matters.jpg')
        addDir('FIREFLY','http://science.discovery.com/services/taxonomy/FIREFLY/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_firefly.jpg')
        addDir('FRINGE','http://science.discovery.com/services/taxonomy/FRINGE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/fringe-130x97.jpg')
        addDir('HEAD RUSH','http://science.discovery.com/services/taxonomy/HEAD%20RUSH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/headrush.jpg')
        addDir('HOW DO THEY DO IT','http://science.discovery.com/services/taxonomy/HOW%20DO%20THEY%20DO%20IT/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/how-do-they-do-it-130x97.jpg')
        addDir('HOW THE UNIVERSE WORKS','http://science.discovery.com/services/taxonomy/HOW%20THE%20UNIVERSE%20WORKS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/htuw-fixed-130x97.jpg')
        addDir("HOW IT'S MADE","http://science.discovery.com/services/taxonomy/HOW%20IT'S%20MADE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/howitsmade.jpg')
        addDir('KILLER ROBOTS','http://science.discovery.com/services/taxonomy/KILLER%20ROBOTS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/killer_robots-130x97.jpg')
        addDir('LDRS','http://science.discovery.com/services/taxonomy/LDRS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/ldrs-130x97.jpg')
        addDir('MONSTER BUG WARS','http://science.discovery.com/services/taxonomy/MONSTER%20BUG%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/2monsterbugwars-130x97.jpg')
        addDir('MUTANT PLANET','http://science.discovery.com/services/taxonomy/MUTANT%20PLANET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_mutant-planet.jpg')        
        addDir('ODDITIES','http://science.discovery.com/services/taxonomy/ODDITIES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_oddities.jpg')
        addDir('ODDITIES SAN FRANCISCO','http://science.discovery.com/services/taxonomy/ODDITIES%20SAN%20FRANCISCO/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_odditiessf.jpg')
        addDir('PROPHETS OF SCIENCE FICTION','http://science.discovery.com/services/taxonomy/PROPHETS%20OF%20SCIENCE%20FICTION/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_prophets-of-scifi.jpg')
        addDir('PUNKIN CHUNKIN','http://science.discovery.com/services/taxonomy/PUNKIN%20CHUNKIN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/punkin-chunkin-show-carousel-badge.jpg')
        addDir('SCI FI SCIENCE','http://science.discovery.com/services/taxonomy/SCI%20FI%20SCIENCE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sci-fi-sci-130x97.jpg')
        addDir("STEPHEN HAWKING'S SCI FI MASTERS","http://science.discovery.com/services/taxonomy/STEPHEN%20HAWKING'S%20SCI%20FI%20MASTERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/sc-showbadge_scifi-masters.jpg')
        addDir('STRIP THE CITY','http://science.discovery.com/services/taxonomy/STRIP%20THE%20CITY/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/strip-the-city-130x97.jpg')
        addDir('STUCK WITH HACKETT','http://science.discovery.com/services/taxonomy/STUCK%20WITH%20HACKETT/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/stuckwithhacket-130x97.jpg')
        addDir('STUFF YOU SHOULD KNOW','http://science.discovery.com/services/taxonomy/STUFF%20YOU%20SHOULD%20KNOW%20VIDEOS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sysk-badge-130x97.jpg')
        addDir('THROUGH THE WORMHOLE','http://science.discovery.com/services/taxonomy/THROUGH%20THE%20WORMHOLE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_wormhole.jpg')
        addDir('TREK NATION','http://science.discovery.com/services/taxonomy/TREK%20NATION/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/trek-nation-130x97.jpg')
        addDir('WONDERS WITH BRIAN COX','http://science.discovery.com/services/taxonomy/WONDERS%20WITH%20BRIAN%20COX/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/wonders-brian-cox-130.jpg')        
        GA("Adventure","Science")
        VIEWSB()

def VELO():
        addDir('ALL GIRLS GARAGE','http://velocity.discovery.com/services/taxonomy/ALL%20GIRLS%20GARAGE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-all-girls-garage.jpg')
        addDir('CAR FIX','http://velocity.discovery.com/services/taxonomy/CAR%20FIX/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-carfix.jpg')
        addDir('CAFE RACER','http://velocity.discovery.com/services/taxonomy/CAFE%20RACER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-cafe-racer.jpg')
        addDir('CHASING CLASSIC CARS','http://velocity.discovery.com/services/taxonomy/CHASING%20CLASSIC%20CARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-chasing-classic-cars.jpg')
        addDir('EXTREME FISHING','http://velocity.discovery.com/services/taxonomy/EXTREME%20FISHING/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/extreme-fishing-130x97.jpg')
        addDir('FIFTH GEAR','http://velocity.discovery.com/services/taxonomy/FIFTH%20GEAR/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/fifth-gear-130x97.jpg')
        addDir('INSIDE WEST COAST CUSTOMS','http://velocity.discovery.com/services/taxonomy/INSIDE%20WEST%20COAST%20CUSTOMS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-iwcc.jpg')
        addDir('MECUM AUTO AUCTIONS','http://velocity.discovery.com/services/taxonomy/MECUM%20AUTO%20AUCTIONS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-mecum-auctions.jpg')
        addDir('ONE OF A KIND','http://velocity.discovery.com/services/taxonomy/ONE%20OF%20A%20KIND/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-one-of-a-kind.jpg')
        addDir("OVERHAULIN'","http://velocity.discovery.com/services/taxonomy/OVERHAULIN'/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/badge-overhaulin.jpg')
        addDir("WHAT'S MY CAR WORTH?",'http://velocity.discovery.com/services/taxonomy/WHATS%20MY%20CAR%20WORTH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-whats-my-car-worth.jpg')
        addDir('WHEELER DEALERS','http://velocity.discovery.com/services/taxonomy/WHEELER%20DEALERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-wheeler-dealers.jpg')
        GA("Adventure","Velocity")
        VIEWSB()

def KIDZone(murl):
    addDir('National Geographic Kids','ngk',71,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
    addDir('WB Kids','wbk',77,"%s/art/wb.png"%selfAddon.getAddonInfo("path"))
    addDir('Youtube Kids','wbk',84,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    GA("None","KidZone")
    VIEWSB()
    
def YOUKIDS():
    addDir('Sesame Street','sesamestreet',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Yo Gabba Gabba!','yogabbagabba',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Houston Zoo','houstonzoo',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Simple Kids Crafts','simplekidscrafts',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Cartoon Network','cartoonnetwork',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Muppets Studio','MuppetsStudio',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Word World PBS','WordWorldPBS',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Big Red Hat Kids','bigredhatkids',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Baby Einstein','TerrapinStation5',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Activity Village','activityv',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Hoopla Kids','hooplakidz',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('4KidsTV','4KidsTV',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('School House Rock Kids','MrRiggyRiggs',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Arthur','MsArthurTV',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('POCOYO','pocoyotv',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Disney jr','disneyjunior',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Mickey Mouse','MickeyMouseCartoon',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Tom and Jerry','TheTomEJerryShow',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Dora','TheDoraTheExplorerHD',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('SpongeBob','Spongebob4Children',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Curious George','ngk',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Kids Camp','kidscamp',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Timon and Pumbaa','timonandpumbaa1',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Dragon Tales','DejectedDragon',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    addDir('Aladdin','aladdinvids',47,"%s/art/youkids.png"%selfAddon.getAddonInfo("path"))
    GA("KidZone","YoutubeKids")
    VIEWSB()
    
def NG():
    addDir('National Geographic Channel','ngc','',"%s/art/ngccm.png"%selfAddon.getAddonInfo("path"))
    addDir('Nat Geo Wild','ngw','',"%s/art/ngwcm.png"%selfAddon.getAddonInfo("path"))
    addDir('Nat Geo Animals','nga',71,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
    GA("Adventure","NationalGeo")
    VIEWSB()

def NGDir(murl):
    if murl  =='ngc':
        addDir('Full Episodes','http://video.nationalgeographic.com/video/national-geographic-channel/full-episodes/',72,"%s/art/ngc.png"%selfAddon.getAddonInfo("path"))
        addDir('Shows','http://video.nationalgeographic.com/video/national-geographic-channel/shows/',72,"%s/art/ngc.png"%selfAddon.getAddonInfo("path"))
        addDir('Specials','http://video.nationalgeographic.com/video/national-geographic-channel/specials-1/',72,"%s/art/ngc.png"%selfAddon.getAddonInfo("path"))
        addDir('Extras','http://video.nationalgeographic.com/video/national-geographic-channel/extras/',72,"%s/art/ngc.png"%selfAddon.getAddonInfo("path"))
        GA("NationalGeo","NGC")
    elif murl  =='ngw':
        addDir('Full Episodes','http://video.nationalgeographic.com/video/nat-geo-wild/full-episodes-1/',72,"%s/art/ngw.png"%selfAddon.getAddonInfo("path"))
        addDir('Shows','http://video.nationalgeographic.com/video/nat-geo-wild/shows-1/',72,"%s/art/ngw.png"%selfAddon.getAddonInfo("path"))
        addDir('Specials','http://video.nationalgeographic.com/video/nat-geo-wild/specials-2/',72,"%s/art/ngw.png"%selfAddon.getAddonInfo("path"))
        addDir('Extras','http://video.nationalgeographic.com/video/nat-geo-wild/extras-1/',72,"%s/art/ngw.png"%selfAddon.getAddonInfo("path"))
        GA("NationalGeo","NGW")
    elif murl  =='nga':
        addDir('Amphibians','http://video.nationalgeographic.com/video/animals/amphibians-animals/',72,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
        addDir('Birds','http://video.nationalgeographic.com/video/animals/birds-animals/',72,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
        addDir('Bugs','http://video.nationalgeographic.com/video/animals/bugs-animals/',72,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
        addDir('Crittercam','http://video.nationalgeographic.com/video/animals/crittercam-animals/',72,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
        addDir('Fish','http://video.nationalgeographic.com/video/animals/fish-animals/',72,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
        addDir('Invertebrates','http://video.nationalgeographic.com/video/animals/invertebrates-animals/',72,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
        addDir('Mammals','http://video.nationalgeographic.com/video/animals/mammals-animals/',72,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
        addDir('Reptiles','http://video.nationalgeographic.com/video/animals/reptiles-animals/',72,"%s/art/nga2.png"%selfAddon.getAddonInfo("path"))
        GA("NationalGeo","NGA")
    elif murl  =='ngk':
        addDir('Animals & Pets','http://video.nationalgeographic.com/video/kids/animals-pets-kids/',72,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('Cartoons & Shows','http://video.nationalgeographic.com/video/kids/cartoons-tv-movies-kids/',72,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        #addDir('En Espanol','http://video.nationalgeographic.com/video/kids/en-espanol-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('Explorers','http://video.nationalgeographic.com/video/kids/explorers-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('Forces of Nature','http://video.nationalgeographic.com/video/kids/forces-of-nature-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('Green','http://video.nationalgeographic.com/video/kids/green-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('History','http://video.nationalgeographic.com/video/kids/history-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        #addDir('Mandarin','http://video.nationalgeographic.com/video/kids/mandarin-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('Movies & Books','http://video.nationalgeographic.com/video/kids/movies-books-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('My Shot Minute','http://video.nationalgeographic.com/video/kids/my-shot-minute-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('People & Places','http://video.nationalgeographic.com/video/kids/people-places-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('Science & Space','http://video.nationalgeographic.com/video/kids/science-space-kids/',73,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        addDir('Weird & Wacky','http://video.nationalgeographic.com/video/kids/weird-wacky-kids/',72,"%s/art/ngk.png"%selfAddon.getAddonInfo("path"))
        GA("KidZone","NGK")

def WB():
        addDir('Looney Tunes','Looney Tunes',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/LooneyTunes_video.jpg')
        addDir('Ozzy and Drix','Ozzy & Drix',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/OzzieDrix_video.jpg')
        addDir('Shaggy and Scoobydoo Get A Clue','Shaggy & Scooby-Doo Get A Clue!',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/ShaggyScoobyGetAClue_video.jpg')
        addDir('The Smurfs','Smurfs',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/smurf_video.jpg')
        addDir('The Flintstones','The Flintstones',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/Flintstones_video.jpg')
        addDir('The Jetsons','The Jetsons',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/Jetsons_video.jpg')
        addDir('The New Scoobydoo Mysteries','The New Scooby-Doo Mysteries',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/ScoobyDooMysteries_video.jpg')
        addDir('Thundercats','ThunderCats',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/Thundercats.jpg')
        addDir('Tom and Jerry Tales','Tom And Jerry Tales',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/TomJerryTales_video.jpg')
        addDir('Xiaolin Showdown','Xiaolin Showdown',78,'http://staticswf.kidswb.com/franchise/content/images/touts/video_channel_thumbs/XiaolinShowdown_video.jpg')
        GA("KidZone","WBK")

def DOCS():
        addDir('Vice','http://www.vice.com/shows',104,"%s/art/vice.png"%selfAddon.getAddonInfo("path"))
        addDir('Documentary Heaven','doc1',86,"%s/art/dh.png"%selfAddon.getAddonInfo("path"))
        addDir('Top Documentary Films','doc2',86,"%s/art/topdoc.png"%selfAddon.getAddonInfo("path"))
        addDir('Documentary Log','doc3',86,"%s/art/doclog.png"%selfAddon.getAddonInfo("path"))
        addDir('Documentaries (Movie25)','http://www.movie25.com/movies/documentary/',1,"%s/art/doc.png"%selfAddon.getAddonInfo("path"))
        GA("None","Documentary")

        
def GETMETA(mname,genre,year,thumb): 
        if selfAddon.getSetting("meta-view") == "true":
                mname=mname.replace(' 720p BRRip','').replace(' 720p HDRip','').replace(' 720p WEBRip','').replace(' 720p BluRay','').replace('()','')
                mname=mname.replace('[DVD]','').replace('[TS]','').replace('[TC]','').replace('[CAM]','').replace('[SCREENER]','').replace('[COLOR blue]','').replace('[COLOR red]','').replace('[/COLOR]','')
                namelen=len(mname)
                print mname[-1:namelen]
                if mname[-1:namelen]==')':
                        nam= namelen- 5
                        name= mname[0:namelen-6]
                else:
                        name = mname
                name=name.replace('-','').replace('&','').replace('acute;','').replace('C ','')
                name = name.decode("ascii", "ignore")
                if year =='':
                        year=''
                meta = grab.get_meta('movie',name,None,None,year,overlay=6)# first is Type/movie or tvshow, name of show,tvdb id,imdb id,string of year,unwatched = 6/watched  = 7
                print "Movie mode: %s"%name
                infoLabels = {'rating': meta['rating'],'duration': meta['duration'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],
                  'plot': meta['plot'],'title': meta['title'],'writer': meta['writer'],'cover_url': meta['cover_url'],
                  'director': meta['director'],'cast': meta['cast'],'backdrop_url': meta['backdrop_url'],'tmdb_id': meta['tmdb_id'],'year': meta['year']}
                if infoLabels['genre']=='':
                        infoLabels['genre']=genre
                if infoLabels['cover_url']=='':
                        infoLabels['cover_url']=thumb
        else:
                infoLabels = {'genre': genre,'title': mname,'cover_url': thumb,'year': year,'backdrop_url': ''}
        return infoLabels

def GETMETAB(name,genre,year,thumb): 
        if selfAddon.getSetting("meta-view") == "true":
                meta = grab.get_meta('movie',name,None,None,year,overlay=6)# first is Type/movie or tvshow, name of show,tvdb id,imdb id,string of year,unwatched = 6/watched  = 7
                print "Movie mode: %s"%name
                infoLabels = {'rating': meta['rating'],'duration': meta['duration'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],
                  'plot': meta['plot'],'title': meta['title'],'writer': meta['writer'],'cover_url': meta['cover_url'],
                  'director': meta['director'],'cast': meta['cast'],'backdrop_url': meta['backdrop_url'],'tmdb_id': meta['tmdb_id'],'year': meta['year']}
                if infoLabels['genre']=='':
                        infoLabels['genre']=genre
                if infoLabels['cover_url']=='':
                        infoLabels['cover_url']=thumb
        else:
                infoLabels = {'genre': genre,'title': name,'cover_url': thumb,'year': year,'backdrop_url': ''}
        return infoLabels
        
   
                
def LISTMOVIES(murl):
        link=OPENURL(murl)
        match=re.compile('<div class="movie_pic"><a href="(.+?)" ><img src="(.+?)" width=".+?" height=".+?" /></a></div>\n  <div class="movie_about">\n    <div class="movie_about_text">\n      <h1><a href=".+?" >(.+?)</a></h1>\n      <div class="c">Genre:      <a href=".+?/" title=\'.+?\'>(.+?)</a>').findall(link)
        # got help from j0anita above
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,mname,genre in match:
                namelen=len(mname)
                if mname[-2:namelen-1] == ')':
                        nam= namelen- 6
                        year = mname[nam:namelen-2]
                        name= mname[0:namelen-7]
                elif mname[-1:namelen] == ')':
                        nam= namelen- 5
                        year = mname[nam:namelen-1]
                        name= mname[0:namelen-6]
                else:
                        name = mname
                        year = ''
                name=name.replace('-','').replace('&','').replace('acute;','')
                addInfo(name+'('+year+')',url,3,thumb,genre,year)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        
        GA("None","Movie25-list")
        paginate=re.compile('http://www.movie25.com/movies/.+?/index-(.+?).html').findall(murl)
       
        if (len(paginate) == 0):
                purl = murl + 'index-2.html'
                addDir('[COLOR blue]Page 2[/COLOR]',purl,1,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        else:
                paginate=re.compile('http://www.movie25.com/movies/(.+?)/index-(.+?).html').findall(murl)
                for section, page in paginate:
                        pg= int(page) +1
                        xurl = Mainurl + str(section) + '/' + 'index-'+ str (pg) + '.html'
                addDir('[COLOR red]Home[/COLOR]','',0,"%s/art/home.png"%selfAddon.getAddonInfo("path"))
                addDir('[COLOR blue]Page '+ str(pg)+'[/COLOR]',xurl,1,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        VIEWS()
def LISTSP(murl): 
        urllist=['http://oneclickwatch.org/category/movies/','http://oneclickwatch.org/category/movies/page/2/','http://oneclickwatch.org/category/movies/page/3/','http://oneclickwatch.org/category/movies/page/4/','http://oneclickwatch.org/category/movies/page/5/','http://oneclickwatch.org/category/movies/page/6/','http://oneclickwatch.org/category/movies/page/7/','http://oneclickwatch.org/category/movies/page/8/','http://oneclickwatch.org/category/movies/page/9/','http://oneclickwatch.org/category/movies/page/10/','http://oneclickwatch.org/category/movies/page/11/','http://oneclickwatch.org/category/movies/page/12/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = 12
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for murl in urllist:
                link=OPENURL(murl)
                match=re.compile('<h2 class="pagetitle"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>\r\n\t\t\t\t<small>Posted: .+?<strong>.+?</strong> in <a href=".+?" title="View all posts in Movies" rel="category tag">Movies</a><br />\r\n\t\t\t\t</small>\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="postcomments"><a href=".+?" title=".+?">0</a></div>\r\n\r\n\t\t\t\t<div class="entry">\r\n\t\t\t\t\t<p>(.+?) Plot:').findall(link)
                for url,sitename,mname in match:
                        match=re.compile('(.+?) / .+?').findall(mname)
                        for nname in match:
                                mname = nname
                        match=re.compile('(.+?) aka .+?').findall(mname)
                        for nname in match:
                                mname = nname
                        mname=mname.replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        namelen=len(mname)
                        if mname[-2:namelen-1] == ')':
                                nam= namelen- 6
                                year = mname[nam:namelen-2]
                                name= mname[0:namelen-7]
                        else:
                                nam= namelen- 5
                                year = mname[nam:namelen-1]
                                year2='('+year+')'
                                name= mname[0:namelen-6]
                        year=year.replace('(2 )','').replace(') ak','')
                        match=re.compile('720p BRRip').findall(sitename)
                        if (len(match) > 0):
                                year2 = '('+year+')'+'[COLOR red] 720p BRRip[/COLOR]'
                                addInfo(name+year2,url,26,'','',year)
                        match=re.compile('720p HDRip').findall(sitename)
                        if (len(match) > 0):
                                year2 = '('+year+')'+'[COLOR red] 720p HDRip[/COLOR]'
                                addInfo(name+year2,url,26,'','',year)
                        match=re.compile('720p WEBRip').findall(sitename)
                        if (len(match) > 0):
                                year2 = '('+year+')'+'[COLOR red] 720p WEBRip[/COLOR]'
                                addInfo(name+year2,url,26,'','',year)
                        match=re.compile('720p BluRay').findall(sitename)
                        if (len(match) > 0):
                                year2 = '('+year+')'+'[COLOR red] 720p BluRay[/COLOR]'
                                addInfo(name+year2,url,26,'','',year)
                        name=name.replace('-','').replace('&','').replace('acute;','')
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("HD","Oneclickwatch")
        
def LISTSP2(murl):
        if murl=='3D':
                addDir('Search Newmyvideolinks','movieNEW',102,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                try:
                        urllist=['http://newmyvideolinks.com/category/movies/3-d-movies/','http://newmyvideolinks.com/category/movies/3-d-movies/page/2/']
                except:
                        urllist=['http://newmyvideolinks.com/category/movies/3-d-movies/']
        elif murl=='TV':
                addDir('Search Newmyvideolinks','tvNEW',102,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                urllist=['http://newmyvideolinks.com/category/tv-shows/','http://newmyvideolinks.com/category/tv-shows/page/2/','http://newmyvideolinks.com/category/tv-shows/page/3/','http://newmyvideolinks.com/category/tv-shows/page/4/','http://newmyvideolinks.com/category/tv-shows/page/5/','http://newmyvideolinks.com/category/tv-shows/page/6/','http://newmyvideolinks.com/category/tv-shows/page/7/','http://newmyvideolinks.com/category/tv-shows/page/8/','http://newmyvideolinks.com/category/tv-shows/page/9/','http://newmyvideolinks.com/category/tv-shows/page/10/']
        else:
                addDir('Search Newmyvideolinks','movieNEW',102,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                urllist=['http://newmyvideolinks.com/category/movies/bluray/','http://newmyvideolinks.com/category/movies/bluray/page/2/','http://newmyvideolinks.com/category/movies/bluray/page/3/','http://newmyvideolinks.com/category/movies/bluray/page/4/','http://newmyvideolinks.com/category/movies/bluray/page/5/','http://newmyvideolinks.com/category/movies/bluray/page/6/','http://newmyvideolinks.com/category/movies/bluray/page/7/','http://newmyvideolinks.com/category/movies/bluray/page/8/','http://newmyvideolinks.com/category/movies/bluray/page/9/','http://newmyvideolinks.com/category/movies/bluray/page/10/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for xurl in urllist:
                link=OPENURL(xurl)
                match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
                if len(match)>0:
                        for url,thumb,name in match:
                                if murl=='TV':
                                        match=re.compile('720p').findall(name)
                                        if (len(match)>0):
                                                addDir(name,url,35,thumb)
                                     
                                else:
                                        addDir(name,url,35,thumb)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False   

                else:
                        match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)" alt=".+?" width=".+?" height=".+?" class=".+?" />').findall(link)
                        for url,name,thumb in match:
                                if murl=='TV':
                                        match=re.compile('720p').findall(name)
                                        if (len(match)>0):
                                                addDir(name,url,35,thumb)
                                                
                                else:
                                        addDir(name,url,35,thumb)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False   
        dialogWait.close()
        del dialogWait
        GA("HD-3D-HDTV","Newmyvideolinks")

def SearchhistoryNEW(murl):
        if murl == 'tvNEW':
            seapath=os.path.join(datapath,'Search')
            SeaFile=os.path.join(seapath,'SearchHistoryTv')
            if not os.path.exists(SeaFile):
                url='tvNEW'
                SEARCHNEW(url)
            else:
                addDir('Search','tvNEW',101,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
                searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                for seahis in reversed(searchis):
                        url=seahis
                        seahis=seahis.replace('%20',' ')
                        addDir(seahis,url,101,thumb)
        elif murl == 'movieNEW':
            seapath=os.path.join(datapath,'Search')
            SeaFile=os.path.join(seapath,'SearchHistory25')
            if not os.path.exists(SeaFile):
                url='movieNEW'
                SEARCHNEW(url)
            else:
                addDir('Search','movieNEW',101,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
                thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
                searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                for seahis in reversed(searchis):
                        url=seahis
                        seahis=seahis.replace('%20',' ')
                        addDir(seahis,url,101,thumb)
            

def SEARCHNEW(murl):
        if murl == 'movieNEW':
                seapath=os.path.join(datapath,'Search')
                SeaFile=os.path.join(seapath,'SearchHistory25')
                try:
                    os.makedirs(seapath)
                except:
                    pass
                keyb = xbmc.Keyboard('', 'Search Movies')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        surl='http://newmyvideolinks.com/index.php?s='+encode
                        if not os.path.exists(SeaFile) and encode != '':
                            open(SeaFile,'w').write('search="%s",'%encode)
                        else:
                            if encode != '':
                                open(SeaFile,'a').write('search="%s",'%encode)
                        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                        for seahis in reversed(searchis):
                            print seahis
                        if len(searchis)>=10:
                            searchis.remove(searchis[0])
                            os.remove(SeaFile)
                            for seahis in searchis:
                                try:
                                    open(SeaFile,'a').write('search="%s",'%seahis)
                                except:
                                    pass
        elif murl == 'tvNEW':
                seapath=os.path.join(datapath,'Search')
                SeaFile=os.path.join(seapath,'SearchHistoryTv')
                try:
                    os.makedirs(seapath)
                except:
                    pass
                keyb = xbmc.Keyboard('', 'Search TV Shows')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        surl='http://newmyvideolinks.com/index.php?s='+encode
                        if not os.path.exists(SeaFile) and encode != '':
                            open(SeaFile,'w').write('search="%s",'%encode)
                        else:
                            if encode != '':
                                open(SeaFile,'a').write('search="%s",'%encode)
                        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                        for seahis in reversed(searchis):
                            continue
                        if len(searchis)>=10:
                            searchis.remove(searchis[0])
                            os.remove(SeaFile)
                            for seahis in searchis:
                                try:
                                    open(SeaFile,'a').write('search="%s",'%seahis)
                                except:
                                    pass

                
        else:
                encode = murl
                surl='http://newmyvideolinks.com/index.php?s='+encode
        link=OPENURL(surl)
        match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
        if len(match)>0:
                for url,thumb,name in match:
                            addDir(name,url,35,thumb)

        else:
                match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)" alt=".+?" width=".+?" height=".+?" class=".+?" />').findall(link)
                for url,name,thumb in match:
                            addDir(name,url,35,thumb)
        GA("Newmyvideolinks","Search")

def UFCNEW():
        try: 
                urllist=['http://newmyvideolinks.com/index.php?s=ufc','http://newmyvideolinks.com/page/2/?s=ufc']
        except:
                urllist=['http://newmyvideolinks.com/index.php?s=ufc']
        for surl in urllist:
                link=OPENURL(surl)
                match=re.compile('<a href="(.+?)" rel=".+?" title=".+?"> <img src="(.+?)" width=".+?" height=".+?" title="(.+?)" class=".+?"></a>').findall(link)
                if len(match)>0:
                        for url,thumb,name in match:
                                match=re.compile('UFC').findall(name)
                                if len(match)>0:
                                        addDir(name,url,35,thumb)

                else:
                        match=re.compile('href="(.+?)" title="(.+?)"><img src="(.+?)" alt=".+?" width=".+?" height=".+?" class=".+?" />').findall(link)
                        for url,name,thumb in match:
                                match=re.compile('UFC').findall(name)
                                if len(match)>0:
                                       addDir(name,url,35,thumb)
        GA("Newmyvideolinks","UFC")

def LISTSP3(murl):
        if murl == 'HD':
                url='http://www.dailyflix.net/index.php?/forum/196-hd-movies-2012-2013/page__sort_key__last_post__sort_by__Z-A'
        link=OPENURL(url)
        match=re.compile('href="(.+?)" title=.+? class=.+?>(.+?)</a>').findall(link)
        for url, name in match:
                addDir(name,url,54,'')
        GA("HD-TV","Dailyfix")

def LISTSP4(murl):
        urllist=['http://oneclickmoviez.com/category/bluray/','http://oneclickmoviez.com/category/bluray/page/2/','http://oneclickmoviez.com/category/bluray/page/3/','http://oneclickmoviez.com/category/bluray/page/4/','http://oneclickmoviez.com/category/bluray/page/5/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for xurl in urllist:
                link=OPENURL(xurl)
                match=re.compile('href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h2>\n</div>\n<div class="cover">\n<div class="entry">\n\t\t\t\t\t<p style="text-align: center;"><img class="alignnone" title="poster" src="(.+?)" ').findall(link)
                for url,name, thumb in match:
                        addDir(name,url,56,thumb)   
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False    
        dialogWait.close()
        del dialogWait
        GA("HD","Oneclickmoviez")

def LISTSP5(murl):
        link=OPENURL(murl)
        match=re.compile("<a href=\'(.+?)'.+?Calibri'>([^<]+)</font></a><br>").findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for url,name in match:
                addDir(name,url,58,'')
        loadedLinks = loadedLinks + 1
        percent = (loadedLinks * 100)/totalLinks
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
        if (dialogWait.iscanceled()):
                return False    
        dialogWait.close()
        del dialogWait
        GA("HD","Starplay")
        
def LISTINT(name,url):
        MainUrl = "http://www.einthusan.com/movies/"
        urllist=['http://www.einthusan.com/movies/index.php?lang=hindi','http://www.einthusan.com/movies/index.php?lang=hindi&organize=Activity&filtered=RecentlyPosted&org_type=Activity&page=2','http://www.einthusan.com/movies/index.php?lang=hindi&organize=Activity&filtered=RecentlyPosted&org_type=Activity&page=3',
                 'http://www.einthusan.com/movies/index.php?lang=hindi&organize=Activity&filtered=RecentlyPosted&org_type=Activity&page=4','http://www.einthusan.com/movies/index.php?lang=hindi&organize=Activity&filtered=RecentlyPosted&org_type=Activity&page=5',
                 'http://www.einthusan.com/movies/index.php?lang=hindi&organize=Activity&filtered=RecentlyPosted&org_type=Activity&page=6','http://www.einthusan.com/movies/index.php?lang=hindi&organize=Activity&filtered=RecentlyPosted&org_type=Activity&page=7',
                 'http://www.einthusan.com/movies/index.php?lang=hindi&organize=Activity&filtered=RecentlyPosted&org_type=Activity&page=8']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for murl in urllist:
                link=OPENURL(murl)
                match = re.compile('<a class="movie-cover-wrapper" href="(.+?)"><img src="(.+?)" alt="(.+?)"').findall(link)
                for url,thumb,name in match:
                        name = name.replace('hindi movie online','')
                        addDir(name,MainUrl+url,38,MainUrl+thumb)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("INT","Einthusan")
        
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
                link=OPENURL(murl)
                match=re.compile('href="(.+?)"><img src="(.+?)" width=".+?" alt=".+?" /></a>\r\n\t\t</div>\r\n\t\t<div class=".+?">\r\n\t\t<div class=".+?">\r\n\t\t\t<h1><a href=".+?">(.+?)</a></h1>').findall(link)
                for url,thumb,name in match:
                        match=re.compile('Movie').findall(name)
                        if (len(match)>0):
                                name = name.replace('xoxix','')
                                addDir(name,MainUrl+url,40,thumb)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("INT","Dramacrazy")

        
def LISTINT3(url):
        urllist=['http://www.cinevip.org/','http://www.cinevip.org/page/2','http://www.cinevip.org/page/3','http://www.cinevip.org/page/4','http://www.cinevip.org/page/5','http://www.cinevip.org/page/6','http://www.cinevip.org/page/7','http://www.cinevip.org/page/8','http://www.cinevip.org/page/9','http://www.cinevip.org/page/10']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for murl in urllist:
                link=OPENURL(murl)
                match=re.compile('<a class="entry-thumbnails-link" href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" class=".+?" alt=".+? Genero:(.+?) Titulo:.+? Info:(.+?) Sinopsis:(.+?)" title="(.+?)" />').findall(link)
                for url,thumb,genre,lang,desc,name in match:
                        lang ='[COLOR red]'+lang+'[/COLOR]'
                        lang = lang.replace('Audio','').replace('Español','').replace('Subtitulos','[COLOR blue]Sub(ESP)[/COLOR]').replace('DVDRip','')
                        name=name.replace(') Online','').replace('Ver ','')
                        name=name+')'
                        addSport(name+' '+lang,url,67,thumb,desc,'',genre)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("INT","Cinevip")

def LISTINT4(url):
        urllist=['http://kino-live.org/hq/','http://kino-live.org/hq/page/2/','http://kino-live.org/hq/page/3/','http://kino-live.org/hq/page/4/','http://kino-live.org/hq/page/5/','http://kino-live.org/hq/page/6/','http://kino-live.org/hq/page/7/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(urllist)
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for murl in urllist:
                #html = net().http_GET(murl).content
                link=OPENURL(murl)
                match=re.compile("""<a href="(.+?)">(.+?)</a>&nbsp;</div>\n<div class="ah3"> HQ,(.+?)</div><br>\n<div class=".+?"><div id=".+?" style=".+?">.+?<img src="(.+?)" style=".+?" alt=\'.+?' title=\'.+?'  /></a><!--TEnd-->(.+?)<br />""").findall(link)
                for url,name,genre,thumb,desc in match:
                        thumb='http://kino-live.org/'+thumb
                        addSport(name,url,69,thumb,desc,'',genre)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("INT","Kino-live")
        VIEWSB()
        
def ESPNList(murl):
        link=OPENURL(murl)
        match=re.compile('"videoDuration":"(.+?)",.+?"video":.+?{"headline":"(.+?)",.+?,"includePlatforms":.+?,"imageUrl":"(.+?)","mobileSubHead":"(.+?)","internalUrl720p":"(.+?)",').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Sports list is loaded.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Loading....[/B]',remaining_display)
        for dur,name,thumb,desc, url, in match:
                print "1st "+name
                url=url+'xovc'+desc+'xovc'+thumb+'xovc'
                addSport(name,url,46,thumb,desc,dur,'')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Loading....[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("ESPN","ESPN-List")

def YOUList(mname,durl):
        murl='http://gdata.youtube.com/feeds/api/users/'+durl+'/uploads?start-index=1&max-results=50'
        link=OPENURL(murl)
        match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
        for url,desc,thumb,name in match:
                name=name.replace('<','')
                addSport(name,url,48,thumb,desc,'','')
        GA(mname,"Youtube-List")


def UFCMOVIE25():
                surl='http://www.movie25.com/search.php?key=ufc&submit='
                link=OPENURL(surl)
                match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_blank">\n                            <img src="(.+?)" width=".+?" height=".+?" />\n                            </a></div>\n            <div class="movie_about">\n              <div class="movie_about_text">\n                <h1><a href=".+?" target="_blank">\n                  (.+?)                </a></h1>\n                <div class="c">Genre:\n                  <a href=".+?" target=\'.+?\'>(.+?)</a>').findall(link)
                dialogWait = xbmcgui.DialogProgress()
                ret = dialogWait.create('Please wait until Movie list is cached.')
                totalLinks = len(match)
                loadedLinks = 0
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
                for url,thumb,mname,genre in match:
                        namelen=len(mname)
                        if mname[-4:namelen-3] == ')':
                                nam= namelen- 8
                                year = mname[nam:namelen-4]
                                name= mname[0:namelen-9]
                        elif mname[-3:namelen-2] == ')':
                                nam= namelen- 7
                                year = mname[nam:namelen-3]
                                name= mname[0:namelen-8]
                        else:
                                name = mname
                                year = ''
                        name=name.replace('-','').replace('&','').replace('acute;','')
                        furl= 'http://movie25.com/'+url
                        addInfo(name+'('+year+')',furl,3,thumb,genre,year)
                        loadedLinks = loadedLinks + 1
                        percent = (loadedLinks * 100)/totalLinks
                        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                        dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                        if (dialogWait.iscanceled()):
                                return False 
                dialogWait.close()
                del dialogWait
                addDir('[COLOR blue]Page 2[/COLOR]','http://www.movie25.com/search.php?page=2&key=ufc',9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
                GA("UFC","UFC_Movie25-List")



def OCList(murl):
        link=OPENURL(murl)
        match=re.compile('<item><titl[^>]+>([^<]+)</title><description>(.+?)</description>.+?<plrelease:url>(.+?)</plrelease:url></plfile:release></media:content><pubDate>.+?</pubDate><plmedia:defaultThumbnailUrl>(.+?)</plmedia:defaultThumbnailUrl>').findall(link)
        for name,desc,url,thumb in match:
                addSport(name,url,52,thumb,desc,'','')
        GA("Sports","OC-List")

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
                addDir(name+'  [COLOR blue]'+view+'[/COLOR]',url,65,thumbList[i])
                i=i+1
        GA("Discovery",mname+"-list")

def LISTNG(murl):
    MainUrl='http://video.nationalgeographic.com'
    link=OPENURL(murl)
    match=re.compile('<a href="(.+?)">More \xc2\xbb</a></p><h3>(.+?)\n        \n    </h3><ul class=".+?"><li><a class=".+?" href=".+?" title=".+?"><img src="(.+?)">').findall(link)
    for url, name, thumb in match:
            addDir(name,MainUrl+url,73,MainUrl+thumb)
    GA("NationalGeo","NG-Show")
        
def LISTNG2(murl):
    MainUrl='http://video.nationalgeographic.com'
    link=OPENURL(murl)
    match2=re.compile('http://video.nationalgeographic.com/video/animals').findall(murl)
    match3=re.compile('http://video.nationalgeographic.com/video/kids').findall(murl)
    match=re.compile('<a href="(.+?)" title="(.+?)"><img src="(.+?)"></a>').findall(link)
    for url, name, thumb in match:
        name=name.replace("&#39;","'").replace('&lt;i&gt;','').replace('&lt;/i&gt;','').replace('&quot;','"').replace('&amp;quot;','"').replace('&amp;','&')
        if (len(match2)==0)and(len(match3)==0):
            #addDir(name,MainUrl+url,74,MainUrl+thumb)
            addSport(name,MainUrl+url,74,MainUrl+thumb,'','','')
        else:
            #addDir(name,MainUrl+url,75,MainUrl+thumb)
            addSport(name,MainUrl+url,75,MainUrl+thumb,'','','')
    paginate=re.compile("""\n            if ((.+?) === (.+?)) .+?\n                .+?<li><a href="(.+?)">Next &raquo;</a></li>""").findall(link)
    if (len(paginate)>0):
        for pges, pg, pgtot,purl in paginate:
            pg=pg.replace('(','')
            pgtot=pgtot.replace(')','')
            if pgtot!=pg:
                addDir('Page '+str(int(pg)+1),MainUrl+purl+pg+'/',73,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
    GA("NG-Show","List")
    
def LISTWB(murl):
    furl='http://staticswf.kidswb.com/kidswb/xml/videofeedlight.xml'
    link=OPENURL(furl)
    link=link.replace('&quot;','').replace('&#039;','').replace('&#215;','').replace('&#038;','').replace('&#8216;','').replace('&#8211;','').replace('&#8220;','').replace('&#8221;','').replace('&#8212;','').replace('&amp;','&').replace("`",'')
    match = re.compile('<item><media:title>([^<]+)</media:title><media:description>([^<]+)</media:description><guid isPermaLink="false">([^<]+)</guid><av:show season="1">'+murl+'</av:show><media:thumbnail url="([^<]+)"/></item>').findall(link)
    for name,desc,url,thumb in match:
        addSport(name,url,79,thumb,desc,'','')
    GA("WB","List")

def LISTDOC(murl):
    if murl=='doc1':
        GA("Documantary","DhHome")
        addDir('[COLOR red]Search[/COLOR]','search',89,'')
        addDir('[COLOR red]Popular[/COLOR]','http://documentaryheaven.com/popular/',89,'')
        addDir('[COLOR red]Recent[/COLOR]','http://documentaryheaven.com/all/',87,'')
        url='http://documentaryheaven.com/'
        link=OPENURL(url)
        match=re.compile('<li class=".+?"><a href="(.+?)" title=".+?">(.+?)</a> </li>').findall(link)
        for url, name in match:
            addDir(name,url,87,'')
    elif murl=='doc2':
        GA("Documantary","TDFHome")
        addDir('[COLOR red]Recent[/COLOR]','http://topdocumentaryfilms.com/all/',87,'')
        addDir('[COLOR red]Recommended[/COLOR]','rec',89,'')
        url='http://topdocumentaryfilms.com/'
        link=OPENURL(url)
        match=re.compile('href="(.+?)" title=".+?">(.+?)</a>.+?</li>').findall(link)
        for url, name in match:
            addDir(name,url,87,'')
    elif murl=='doc3':
        GA("Documantary","DLHome")
        addDir('[COLOR red]Latest[/COLOR]','http://www.documentary-log.com/',87,'')
        addDir("[COLOR red]Editor's Picks[/COLOR]",'http://www.documentary-log.com/category/editors-picks/',87,'')
        url='http://www.documentary-log.com/'
        link=OPENURL(url)
        match=re.compile('<li class="cat-item cat-item-.+?"><a href="(.+?)" title="(.+?)">(.+?)</a> ([^<]+)').findall(link)
        for url, desc, name, leng in match:
            addDir2(name+'  '+leng,url,87,'',desc)

def LISTDOC2(murl):
    match=re.compile('documentaryheaven').findall(murl)
    if (len(match)>0):
        GA("DhHome","Dh-List")
        link=OPENURL(murl)
        match=re.compile('<a href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        if (len(match)==0):
            match=re.compile('href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        for url,thumb,name,desc in match:
            #addDir(name,url,88,thumb)
            addSport(name,url,88,thumb,desc,'','')
        paginate=re.compile("class='page current'>1</span></li><li><a href='http://documentaryheaven.com/.+?/page/2/'").findall(link)
        if (len(paginate)>0):
            addDir('[COLOR blue]Page 2[/COLOR]',murl+'page/2/',87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        else:
                paginate=re.compile('http://documentaryheaven.com/(.+?)/page/(.+?)/').findall(murl)
                for section, page in paginate:
                        pg= int(page) +1
                        xurl = 'http://documentaryheaven.com/' + str(section) + '/page/'+ str (pg) + '/'
                addDir('[COLOR blue]Page '+ str(pg)+'[/COLOR]',xurl,87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

    match2=re.compile('topdocumentaryfilms').findall(murl)
    if (len(match2)>0):
        i=0
        GA("TDFHome","TDF-List")
        link=OPENURL(murl)
        link=link.replace('\n','')
        url=re.compile('href="([^<]+)">Watch now').findall(link)
        match=re.compile('href=".+?".+?src="(.+?)".+?alt="(.+?)"').findall(link)
        desc=re.compile('>([^<]+)</p><p><strong>').findall(link)
        for thumb,name in match:
            #addDir(name,url,88,thumb)
            addSport(name,url[i],88,thumb,desc[i],'','')
            i=i+1
        paginate=re.compile('</a>.+?href="([^<]+)">Next</a></div>').findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                addDir('[COLOR blue]Next[/COLOR]',purl,87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

    match3=re.compile('documentary-log').findall(murl)
    if (len(match3)>0):
        GA("DLHome","DL-List")
        i=0
        link=OPENURL(murl)
        match=re.compile('<img src="(.+?)" alt="(.+?)" class=".+?" />\n').findall(link)
        url=re.compile('<h2 class="title-1">\n      <a href="([^<]+)" title=').findall(link)
        desc=re.compile('<p>([^<]+)<').findall(link)
        for thumb,name in match:
            addDir2(name,url[i],88,thumb,desc[i])
            i=i+1
        paginate=re.compile("<a href='([^<]+)' class='nextpostslink'>").findall(link)
        if (len(paginate)>0):
            for purl in paginate:
                addDir('[COLOR blue]Next[/COLOR]',purl,87,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

                  
def LISTDOCPOP(murl):
    if murl=='search':
        keyb = xbmc.Keyboard('', 'Search Documentaries')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://documentaryheaven.com/?s='+encode
                link=OPENURL(surl)
        match=re.compile('<a href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        if (len(match)==0):
            match=re.compile('href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        for url,thumb,name,desc in match:
            addSport(name,url,88,thumb,desc,'','')

        paginate=re.compile("<span class=\'page current\'>1</span></li><li><a href=\'http://documentaryheaven.com/page/2/.?s=.+?\'").findall(link)
        if (len(paginate)>0):
            addDir('[COLOR blue]Page 2[/COLOR]','http://documentaryheaven.com/page/2/?s='+encode,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
    elif murl=='rec':
        rurl='http://topdocumentaryfilms.com/'
        link=OPENURL(rurl)
        match=re.compile('href="([^<]+)">([^<]+)</a></li><li><a').findall(link)
        for url,name in match:
            addDir(name,url,88,'')
    else:
        link=OPENURL(murl)
        match=re.compile("<li><a href='(.+?)'>(.+?)</a></li>").findall(link)
        for url,name in match:
            addDir(name,url,88,'')
            
def Vice(murl):
    GA("Documentary","Vice")
    link=OPENURL(murl)
    match=re.compile('<a href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" /></a>    <h2><a href=".+?">(.+?)</a></h2>\n    <p>(.+?)</p>').findall(link)
    for url,thumb,name,desc in match:
        url='http://www.vice.com'+url
        addDir2(name,url,105,thumb,desc)

def ViceList(murl):
    GA("Vice","Vice-list")
    link=OPENURL(murl)
    match=re.compile('<img src="(.+?)" alt="" width=".+?" height=".+?">\n                    <span class=".+?"></span>\n            </a>\n    <h2><a onClick=".+?" href="(.+?)">(.+?)</a></h2>').findall(link)
    for thumb,url,name in match:
        url='http://www.vice.com'+url
        addDir2(name,url,106,thumb,'')

def ViceLink(mname,murl):
    GA("Vice","Watched")
    link=OPENURL(murl)
    desci=re.compile('<meta name="description" content="(.+?)" />').findall(link)
    if len(desci)>0:
        desc=desci[0]
    else:
        desc=''
    thumbi=re.compile('<meta property="og:image" content="(.+?)" />').findall(link)
    if len(thumbi)>0:
        thumb=thumbi[0]
    else:
        thumb=''
    match=re.compile('content="http://player.ooyala.com/player.swf.?embedCode=(.+?)&amp;.+?"').findall(link)
    if len(match)>0:
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        durl='http://player.ooyala.com/player/ipad/'+match[0]+'.m3u8'
        link2=OPENURL(durl)
        match=re.compile('http://(.+?).m3u8').findall(link2)
        if len(match)==0:
            xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Played,5000)")
        else:
            if selfAddon.getSetting("vice-qua") == "0":
                try:
                    stream_url = 'http://'+match[3]+'.m3u8'
                except:
                    stream_url = 'http://'+match[0]+'.m3u8'
            elif selfAddon.getSetting("vice-qua") == "1":
                try:
                    stream_url = 'http://'+match[0]+'.m3u8'
                except:
                    stream_url = 'http://'+match[2]+'.m3u8'
            else:
                try:
                    stream_url = 'http://'+match[2]+'.m3u8'
                except:
                    stream_url = 'http://'+match[0]+'.m3u8'
            listitem = xbmcgui.ListItem(mname, thumbnailImage= thumb)
            listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
            playlist.add(stream_url,listitem)
            xbmcPlayer = xbmc.Player()
            xbmcPlayer.play(playlist)
            addDir('','','','')
    
    match2=re.compile('content="http://www.youtube.com/v/(.+?)" />').findall(link)
    if len(match2)>0:
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        url='http://www.youtube.com/watch?v='+match2[0]
        media = urlresolver.HostedMediaFile(str(url))
        source = media
        listitem = xbmcgui.ListItem(mname)
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False  
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addDir('','','','')

def Searchhistory():
        seapath=os.path.join(datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        if not os.path.exists(SeaFile):
            url='m25'
            SEARCH(url)
        else:
            addDir('Search','m25',4,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    addDir(seahis,url,4,thumb)
            
            
        
def SEARCH(murl):
        seapath=os.path.join(datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistory25')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'm25':
            keyb = xbmc.Keyboard('', 'Search Movies')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://www.movie25.com/search.php?key='+encode+'&submit='
                    if not os.path.exists(SeaFile) and encode != '':
                        open(SeaFile,'w').write('search="%s",'%encode)
                    else:
                        if encode != '':
                            open(SeaFile,'a').write('search="%s",'%encode)
                    searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                    for seahis in reversed(searchis):
                        continue
                    if len(searchis)>=10:
                        searchis.remove(searchis[0])
                        os.remove(SeaFile)
                        for seahis in searchis:
                            try:
                                open(SeaFile,'a').write('search="%s",'%seahis)
                            except:
                                pass
        else:
                encode = murl
                surl='http://www.movie25.com/search.php?key='+encode+'&submit='
        link=OPENURL(surl)
        match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_blank">\n                            <img src="(.+?)" width=".+?" height=".+?" />\n                            </a></div>\n            <div class="movie_about">\n              <div class="movie_about_text">\n                <h1><a href=".+?" target="_blank">\n                  (.+?)                </a></h1>\n                <div class="c">Genre:\n                  <a href=".+?" target=\'.+?\'>(.+?)</a>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,mname,genre in match:
                namelen=len(mname)
                if mname[-4:namelen-3] == ')':
                        nam= namelen- 8
                        year = mname[nam:namelen-4]
                        name= mname[0:namelen-9]
                elif mname[-3:namelen-2] == ')':
                        nam= namelen- 7
                        year = mname[nam:namelen-3]
                        name= mname[0:namelen-8]
                else:
                        name = mname
                        year = ''
                name=name.replace('-','').replace('&','').replace('acute;','')
                furl= 'http://movie25.com/'+url
                addInfo(name+'('+year+')',furl,3,thumb,genre,year)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False 
        dialogWait.close()
        del dialogWait
        addDir('[COLOR blue]Page 2[/COLOR]','http://www.movie25.com/search.php?page=2&key='+encode,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        GA("None","Search")

def YEARB(murl):
        link=OPENURL(murl)
        match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_blank">\n                            <img src="(.+?)" width=".+?" height=".+?" />\n                            </a></div>\n            <div class="movie_about">\n              <div class="movie_about_text">\n                <h1><a href=".+?" target="_blank">\n                  (.+?)                </a></h1>\n                <div class="c">Genre:\n                  <a href=".+?" target=\'.+?\'>(.+?)</a>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,mname,genre in match:
                namelen=len(mname)
                if mname[-4:namelen-3] == ')':
                        nam= namelen- 8
                        year = mname[nam:namelen-4]
                        name= mname[0:namelen-9]
                elif mname[-3:namelen-2] == ')':
                        nam= namelen- 7
                        year = mname[nam:namelen-3]
                        name= mname[0:namelen-8]
                else:
                        name = mname
                        year = ''
                name=name.replace('-','').replace('&','').replace('acute;','')
                furl= 'http://movie25.com/'+url
                addInfo(name+'('+year+')',furl,3,thumb,genre,year)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False 
        dialogWait.close()
        del dialogWait
        ye = murl[39:44]
        addDir('[COLOR blue]Page 2[/COLOR]','http://www.movie25.com/search.php?page=2&year='+str(ye),9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        VIEWS()
        GA("Year","Year-list")
        
def NEXTPAGE(murl):
    match=re.compile('documentaryheaven').findall(murl)
    if (len(match)>0):
        link=OPENURL(murl)
        match=re.compile('<a href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        if (len(match)==0):
            match=re.compile('href="(.+?)" title="" rel=".+?"><img class=".+?" src="(.+?)" alt="(.+?)".+?</a>\n                            </div>     \n                            <div id="postDis">\n                            \t(.+?)[...]').findall(link)
        for url,thumb,name,desc in match:
            addSport(name,url,88,thumb,desc,'','')
        paginate=re.compile('http://documentaryheaven.com/page/(.+?)/.?s=(.+?)').findall(murl)
        for page, search in paginate:
            pgs = int(page)+1
            jurl='http://documentaryheaven.com/page/'+str(pgs)+'/?s='+str(search)
        addDir('[COLOR blue]Page '+str(pgs)+'[/COLOR]',jurl,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

    else:
        link=OPENURL(murl)
        match=re.compile('<div class="movie_pic"><a href="(.+?)" target="_blank">\n                            <img src="(.+?)" width=".+?" height=".+?" />\n                            </a></div>\n            <div class="movie_about">\n              <div class="movie_about_text">\n                <h1><a href=".+?" target="_blank">\n                  (.+?)                </a></h1>\n                <div class="c">Genre:\n                  <a href=".+?" target=\'.+?\'>(.+?)</a>').findall(link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,mname,genre in match:
                namelen=len(mname)
                if mname[-4:namelen-3] == ')':
                        nam= namelen- 8
                        year = mname[nam:namelen-4]
                        name= mname[0:namelen-9]
                elif mname[-3:namelen-2] == ')':
                        nam= namelen- 7
                        year = mname[nam:namelen-3]
                        name= mname[0:namelen-8]
                else:
                        name = mname
                        year = ''
                name=name.replace('-','').replace('&','').replace('acute;','')
                furl= 'http://movie25.com/'+url
                addInfo(name+'('+year+')',furl,3,thumb,genre,year)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False
        dialogWait.close()
        del dialogWait
        matchx=re.compile('http://www.movie25.com/search.php.+?page=(.+?)&year=(.+?)').findall(murl)
        if len(matchx)>0:
                durl = murl + '/'
                paginate=re.compile('http://www.movie25.com/search.php.+?page=(.+?)&year=(.+?)/').findall(durl)
                for page, yearb in paginate:
                        pgs = int(page)+1
                        jurl='http://www.movie25.com/search.php?page='+str(pgs)+'&year='+str(yearb)
                xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
                VIEWS()                
        else:
                durl = murl + '/'
                paginate=re.compile('http://www.movie25.com/search.php.+?page=(.+?)&key=(.+?)/').findall(durl)
                for page, search in paginate:
                        pgs = int(page)+1
                        jurl='http://www.movie25.com/search.php?page='+str(pgs)+'&key='+str(search)
        addDir('[COLOR red]Home[/COLOR]','',0,"%s/art/home.png"%selfAddon.getAddonInfo("path"))
        addDir('[COLOR blue]Page '+str(pgs)+'[/COLOR]',jurl,9,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        
        


def LISTTV(murl):
        Tvurl='http://www.iwatchonline.org/tv-show'
        link=OPENURL(murl)
        match=re.compile('<a href="(.+?)" ><img src="(.+?)"  border=".+?"  alt=.+?  title=(.+?)  id=".+?"  style').findall(link)
        for url,thumb,name in match:
                name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                namelen=len(name)     
                addDir(name,url,29,thumb)
        paginate=re.compile('http://www.iwatchonline.org/tv-show/(.+?).?limit=18').findall(murl)
        paginate2=re.compile('http://www.iwatchonline.org/tv-show/(.+?).?page=(.+?)&limit=18').findall(murl)
        for section in paginate:
                if (len(paginate) > 0)and (len(paginate2) == 0) :
                        purl = Tvurl + '/'+section+'?page=2&limit=18'
                        addDir('[COLOR blue]Page 2[/COLOR]',purl,28,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
                
        paginate=re.compile('http://www.iwatchonline.org/tv-show/(.+?).?page=(.+?)&limit=18').findall(murl)
        for section, page in paginate:
                if (len(paginate) > 0):
                        pg= int(page) +1
                        purl = Tvurl + '/'+section+'?page='+str(pg)+'&limit=18'
                        addDir('[COLOR red]Home[/COLOR]','http://www.iwatchonline.org',0,"%s/art/home.png"%selfAddon.getAddonInfo("path"))
                        addDir('[COLOR blue]Page '+ str(pg)+'[/COLOR]',purl,28,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        VIEWS()
        GA("TV","iWatchonline")
def LISTTV2(murl):
        urllist=['http://www.movie1k.org/category/tv-show/','http://www.movie1k.org/category/tv-show/page/2/','http://www.movie1k.org/category/tv-show/page/3/','http://www.movie1k.org/category/tv-show/page/4/','http://www.movie1k.org/category/tv-show/page/5/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = 5
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for murl in urllist:
                link=OPENURL(murl)
                match=re.compile('href="(.+?)"><img width=".+?" height=".+?" src="(.+?)" class=".+?" alt="Watch.+?" title="(.+?)" />').findall(link)
                for url,thumb,name in match:
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        addDir(name,url,31,thumb)
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("TV","Movie1k")        
def LISTTV3(murl):
        urllist=['http://oneclickwatch.org/category/tv-shows/','http://oneclickwatch.org/category/tv-shows/page/2/','http://oneclickwatch.org/category/tv-shows/page/3/','http://oneclickwatch.org/category/tv-shows/page/4/','http://oneclickwatch.org/category/tv-shows/page/5/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = 5
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for murl in urllist:
                link=OPENURL(murl)
                match=re.compile('<a href="(.+?)" rel="bookmark" title="Permanent Link to .+?">(.+?)</a>').findall(link)
                for url,name in match:
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        addDir(name,url,31,'')
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("TV","Oneclickwatch")


def LISTTV4(murl):
        addLink('[COLOR red]First Set of Links Are SD usually the first 4, The rest are HD[/COLOR]','',"%s/art/tvb.png"%selfAddon.getAddonInfo("path"))
        urllist=['http://www.rlsmix.net/category/tv-shows/','http://www.rlsmix.net/category/tv-shows/page/2/','http://www.rlsmix.net/category/tv-shows/page/3/','http://www.rlsmix.net/category/tv-shows/page/4/','http://www.rlsmix.net/category/tv-shows/page/5/']
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Show list is cached.')
        totalLinks = 5
        loadedLinks = 0
        remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0,'[B]Will load instantly from now on[/B]',remaining_display)
        for murl in urllist:
                link=OPENURL(murl)
                match=re.compile('<a href="(.+?)" title="Permanent Link to (.+?)">').findall(link)
                for url,name in match:
                        name=name.replace('\xc2\xa0','').replace('" ','').replace(' "','').replace('"','').replace("&#039;","'").replace("&amp;","and").replace("&#8217;","'").replace("amp;","and").replace("#8211;","-")
                        addDir(name,url,62,'')
                
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Pages loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        GA("TV","Rlsmix")
        
############################################################################################ WFS BEGINS ##############################################################################
def GETMETAShow(mname): 
        if selfAddon.getSetting("meta-view") == "true":
                name=mname.replace(' [COLOR red]Recently Updated[/COLOR]','').replace('.','').replace('M.D.','').replace('<span class="updated">Updated!</span>','')    
                year=''
                namelen=len(name)
                if name[-1:namelen] == ' ':
                       name= name[0:namelen-1]
                namelen=len(name)
                if name[-1:namelen] == '  ':
                       name= name[0:namelen-1]
                namelen=len(name)
                if name[-1:namelen] == '  ':
                       name= name[0:namelen-1]
                if name == 'Chase':
                        name = 'Chase (2010)'
                elif name == 'Castle':
                        name = 'Castle (2009)'
                name= name.replace('-','').replace('-2012','').replace('acute;','').replace('Vampire Diaries','The Vampire Diaries').replace('Comedy Central Roast','Comedy Central Roasts')
                name= name.replace('Doctor Who  2005','Doctor Who').replace(' (US)','(US)').replace(' (UK)','(UK)').replace(' (AU)','(AU)').replace('%','')
                meta = grab.get_meta('tvshow',name,None,None,year,overlay=6)# first is Type/movie or tvshow, name of show,tvdb id,imdb id,string of year,unwatched = 6/watched  = 7
                print "Tv Mode: %s"%name
                infoLabels = {'rating': meta['rating'],'duration': meta['duration'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],
                  'plot': meta['plot'],'title': mname,'cover_url': meta['cover_url'],
                  'cast': meta['cast'],'studio': meta['studio'],'banner_url': meta['banner_url'],
                      'backdrop_url': meta['backdrop_url'],'status': meta['status']}
                if infoLabels['cover_url']=='':
                        infoLabels['cover_url']="%s/art/vidicon.png"%selfAddon.getAddonInfo("path")
        else:
                infoLabels = {'title': mname,'cover_url': "%s/art/vidicon.png"%selfAddon.getAddonInfo("path"),'backdrop_url': ''}
        return infoLabels

def GETMETAEpi(mname,data):
        if selfAddon.getSetting("meta-view") == "true":
                match=re.compile('(.+?)xoxc(.+?)xoxc(.+?)xoxc(.+?)xoxc').findall(data)
                for showname, sea, epi, epiname in match:
                        showname= showname.replace('-','').replace('-2012','').replace('acute;','').replace('Comedy Central Roast','Comedy Central Roasts')
                        showname= showname.replace('Doctor Who  2005','Doctor Who').replace(' (US)','(US)').replace(' (UK)','(UK)').replace(' (AU)','(AU)').replace('%','').replace(' [COLOR red]Recently Updated[/COLOR]','').replace('.','').replace('M.D.','').replace('<span class="updated">Updated!</span>','')
                        print showname+' '+sea+' '+epi+' '+epiname
                meta = grab.get_episode_meta(str(showname),None, int(sea), int(epi),episode_title=str(epiname), overlay='6')
                print "Episode Mode: Name %s Season %s - Episode %s"%(str(epiname),str(sea),str(epi))
                infoLabels = {'rating': meta['rating'],'duration': meta['duration'],'genre': meta['genre'],'mpaa':"rated %s"%meta['mpaa'],
                      'plot': meta['plot'],'title': meta['title'],'cover_url': meta['cover_url'],
                      'poster': meta['poster'],'season': meta['season'],'episode': meta['episode'],'backdrop_url': meta['backdrop_url']}
        else:
                infoLabels = {'title': mname,'cover_url': '','backdrop_url': ''}       
        
        return infoLabels

def MAINWFS():
        addDir('Search','wfs',522,"%s/art/wfs/search.png"%selfAddon.getAddonInfo("path"))
        addDir('A-Z','http://watch-freeseries.mu/tvseries',510,"%s/art/wfs/az.png"%selfAddon.getAddonInfo("path"))
        addDir('This Week Episodes','http://watch-freeseries.mu/this-week-episodes/',528,"%s/art/wfs/latest.png"%selfAddon.getAddonInfo("path"))
        addDir('Popular TV Series','http://watch-freeseries.mu/',511,"%s/art/wfs/popu.png"%selfAddon.getAddonInfo("path"))
        addDir('TV Series','http://watch-freeseries.mu/tvseries',506,"%s/art/wfs/series.png"%selfAddon.getAddonInfo("path"))
        addDir('Year','http://watch-freeseries.mu/',505,"%s/art/wfs/year.png"%selfAddon.getAddonInfo("path"))
        addDir('Genre','http://watch-freeseries.mu/',502,"%s/art/wfs/genre.png"%selfAddon.getAddonInfo("path"))
        addDir('Download All Meta','http://watch-freeseries.mu/',527,"%s/art/wfs/metaall.png"%selfAddon.getAddonInfo("path"))
        GA("Plugin","WFS")
        VIEWSB()
    

def GetMetAll():
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('Download All Meta.', 'Download all meta information for videos at once.','Its better to get it out the way.', 'Would you like to download it? It takes around 20 minutes.','No', 'Yes')
        if ret==True:
                if selfAddon.getSetting("meta-view") == "false":
                    ret = dialog.ok('Error','Enable Metadata in Settings first')
                else:
                    urllist=[]
                    loadedparts = 1
                    urllist.append('http://watch-freeseries.mu/index.php?action=episodes_searchShow&letter=1')
                    for i in string.ascii_uppercase:
                            url='http://watch-freeseries.mu/index.php?action=episodes_searchShow&letter='+i  
                            urllist.append(url)
                    for murl in urllist:
                            print murl
                            link=OPENURL(murl)
                            match=re.compile('<div class=".+?">\n                    <a href="(.+?)">\n                        <span class=".+?">(.+?)</span>\n                        <span class=".+?t">(.+?)</span>\n').findall(link)
                            dialogWait = xbmcgui.DialogProgress()
                            ret = dialogWait.create('[B]Please wait until TV Shows Meta is cached.[/B]')
                            totalLinks = len(match)
                            loadedLinks = 0
                            parts= len(urllist)
                            remaining_display = 'Parts loaded:: [B]'+str(loadedparts)+' / '+str(parts)+'[/B].''       TV Shows loaded:: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                            dialogWait.update(0, 'Process loads in 27 parts Numbers, A thru Z',remaining_display)
                            for url,name,year in match:
                                    GETMETAShow(name)
                                    loadedLinks = loadedLinks + 1
                                    percent = (loadedLinks * 100)/totalLinks
                                    remaining_display ='Parts loaded:: [B]'+str(loadedparts)+' / '+str(parts)+'[/B].''       TV Shows loaded:: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                                    dialogWait.update(percent,'Process loads in 27 parts Numbers, A thru Z',remaining_display)
                                    if (dialogWait.iscanceled()):
                                            return False
                            loadedparts = loadedparts + 1
                    xbmc.executebuiltin("XBMC.Notification(Nice!,Metacontainer DB Installation Success,5000)")

        MAINWFS()
def AtoZWFS():
        addDir('0-9','http://watch-freeseries.mu/index.php?action=episodes_searchShow&letter=1',506,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
        for i in string.ascii_uppercase:
                addDir(i,'http://watch-freeseries.mu/index.php?action=episodes_searchShow&letter='+i,506,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
        GA("WFS","A-Z")
        VIEWSB()        
def GENREWFS(url):
        addDir('Action','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=2',506,"%s/art/wfs/act.png"%selfAddon.getAddonInfo("path"))
        addDir('Adventure','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=5',506,"%s/art/wfs/adv.png"%selfAddon.getAddonInfo("path"))
        addDir('Animation','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=6',506,"%s/art/wfs/ani.png"%selfAddon.getAddonInfo("path"))
        addDir('Awards','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=32',506,"%s/art/wfs/awa.png"%selfAddon.getAddonInfo("path"))
        addDir('Biography','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=8',506,"%s/art/wfs/bio.png"%selfAddon.getAddonInfo("path"))
        addDir('Cartoons','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=30',506,"%s/art/wfs/car.png"%selfAddon.getAddonInfo("path"))
        addDir('Comedy','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=9',506,"%s/art/wfs/com.png"%selfAddon.getAddonInfo("path"))
        addDir('Cooking','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=38',506,"%s/art/wfs/coo.png"%selfAddon.getAddonInfo("path"))
        addDir('Crime','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=10',506,"%s/art/wfs/cri.png"%selfAddon.getAddonInfo("path"))
        addDir('Documentary','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=11',506,"%s/art/wfs/doc.png"%selfAddon.getAddonInfo("path"))
        addDir('Drama','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=3',506,"%s/art/wfs/dra.png"%selfAddon.getAddonInfo("path"))
        addDir('Family','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=12',506,"%s/art/wfs/fam.png"%selfAddon.getAddonInfo("path"))
        addDir('Fantasy','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=1',506,"%s/art/wfs/fan.png"%selfAddon.getAddonInfo("path"))
        addDir('Fashion','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=35',506,"%s/art/wfs/fas.png"%selfAddon.getAddonInfo("path"))
        addDir('Food','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=31',506,"%s/art/wfs/foo.png"%selfAddon.getAddonInfo("path"))
        addDir('Game Show','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=33',506,"%s/art/wfs/gam.png"%selfAddon.getAddonInfo("path"))
        addDir('History','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=14',506,"%s/art/wfs/his.png"%selfAddon.getAddonInfo("path"))
        addDir('Horror','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=4',506,"%s/art/wfs/hor.png"%selfAddon.getAddonInfo("path"))
        addDir('Late Night','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=37',506,"%s/art/wfs/lat.png"%selfAddon.getAddonInfo("path"))
        addDir('Motorsports','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=29',506,"%s/art/wfs/mot.png"%selfAddon.getAddonInfo("path"))
        addDir('Music','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=17',506,"%s/art/wfs/mus.png"%selfAddon.getAddonInfo("path"))
        addDir('Musical','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=18',506,"%s/art/wfs/musi.png"%selfAddon.getAddonInfo("path"))
        addDir('Mystery','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=16',506,"%s/art/wfs/mys.png"%selfAddon.getAddonInfo("path"))
        addDir('Reality Tv','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=19',506,"%s/art/wfs/rea.png"%selfAddon.getAddonInfo("path"))
        addDir('Romance','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=20',506,"%s/art/wfs/rom.png"%selfAddon.getAddonInfo("path"))
        addDir('Sci-Fi','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=21',506,"%s/art/wfs/sci.png"%selfAddon.getAddonInfo("path"))
        addDir('Short','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=22',506,"%s/art/wfs/sho.png"%selfAddon.getAddonInfo("path"))
        addDir('Sport','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=23',506,"%s/art/wfs/spo.png"%selfAddon.getAddonInfo("path"))
        addDir('Talk','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=27',506,"%s/art/wfs/tal.png"%selfAddon.getAddonInfo("path"))
        addDir('Talk Show','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=39',506,"%s/art/wfs/tals.png"%selfAddon.getAddonInfo("path"))
        addDir('Teen','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=34',506,"%s/art/wfs/tee.png"%selfAddon.getAddonInfo("path"))
        addDir('Thriller','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=24',506,"%s/art/wfs/thr.png"%selfAddon.getAddonInfo("path"))
        addDir('War','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=25',506,"%s/art/wfs/war.png"%selfAddon.getAddonInfo("path"))
        addDir('Western','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=26',506,"%s/art/wfs/wes.png"%selfAddon.getAddonInfo("path"))
        GA("WFS","Genre")
        VIEWSB()
def YEARWFS():
        addDir('2013','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2013',506,"%s/art/wfs/2013.png"%selfAddon.getAddonInfo("path"))
        addDir('2012','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2012',506,"%s/art/wfs/2012.png"%selfAddon.getAddonInfo("path"))
        addDir('2011','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2011',506,"%s/art/wfs/2011.png"%selfAddon.getAddonInfo("path"))
        addDir('2010','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2010',506,"%s/art/wfs/2010.png"%selfAddon.getAddonInfo("path"))
        addDir('2009','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2009',506,"%s/art/wfs/2009.png"%selfAddon.getAddonInfo("path"))
        addDir('2008','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2008',506,"%s/art/wfs/2008.png"%selfAddon.getAddonInfo("path"))
        addDir('2007','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2007',506,"%s/art/wfs/2007.png"%selfAddon.getAddonInfo("path"))
        addDir('2006','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2006',506,"%s/art/wfs/2006.png"%selfAddon.getAddonInfo("path"))
        addDir('2005','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2005',506,"%s/art/wfs/2005.png"%selfAddon.getAddonInfo("path"))
        addDir('2004','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2004',506,"%s/art/wfs/2004.png"%selfAddon.getAddonInfo("path"))
        addDir('2003','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2003',506,"%s/art/wfs/2003.png"%selfAddon.getAddonInfo("path"))
        GA("WFS","Year")
        VIEWSB()
def LISTEpi(murl):
        link=OPENURL(murl)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Latest Episodes are cached.')
        match=re.compile('<a href="(.+?)">\n                                                                        <img src="(.+?)"/>\n                                                                    </a>\n                            </div>\n                                <div class=".+?">\n                                <a class=".+?" style=".+?" href=".+?">(.+?)<br>(.+?)</a>(.+?)<br/>(.+?)\n                            </div>\n').findall(link)
        totalLinks = len(match)
        print totalLinks
        loadedLinks = 0
        remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,epname,eps,epnum in match:
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Episodes loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False
                addDir(name+'   "'+epname+'"',url,503,thumb)
        GA("WFS","Latest-list")
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        
def LISTShows(murl):
        link=OPENURL(murl)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Tv Shows are cached.')
        match=re.compile('<div class=".+?">\n                    <a href="(.+?)">\n                        <span class=".+?">(.+?)</span>\n                        <span class=".+?t">(.+?)</span>\n').findall(link)
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,name,year in match:
                
                match=re.compile('<span class="updated">Updated!</span>').findall(name)
                if (len(match)>0):
                        name=name.replace(' <span class="updated">Updated!</span>','')
                        name= name+'  [COLOR red]Recently Updated[/COLOR]'
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False
                addInfo2(name,url,507,'','')
        GA("WFS","Shows-list")
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')


        
def LISTPop(murl):
        link=OPENURL(murl)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Tv Shows are cached.')
        match=re.compile('<a href="(.+?)" title="(.+?)"><span class="new_rank">.+?</span>').findall(link)
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,name in match:
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False
                addInfo2(name,url,507,'','')
        GA("WFS","MostPOP-list")
        xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')

        
                
def LISTSeason(mname,murl):
        GA("WFS","Sea-list")
        link=OPENURL(murl)
        mname=mname.replace('Vampire Diaries','The Vampire Diaries')

        match=re.compile('<h4><a href="#(.+?)">(.+?)</a></h4>\n').findall(link)
        for num,name in match:
                mname=mname.replace(' [COLOR red]Recently Updated[/COLOR]','').replace('.','').replace('M.D.','').replace('<span class="updated">Updated!</span>','')
                mname= mname.replace('-','').replace('-2012','').replace('acute;','').replace('Vampire Diaries','The Vampire Diaries').replace('Comedy Central Roast','Comedy Central Roasts')
                mname= mname.replace('Doctor Who  2005','Doctor Who').replace(' (US)','(US)').replace(' (UK)','(UK)').replace(' (AU)','(AU)').replace('%','')
                if selfAddon.getSetting("meta-view") == "true":
                        cover = grab.get_seasons(mname, None, num, overlay=6)
                        covers= re.compile("cover_url.+?'(.+?)'").findall(str(cover))
                        for thumb in covers:
                                print thumb
                else:
                        thumb=''
                addDir(name,murl+'xoxc'+mname+'xoxc'+num+'xoxc',508,str(thumb))
        xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
        if selfAddon.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting('seasons-view'))          
        
def LISTEpilist(name,murl):
        GA("WFS","Epi-list")
        match=re.compile('http://watch-freeseries.mu/tv/.+?/.+?xoxc(.+?)xoxc(.+?)xoxc').findall(murl)
        for showname, sea in match:
                season=sea
                murl=murl.replace('xoxc'+sea+'xoxc','').replace(str(showname),'').replace('xoxc','')
        link=OPENURL(murl)
        match2=re.compile(r'\d+').findall(name)
        for num in match2:
                x=str(num)
        match=re.compile('class="link-name" href="(.+?)/season/'+x+'/(.+?)">(.+?)</a></td>\n').findall(link)
        for url,url2,name in match:
                url=url+'/season/'+x+'/'+url2
                name =name +'xoxc'
                match=re.compile('Episode (.+?) - (.+?)xoxc').findall(name)
                for epinum, epiname in match:
                        print epinum

                data=str(showname)+'xoxc'+str(season)+'xoxc'+str(epinum)+'xoxc'+str(epiname)+'xoxc'
                name=name.replace('xoxc','')
                addEpi(name,url,503,'',data)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
        if selfAddon.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting('episodes-view'))        
        


def Searchhistorywfs():
        seapath=os.path.join(datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='wfs'
            SEARCHWFS(url)
        else:
            addDir('Search','wfs',504,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    addDir(seahis,url,504,thumb)
            
            
    


def SEARCHWFS(murl):
        seapath=os.path.join(datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'wfs':
                keyb = xbmc.Keyboard('', 'Search For Shows or Episodes')
                keyb.doModal()
                if (keyb.isConfirmed()):
                        search = keyb.getText()
                        encode=urllib.quote(search)
                        surl='http://watch-freeseries.mu/index.php?action=episodes_ajaxQuickSearchSuggest&limit=10&keywords='+encode
                        if not os.path.exists(SeaFile) and encode != '':
                            open(SeaFile,'w').write('search="%s",'%encode)
                        else:
                            if encode != '':
                                open(SeaFile,'a').write('search="%s",'%encode)
                        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                        for seahis in reversed(searchis):
                            continue
                        if len(searchis)>=10:
                            searchis.remove(searchis[0])
                            os.remove(SeaFile)
                            for seahis in searchis:
                                try:
                                    open(SeaFile,'a').write('search="%s",'%seahis)
                                except:
                                    pass
        else:
                encode = murl
                surl='http://watch-freeseries.mu/index.php?action=episodes_ajaxQuickSearchSuggest&limit=10&keywords='+encode
        req = urllib2.Request(surl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('{"id":.+?,"label":".+?","value":"(.+?)","modrwName":"(.+?)"}').findall(link)
        for name,url in match:
                url=url.replace('\/','/')
                match=re.compile('season').findall(url)
                if (len(match)>0):
                        addDir(name,url,503,'')
                else:
                    addInfo2(name,url,507,'','')
        GA("WFS","Search")

def GETLINKWFS(url):
        link=OPENURL(url)
        match=re.compile('<br>\n        <a href="(.+?)" title="" class=".+?"').findall(link)
        for url in match:
                return url   

def VIDEOLINKSWFS(name,url):
        GA("WSF","Watched")
        sources = []
        link=OPENURL(url)
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,3000)")
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">putlocker.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Putlocker'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">sockshare.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Sockshare'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">flashx.tv</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Flashx'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">180upload.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='180upload'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">nowvideo.eu</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Nowvideo'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">movreel.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Movreel'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">sharesix.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='ShareSix'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">filenuke.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Filenuke'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">videoweed.es</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Videoweed'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">novamov.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Novamov'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">vidbux.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host='Vidbux'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">vidxden.com</a></p></td>').findall(link)
        for url in match[0:2]:
                url=GETLINKWFS(url)
                host= 'Vidxden'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
                
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                      stream_url = False
                      return
                listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': name, 'Year': ''} )       
                xbmc.Player().play(stream_url, listitem)
                addDir('','','','')
############################################################################################ WFS ENDS ##############################################################################
############################################################################################ SERIES GATE BEGIN ##############################################################################
def MAINSG():
        addDir('Search','sg',612,"%s/art/wfs/search.png"%selfAddon.getAddonInfo("path"))
        addDir('A-Z','http://seriesgate.tv/',610,"%s/art/wfs/az.png"%selfAddon.getAddonInfo("path"))
        addDir('Latest Episodes','http://seriesgate.tv/latestepisodes/',602,"%s/art/wfs/latest.png"%selfAddon.getAddonInfo("path"))
        HOMESG()
        GA("Plugin","SeriesGate")
        #addDir('TV Series','http://watch-freeseries.mu/tvseries',506,"%s/art/wfs/series.png"%selfAddon.getAddonInfo("path"))
        #addDir('Year','http://watch-freeseries.mu/',505,"%s/art/wfs/year.png"%selfAddon.getAddonInfo("path"))
        #addDir('Genre','http://watch-freeseries.mu/',502,"%s/art/wfs/genre.png"%selfAddon.getAddonInfo("path"))
def HOMESG():
        url='http://seriesgate.tv/'
        link=OPENURL(url)
        addLink('[COLOR red]Updated Shows[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[0:5]:
            addDir(name,url,604,thumb)
        addLink('[COLOR red]Knee Slapping Comedies[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[5:10]:
            addDir(name,url,604,thumb)
        addLink('[COLOR red]Turmoil and Tears: Drama[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[10:15]:
            addDir(name,url,604,thumb)
        addLink('[COLOR red]Rumbling and Tumbling Action[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[15:20]:
            addDir(name,url,604,thumb)
        addLink("[COLOR red]Editor's Flicks[/COLOR]",'','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[20:25]:
            addDir(name,url,604,thumb)
        addLink('[COLOR red]New to SeriesGate[/COLOR]','','')
        match=re.compile('<a href = "([^<]+)" style=".+?"><img src="(.+?)"  height=".+?" width=".+?" alt="Watch (.+?)"').findall(link)
        for url,thumb,name in match[25:30]:
            addDir(name,url,604,thumb)
            
def AtoZSG():
        addDir('0-9','0-9',611,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
        for i in string.ascii_uppercase:
                addDir(i,i,611,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
        GA("SeriesGate","A-Z")
        VIEWSB()
        
def AllShows(murl):
        gurl='http://seriesgate.tv/'
        link=OPENURL(gurl)
        match=re.compile('{"n":"(.+?)","u":"(.+?)","i":"(.+?)"}').findall(link)
        for name,surl,imdb, in match:
                name2 =name
                if name[0:3]=='The':
                    name2=name.replace('The ','')
                if murl == '0-9':
                    if name2[0:1] <= '9':
                        durl='http://seriesgate.tv/'+surl+'/'
                        thumb ='http://cdn.seriesgate.tv/6/cover/110x160/'+surl+'.png'
                        addDir(name,durl,604,thumb)
                    
                elif name2[0:1] == murl:
                    durl='http://seriesgate.tv/'+surl+'/'
                    thumb ='http://cdn.seriesgate.tv/6/cover/110x160/'+surl+'.png'
                    addDir(name,durl,604,thumb)
        GA("SeriesGate","AllShows")
def LISTEpiSG(murl):
    link=OPENURL(murl)
    match=re.compile('<a href="(.+?)"><div  class=".+?"><img  class=".+?" src=""  data-original ="(.+?)" width=".+?" height=".+?"  alt=".+?" title = "(.+?)" /><div class=".+?"><span style=".+?">(.+?)</span><div class=".+?"></div><span>(.+?)</span><div class=".+?">').findall(link)
    for url,thumb,epiname, showname, seep in match:
        durl = url+'more_sources/'
        addDir(showname+' [COLOR red]'+seep+'[/COLOR]'+" "+'"'+epiname+'"',durl,609,thumb)
    GA("SeriesGate","Latest-list")
def LISTSeasonSG(mname,murl):
    link=OPENURL(murl)
    match=re.compile('<div class="season_page">\n\t\t\t\t\t\t<a href="(.+?)" >(.+?)</a>').findall(link)
    for url, seaname in match:
        num=re.compile('Season ([^<]+)').findall(seaname)
        if selfAddon.getSetting("meta-view") == "true":
            print num[0]
            cover = grab.get_seasons(mname, None, num[0], overlay=6)
            print str(cover)
            covers= re.compile("cover_url.+?'(.+?)'").findall(str(cover))
            for thumb in covers:
                thumb = str(thumb)
                thumb= thumb.replace("',","%s/art/tv2.png"%selfAddon.getAddonInfo("path"))
                print thumb
        else:
            thumb=''
        durl = 'http://seriesgate.tv'+url
        addDir(seaname,durl,605,str(thumb))
        xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
        GA("SeriesGate","Sea-list")
def LISTEpilistSG(mname,murl):
    link=OPENURL(murl)
    #match=re.compile('<div class=".+?" style=".+?" >(.+?)- <span><a href = ".+?">.+?</a></span></div><div class=".+?" >(.+?)</div><div class = ".+?"></div><div style=".+?"><a href="(.+?)"><img src="(.+?)" width=".+?" height=".+?"  alt=".+?" title = "(.+?)" ></a></div><div class = ".+?" style = ".+?"><div class="s_page_season_description">(.+?)</div>').findall(link)
    #if len(match) == 0:
    match=re.compile('<div class=".+?" style=".+?" >(.+?)- <span><a href = ".+?">.+?</a></span></div><div class=".+?" >(.+?)</div><div class = ".+?"></div><div style=".+?"><a href="(.+?)"><img src="(.+?)" width=".+?" height=".+?"  alt=".+?" title = "(.+?)" ></a>').findall(link)
    for seep, airdate, url, thumb, epiname in match:
        durl = 'http://seriesgate.tv'+url+'more_sources/'
        addDir2(seep+" "+'"'+epiname+'"',durl,609,thumb,'')
    GA("SeriesGate","Epi-list")

def SearchhistorySG():
        seapath=os.path.join(datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        if not os.path.exists(SeaFile):
            url='sg'
            SEARCHSG(url)
        else:
            addDir('Search','sg',608,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
            thumb="%s/art/link.png"%selfAddon.getAddonInfo("path")
            searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
            for seahis in reversed(searchis):
                    url=seahis
                    seahis=seahis.replace('%20',' ')
                    addDir(seahis,url,608,thumb)
            
            


def SEARCHSG(murl):
        seapath=os.path.join(datapath,'Search')
        SeaFile=os.path.join(seapath,'SearchHistoryTv')
        try:
            os.makedirs(seapath)
        except:
            pass
        if murl == 'sg':
            keyb = xbmc.Keyboard('', 'Search For Shows or Episodes')
            keyb.doModal()
            if (keyb.isConfirmed()):
                    search = keyb.getText()
                    encode=urllib.quote(search)
                    surl='http://seriesgate.tv/search/indv_episodes/'+encode+'/'
                    if not os.path.exists(SeaFile) and encode != '':
                        open(SeaFile,'w').write('search="%s",'%encode)
                    else:
                        if encode != '':
                            open(SeaFile,'a').write('search="%s",'%encode)
                    searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
                    for seahis in reversed(searchis):
                        continue
                    if len(searchis)>=10:
                        searchis.remove(searchis[0])
                        os.remove(SeaFile)
                        for seahis in searchis:
                            try:
                                open(SeaFile,'a').write('search="%s",'%seahis)
                            except:
                                pass


        else:
            encode = murl
            surl='http://seriesgate.tv/search/indv_episodes/'+encode+'/'    
        req = urllib2.Request(surl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        addLink('[COLOR red]Shows[/COLOR]','','')
        match=re.compile('src = "([^<]+)" height=".+?" width=".+?" alt=""  /></a><div class = ".+?" style=".+?"><div class = ".+?"><a href = "([^<]+)">([^<]+)</a></div><a href = ".+?">').findall(link)
        for thumb,url,name in match:
                addDir(name,url,604,thumb)
        addLink('[COLOR red]Episodes[/COLOR]','','')
        match=re.compile('src="([^<]+)" width=".+?" height=".+?"  /></a></div><div style=".+?"><a style=".+?" href = "([^<]+)"><span style=".+?">([^<]+)</span></a><span style=".+?">EPISODE</span><div class=".+?"></div><span style=".+?">([^<]+)</span>').findall(link)
        for thumb,url,epiname, name in match:
                durl = url+'more_sources/'
                addDir(name+' [COLOR red]"'+epiname+'"[/COLOR]',durl,609,thumb)
        GA("SeriesGate","Search")


def GETLINKSG(murl):
        durl= 'http://seriesgate.tv'+murl
        link=OPENURL(durl)
        link=link.replace('var url = "http://cdn.seriesgate.tv','')
        match=re.compile('var url = "(.+?)";').findall(link)
        for url in match:
                return url

def VIDEOLINKSSG(mname,murl):
        
        GA("SG","Watched")
        sources = []
        link=OPENURL(murl)
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,3000)")
        match=re.compile('TARGET=".+?" href="(.+?)">XVidStage</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='XVidStage'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match2=re.compile('TARGET=".+?" href="(.+?)">Sockshare</a>').findall(link)
        if len(match2)==0:
            match2=re.compile('TARGET=".+?" href="(.+?)">SockShare</a>').findall(link)
        for url in match2[0:3]:
                url=GETLINKSG(url)
                host='Sockshare'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">nowvideo</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='Nowvideo'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match3=re.compile('TARGET=".+?" href="(.+?)">Putlocker</a>').findall(link)
        if len(match3)==0:
            match3=re.compile('TARGET=".+?" href="(.+?)">PutLocker</a>').findall(link)
        for url in match3[0:3]:
                url=GETLINKSG(url)
                host='Putlocker'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">Flashx TV</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='Flashx'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">HostingBulk</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='HostingBulk'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">MovReel</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='MovReel'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">Share Six</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='Share Six'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">2GB Hosting</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='2GB Hosting'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">Filenuke</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='Filenuke'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">VideoWeed</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='Videoweed'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">NovaMov</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='Novamov'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">vidbux</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host='Vidbux'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('TARGET=".+?" href="(.+?)">Vidxden</a>').findall(link)
        for url in match[0:3]:
                url=GETLINKSG(url)
                host= 'Vidxden'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
                
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                      stream_url = False
                      return
                listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': name, 'Year': ''} )       
                xbmc.Player().play(stream_url, listitem)
                addDir('','','','')
############################################################################################ SERIES GATE END ##############################################################################



def VIDEOLINKS(name,url):
        link=OPENURL(url)
        qual = re.compile('<h1 >Links - Quality\n              \n              (.+?) <a name="link"></a> </h1>').findall(link)
        quality=str(qual)
        quality=quality.replace("'","")
        putlocker=re.compile('<li class=link_name>putlocker</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(putlocker) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Putlocker[/COLOR]",url,11,"%s/art/put.png"%selfAddon.getAddonInfo("path"),"%s/art/put.png"%selfAddon.getAddonInfo("path"))
        oeupload=re.compile('<li class=link_name>180upload</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(oeupload) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : 180upload[/COLOR]",url,12,"%s/art/180u.png"%selfAddon.getAddonInfo("path"),"%s/art/180u.png"%selfAddon.getAddonInfo("path"))
        filenuke=re.compile('<li class=link_name>filenuke</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(filenuke) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Filenuke[/COLOR]",url,13,"%s/art/fn.png"%selfAddon.getAddonInfo("path"),"%s/art/fn.png"%selfAddon.getAddonInfo("path"))
        flashx=re.compile('<li class=link_name>flashx</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(flashx) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Flashx[/COLOR]",url,15,"%s/art/flash.png"%selfAddon.getAddonInfo("path"),"%s/art/flash.png"%selfAddon.getAddonInfo("path"))
        novamov=re.compile('<li class=link_name>novamov</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(novamov) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Novamov[/COLOR]",url,16,"%s/art/nov.png"%selfAddon.getAddonInfo("path"),"%s/art/nov.png"%selfAddon.getAddonInfo("path"))
        uploadc=re.compile('<li class=link_name>uploadc</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(uploadc) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Uploadc[/COLOR]",url,17,"%s/art/uc.png"%selfAddon.getAddonInfo("path"),"%s/art/uc.png"%selfAddon.getAddonInfo("path"))
        xvidstage=re.compile('<li class=link_name>xvidstage</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(xvidstage) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Xvidstage[/COLOR]",url,18,"%s/art/xvid.png"%selfAddon.getAddonInfo("path"),"%s/art/xvid.png"%selfAddon.getAddonInfo("path"))        
        zooupload=re.compile('<li class=link_name>zooupload</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(zooupload) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Zooupload[/COLOR]",url,19,"%s/art/zooup.png"%selfAddon.getAddonInfo("path"),"%s/art/zooup.png"%selfAddon.getAddonInfo("path"))
        zalaa=re.compile('<li class=link_name>zalaa</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(zalaa) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Zalaa[/COLOR]",url,20,"%s/art/zalaa.png"%selfAddon.getAddonInfo("path"),"%s/art/zalaa.png"%selfAddon.getAddonInfo("path"))
        vidxden=re.compile('<li class=link_name>vidxden</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(vidxden) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Vidxden[/COLOR]",url,21,"%s/art/vidx.png"%selfAddon.getAddonInfo("path"),"%s/art/vidx.png"%selfAddon.getAddonInfo("path"))
        vidbux=re.compile('<li class=link_name>vidbux</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        if len(vidbux) > 0:
                addDirb(name+" [COLOR red]"+quality+"[/COLOR]"+"[COLOR blue] : Vidbux[/COLOR]",url,14,"%s/art/vidb.png"%selfAddon.getAddonInfo("path"),"%s/art/vidb.png"%selfAddon.getAddonInfo("path"))

def PUTLINKS(name,url):
        link=OPENURL(url)
        putlocker=re.compile('<li class=link_name>putlocker</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in putlocker:
                addDirb(name,url,5,"%s/art/put.png"%selfAddon.getAddonInfo("path"),"%s/art/put.png"%selfAddon.getAddonInfo("path"))
def OELINKS(name,url):
        link=OPENURL(url)
        oeupload=re.compile('<li class=link_name>180upload</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in oeupload:
                addDirb(name,url,5,"%s/art/180u.png"%selfAddon.getAddonInfo("path"),"%s/art/180u.png"%selfAddon.getAddonInfo("path"))
def FNLINKS(name,url):
        link=OPENURL(url)
        filenuke=re.compile('<li class=link_name>filenuke</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in filenuke:
                addDirb(name,url,5,"%s/art/fn.png"%selfAddon.getAddonInfo("path"),"%s/art/fn.png"%selfAddon.getAddonInfo("path"))
def FLALINKS(name,url):
        link=OPENURL(url)
        flashx=re.compile('<li class=link_name>flashx</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in flashx:
                addDirb(name,url,5,"%s/art/flash.png"%selfAddon.getAddonInfo("path"),"%s/art/flash.png"%selfAddon.getAddonInfo("path"))
def VIDLINKS(name,url):
        link=OPENURL(url)
        vidbux=re.compile('<li class=link_name>vidbux</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in vidbux:
                addDirb(name,url,5,"%s/art/vidb.png"%selfAddon.getAddonInfo("path"),"%s/art/vidb.png"%selfAddon.getAddonInfo("path"))
def NOVLINKS(name,url):
        link=OPENURL(url)
        novamov=re.compile('<li class=link_name>novamov</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in novamov:
                addDirb(name,url,5,"%s/art/nov.png"%selfAddon.getAddonInfo("path"),"%s/art/nov.png"%selfAddon.getAddonInfo("path"))
def UPLINKS(name,url):
        link=OPENURL(url)
        uploadc=re.compile('<li class=link_name>uploadc</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in uploadc:
                addDirb(name,url,5,"%s/art/uc.png"%selfAddon.getAddonInfo("path"),"%s/art/uc.png"%selfAddon.getAddonInfo("path"))
def XVLINKS(name,url):
        link=OPENURL(url)
        xvidstage=re.compile('<li class=link_name>xvidstage</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in xvidstage:
                addDirb(name,url,5,"%s/art/xvid.png"%selfAddon.getAddonInfo("path"),"%s/art/xvid.png"%selfAddon.getAddonInfo("path"))
def ZOOLINKS(name,url):
        link=OPENURL(url)
        zooupload=re.compile('<li class=link_name>zooupload</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in zooupload:
                addDirb(name,url,5,"%s/art/zooup.png"%selfAddon.getAddonInfo("path"),"%s/art/zooup.png"%selfAddon.getAddonInfo("path"))
def ZALINKS(name,url):
        link=OPENURL(url)
        zalaa=re.compile('<li class=link_name>zalaa</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in zalaa:
                addDirb(name,url,5,"%s/art/zalaa.png"%selfAddon.getAddonInfo("path"),"%s/art/zalaa.png"%selfAddon.getAddonInfo("path"))
def VIDXLINKS(name,url):
        link=OPENURL(url)
        vidxden=re.compile('<li class=link_name>vidxden</li>.+?javascript:window.open.+?url=(.+?)\'').findall(link)
        for url in vidxden:
                addDirb(name,url,5,"%s/art/vidx.png"%selfAddon.getAddonInfo("path"),"%s/art/vidx.png"%selfAddon.getAddonInfo("path"))

def LINKSP(name,url):
        link=OPENURL(url)
        putlocker=re.compile('<a href="(.+?)">putlocker.com</a><br />').findall(link)
        for url in putlocker:
                match=re.compile('http://pastebin.com/.+?').findall(url)
                if (len(match) > 0):
                        link=OPENURL(url)
                        addLink('If list is empty,means the links are downloadable only','','')
                else:
                        addDirb(name,url,5,"%s/art/put.png"%selfAddon.getAddonInfo("path"),"%s/art/put.png"%selfAddon.getAddonInfo("path"))
        flashx=re.compile('<a href="(.+?)">flashx.tv</a><br />').findall(link)
        for url in flashx:
                addDirb(name,url,5,"%s/art/flash.png"%selfAddon.getAddonInfo("path"),"%s/art/flash.png"%selfAddon.getAddonInfo("path"))
        nowvideo=re.compile('<a href="(.+?)">nowvideo.eu</a><br />').findall(link)
        for url in nowvideo:
                addDirb(name,url,5,"%s/art/nov.png"%selfAddon.getAddonInfo("path"),"%s/art/nov.png"%selfAddon.getAddonInfo("path"))
        uploadc=re.compile('<a href="(.+?)">uploadc.com</a><br />').findall(link)
        for url in uploadc:
                addDirb(name,url,5,"%s/art/uc.png"%selfAddon.getAddonInfo("path"),"%s/art/uc.png"%selfAddon.getAddonInfo("path"))
        vidxden=re.compile('<a href="(.+?)">vidxden.com</a><br />').findall(link)
        for url in vidxden:
                addDirb(name,url,5,"%s/art/vidx.png"%selfAddon.getAddonInfo("path"),"%s/art/vidx.png"%selfAddon.getAddonInfo("path"))
        vidbux=re.compile('<a href="(.+?)">vidbux.com</a><br />').findall(link)
        for url in vidbux:
                addDirb(name,url,5,"%s/art/vidb.png"%selfAddon.getAddonInfo("path"),"%s/art/vidb.png"%selfAddon.getAddonInfo("path"))

    
def LINKSP2(mname,url):
        GA("Newmyvideolinks","Watched") 
        sources = []
        link=OPENURL(url)
        link=link.replace('http://newmyvideolinks.com','')
        match=re.compile('<li><a href="h(.+?)">(.+?)</a></li>').findall(link)
        for murl, name in match:
                murl='h'+murl
                #murl=murl.replace('http://newmyvideolinks.com','')
                #name=name.replace('Home','')
                hosted_media = urlresolver.HostedMediaFile(url=murl, title=name)
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Movie doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(reversed(sources))
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Actual HD Movie Requires Buffer Time,7000)")
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                        stream_url = False
                        return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )
                
                xbmc.Player().play(stream_url, listitem)
                
                addDir('','','','')


def LINKSP3(mname,url):
        GA("Dailyfix","Watched")
        sources = []
        link=OPENURL(url)
        match=re.compile("<a href='(.+?)' class='.+?' title='.+?' rel='.+?'>.+?</a").findall(link)
        for murl in match:
                host=re.compile("http://(.+?).com/.+?").findall(murl)
                for hname in host:
                        hname=hname.replace('www.','')
                        hosted_media = urlresolver.HostedMediaFile(url=murl, title=hname)
                        sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Movie doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Actual HD Movie Requires Buffer Time,7000)")
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                        stream_url = False
                        return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )
                
                xbmc.Player().play(stream_url, listitem)
                
                addDir('','','','')

def getlink(url):
        link=OPENURL(url)
        match=re.compile("TargetUrl = \'(.+?)\'").findall(link)
        for vlink in match:
               vid = vlink
        return vid

def LINKSP4(mname,murl):
        sources = []
        GA("Oneclickmovies","Watched")
        link=OPENURL(murl)
        link= link.replace('href="http://oneclickmoviez.com/dws/MEGA','')
        match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>.+?</p>').findall(link)
        for url, host in match:
                print url
                vlink = getlink(url)
                hosted_media = urlresolver.HostedMediaFile(url=vlink, title=host)
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                        stream_url = False
                        return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )         
                xbmc.Player().play(stream_url, listitem)
                        
                addDir('','','','')

def LINKSP5(mname,url):
        GA("Starplay","Watched")
        MainUrl = "http://87.98.161.165/"
        url=MainUrl+url
        link=OPENURL(url)
        match=re.compile("\nfile: \'(.+?)\',\n \nimage: \'/(.+?)\',\n").findall(link)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        desc=' '
        for stream_url, thumb in match:
                stream_url=MainUrl+stream_url
                listitem = xbmcgui.ListItem(mname,thumbnailImage= MainUrl+thumb)
                playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        
        addDir('','','','')
        
def LINKINT(mname,url):
        GA("Einthusan","Watched")
        MainUrl = "http://www.einthusan.com/movies/"
        link=OPENURL(url)
        match = re.compile("'hd-2': { 'file': '(.+?)'").findall(link)
        thumb = re.compile('<img src="(../images.+?)"').findall(link)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        desc=' '
        for stream_url in match:
                listitem = xbmcgui.ListItem(mname,thumbnailImage= MainUrl+thumb[0])
                playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        
        addDir('','','','')

def LINKINT2(name,murl):
        MainUrl = "http://www.dramacrazy.net"
        sources = []
        link=OPENURL(murl)
        match=re.compile('<a class=".+?" href="(.+?)">(.+?)</a>\r\n\t\t\t\t\t\t\t\t<p class=".+?">.+?</p>\r\n\t\t\t\t<div class=".+?"></div>\r\n\t\t\t</div>\r\n\t\t\t\t\t</div>\r\n\t\t<div class=".+?">\r\n\t\t\t\t\t\t<div class=".+?">').findall(link)
        for url, name in match:
                url =MainUrl+url
                link=OPENURL(url)
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
                        addLink('[COLOR blue]'+linkname+' Links[/COLOR]','',selfAddon.getAddonInfo("path")+'/art/'+imagename+'.png')
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
                                        addPlayableLink(partName,'http://www.dramacrazy.net/' + partLink,42,selfAddon.getAddonInfo("path")+'/art/'+imagename+'.png')

def LINKINT3(name,murl):
        sources = []
        GA("Cinevip","Watched")
        link=OPENURL(murl)
        match=re.compile('<span class=".+?">(.+?)</span></td>\n<td>(.+?)</td>\n<td>.+?</td>\n<td>.+?href=http://adf.ly/.+?/(.+?)>').findall(link)
        if len(match) == 0:
                match=re.compile('<span class=".+?">(.+?)</span></td>\n<td>(.+?)</td>\n<td>.+?</td>\n<td>.+?href="http://adf.ly/.+?/(.+?)"').findall(link)
        for host, lang, url in match:
                print url
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host+' [COLOR red]'+lang+'[/COLOR]')
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                        stream_url = False
                        return
                listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': name, 'Year': ''} )         
                xbmc.Player().play(stream_url, listitem)
                        
                addDir('','','','')

def LINKINT4(mname,url):
        GA("Kino-live","Watched")
        link=OPENURL(url)
        match=re.compile('puid.+?=.+?file=.+? or (.+?)" />').findall(link)
        thumb=re.compile('onclick=".+?" ><img src="(.+?)"').findall(link)
        print thumb
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        try:
            thumb2='http://kino-live.org'+str(thumb[0])
        except:
            thumb2 =''
        for stream_url in match:
                listitem = xbmcgui.ListItem(mname,thumbnailImage= thumb2)
                playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        
        addDir('','','','')

def ESPNLink(mname,murl):
        GA("ESPN-List","Watched")
        match=re.compile('(.+?)xovc(.+?)xovc(.+?)xovc').findall(murl)
        for url, desc, thumb in match:
                print url
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = url
        listitem = xbmcgui.ListItem(mname,thumbnailImage= thumb)
        listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addStop('','','','')


def YOULink(mname,url):
        print url
        GA("Youtube-List","Watched")
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+url+"&hd=1"
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = url
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addStop('','','','')
        
def OCLink(mname,url):
        GA("OC-List","Watched")
        link=OPENURL(url)
        match=re.compile('<video src="(.+?)" title="(.+?)" abstract="(.+?)" copyright="Outdoor Channel"').findall(link)
        for video, title, desc in match:
                print video
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        stream_url = video
        listitem = xbmcgui.ListItem(mname)
        listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addStop('','','','')

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
            title=title.replace('3E','').replace('\u0027',"").replace('\u0026#8212\u003B',' ').replace('\u002D',' ')
            mtitle = title
        Thumb=re.compile('"thumbnailURL": "(.+?)",').findall(link)
        for thumb in Thumb:
            thumbList.append(thumb)
        Plot=re.compile('"videoCaption": "(.+?)",').findall(link)
        for plot in Plot:
            plotList.append(plot)
        ETitle=re.compile('"episodeTitle": "(.+?)",').findall(link)
        for etitle in ETitle:
            etitle=etitle.replace('3E','').replace('\u0027',"").replace('\u0026#8212\u003B',' ').replace('\u002D',' ')
            ETitleList.append(etitle)
        match=re.compile('"m3u8": "http://discidevflash-f.akamaihd.net/i/digmed/hdnet/(.+?)/(.+?)/(.+?)-(.+?).mp4').findall(link)
        for id1, id2, id3, quality in match:
                idlist1.append(id1)
                idlist2.append(id2)
                idlist3.append(id3)
                qualitylist.append(quality)
        i=0
        GA(mtitle,"Watching")
        for i in range(len(match)):
                match1=re.compile('3500k').findall(qualitylist[i])
                match2=re.compile('1500k').findall(qualitylist[i])
                if selfAddon.getSetting("bit-disc") == "0":
                    if (len(match1)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-3500k.mp4?seek=5'
                    elif (len(match1)==0) and (len(match2)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-1500k.mp4?seek=5'
                    else:
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-600k.mp4?seek=5'    
                elif selfAddon.getSetting("bit-disc") == "1":
                    if (len(match2)>0):
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-1500k.mp4?seek=5'
                    else:
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-600k.mp4?seek=5'
                else:
                            final= 'http://discidevflash-f.akamaihd.net/digmed/hdnet/'+idlist1[i]+'/'+idlist2[i]+'/'+idlist3[i]+'-600k.mp4?seek=5'
                match2=re.compile('1500k').findall(quality)
                listitem = xbmcgui.ListItem('',thumbnailImage=thumbList[i])
                tot = i + 1
                listitem.setInfo('video', {'Title':'[COLOR blue]'+ETitleList[i]+'[/COLOR]','Plot': plotList[i],'Genre': '[B]Clip '+str(tot)+'/'+str(len(match))+' on playlist[/B]        '+mtitle} )
                #ListItem.Tagline
                print "llll "+ ETitleList[i]
                playlist.add(final,listitem)
                i=i+1
      
        xbmc.Player().play(playlist)
        xbmc.sleep(1000)
        xbmc.Player().pause()
        if idlist3[0][0:7]==idlist3[1][0:7]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
        elif idlist3[0][6:13]==idlist3[1][6:13]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
        elif idlist3[1][6:13]==idlist3[2][6:13]:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],"+str(len(match))+" Clips loaded to playlist,10000)")
        else:
                xbmc.executebuiltin("XBMC.Notification([B]Attention![/B],Related clips loaded to playlist,10000)")
        addStop('','','','')

def LINKNG(mname,murl):
        GA(mname,"Watched")
        link=OPENURL(murl)
        match=re.compile('property=".+?" content="(.+?)" />\n    <meta property=".+?" content=".+?" />\n    <meta property=".+?" content=".+?" />\n    <meta property=".+?" content=".+?" />\n\n\n    \n    <meta property=".+?" content=".+?" />\n\n    \n    <meta property=".+?" content="(.+?)" />\n\n    \n\n    <meta property=".+?" content="(.+?)" ').findall(link)
        for thumb, desc, vid in match:
                video=vid
        match2=re.compile('<source src="(.+?)" type="video/mp4" />').findall(link)
        for vidurl in match2:
                link2=OPENURL(vidurl)
                match3=re.compile('<video src="(.+?)1800.mp4"').findall(link2)
                for hd in match3:
                        hdlink=hd
                match8=re.compile('<video src="(.+?)1800(.+?).mp4"').findall(link2)
                for hd,hd1 in match8:
                        hdlink=hd
                        print hdlink
        match4=re.compile('shows').findall(murl)
        match5=re.compile('specials').findall(murl)
        match6=re.compile('extras').findall(murl)
        match7=re.compile('nat-geo-wild').findall(murl)
        if selfAddon.getSetting("bit-natgeo") == "0":
                try:
                        stream_url = hdlink + '1800.mp4'
                except:
                        stream_url = hdlink + '1800'+hd1+'.mp4'
        elif selfAddon.getSetting("bit-natgeo") == "1":
                if (len(match4)>0)or(len(match5)>0)or(len(match6)>0)or(len(match7)>0):
                        stream_url = hdlink + '660.mp4'
                else:
                        try:
                            stream_url = hdlink + '800.mp4'
                        except:
                            stream_url = hdlink + '800'+hd1+'.mp4'
        elif selfAddon.getSetting("bit-natgeo") == "2":
                if (len(match4)>0)or(len(match5)>0)or(len(match6)>0)or(len(match7)>0):
                        stream_url = hdlink + '220.mp4'
                else:
                        try:
                            stream_url = hdlink + '300.mp4'
                        except:
                            stream_url = hdlink + '300'+hd1+'.mp4'
        elif selfAddon.getSetting("bit-natgeo") == "3":
                try:
                        stream_url = video
                except:
                        stream_url = hdlink + '300.mp4'
        print stream_url
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        listitem = xbmcgui.ListItem(mname,thumbnailImage=thumb)
        listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addStop('','','','')
        
def LINKNG2(mname,murl):
        GA(mname,"Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        MainUrl='http://video.nationalgeographic.com'
        link=OPENURL(murl)
        descm=re.compile("caption : .+?3E([^<]+)\u003C.+?\u003E',").findall(link)
        for desc in descm:
            desc=desc.replace('3E','').replace('\u0027',"").replace('\u0026#8212\u003B',' ').replace('\u002D',' ')
        thumbm=re.compile('poster : "http://".+?"([^<]+)",').findall(link)
        for thumb in thumbm:
            thumb=MainUrl+thumb
        vlink=re.compile("HTML5src:'(.+?)'").findall(link)
        for vidlink in vlink:
            flink=MainUrl+vidlink
            link2=OPENURL(flink)
            match=re.compile('http://(.+?)\n').findall(link2)
            for vlink2 in match:
                vlink2='http://'+vlink2
            if (len(match)==0):
                xbmc.executebuiltin("XBMC.Notification([B]Sorry![/B],No video link available,3000)")
            else:
                bitmatch1=re.compile('1800').findall(vlink2)
                if (len(bitmatch1)>0):
                    stream_url = vlink2
                else:
                    stream_url = vlink2
                bitmatch2=re.compile('660').findall(vlink2)
                if (len(bitmatch1)==0)and(len(bitmatch2)>0):
                    stream_url = vlink2
                else:
                    stream_url = vlink2
            
                listitem = xbmcgui.ListItem(mname,thumbnailImage=thumb)
                listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
                playlist.add(stream_url,listitem)
                xbmcPlayer = xbmc.Player()
                xbmcPlayer.play(playlist)
            addStop('','','','')

def LINKWB(mname,murl):
        GA("WB","Watched")
        url='http://metaframe.digitalsmiths.tv/v2/WBtv/assets/'+murl+'/partner/11?format=json'
        link=OPENURL(url)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        bit700=re.compile('"bitrate": "700", "uri": "(.+?)"').findall(link)
        bit500=re.compile('"bitrate": "500", "uri": "(.+?)"').findall(link)
        if (len(bit700)>0):
                stream_url=bit700[0]
        else:
                stream_url=bit500[0]
        desc=re.compile('"description": "(.+?)", "rating"').findall(link)
        desc=desc[0].replace('\\','')
        thumb=re.compile('"images": .+?".+?": .+?"width": .+?, "uri": "(.+?)"').findall(link)
        listitem = xbmcgui.ListItem(mname,thumbnailImage=thumb[0])
        listitem.setInfo("Video", infoLabels={ "Title": mname, "Plot": desc})
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addStop('','','','')

def LINKDOC(mname,murl):
    match=re.compile('documentaryheaven').findall(murl)
    if (len(match)>0):
        GA("DocumentaryHeaven","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=OPENURL(murl)
        match=re.compile('<div id="command"><a class="lightSwitcher" href="#">.+?</a></div>                      \n                     <div class=\'video\'><iframe.+?src="(.+?)"').findall(link)
        for url in match:
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
        if (len(match)==0):
            match=re.compile('<iframe\r\nwidth=".+?" height=".+?" src="(.+?)"').findall(link)
            print match[0]
            link2=OPENURL(match[0])
            match2=re.compile('href="/watch.?v=(.+?)"').findall(link2)
            url='http://www.youtube.com/watch?v='+match2[0]
        
        print "vlink " +url
        media = urlresolver.HostedMediaFile(str(url))
        source = media
        listitem = xbmcgui.ListItem(mname)
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False  
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addDir('','','','')

    match2=re.compile('topdocumentaryfilms').findall(murl)
    if (len(match2)>0):
        sources=[]
        GA("TopDocumentaryFilms","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=OPENURL(murl)
        link=link.replace('src="http://cdn.tdfimg.com/wp-content/uploads','')
        match=re.compile('src="(.+?)"').findall(link)
        for url in match:
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
            match7=re.compile('google').findall(url)
            if (len(match7)>0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,link down,3000)")
                return
            match6=re.compile('youtube').findall(url)
            if (len(match6)>0):
                match=re.compile('http://www.youtube.com/embed/n_(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                if (len(match)>0):
                    url='http://www.youtube.com/watch?feature=player_embedded&v=n_'+match[0]
                else:
                    match=re.compile('http://www.youtube.com/embed/(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                    if (len(match)>0):
                        url='http://www.youtube.com/watch?feature=player_embedded&v='+match[0]
                    match2=re.compile('videoseries').findall(url)
                    if (len(match2)>0):
                        link2=OPENURL(url)
                        match2=re.compile('href="/watch.?v=(.+?)"').findall(link2)
                        match3=re.compile("http://www.youtube.com/embed/videoseries.?list=(.+?)&amp;iv_load_policy=3").findall(url)
                        print match3
                        url='http://www.youtube.com/watch?v='+match2[0]
                               
                    else:
                        url=url.replace('?rel=0','')
        """hosted_media = urlresolver.HostedMediaFile(url=url, title=host+' [COLOR red]'+lang+'[/COLOR]')
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)"""
        
        print "vlink " +str(url)
        media = urlresolver.HostedMediaFile(str(url))
        source = media
        listitem = xbmcgui.ListItem(mname)
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False
        
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addDir('','','','')

    match3=re.compile('documentary-log.com').findall(murl)
    if (len(match3)>0):        

        GA("Documentary-Log","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=OPENURL(murl)
        link=link.replace('src="http://cdn.tdfimg.com/wp-content/uploads','')
        match=re.compile('src="(.+?)" .+?></iframe>').findall(link)
        if (len(match)==0):
            link=link.replace('src="http://www.documentary-log.com/wp-cont','')
            match=re.compile('src="(.+?)" .+?/>').findall(link)
        for url in match:
            match4=re.compile('vimeo').findall(url)
            if (len(match4)>0):
                url=url.replace('?title=0&amp;byline=0&amp;portrait=0','')
                url=url.replace('http://player.vimeo.com/video','http://vimeo.com')
            match5=re.compile('dailymotion').findall(url)
            if (len(match5)>0):
                url=url.replace('http://www.dailymotion.com/embed/video','http://www.dailymotion.com/video')
            match7=re.compile('google').findall(url)
            if (len(match7)>0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,link down,3000)")
                return
            match6=re.compile('youtube').findall(url)
            if (len(match6)>0):
                match=re.compile('http://www.youtube.com/embed/n_(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                if (len(match)>0):
                    url='http://www.youtube.com/watch?feature=player_embedded&v=n_'+match[0]
                else:
                    match=re.compile('http://www.youtube.com/embed/(.+?).?rel=0&amp;iv_load_policy=3').findall(url)
                    if (len(match)>0):
                        url='http://www.youtube.com/watch?feature=player_embedded&v='+match[0]
                    match2=re.compile('videoseries').findall(url)
                    if (len(match2)>0):
                        link2=OPENURL(url)
                        match2=re.compile('href="/watch.?v=(.+?)"').findall(link2)
                        match3=re.compile("http://www.youtube.com/embed/videoseries.?list=(.+?)&amp;iv_load_policy=3").findall(url)
                        print match3
                        url='http://www.youtube.com/watch?v='+match2[0]
                               
                    else:
                        url=url.replace('?rel=0','')
        
        print "vlink " +str(url)
        media = urlresolver.HostedMediaFile(str(url))
        source = media
        listitem = xbmcgui.ListItem(mname)
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False
        
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        addDir('','','','')

        
def LOAD_AND_PLAY_VIDEO(url,name):
        GA("Dramacrazy","Watched")
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
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(videoUrl)
        
        return ok
                      
def PLAY(name,url):
        GA("Movie25-Oneclickwatch","Watched")
        name=name.replace('[DVD]','').replace('[TS]','').replace('[TC]','').replace('[CAM]','').replace('[SCREENER]','').replace('[COLOR blue]','').replace('[COLOR red]','').replace('[/COLOR]','')
        name=name.replace(' : Putlocker','').replace(' : 180upload','').replace(' : Filenuke','').replace(' : Flashx','').replace(' : Novamov','').replace(' : Uploadc','').replace(' : Xvidstage','').replace(' : Zooupload','').replace(' : Zalaa','').replace(' : Vidxden','').replace(' : Vidbux','')
        name=name.replace(' 720p BRRip','').replace(' 720p HDRip','').replace(' 720p WEBRip','').replace(' 720p BluRay','')
        namelen=len(name)
        if name[-2:namelen-1] == ')':
                nam= namelen- 6
                year = name[nam:namelen-2]
                name= name[0:namelen-7]
        else:
                nam= namelen- 5
                year = name[nam:namelen-1]
                name= name[0:namelen-6]
        infoLabels = GETMETAB(name,'',year,'')
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png",thumbnailImage=infoLabels['cover_url'])
        listitem.setInfo("Video", infoLabels = infoLabels)
        listitem.setProperty('mimetype', 'video/x-msvideo')
        listitem.setProperty('IsPlayable', 'true')
        media = urlresolver.HostedMediaFile(url)
        source = media
        if source:
                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                stream_url = source.resolve()
                if source.resolve()==False:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                        return
        else:
              stream_url = False  
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        
        addDir('','','','')
      
def VIDEOLINKST(mname,url):
        GA("iWatchonline","Watched")
        Mainurl ='http://www.iwatchonline.org'
        url=Mainurl+url
        sources = []
        match=re.compile('http://www.iwatchonline.org/episode/(.+?)-.+?').findall(url)
        for movieid in match:
                url=url + '?tmpl=component&option=com_jacomment&view=comments%20&contentoption=com_content&contentid='+ movieid
        link=OPENURL(url)
        match=re.compile('<a href="(.+?)" target="_BLANK" class="vidLinks">(.+?)</a>').findall(link)
        for url, name in match:
                hosted_media = urlresolver.HostedMediaFile(url=url, title=name)
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                        stream_url = False
                        return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )         
                xbmc.Player().play(stream_url, listitem)
                
                addDir('','','','')
            
def VIDEOLINKST2(mname,url):
        sources = []
        GA("Movie1k","Watched")
        link=OPENURL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a><br />').findall(link)
        if (len(match)>0):
                for url, host in match:
                        print "mam "+url
                        hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                        sources.append(hosted_media)
                if (len(sources)==0):
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
                else:
                        source = urlresolver.choose_source(sources)
                        if source:
                                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                                stream_url = source.resolve()
                                if source.resolve()==False:
                                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                        return
                        else:
                                stream_url = False
                                return
                        listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                        listitem.setInfo('video', {'Title': mname, 'Year': ''} )         
                        xbmc.Player().play(stream_url, listitem)
                        
                        addDir('','','','')
        elif(len(match)==0):
                match=re.compile(': (.+?)</strong></p>\n<p><a href=".+?watch.php.?idl=(.+?)"').findall(link)        
                for host, url in match:

                        hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                        sources.append(hosted_media)
                if (len(sources)==0):
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
                else:
                        source = urlresolver.choose_source(sources)
                        if source:
                                xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                                stream_url = source.resolve()
                                if source.resolve()==False:
                                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                        return
                        else:
                                stream_url = False
                                return
                        listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                        listitem.setInfo('video', {'Title': mname, 'Year': ''} )
                        xbmc.Player().play(stream_url, listitem)
                        addDir('','','','')


def LINKTV4(mname,url):
        sources = []
        GA("RlsmixTV","Watched")
        link=OPENURL(url)
        link= link.replace('TV Rage','').replace('Homepage','').replace('href="http://www.tvrage.com','').replace('href="http://www.cbs.com','').replace('Torrent Search','').replace('Season Download','').replace('href="http://uppix.net','').replace('href="http://www.torrentz.com','').replace('href="http://directdownload.tv','')
        match=re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(link)
        for url, host in match:
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Resolving Link,3000)")
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                        stream_url = False
                        return
                listitem = xbmcgui.ListItem(mname, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': mname, 'Year': ''} )         
                xbmc.Player().play(stream_url, listitem)
                        
                addDir('','','','')





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
                        addLink ('[B]PLAY VIDEO[/B]',videoUrl,imgUrl)
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
                        addLink ('[B]PLAY VIDEO[/B]',videoUrl,imgUrl)
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
                        addLink ('[B]PLAY VIDEO[/B]',videoUrl,'')

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
                        addLink ('[B]PLAY VIDEO[/B]',videoUrl,'')
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
                        addLink ('[B]PLAY VIDEO[/B]: '+name,videoUrl,imgUrl)
                
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
                
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
                
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
                
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
                                addLink ('PLAY Standard Quality ',dm_low[0],imgSrc[0])
                        if(len(dm_high) > 0):
                                addLink ('PLAY High Quality ',dm_high[0],imgSrc[0])
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
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
                        addLink ('[B]PLAY VIDEO[/B]: '+videoTitle,videoUrl,imgUrl)
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
                        addLink ('PLAY High Quality Video',link,'')
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
                                addLink ('[B]PLAY VIDEO[/B]',videoUrl,"")
        except: pass


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
            VISITOR = selfAddon.getSetting('visitor_ga')
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
            if xbmc.getCondVisibility('system.platform.osx'):
                if xbmc.getCondVisibility('system.platform.atv2'):
                    log_path = '/var/mobile/Library/Preferences'
                else:
                    log_path = os.path.join(os.path.expanduser('~'), 'Library/Logs')
            elif xbmc.getCondVisibility('system.platform.ios'):
                log_path = '/var/mobile/Library/Preferences'
            elif xbmc.getCondVisibility('system.platform.windows'):
                log_path = xbmc.translatePath('special://home')
                log = os.path.join(log_path, 'xbmc.log')
                logfile = open(log, 'r').read()
            elif xbmc.getCondVisibility('system.platform.linux'):
                log_path = xbmc.translatePath('special://home/temp')
            else:
                log_path = xbmc.translatePath('special://logpath')
            log = os.path.join(log_path, 'xbmc.log')
            logfile = open(log, 'r').read()
        except:
            logfile='Starting XBMC (Unknown Git:.+?Platform: Unknown. Built.+?'
        print '==========================   '+PATH+' '+VERSION+'   =========================='
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
        VISITOR = selfAddon.getSetting('visitor_ga')
        match=re.compile('Starting XBMC \((.+?) Git:.+?Platform: (.+?)\. Built.+?').findall(logfile)
        for build, PLATFORM in match:
            if re.search('12.0',build,re.IGNORECASE): 
                build="Frodo" 
            if re.search('11.0',build,re.IGNORECASE): 
                build="Eden" 
            if re.search('13.0',build,re.IGNORECASE): 
                build="Gotham" 
            print build
            print PLATFORM
            utm_gif_location = "http://www.google-analytics.com/__utm.gif"
            utm_track = utm_gif_location + "?" + \
                    "utmwv=" + VERSION + \
                    "&utmn=" + str(randint(0, 0x7fffffff)) + \
                    "&utmt=" + "event" + \
                    "&utme="+ quote("5(APP LAUNCH*"+build+"*"+PLATFORM+")")+\
                    "&utmp=" + quote(PATH) + \
                    "&utmac=" + UATRACK + \
                    "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR,VISITOR,"2"])
            try:
                print "============================ POSTING APP LAUNCH TRACK EVENT ============================"
                send_request_to_google_analytics(utm_track)
            except:
                print "============================  CANNOT POST APP LAUNCH TRACK EVENT ============================" 
checkGA()




"""def MESSAGE():
        class MessClass(xbmcgui.Window):
            def __init__(self):
                xbmc.Player().play("%s/resources/message/music.mp3"%selfAddon.getAddonInfo("path"), xbmcgui.ListItem('Message'))
                self.addControl(xbmcgui.ControlImage(0,0,1280,720,"%s/resources/message/messg.png"%selfAddon.getAddonInfo("path")))
            def onAction(self, action):
                if action == 92 or action == 10:
                        xbmc.Player().stop()
                        self.close()

        mess = MessClass()
        mess.doModal()
        del mess"""

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
        liz=xbmcgui.ListItem(name, iconImage="%s/art/link.png"%selfAddon.getAddonInfo("path"), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addStop(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    
def addDir2(name,url,mode,iconimage,desc):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addSport(name,url,mode,iconimage,desc,dur,gen):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc, "Duration": dur ,"Genre": gen} )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addDirb(name,url,mode,iconimage,fan):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fan)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addInfo(name,url,mode,iconimage,gen,year):
        ok=True
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        name=name.replace('()','')
        infoLabels = GETMETA(name,gen,year,iconimage)
        if selfAddon.getSetting("meta-view") == "true":
                tmdbid=infoLabels['tmdb_id']
        args=[(url,name)]
        script1="%s/resources/addFavs.py"%selfAddon.getAddonInfo('path')
        script2="%s/resources/delFavs.py"%selfAddon.getAddonInfo('path')
        script3="%s/resources/Trailers.py"%selfAddon.getAddonInfo('path')
        Commands=[("[B][COLOR blue]Add[/COLOR][/B] to My Fav's","XBMC.RunScript(" + script1 + ", " + str(args) + ")"),
              ("[B][COLOR red]Remove[/COLOR][/B] from My Fav's","XBMC.RunScript(" + script2 + ", " + str(args) + ")")]
        if selfAddon.getSetting("meta-view") == "true":
                Commands.append(("Play Trailer","XBMC.RunScript(" + script3 + ", " + str(tmdbid) + ")"))
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=infoLabels['cover_url'])
        liz.addContextMenuItems( Commands )
        liz.setInfo( type="Video", infoLabels = infoLabels)
        liz.setProperty('fanart_image', infoLabels['backdrop_url'])
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addInfo2(name,url,mode,iconimage,plot):
        ok=True
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        infoLabels = GETMETAShow(name)
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=infoLabels['cover_url'])
        liz.setInfo( type="Video", infoLabels=infoLabels)
        liz.setProperty('fanart_image', infoLabels['backdrop_url'])
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    
def addEpi(name,url,mode,iconimage,data):
        ok=True
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        infoLabels = GETMETAEpi(name,data)
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=infoLabels['cover_url'])
        liz.setInfo( type="Video", infoLabels=infoLabels)
        liz.setProperty('fanart_image', infoLabels['backdrop_url'])
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addPlayableLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        # adding context menus
        #new name LOAD BEFORE DOWNLOAD AJ
        loadName = name + 'AJLBDAJ'
        contextMenuItems = []
        contextMenuItems.append(('Download', 'XBMC.RunPlugin(%s?mode=13&name=%s&url=%s)' % (sys.argv[0], urllib.quote_plus(loadName), urllib.quote_plus(url))))
        contextMenuItems.append(('Download and Play', 'XBMC.RunPlugin(%s?mode=15&name=%s&url=%s)' % (sys.argv[0], urllib.quote_plus(loadName), urllib.quote_plus(url))))
        contextMenuItems.append(('Download Quietly', 'XBMC.RunPlugin(%s?mode=14&name=%s&url=%s)' % (sys.argv[0], urllib.quote_plus(loadName), urllib.quote_plus(url))))
        
        liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addPlayListLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="%s/art/vidicon.png"%selfAddon.getAddonInfo("path"), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
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
        LISTMOVIES(url)
        
elif mode==2:
        print ""+url
        GENRE(url)

elif mode==4:
        print ""+url
        SEARCH(url)
        
elif mode==420:
        print ""+url
        Searchhistory()

elif mode==3:
        print ""+url
        VIDEOLINKS(name,url)

elif mode==5:
        print ""+url
        PLAY(name,url)

elif mode==6:
        AtoZ()

elif mode==7:
        YEAR()

elif mode==23:
        ENTYEAR()
        
elif mode==8:
        print ""+url
        YEARB(url)

elif mode==9:
        print ""+url
        NEXTPAGE(url)
        
elif mode==10:
        FAVS()

elif mode==11:
        print ""+url
        PUTLINKS(name,url)

elif mode==12:
        print ""+url
        OELINKS(name,url)

elif mode==13:
        print ""+url
        FNLINKS(name,url)

elif mode==14:
        print ""+url
        VIDLINKS(name,url)

elif mode==15:
        print ""+url
        FLALINKS(name,url)

elif mode==16:
        print ""+url
        NOVLINKS(name,url)

elif mode==17:
        print ""+url
        UPLINKS(name,url)

elif mode==18:
        print ""+url
        XVLINKS(name,url)

elif mode==19:
        print ""+url
        ZOOLINKS(name,url)

elif mode==20:
        print ""+url
        ZALINKS(name,url)

elif mode==21:
        print ""+url
        VIDXLINKS(name,url)

elif mode==25:
        print ""+url
        LISTSP(url)

elif mode==26:
        print ""+url
        LINKSP(name,url)
        
elif mode==27:
        print ""+url
        TV()

elif mode==28:
        print ""+url
        LISTTV(url)
        
elif mode==29:
        print ""+url
        VIDEOLINKST(name,url)

elif mode==30:
        print ""+url
        LISTTV2(url)

elif mode==31:
        print ""+url
        VIDEOLINKST2(name,url)
        
elif mode==32:
        print ""+url
        LISTTV3(url)

elif mode==33:
        print ""+url
        HD()

elif mode==34:
        print ""+url
        LISTSP2(url)

elif mode==35:
        print ""+url
        LINKSP2(name,url)

elif mode==36:
        print ""+url
        INT()

elif mode==37:
        print ""+url
        LISTINT(name,url)

elif mode==38:
        print ""+url
        LINKINT(name,url)

elif mode==39:
        print ""+url
        LISTINT2(name,url)

elif mode==40:
        print ""+url
        LINKINT2(name,url)

elif mode==42:
        print ""+url
        LOAD_AND_PLAY_VIDEO(url,name)
        
elif mode==43:
        print ""+url
        SPORTS()

elif mode==44:
        print ""+url
        ESPN()
        
elif mode==45:
        print ""+url
        ESPNList(url)

elif mode==46:
        print ""+url
        ESPNLink(name,url)

elif mode==47:
        print ""+url
        YOUList(name,url)
        
elif mode==48:
        print ""+url
        YOULink(name,url)

elif mode==50:
        print ""+url
        OC()
        
elif mode==51:
        print ""+url
        OCList(url)

elif mode==52:
        print ""+url
        OCLink(name,url)

elif mode==53:
        print ""+url
        LISTSP3(url)

elif mode==54:
        print ""+url
        LINKSP3(name,url)

elif mode==55:
        print ""+url
        LISTSP4(url)

elif mode==56:
        print ""+url
        LINKSP4(name,url)

elif mode==57:
        print ""+url
        LISTSP5(url)

elif mode==58:
        print ""+url
        LINKSP5(name,url)
        
elif mode==59:
        print ""+url
        UFC()
        
elif mode==60:
        print ""+url
        UFCMOVIE25()

elif mode==61:
        print ""+url
        LISTTV4(url)

elif mode==62:
        print ""+url
        LINKTV4(name,url)

elif mode==63:
        print ""+url
        ADVENTURE()
        
elif mode==631:
        print ""+url
        DISC()

elif mode==64:
        print ""+url
        LISTDISC(name,url)

elif mode==65:
        print ""+url
        LINKDISC(name,url)

elif mode==66:
        print ""+url
        LISTINT3(url)

elif mode==67:
        print ""+url
        LINKINT3(name,url)

elif mode==68:
        print ""+url
        LISTINT4(url)

elif mode==69:
        print ""+url
        LINKINT4(name,url)

elif mode==70:
        print ""+url
        NG()

elif mode==71:
        print ""+url
        NGDir(url)

elif mode==72:
        print ""+url
        LISTNG(url)

elif mode==73:
        print ""+url
        LISTNG2(url)

elif mode==74:
        print ""+url
        LINKNG(name,url)

elif mode==75:
        print ""+url
        LINKNG2(name,url)

elif mode==76:
        print ""+url
        KIDZone(url)
        
elif mode==77:
        print ""+url
        WB()
        
elif mode==78:
        print ""+url
        LISTWB(url)

elif mode==79:
        print ""+url
        LINKWB(name,url)

elif mode==80:
        print ""+url
        MILIT()
        
elif mode==81:
        print ""+url
        SCI()

elif mode==82:
        print ""+url
        VELO()

elif mode==83:
        print ""+url
        ANIP()

elif mode==84:
        print ""+url
        YOUKIDS()

elif mode==85:
        print ""+url
        DOCS()        

elif mode==86:
        print ""+url
        LISTDOC(url)
        
elif mode==87:
        print ""+url
        LISTDOC2(url)

elif mode==88:
        print ""+url
        LINKDOC(name,url)
        
elif mode==89:
        print ""+url
        LISTDOCPOP(url)



        
elif mode==99:
        urlresolver.display_settings()
        
elif mode==100:
        pop()
        
elif mode==101:
        SEARCHNEW(url)

elif mode==102:
        SearchhistoryNEW(url)
        
elif mode==103:
        UFCNEW()
        
elif mode==104:
        Vice(url)
        
elif mode==105:
        ViceList(url)

elif mode==106:        
        ViceLink(name,url)        
        
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

elif mode==601:
        MAINSG()
        
elif mode==602:
        print ""+url
        LISTEpiSG(url)

elif mode==603:
        print ""+url
        LISTShowsSG(url)

elif mode==604:
        print ""+url
        LISTSeasonSG(name,url)

elif mode==605:
        print ""+url
        LISTEpilistSG(name,url)

elif mode==606:
        print ""+url
        LISTPopSG(url)

elif mode==607:
        print ""+url
        GENRESG(url)

elif mode==608:
        print ""+url
        SEARCHSG(url)
        
elif mode==612:
        print ""+url
        SearchhistorySG()

elif mode==609:
        print ""+url
        VIDEOLINKSSG(name,url)

     
        
elif mode==610:
        print ""+url
        AtoZSG()
        
elif mode==611:
        print ""+url
        AllShows(url)

        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
