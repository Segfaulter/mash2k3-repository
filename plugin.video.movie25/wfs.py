import urllib,urllib2,re, string,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urlresolver
from t0mm0.common.addon import Addon
from metahandler import metahandlers


#WatchFreeSeries - by Mash2k3 2012.
prepare_zip = False
Mainurl ='http://watch-freeseries.mu/'
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)
grab=metahandlers.MetaData(preparezip=prepare_zip)
addon = Addon('plugin.video.watchfreeseries', sys.argv)
datapath = xbmc.translatePath(selfAddon.getAddonInfo('profile'))

def MAIN():
        addDir('Search','http://watch-freeseries.mu/',4,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
        addDir('A-Z','http://watch-freeseries.mu/tvseries',10,"%s/art/az.png"%selfAddon.getAddonInfo("path"))
        addDir('This Week Episodes','http://watch-freeseries.mu/this-week-episodes/',1,"%s/art/latest.png"%selfAddon.getAddonInfo("path"))
        addDir('Popular TV Series','http://watch-freeseries.mu/',11,"%s/art/popu.png"%selfAddon.getAddonInfo("path"))
        addDir('TV Series','http://watch-freeseries.mu/tvseries',6,"%s/art/series.png"%selfAddon.getAddonInfo("path"))
        addDir('Year','http://watch-freeseries.mu/',5,"%s/art/year.png"%selfAddon.getAddonInfo("path"))
        addDir('Genre','http://watch-freeseries.mu/',2,"%s/art/genre.png"%selfAddon.getAddonInfo("path"))
        addDir('Download All Meta','http://watch-freeseries.mu/',27,"%s/art/metaall.png"%selfAddon.getAddonInfo("path"))
        GA("None","None")
        VIEWSB()
    

def GetMetAll():
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('Download All Meta.', 'Download all meta information for videos at once.','Its better to get it out the way.', 'Would you like to download it? It takes around 20 minutes.','No', 'Yes')
        if ret==True:
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
                                GETMETA(name,'')
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='Parts loaded:: [B]'+str(loadedparts)+' / '+str(parts)+'[/B].''       TV Shows loaded:: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                                dialogWait.update(percent,'Process loads in 27 parts Numbers, A thru Z',remaining_display)
                                if (dialogWait.iscanceled()):
                                        return False
                        loadedparts = loadedparts + 1
                xbmc.executebuiltin("XBMC.Notification(Nice!,Metacontainer DB Installation Success,5000)")

        MAIN()
def AtoZ():
        addDir('0-9','http://watch-freeseries.mu/index.php?action=episodes_searchShow&letter=1',6,"%s/art/09.png"%selfAddon.getAddonInfo("path"))
        for i in string.ascii_uppercase:
                addDir(i,'http://watch-freeseries.mu/index.php?action=episodes_searchShow&letter='+i,6,"%s/art/%s.png"%(selfAddon.getAddonInfo("path"),i))
        GA("None","A-Z")
        VIEWSB()        
def GENRE(url):
        addDir('Action','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=2',6,"%s/art/act.png"%selfAddon.getAddonInfo("path"))
        addDir('Adventure','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=5',6,"%s/art/adv.png"%selfAddon.getAddonInfo("path"))
        addDir('Animation','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=6',6,"%s/art/ani.png"%selfAddon.getAddonInfo("path"))
        addDir('Awards','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=32',6,"%s/art/awa.png"%selfAddon.getAddonInfo("path"))
        addDir('Biography','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=8',6,"%s/art/bio.png"%selfAddon.getAddonInfo("path"))
        addDir('Cartoons','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=30',6,"%s/art/car.png"%selfAddon.getAddonInfo("path"))
        addDir('Comedy','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=9',6,"%s/art/com.png"%selfAddon.getAddonInfo("path"))
        addDir('Cooking','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=38',6,"%s/art/coo.png"%selfAddon.getAddonInfo("path"))
        addDir('Crime','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=10',6,"%s/art/cri.png"%selfAddon.getAddonInfo("path"))
        addDir('Documentary','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=11',6,"%s/art/doc.png"%selfAddon.getAddonInfo("path"))
        addDir('Drama','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=3',6,"%s/art/dra.png"%selfAddon.getAddonInfo("path"))
        addDir('Family','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=12',6,"%s/art/fam.png"%selfAddon.getAddonInfo("path"))
        addDir('Fantasy','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=1',6,"%s/art/fan.png"%selfAddon.getAddonInfo("path"))
        addDir('Fashion','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=35',6,"%s/art/fas.png"%selfAddon.getAddonInfo("path"))
        addDir('Food','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=31',6,"%s/art/foo.png"%selfAddon.getAddonInfo("path"))
        addDir('Game Show','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=33',6,"%s/art/gam.png"%selfAddon.getAddonInfo("path"))
        addDir('History','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=14',6,"%s/art/his.png"%selfAddon.getAddonInfo("path"))
        addDir('Horror','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=4',6,"%s/art/hor.png"%selfAddon.getAddonInfo("path"))
        addDir('Late Night','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=37',6,"%s/art/lat.png"%selfAddon.getAddonInfo("path"))
        addDir('Motorsports','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=29',6,"%s/art/mot.png"%selfAddon.getAddonInfo("path"))
        addDir('Music','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=17',6,"%s/art/mus.png"%selfAddon.getAddonInfo("path"))
        addDir('Musical','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=18',6,"%s/art/musi.png"%selfAddon.getAddonInfo("path"))
        addDir('Mystery','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=16',6,"%s/art/mys.png"%selfAddon.getAddonInfo("path"))
        addDir('Reality Tv','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=19',6,"%s/art/rea.png"%selfAddon.getAddonInfo("path"))
        addDir('Romance','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=20',6,"%s/art/rom.png"%selfAddon.getAddonInfo("path"))
        addDir('Sci-Fi','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=21',6,"%s/art/sci.png"%selfAddon.getAddonInfo("path"))
        addDir('Short','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=22',6,"%s/art/sho.png"%selfAddon.getAddonInfo("path"))
        addDir('Sport','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=23',6,"%s/art/spo.png"%selfAddon.getAddonInfo("path"))
        addDir('Talk','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=27',6,"%s/art/tal.png"%selfAddon.getAddonInfo("path"))
        addDir('Talk Show','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=39',6,"%s/art/tals.png"%selfAddon.getAddonInfo("path"))
        addDir('Teen','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=34',6,"%s/art/tee.png"%selfAddon.getAddonInfo("path"))
        addDir('Thriller','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=24',6,"%s/art/thr.png"%selfAddon.getAddonInfo("path"))
        addDir('War','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=25',6,"%s/art/war.png"%selfAddon.getAddonInfo("path"))
        addDir('Western','http://watch-freeseries.mu/index.php?action=episodes_searchShow&genre=26',6,"%s/art/wes.png"%selfAddon.getAddonInfo("path"))
        GA("None","Genre")
        VIEWSB()
def YEAR():
        addDir('2013','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2013',6,"%s/art/2013.png"%selfAddon.getAddonInfo("path"))
        addDir('2012','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2012',6,"%s/art/2012.png"%selfAddon.getAddonInfo("path"))
        addDir('2011','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2011',6,"%s/art/2011.png"%selfAddon.getAddonInfo("path"))
        addDir('2010','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2010',6,"%s/art/2010.png"%selfAddon.getAddonInfo("path"))
        addDir('2009','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2009',6,"%s/art/2009.png"%selfAddon.getAddonInfo("path"))
        addDir('2008','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2008',6,"%s/art/2008.png"%selfAddon.getAddonInfo("path"))
        addDir('2007','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2007',6,"%s/art/2007.png"%selfAddon.getAddonInfo("path"))
        addDir('2006','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2006',6,"%s/art/2006.png"%selfAddon.getAddonInfo("path"))
        addDir('2005','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2005',6,"%s/art/2005.png"%selfAddon.getAddonInfo("path"))
        addDir('2004','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2004',6,"%s/art/2004.png"%selfAddon.getAddonInfo("path"))
        addDir('2003','http://watch-freeseries.mu/index.php?action=episodes_searchShow&year=2003',6,"%s/art/2003.png"%selfAddon.getAddonInfo("path"))
        GA("None","Year")
        VIEWSB()






def GETMETA(mname,thumb): 
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
                        infoLabels['cover_url']=thumb
        else:
                infoLabels = {'title': mname,'cover_url': thumb,'backdrop_url': ''}
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
                addDir(name+'   "'+epname+'"',url,3,thumb)
        GA("None","LatestEPI-list")
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
                addInfo(name,url,7,'','')
        GA("None","Shows-list")
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
                addInfo(name,url,7,'','')
        GA("None","MostPOP-list")
        xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
        
                
def LISTSeason(mname,murl):
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
                addDir(name,murl+'xoxc'+mname+'xoxc'+num+'xoxc',8,str(thumb))
        xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
        if selfAddon.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting('seasons-view'))          

