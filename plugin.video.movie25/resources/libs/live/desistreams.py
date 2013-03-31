import urllib,urllib2,re,cookielib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def DESISTREAMS():
        main.GA("Live","Desistreams")
        main.addDir('Sports','sports',130,"%s/art/desistream.png"%selfAddon.getAddonInfo("path"))
        main.addDir('English Channels','english',130,"%s/art/desistream.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Indian Channels','indian',130,"%s/art/desistream.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Pakistani Channels','pakistani',130,"%s/art/desistream.png"%selfAddon.getAddonInfo("path"))
        main.addDir('Bangladeshi Channels','bangladeshi',130,"%s/art/desistream.png"%selfAddon.getAddonInfo("path"))

def DESISTREAMSList(murl):
        link=main.OPENURL('http://www.desistreams.tv/')
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        if murl=='sports':
            main.GA("Desi-Sport","Watched")
            main.addLink('Sky Sports 1','rtmp://live.ukcast.tv/broadcast playpath=sky_sportsi1.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=sky_sports1&vw=600&vh=430','http://www.desistreams.tv/images/sky_sports1.jpg')
            main.addLink('Sky Sports 2','rtmp://live.ukcast.tv/broadcast playpath=sky_sportsi2.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=sky_sports2&vw=600&vh=430','http://www.desistreams.tv/images/sky_sports2.jpg')
            main.addLink('Sky Sports 3','rtmp://live.ukcast.tv/broadcast playpath=sky_sportsi3.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=sky_sports3&vw=600&vh=430','http://www.desistreams.tv/images/sky_sports3.jpg')
            main.addLink('NBA TV','rtmp://cdn.livecaster.tv/stream playpath=nbu7 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=nbu7&vw=600&vh=430','http://www.desistreams.tv/images/nba.png')
            main.addLink('Live Footy','rtmp://cdn.livecaster.tv/broadcast playpath=espn.stream swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=espn&vw=600&vh=430','http://www.desistreams.tv/images/espn.jpg')
            main.addLink('Geo Super','rtmp://cdn.livecaster.tv/stream playpath=13246540114814 swfUrl=http://www.livecaster.tv/player/player.swf pageUrl=http://www.livecaster.tv/embed.php?u=Geosuper&vw=600&vh=470','http://www.desistreams.tv/images/geo_super.png')
            main.addLink('PTV Sports','rtmp://cdn.livecaster.tv/broadcast playpath=onlineptvsports swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=ptvsportsss1&vw=600&vh=430','http://www.desistreams.tv/images/ptv_sports.PNG')
            main.addLink('PTV Sports 2','rtmp://live.ukcast.tv/broadcast playpath=sportsptv swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=sportsptv&vw=600&vh=430','http://www.desistreams.tv/images/ptv_sports.PNG')
            main.addLink('Ten Cricket','rtmp://80.82.78.37/cast playpath=12377 swfUrl=http://95.211.219.184/player-licensed.swf live=true timeout=15 pageUrl=http://www.flashcast.tv/embed.php?live=tencricketyo&vw=600&vh=430','http://www.desistreams.tv/images/ten_cricket.png')
            main.addLink('Ten Cricket','rtmp://80.82.78.37/cast playpath=454666h swfUrl=http://95.211.219.184/player-licensed.swf live=true timeout=15 pageUrl=http://www.flashcast.tv/embed.php?live=ten_cricktu&vw=600&vh=430','http://www.desistreams.tv/images/ten_cricket.png')
            main.addLink('Star Cricket','rtmp://109.123.126.28/live playpath=starcricketnew?id=39362 swfUrl=http://www.ucaster.eu/static/scripts/eplayer.swf live=true timeout=15 pageUrl=http://www.ucaster.eu/embedded/starcricketnew/1/600/430','http://www.desistreams.tv/images/star_cricket.png')
            main.addLink('Star Cricket HQ','rtmp://live.ukcast.tv/broadcast playpath=star_cricket.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=star_cricket&vw=600&vh=430','http://www.desistreams.tv/images/star_cricket.png')
            main.addLink('Willow Cricket','rtmp://cdn.livecaster.tv/stream playpath=willo8 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=willo8&vw=600&vh=430','http://www.desistreams.tv/images/willow_cricket.PNG')
            main.addLink('Star Sports','rtmp://live.ukcast.tv/broadcast playpath=star_sports74.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=star_sports74&vw=600&vh=430','http://www.desistreams.tv/images/star_sports.png')
            main.addLink('Ten Sports','rtmp://cdn.livecaster.tv/broadcast playpath=1155200 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=TenSportsLive&vw=600&vh=470','http://www.desistreams.tv/images/ten_sports.jpg')
            main.addLink('Ten Sports 2','rtmp://cdn.livecaster.tv/stream playpath=ten_sports9.stream swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=ten_sports9&vw=600&vh=430','http://www.desistreams.tv/images/ten_sports.jpg')
            main.addLink('WWE TV','rtmp://cdn.livecaster.tv/stream playpath=wwe2.stream swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=wwe2&vw=600&vh=430','http://desistreams.tv/images/wwe.jpg')
            main.addLink('Sony Six (IPL)','rtmp://cdn.livecaster.tv/stream playpath=sab_tv66 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=sab_tv66&vw=600&vh=430','http://www.desistreams.tv/images/sony_six.png')
            main.addLink('JSC Sports +2','rtmp://live.ukcast.tv/broadcast playpath=jscu swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=jscu&vw=600&vh=430','http://www.desistreams.tv/images/jsc+2.png')
            main.addLink('ESPN UK','rtmp://live.ukcast.tv/broadcast playpath=espn_uk.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=espn_uk&vw=600&vh=430','http://www.desistreams.tv/images/espn_uk.png')
            main.addLink('ESPN USA','rtmp://live.ukcast.tv/broadcast playpath=espn_usa.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=espn_usa&vw=600&vh=430','http://www.desistreams.tv/images/espn.jpg')
            main.addLink('Bein Sport','rtmp://live.ukcast.tv/broadcast playpath=bein_sport99.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=bein_sport99&vw=600&vh=430','http://www.desistreams.tv/images/bein_sport.jpeg')
        elif murl=='english':
            main.GA("Desi-English","Watched")
            main.addLink('ITV 1','rtmp://live.ukcast.tv/broadcast playpath=itv1.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=itv1&vw=600&vh=430','http://desistreams.tv/images/itv1.jpg')
            main.addLink('BBC One','rtmp://live.ukcast.tv/broadcast playpath=bbc11.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=bbc11&vw=600&vh=430','http://www.desistreams.tv/images/bbc1.jpg')
            main.addLink('Fox Movies','rtmp://live.ukcast.tv/broadcast playpath=fox_movies.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=fox_movies&vw=600&vh=430','http://www.desistreams.tv/images/fox_movies.jpg')
            main.addLink('Star Movies','rtmp://cdn.livecaster.tv/stream playpath=star_news66 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=star_news66&vw=600&vh=430','http://www.desistreams.tv/images/star_movies.jpg')
            main.addLink('ABC USA','rtmp://cdn.livecaster.tv/stream playpath=abc9 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=abc9&vw=600&vh=430','http://www.desistreams.tv/images/abc.jpg')
            main.addLink('ABC USA 2','rtmp://live.ukcast.tv/broadcast playpath=abc_usa.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=abc_usa&vw=600&vh=430','http://www.desistreams.tv/images/abc.jpg')
            main.addLink('CW USA','rtmp://cdn.livecaster.tv/stream playpath=cwww swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=cwww&vw=600&vh=430','http://www.desistreams.tv/images/cw.jpg')
            main.addLink('CW USA 2','rtmp://live.ukcast.tv/broadcast playpath=cw_usa.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=cw_usa&vw=600&vh=430','http://www.desistreams.tv/images/cw.jpg')
            main.addLink('CBS USA','rtmp://live.ukcast.tv/broadcast playpath=cbsu swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=cbsu&vw=600&vh=430','http://www.desistreams.tv/images/cbs.jpg')
            main.addLink('Fox USA','rtmp://198.100.149.81/live/fxo7 playpath=fxo7.video swfUrl=http://www.islbroadcast.com/player/player.swf live=true timeout=15 pageUrl=http://www.islbroadcast.com/embed.php?n=fxo7&vw=980&vh=551','http://www.desistreams.tv/images/fox.jpg')
            main.addLink('FX USA','rtmp://cdn.livecaster.tv/stream playpath=fx08 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=fx08&vw=600&vh=430','http://www.desistreams.tv/images/fx.gif')
            main.addLink('FX USA 2','rtmp://live.ukcast.tv/broadcast playpath=fx_usa.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=fx_usa&vw=600&vh=430','http://www.desistreams.tv/images/fx.gif')
            main.addLink('HBO USA','rtmp://live.ukcast.tv/broadcast playpath=hobusa swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=hobusa&vw=600&vh=430','http://www.desistreams.tv/images/hbo.gif')
            main.addLink('NBC USA','rtmp://cdn.livecaster.tv/stream playpath=nbc9 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=nbc9&vw=600&vh=430','http://www.desistreams.tv/images/nbc.png')
            main.addLink('NBC USA 2','rtmp://live.ukcast.tv/broadcast playpath=nbc_usa.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=nbc_usa&vw=600&vh=430','http://www.desistreams.tv/images/nbc.png')
            main.addLink('Food Network','rtmp://cdn.livecaster.tv/stream playpath=food_6 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=food_6&vw=600&vh=430','http://www.desistreams.tv/images/food_network.jpg')
            main.addLink('Bravo','rtmpt://cdn.livecaster.tv/stream playpath=bravo9 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=bravo9&vw=600&vh=430','http://www.desistreams.tv/images/bravo.gif')
            main.addLink('TBS USA','rtmp://142.4.216.154/edge playpath=rp6zlxo29ob14q1 swfUrl=http://player.ilive.to/player_embed.swf live=true timeout=15 pageUrl=http://www.ilive.to/embedplayer.php?width=980&height=551&channel=40300&autoplay=true','http://www.desistreams.tv/images/tbs.jpg')
            main.addLink('USA Network','rtmp://cdn.livecaster.tv/stream playpath=usa9 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=usa9&vw=600&vh=430','http://www.desistreams.tv/images/usahd.png')
            main.addLink('USA Network 2','rtmp://live.ukcast.tv/broadcast playpath=usa_network.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=usa_network&vw=600&vh=430','http://www.desistreams.tv/images/usahd.png')
            main.addLink('Fox News USA','rtmp://cdn.livecaster.tv/stream playpath=fox_news77 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=fox_news77&vw=600&vh=430','http://www.desistreams.tv/images/foxnews.png')
            main.addLink('Cartoon Network USA','rtmp://cdn.livecaster.tv/stream playpath=32asuBUzU9 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=32asuBUzU9&vw=980&vh=551','http://www.desistreams.tv/images/cartoon_network.jpg')
            main.addLink('Nickelodeon USA','rtmp://cdn.livecaster.tv/stream playpath=nickkp swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=nickkp&vw=600&vh=430','http://www.desistreams.tv/images/nickelodeon.jpg')
            main.addLink('CNBC USA','rtmp://cdn.livecaster.tv/stream playpath=cnbcc swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=cnbcc&vw=600&vh=430','http://www.desistreams.tv/images/cnbc.png')
            main.addLink('Lifetime USA','rtmp://cdn.livecaster.tv/stream playpath=lifetime4 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=lifetime4&vw=600&vh=430','http://www.desistreams.tv/images/life_time.png')
            main.addLink('Starz USA','rtmp://live.ukcast.tv/broadcast playpath=starz.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=starz&vw=600&vh=430','http://www.desistreams.tv/images/starz_usa.jpg')
            main.addLink('Discovery USA','rtmp://live.ukcast.tv/broadcast playpath=discoveryu swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=discoveryu&vw=600&vh=430','http://www.desistreams.tv/images/discovery_channel.jpg')
            main.addLink('BBC World News','rtmp://cdn.livecaster.tv/live playpath=bbcworldnews.stream swfUrl=http://www.wcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.wcast.tv/embed.php?u=bbcworldnews&vw=600&vh=430','http://www.desistreams.tv/images/bbc_world_news.jpg')
            main.addLink('Fashion TV','rtmp://cdn.livecaster.tv/broadcast playpath=ftv.stream swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=ftv1&vw=600&vh=430','http://www.desistreams.tv/images/ftv.jpg')
            main.addLink('CNN Int.','rtmp://live.ukcast.tv/broadcast playpath=cnn1.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=cnn1&vw=600&vh=430','http://www.desistreams.tv/images/cnn.gif')
            main.addLink('Star World','rtmp://live.ukcast.tv/broadcast playpath=star_world.stream swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=star_world&vw=600&vh=430','http://www.desistreams.tv/images/star_world.jpg')
        elif murl=='indian':
           
            match=re.compile('<font color="brown" size="4"><b>Indian Channels</b></font></center>(.+?)<center><font color="brown" size="4"><b>Pakistani Channels</b></font></center>').findall(link)
            for entry in match:
                match2=re.compile('<a href="(.+?)" Target=.+?><center><img src="(.+?)" width=".+?" height=".+?" alt="" /></a><br />(.+?)<').findall(entry)
                for url,thumb,name in match2:
                    url=url.replace('http://desistreams.tv/','')
                    main.addPlay(name,'http://www.desistreams.tv/'+url,131,'http://www.desistreams.tv/'+thumb)
        elif murl=='pakistani':
            main.GA("Desi-Pakistani","Watched")
            main.addLink('Urdu 1','rtmp://cdn.livecaster.tv/broadcast playpath=urdupk1 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=urdupk1&vw=600&vh=430','http://www.desistreams.tv/images/urdu_1.jpg')
            main.addLink('Ary News','rtmp://cdn.livecaster.tv/stream playpath=arynews swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=arynews&vw=600&vh=430','http://desistreams.tv/images/ary_news.jpg')
            main.addLink('Geo News','rtmp://cdn.livecaster.tv/stream playpath=geonewsa swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=geonewsa&vw=600&vh=430','http://desistreams.tv/images/geo_news.jpg')
            main.addLink('Geo News 2','rtmp://live.wcast.tv/broadcast playpath=115517 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=geonews115&vw=600&vh=430','http://www.desistreams.tv/images/geo_news.jpg')
            main.addLink('ARY QTV','rtmp://cdn.livecaster.tv/stream playpath=qtv swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=qtv&vw=600&vh=430','http://www.desistreams.tv/images/qtv.png')
            main.addLink('Hum TV','rtmp://live.ukcast.tv/broadcast playpath=humtvj swfUrl=http://www.ukcast.tv/player/player.swf live=true timeout=15 pageUrl=http://www.ukcast.tv/embed.php?u=humtvj&vw=600&vh=470','http://www.desistreams.tv/images/hum_tv.png')
            main.addLink('Hum TV 2','rtmp://cdn.livecaster.tv/broadcast playpath=115520 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=humtv2&vw=600&vh=470','http://www.desistreams.tv/images/hum_tv.png')
            main.addLink('Geo Entertainment 2','rtmp://cdn.livecaster.tv/broadcast playpath=ent1 swfUrlhttp://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=GeoTv&vw=600&vh=430','http://www.desistreams.tv/images/geo_entertainment.jpg')
            main.addLink('Ary Digital 2','rtmp://cdn.livecaster.tv/broadcast playpath=111206 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=aryhq072&vw=600&vh=430','http://www.desistreams.tv/images/ary_digital.jpg')
            main.addLink('Masala TV','rtmp://cdn.livecaster.tv/stream playpath=masalo swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=masalo&vw=600&vh=430','http://www.desistreams.tv/images/masala_tv.png')
            main.addLink('Express Entertainment','rtmp://cdn.livecaster.tv/stream playpath=express5 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=express5&vw=600&vh=430','http://www.desistreams.tv/images/express_entertainment.png')
            main.addLink('Express News','rtmp://cdn.livecaster.tv/stream playpath=expressnewsi2 swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=expressnewsi2&vw=600&vh=430','http://www.desistreams.tv/images/express_news.png')
            main.addLink('Dubbed Movies','rtmp://cdn.livecaster.tv/stream playpath=dubbedmovie swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=dubbedmovie&vw=600&vh=430','http://www.desistreams.tv/images/dubbed_movies.jpg')
            main.addLink('PTV Home','rtmp://cdn.livecaster.tv/stream playpath=ptv_home.stream swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=ptv_home&vw=600&vh=430','http://www.desistreams.tv/images/ptv_home.jpg')
            main.addLink('Cartoon Network','rtmp://cdn.livecaster.tv/stream playpath=cartoonnet9.stream swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=cartoonnet9&vw=600&vh=430','http://desistreams.tv/images/cartoon_network.jpg')
        elif murl=='bangladeshi':
            main.GA("Desi-Bangla","Watched")
            main.addLink('OTV Bangla','rtmp://cdn.livecaster.tv/stream playpath=otv_bangla.stream swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=otv_bangla&vw=600&vh=430','http://www.desistreams.tv/images/otv_bangla.gif')
            main.addLink('Tarang Bangla','rtmp://cdn.livecaster.tv/stream playpath=tarang_bangla.stream swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl=http://www.livecaster.tv/embed.php?u=tarang_bangla&vw=600&vh=430','http://www.desistreams.tv/images/tarang_bangla.gif')

def DESISTREAMSLink(mname,murl):
        link=main.OPENURL(murl)
        main.GA("Desi-Indian","Watched")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        ok=True
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<script type=\'text/javascript\'> width=(.+?), height=(.+?), channel=\'(.+?)\', g=\'.+?\';</script><script type=\'text/javascript\' src=\'(.+?)\'>').findall(link)
        for wid,hei,fid,streamer in match[0:1]:
                continue
        if len(match)==0:
            match=re.compile('<script type=\'text/javascript\'>fid=\'(.+?)\'; v_width=(.+?); v_height=(.+?);</script><script type=\'text/javascript\' src=\'(.+?)\'>').findall(link)
            for fid,wid,hei,streamer in match[0:1]:
                continue
        livecaster = re.compile("livecaster").findall(streamer)
        if len(livecaster)>0:
            pageUrl='http://www.livecaster.tv/embed.php?u='+fid+'&vw='+wid+'&vh='+hei
            if mname=='Live Footy' or mname=='PTV Sports'or mname=='Ten Sports':
                if fid=='ptvsportsss1':
                    fid='onlineptvsports'
                    stream_url ='rtmp://cdn.livecaster.tv/broadcast playpath='+fid+' swfUrl=http://www.livecaster.tv/player/player.swf pageUrl='+pageUrl
                elif fid=='TenSportsLive':
                    fid='1155200'
                    stream_url ='rtmp://cdn.livecaster.tv/broadcast playpath='+fid+' swfUrl=http://www.livecaster.tv/player/player.swf pageUrl='+pageUrl
            else:
                if fid =='Geosuper':
                    fid='13246540114814'
                elif fid=='ten_sports9':
                    fid='ten_sports9.stream'
                elif fid=='wwe2':
                    fid='wwe2.stream'
                stream_url ='rtmp://cdn.livecaster.tv/stream playpath='+fid+' swfUrl=http://www.livecaster.tv/player/player.swf live=true timeout=15 pageUrl='+pageUrl
            
        ukcast = re.compile("ukcast").findall(streamer)
        if len(ukcast)>0:
            pageUrl='http://www.ukcast.tv/embed.php?u='+fid+'&vw='+wid+'&vh='+hei
            if mname=='PTV Sports 2'or mname=='JSC Sports +2':
                stream_url ='rtmp://live.ukcast.tv/broadcast playpath='+fid+' swfUrl=http://www.ukcast.tv/player/player.swf pageUrl='+pageUrl
            else:
                if fid=='espnukk':
                    fid='espn_uk'
                stream_url ='rtmp://live.ukcast.tv/broadcast playpath='+fid+'.stream swfUrl=http://www.ukcast.tv/player/player.swf pageUrl='+pageUrl
        listitem = xbmcgui.ListItem(mname)
        playlist.add(stream_url,listitem)
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playlist)
        return ok
