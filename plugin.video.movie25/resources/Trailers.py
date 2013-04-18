import xbmc, xbmcaddon, xbmcgui, xbmcplugin, xbmcvfs,cookielib,string, urllib, urllib2,re
#import urlresolver
addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)


tmdbid = sys.argv[1]
tmdbid=tmdbid.replace('"','').replace("'","").replace('[','').replace(']','').replace('(','').replace(')','').replace(',','')


def trailer(tmdbid):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:10.0a1) Gecko/20111029 Firefox/10.0a1'
    request= 'http://api.themoviedb.org/3/movie/' + tmdbid + '/trailers?api_key=d5da2b7895972fffa2774ff23f40a92f'
    txheaders= {'Accept': 'application/json','User-Agent':user_agent}
    req = urllib2.Request(request,None,txheaders)
    response=urllib2.urlopen(req).read()
    if re.search('"size":"HD"',response):
        quality=re.compile('"size":"HD","source":"(.+?)"').findall(response)[0]
        youtube='http://www.youtube.com/watch?v=' + quality
        stream_url= "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+quality+"&hd=1"
        xbmc.Player().play(stream_url)
    elif re.search('"size":"HQ"',response):
        quality=re.compile('"size":"HQ","source":"(.+?)"').findall(response)[0]
        youtube='http://www.youtube.com/watch?v=' + quality
        stream_url= "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+quality+"&hd=1"
        xbmc.Player().play(stream_url)
    elif re.search('"size":"Standard"',response):
        quality=re.compile('"size":"Standard","source":"(.+?)"').findall(response)[0]
        youtube='http://www.youtube.com/watch?v=' + quality
        stream_url= "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+quality+"&hd=1"
        xbmc.Player().play(stream_url)
        xbmc.Player().play(stream_url)
    else:
        xbmc.executebuiltin("XBMC.Notification(Sorry!,No Trailer Available For This Movie,3000)")
    

if tmdbid == '':
    xbmc.executebuiltin("XBMC.Notification(Sorry!,No Trailer Available For This Movie,3000)")
else:
    xbmc.executebuiltin("XBMC.Notification(Please Wait!,Loading Trailer,1500)")
    trailer(tmdbid)
