import re
from t0mm0.common.net import Net
import urllib2
from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin
import xbmcgui
net = Net()

class MovreelResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "movreel"

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)
        self.net = Net()

    def get_media_url(self, host, media_id):
        try:
            print 'HOST: '+host
            print 'MEDIA ID: '+media_id
            url = self.get_url(host, media_id)
            html = self.net.http_GET(url).content
            #Show dialog box so user knows something is happening
            dialog = xbmcgui.DialogProgress()
            dialog.create('Resolving', 'Resolving Movreel Link...')       
            dialog.update(0)
        
            print 'Movreel - Requesting GET URL: %s' % url
            html = net.http_GET(url).content
        
            dialog.update(33)
        
            #Check page for any error msgs
            if re.search('This server is in maintenance mode', html):
                print '***** Movreel - Site reported maintenance mode'
                raise Exception('File is currently unavailable on the host')

            #Set POST data values
            op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
            postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
            method_free = re.search('<input type="(submit|hidden)" name="method_free" (style=".*?" )*value="(.*?)">', html).group(3)
            method_premium = re.search('<input type="(hidden|submit)" name="method_premium" (style=".*?" )*value="(.*?)">', html).group(3)
            
            if method_free:
                usr_login = ''
                fname = re.search('<input type="hidden" name="fname" value="(.+?)">', html).group(1)
                data = {'op': op, 'usr_login': usr_login, 'id': postid, 'referer': url, 'fname': fname, 'method_free': method_free}
            else:
                rand = re.search('<input type="hidden" name="rand" value="(.+?)">', html).group(1)
                data = {'op': op, 'id': postid, 'referer': url, 'rand': rand, 'method_premium': method_premium}
        
            print 'Movreel - Requesting POST URL: %s DATA: %s' % (url, data)
            html = net.http_POST(url, data).content

            #Only do next post if Free account, skip to last page for download link if Premium
            if method_free:
                #Check for download limit error msg
                if re.search('<p class="err">.+?</p>', html):
                    print '***** Download limit reached'
                    errortxt = re.search('<p class="err">(.+?)</p>', html).group(1)
                    raise Exception(errortxt)
    
                dialog.update(66)
            
                #Set POST data values
                op = re.search('<input type="hidden" name="op" value="(.+?)">', html).group(1)
                postid = re.search('<input type="hidden" name="id" value="(.+?)">', html).group(1)
                rand = re.search('<input type="hidden" name="rand" value="(.+?)">', html).group(1)
                method_free = re.search('<input type="hidden" name="method_free" value="(.+?)">', html).group(1)
            
                data = {'op': op, 'id': postid, 'rand': rand, 'referer': url, 'method_free': method_free, 'down_direct': 1}
    
                print 'Movreel - Requesting POST URL: %s DATA: %s' % (url, data)
                html = net.http_POST(url, data).content

            #Get download link
            dialog.update(100)
            link = re.search('<a id="lnk_download" href="(.+?)">Download Original Video</a>', html, re.DOTALL).group(1)
            
            dialog.close()
            print str(link)
            mediurl = link
        
            return mediurl

        except Exception, e:
            print '**** Movreel Error occured: %s' % e
            raise

    def get_url(self, host, media_id):
        print 'host: '+host
        print 'media_id: '+media_id
        return 'http://www.movreel.com/%s' % media_id

    def get_host_and_id(self, url):
        print 'GET_HOST_AND_ID URL: '+url
        r = re.search('//(.+?)/([0-9a-zA-Z]+)',url)
        if r:
            print r.groups()
            return r.groups()
        else:
            return False
        print 'G_H_I: host: '+str(host)
        print 'G_H_I MEDIA_ID: '+str(media_id)
        return('host', 'media_id')


    def valid_url(self, url, host):
        print 'VALID_URL URL: '+url
        return (re.match('http://(www.)?movreel.com/' +
                         '[0-9A-Za-z]+', url) or
                         'movreel' in host)
