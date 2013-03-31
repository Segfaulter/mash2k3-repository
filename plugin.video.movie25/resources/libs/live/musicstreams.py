# -*- coding: cp1252 -*-
import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def MUSICSTREAMS():
        main.GA("MUSIC-Streams","Watched")
        main.addLink('Heart TV','rtmp://cdn-the-2.musicradio.com:80/LiveVideo playpath=Heart swfUrl=http://heart.gcstatic.com/gusto/a/tv/swf/player.swf live=true timeout=15 pageUrl=http://www.heart.co.uk/tv/player/','http://www.elky666.plus.com/logo/Sky%20Logos/Heart%20TV.png')
        main.addLink('Capital TV','rtmp://cdn-the-2.musicradio.com:80/LiveVideo playpath=Capital swfUrl=http://capital.gcstatic.com/gusto/a/tv/swf/player.swf live=true timeout=15 pageUrl=http://www.capitalfm.com/tv/player/','http://www.atvtoday.co.uk/wp-content/uploads/2012/10/capital-one.gif')
        main.addLink('Vevo TV','http://vevoplaylist-live.hls.adaptive.level3.net/vevo/ch1/appleman.m3u8',"%s/art/vevotv.jpg"%selfAddon.getAddonInfo("path"))
        main.addLink('The Country Network','rtmp://cp76676.live.edgefcs.net:443/live playpath=5uMjNmMjqqV2tI5_ZzsUtHcPRTSQiUli_640_480_600@54976 swfUrl=http://osmf.org/dev/1.6-sprint-3/StrobeMediaPlayback.swf live=true timeout=15','http://upload.wikimedia.org/wikipedia/en/d/dd/The_Country_Network_Logo.png')
        main.addLink('Dance TV','mms://onstreaming01.de.gtk.hu/dancetv','http://b.vimeocdn.com/ps/420/078/4200785_300.jpg')
        main.addLink('For Music Canale 613','rtmp://wowza1.top-ix.org/quartaretetv1 playpath=formusicweb swfUrl=http://lihattv.us/scripts/videogallery.swf live=1 pageUrl=http://lihattv.us/?ch=it','http://www.gingerdj.com/wp-content/uploads/2012/10/FOR-MUSIC-540x342.png')
        main.addLink('IM1 MUSIC','rtmp://im1.tv.flash.glb.ipercast.net/im1.tv-live/live1 live=true timeout=15','http://i2.ytimg.com/vi/Ep0KXtncv2Q/mqdefault.jpg')
        main.addLink('Kiss TV','rtmp://kisstelevision.es.flash3.glb.ipercast.net/kisstelevision.es-live/live live=true timeout=15','http://24.255.54.207:81/sites/default/files/kiss-tv-logo-1.jpg')
        main.addLink('One HD Pop','rtsp://93.114.43.3:1935/live/pophd','http://static.moje-lektire.com/net.tv-tube/tv_repo/2824/thumb.png')
        main.addLink('One HD Rock','rtmpe://93.114.43.3:1935/live playpath=rockhd swfUrl=http://livehd.tv/player/player.swf live=true timeout=15 pageUrl=http://livehd.tv/index.php?stream=dance&resolution=hd token=6c69766568642e747620657374652063656c206d616920746172652121','http://static.tv-tube.tv/net.tv-tube/tv_repo/2825/thumb.png')
        main.addLink('PIK TV','rtmp://fms.pik-tv.com/live/piktv3pik3tv swfUrl=http://pik-tv.com/uppod.swf','http://twimg0-a.akamaihd.net/profile_images/2158748139/fblogo.jpg')
        main.addLink('Radio 105','rtmp://fms.105.net:1935/live playpath=105Test1 live=true timeout=15','http://www.105.net/gfx/lgo/radio-105-network.png')
        main.addLink('Rock TV','rtsp://93.114.43.3:1935/live/rockhd live=true timeout=15','http://userserve-ak.last.fm/serve/_/76786366/Rock+Tv+Heavy+Rotation.jpg')
        main.addLink('Slam TV','rtmp://video.true.nl/slamtv/ playpath=slamtv live=true timeout=15','http://www.logotypes101.com/logos/387/D7E51AFAB8B659F367649E5D41B4C271/slamtv.png')
        main.addLink('Virgin','rtmp://fms.105.net:1935/live playpath=virgin1 live=true timeout=15','http://www.xtimeline.com/__UserPic_Large/4369/ELT200801201019128994435.JPG')
        link=main.OPENURL('https://nkjtvt.googlecode.com/svn/trunk/playlists/musicstreams.xml')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('type=playlistname=Sorted by user-assigned order','').replace('name=Sorted [COLOR=FF00FF00]by user-assigned order[/COLOR]','').replace('name=Live Tv Channels Twothumb','')
        match=re.compile('name=(.+?)thumb=(.+?)URL=(.+?)#').findall(link)
        for name,thumb,url in match:
            match2=re.compile('.+?(.+?)URL').findall(name)
            if len(match2)>0:
                name =match2[0]
            url=url.replace('player=defaultrating=-1.00','').replace('%20',' ').replace('player=default','').replace(' conn=S:OK --live','').replace(' conn=S:OK','')
            main.addLink(name,url,thumb)

        
        