def LISTEpilist(name,murl):
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
                addEpi(name,url,3,'',data)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
        if selfAddon.getSetting('auto-view') == 'true':
                xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting('episodes-view'))        
        
def SEARCH():
        keyb = xbmc.Keyboard('', 'Search For Shows or Episodes')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
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
                            addDir(name,url,3,'')
                        else:
                            addInfo(name,url,7,'','')
        GA("None","Search")

        
def OPENURL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
    
def GETLINK(url):
        link=OPENURL(url)
        match=re.compile('<br>\n        <a href="(.+?)" title="" class=".+?"').findall(link)
        for url in match:
                return url   

def VIDEOLINKS(name,url):
        GA("WSF","Watched")
        sources = []
        link=OPENURL(url)
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Collecting hosts,3000)")
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">putlocker.com</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='Putlocker'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">sockshare.com</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='Sockshare'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">flashx.tv</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='Flashx'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">180upload.com</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='180upload'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">nowvideo.eu</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='Nowvideo'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">filenuke.com</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='Filenuke'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">videoweed.es</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='Videoweed'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">novamov.com</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='Novamov'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        """match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">vidbux.com</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host='Vidbux'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)
        match=re.compile('<td width=".+?"><p><a href="(.+?)" target="_blank">vidxden.com</a></p></td>').findall(link)
        for url in match:
                url=GETLINK(url)
                host= 'Vidxden'
                hosted_media = urlresolver.HostedMediaFile(url=url, title=host)
                sources.append(hosted_media)"""
                
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


