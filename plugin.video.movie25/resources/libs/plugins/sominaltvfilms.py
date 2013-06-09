import urllib,urllib2,re,cookielib,string, urlparse,sys,os
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from t0mm0.common.net import Net as net
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def unescape(text):
        try:            
            rep = {"&nbsp;": " ",
                   "\n": "",
                   "\t": "",   
                   "%3a": ":",
                   "%3A":":",
                   "%2f":"/",
                   "%2F":"/",
                   "%3f":"?",
                   "%3F":"?",
                   "%26":"&",
                   "%3d":"=",
                   "%3D":"=",
                   "%2C":",",
                   "%2c":","
                   }
            for s, r in rep.items():
                text = text.replace(s, r)
				
            # remove html comments
            text = re.sub(r"<!--.+?-->", "", text)    
				
        except TypeError:
            pass

        return text

def MAIN():
        main.GA("Plugin","SominalTv")
        main.addDir('Search','http://www.movie25.com/',624,"%s/art/search.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Hindi','http://www.sominaltvfilms.com/search/label/Hindi%20Movies?&max-results=15',620,"%s/art/wfs/hindi.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Telugu','http://www.sominaltvfilms.com/search/label/Telugu?&max-results=15',620,"%s/art/wfs/telugu.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Tamil','http://www.sominaltvfilms.com/search/label/Tamil?&max-results=15',620,"%s/art/wfs/tamil.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Malayalam','http://www.sominaltvfilms.com/search/label/Malayalam?&max-results=15',620,"%s/art/wfs/malayalam.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Punjabi','http://www.sominaltvfilms.com/search/label/Punjabi?&max-results=15',620,"%s/art/wfs/punjabi.png"%selfAddon.getAddonInfo("path"))
        main.addDir('BluRay','http://www.sominaltvfilms.com/search/label/BluRay?&max-results=15',620,"%s/art/wfs/bluray.png"%selfAddon.getAddonInfo("path"))
        main.addDir('All English Subtitled Movies','http://www.sominaltvfilms.com/search/label/English%20Subtitled?&max-results=15',620,"%s/art/wfs/subtitled.png"%selfAddon.getAddonInfo("path"))
        main.addDir('All Hindi Dubbed Movies','http://www.sominaltvfilms.com/search/label/Hindi%20Dubbed?&max-results=15',620,"%s/art/wfs/dubbed.png"%selfAddon.getAddonInfo("path"))


def AtoZ(url):
    main.addDir('0-9','http://www.sominaltvfilms.com/search/label/%23'+url+'?&max-results=15',620,"%s/art/wfs/09.png"%selfAddon.getAddonInfo("path"))
    for i in string.ascii_uppercase:
            main.addDir(i,'http://www.sominaltvfilms.com/search/label/'+i+url+'?&max-results=15',620,"%s/art/wfs/%s.png"%(selfAddon.getAddonInfo("path"),i))
    main.GA("Watchseries","A-Z")
    main.VIEWSB()
    
def SEARCH():
        keyb = xbmc.Keyboard('', 'Search Movies')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                surl='http://www.sominaltvfilms.com/search?q='+encode+'&x=-452&y=-10'
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('<div class="separator" style=".+?"><a href="(.+?)".+?<img border=".+?src="(.+?)".+?<br.+?(.+?)</div><.+?</div>.+?createSummaryAndThumb.+?","(.+?)","(.+?)",".+?</script>').findall(link)
        for fan,thumb,desc,name,url in match:
            desc=desc.replace('</div><div class="separator" style="clear: both; text-align: left;">','').replace('<span class="Apple-style-span" style="background-color: white; color: #333333; font-family: Verdana, Arial, sans-serif; font-size: 13px; line-height: 18px;">','').replace('</div><div class="separator" style="clear: both; text-align: justify;">','').replace('</div><div class="separator" style="clear: both; text-align: center;">','').replace('</span>','').replace('<span>','').replace('</div><div class="separator" style="clear: both; text-align: justify;"><span class="Apple-style-span" style="background-color: white; color: #333333; font-family: Verdana, Arial, sans-serif; font-size: 13px; line-height: 18px;">','')
            desc=desc.replace('<br>','').replace('</br>','').replace('</div>','').replace('<div>','')
            main.addDirc(name,url,621,thumb,desc,fan)
               

def LIST(mname,murl):
        main.GA("SominalTv","List")
        if mname=='Hindi':
                main.addDir('A-Z','_H',623,"%s/art/wfs/azws.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Hindi English Subtitled','http://www.sominaltvfilms.com/search/label/Hindi-Movies-English-Subtitles?&max-results=15',620,"%s/art/wfs/subtitled.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Hindi BluRay','http://www.sominaltvfilms.com/search/label/Hindi-BluRays?&max-results=15',620,"%s/art/wfs/bluray.png"%selfAddon.getAddonInfo("path"))
        elif mname=='Telugu':
                main.addDir('A-Z','_T',623,"%s/art/wfs/azws.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Telugu English Subtitled','http://www.sominaltvfilms.com/search/label/Telugu-Movies-English-Subtitles?&max-results=15',620,"%s/art/wfs/subtitled.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Telugu BluRay','http://www.sominaltvfilms.com/search/label/Telugu-BluRays?&max-results=15',620,"%s/art/wfs/bluray.png"%selfAddon.getAddonInfo("path"))
        elif mname=='Tamil':
                main.addDir('A-Z','_TT',623,"%s/art/wfs/azws.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Tamil English Subtitled','http://www.sominaltvfilms.com/search/label/Tamil-Movies-English-Subtitles?&max-results=15',620,"%s/art/wfs/subtitled.png"%selfAddon.getAddonInfo("path"))
                main.addDir('Tamil BluRay','http://www.sominaltvfilms.com/search/label/Tamil-BluRays?&max-results=15',620,"%s/art/wfs/bluray.png"%selfAddon.getAddonInfo("path"))
        elif mname=='Malayalam':
                main.addDir('Malayalam English Subtitled','http://www.sominaltvfilms.com/search/label/Malayalam-Movies-English-Subtitles?&max-results=15',620,"%s/art/wfs/subtitled.png"%selfAddon.getAddonInfo("path"))
        elif mname=='Punjabi':
                main.addDir('Punjabi English Subtitled','http://www.sominaltvfilms.com/search/label/Punjabi-Movies-English-Subtitles?&max-results=15',620,"%s/art/wfs/subtitled.png"%selfAddon.getAddonInfo("path"))
        elif mname=='All Hindi Dubbed Movies':
                main.addDir('Hindi Dubbed BluRay','http://www.sominaltvfilms.com/search/label/Hindi-Dubbed-BluRays?&max-results=15',620,"%s/art/wfs/bluray.png"%selfAddon.getAddonInfo("path"))
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('<div class="separator" style=".+?"><a href="(.+?)".+?<img border=".+?src="(.+?)".+?<br.+?(.+?)</div><.+?</div>.+?createSummaryAndThumb.+?","(.+?)","(.+?)",".+?</script>').findall(link)
        for fan,thumb,desc,name,url in match:
            desc=desc.replace('</div><div class="separator" style="clear: both; text-align: left;">','').replace('<span class="Apple-style-span" style="background-color: white; color: #333333; font-family: Verdana, Arial, sans-serif; font-size: 13px; line-height: 18px;">','').replace('</div><div class="separator" style="clear: both; text-align: justify;">','').replace('</div><div class="separator" style="clear: both; text-align: center;">','').replace('</span>','').replace('<span>','').replace('</div><div class="separator" style="clear: both; text-align: justify;"><span class="Apple-style-span" style="background-color: white; color: #333333; font-family: Verdana, Arial, sans-serif; font-size: 13px; line-height: 18px;">','')
            desc=desc.replace('<br>','').replace('</br>','').replace('</div>','').replace('<div>','')
            main.addDirc(name,url,621,thumb,desc,fan)
        paginate = re.compile("""<a class='blog-pager-older-link' href='(.+?)' id='Blog1_blog-pager-older-link' title='Older Posts'><img src='http://3.bp.blogspot.com/-NZpw1vLtyMU/UPxyLMiEanI/AAAAAAAAI1Y/_vDNcnjV7aw/s400/Next.png'/></a>""").findall(link)
        if len(paginate)>0:
            main.addDir('Next',paginate[0],620,"%s/art/next2.png"%selfAddon.getAddonInfo("path"))

def LINK(manme,murl):
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('<a href="http://adf.ly/377117/(.+?)" target="_blank".+?(.+?)</a>').findall(link)
        for url,name in match:
            name=name.replace('<span id="goog_1857978069"></span><span id="goog_1857978070"></span>','').replace('<span style="font-family: Verdana, sans-serif; font-size: x-large;">','').replace('<span style="font-family: Verdana, sans-serif; font-size: large;">','').replace('<span>','').replace('</span>','')
            http= re.compile('http://').findall(url)
            if len(http)==0:
                url='http://'+url
            main.addPlay(name,url,622,'')
    

def LINK2(mname,murl):
        ok=True
        namelist=[]
        urllist=[]
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        link=main.OPENURL(murl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match= re.compile('<link rel=".+?" type="application/json.+?oembed" href="(.+?)"/>').findall(link)
        if match:
            link2=main.OPENURL(match[0])
            link2=link2.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\/','/').replace('\\','')
            docUrl= re.compile('iframe src="(.+?)"').findall(link2)
            thumbs= re.compile('thumbnail_url":"(.+?)",').findall(link2)
            if len(thumbs)>0:
                thumb=thumbs[0]
            else:
                thumb=''
            descs= re.compile('box.?(.+?).?box').findall(link2)
            if len(descs)>0:
                desc=descs[0]
            else:
                desc=''   
            
            if docUrl:
                link2=main.OPENURL(docUrl[0])
                match= re.compile('url_encoded_fmt_stream_map\":\"(.+?),\"').findall(link2)
                if match:
                    streams_map = str(match)
                    stream= re.compile('url=(.+?)&type=.+?&quality=(.+?)[,\"]{1}').findall(streams_map)
                    for group1,group2 in stream:#Thanks to the-one for google-doc resolver
                        stream_url = str(group1)
                        stream_url = unescape(stream_url)
                        urllist.append(stream_url)
                        stream_qlty = str(group2.upper())
                        if (stream_qlty == 'HD720'):
                            stream_qlty = 'HD-720p'
                        elif (stream_qlty == 'LARGE'):
                            stream_qlty = 'SD-480p'
                        elif (stream_qlty == 'MEDIUM'):
                            stream_qlty = 'SD-360p'
                        namelist.append(stream_qlty)
                    dialog = xbmcgui.Dialog()
                    answer =dialog.select("Quality Select", namelist)
                    if answer != -1:
                        main.GA("SominalTv","Watched")
                        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,3000)")
                        stream_url2 = urllist[int(answer)]
                        listitem = xbmcgui.ListItem(mname,thumbnailImage=thumb)
                        listitem.setInfo('video', {'Title': mname, 'Plot': desc} )
                        playlist.add(stream_url2,listitem)
                        xbmcPlayer = xbmc.Player()
                        xbmcPlayer.play(playlist)
                    return ok
                else:
                        xbmc.executebuiltin("XBMC.Notification(Sorry!,Protected Link,5000)")
            