def VIEWSB():
        if selfAddon.getSetting("auto-view") == "true":
                        if selfAddon.getSetting("home-view") == "0":
                                xbmc.executebuiltin("Container.SetViewMode(50)")
                        elif selfAddon.getSetting("home-view") == "1":
                                xbmc.executebuiltin("Container.SetViewMode(500)")

                        return


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
        VISITOR = os.path.join(datapath, 'visitorid')
        if os.path.exists("%s/visitorid"%selfAddon.getAddonInfo('path'))==True:
            VISITOR = open("%s/visitorid"%selfAddon.getAddonInfo('path')).read()
        if os.path.exists("%s/visitorid"%selfAddon.getAddonInfo('path'))==False:
            from random import randint
            txtfile = open("%s/visitorid"%selfAddon.getAddonInfo('path'),'w') 
            txtfile.write(str(randint(0, 0x7fffffff)))
            txtfile.close()
            VISITOR = open("%s/visitorid"%selfAddon.getAddonInfo('path')).read()
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
            VERSION = "4.2.8"
            UATRACK = "UA-38312513-2"
            PROPERTY_ID = environ.get("GA_PROPERTY_ID", "UA-38312513-2")
            PATH = "XBMC-WSF"            
            utm_gif_location = "http://www.google-analytics.com/__utm.gif"
            if name=="None":
                    utm_url = utm_gif_location + "?" + \
                            "utmwv=" + VERSION + \
                            "&utmn=" + str(randint(0, 0x7fffffff)) + \
                            "&utmp=" + quote(PATH) + \
                            "&utmac=" + PROPERTY_ID + \
                            "&utmcc=__utma=%s" % ".".join(["1", "1", VISITOR, "1", "1","2"])
            else:
                if group=="None":
                       utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmp=" + quote(PATH+"/"+name) + \
                                "&utmac=" + PROPERTY_ID + \
                                "&utmcc=__utma=%s" % ".".join(["1", "1", VISITOR, "1", "1","2"])
                else:
                       utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmp=" + quote(PATH+"/"+group+"/"+name) + \
                                "&utmac=" + PROPERTY_ID + \
                                "&utmcc=__utma=%s" % ".".join(["1", "1", VISITOR, "1", "1","2"])
            if not group=="None":
                    utm_track = utm_gif_location + "?" + \
                            "utmwv=" + VERSION + \
                            "&utmn=" + str(randint(0, 0x7fffffff)) + \
                            "&utmp=" + quote(PATH) + \
                            "&utmt=" + "events" + \
                            "&utme="+ quote("5("+PATH+"*"+group+"*"+name+")")+\
                            "&utmac=" + PROPERTY_ID + \
                            "&utmcc=__utma=%s" % ".".join(["1", "1", "1", VISITOR,"1","2"])

            print "Analitycs: %s" % utm_url
            send_request_to_google_analytics(utm_url)
            print "Analitycs: %s" % utm_track
            send_request_to_google_analytics(utm_track)
        except:
            print "================  CANNOT POST TO ANALYTICS  ================"

            
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

def addEpi(name,url,mode,iconimage,data):
        ok=True
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        infoLabels = GETMETAEpi(name,data)
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=infoLabels['cover_url'])
        liz.setInfo( type="Video", infoLabels=infoLabels)
        liz.setProperty('fanart_image', infoLabels['backdrop_url'])
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addInfo(name,url,mode,iconimage,plot):
        ok=True
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        infoLabels = GETMETA(name,iconimage)
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=infoLabels['cover_url'])
        liz.setInfo( type="Video", infoLabels=infoLabels)
        liz.setProperty('fanart_image', infoLabels['backdrop_url'])
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
        LISTEpi(url)

elif mode==6:
        print ""+url
        LISTShows(url)

elif mode==7:
        print ""+url
        LISTSeason(name,url)

elif mode==8:
        print ""+url
        LISTEpilist(name,url)

elif mode==11:
        print ""+url
        LISTPop(url)

elif mode==2:
        print ""+url
        GENRE(url)

elif mode==4:
        print ""+url
        SEARCH()

elif mode==3:
        print ""+url
        VIDEOLINKS(name,url)

elif mode==5:
        print ""+url
        YEAR()
        
        
elif mode==10:
        print ""+url
        AtoZ()
        
elif mode==27:
        print ""+url
        GetMetAll()



xbmcplugin.endOfDirectory(int(sys.argv[1]))
