import urllib,urllib2,re,cookielib,string, urlparse
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,urlresolver
from resources.libs import main

#Mash Up - by Mash2k3 2012.

addon_id = 'plugin.video.movie25'
selfAddon = xbmcaddon.Addon(id=addon_id)

def DISC():
        main.addDir('AFRICA','http://dsc.discovery.com/services/taxonomy/Africa%20the%20Series/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/africa-show-carousel-badge-130x97.jpg')
        main.addDir('ALASKA: THE LAST FRONTIER','http://dsc.discovery.com/services/taxonomy/ALASKA:%20THE%20LAST%20FRONTIER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/alaska_badge_130x97.jpg')
        main.addDir('AMERICAN CHOPPER','http://dsc.discovery.com/services/taxonomy/AMERICAN%20CHOPPER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/american-chopper-badge.jpg')
        main.addDir('AMERICAN GUNS','http://dsc.discovery.com/services/taxonomy/AMERICAN%20GUNS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/american-guns-show-carousel-badge.jpg')
        main.addDir('AMISH MAFIA','http://dsc.discovery.com/services/taxonomy/AMISH%20MAFIA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/amish-mafia-show-carousel-badge-130x97.jpg')
        main.addDir('AUCTION KINGS','http://dsc.discovery.com/services/taxonomy/AUCTION%20KINGS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/auction-kings-show-carousel-badge.jpg')
        main.addDir('BERING SEA GOLD','http://dsc.discovery.com/services/taxonomy/BERING%20SEA%20GOLD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/bsg-full-ep.jpg')
        main.addDir('BERING SEA GOLD: UNDER THE ICE','http://dsc.discovery.com/services/taxonomy/BERING%20SEA%20GOLD%20UNDER%20THE%20ICE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/new-bsg-under-the-ice-show-carousel-badge.jpg')
        main.addDir('BREAKING MAGIC','http://dsc.discovery.com/services/taxonomy/BREAKING%20MAGIC/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/breaking-magic-badge.jpg')
        main.addDir('CASH CAB','http://dsc.discovery.com/services/taxonomy/CASH%20CAB/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/cash-cab-show-carousel-badge.jpg')
        main.addDir('CURIOSITY','http://dsc.discovery.com/services/taxonomy/CURIOSITY/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/curiosity-show-carousel-badge.jpg')
        main.addDir('DEADLIEST CATCH','http://dsc.discovery.com/services/taxonomy/DEADLIeST%20CATCH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/deadliest-catch-show-carousel-badge.jpg')
        main.addDir('DIRTY JOBS','http://dsc.discovery.com/services/taxonomy/DIRTY%20JOBS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/dirty-jobs-show-carousel-badge.jpg')
        main.addDir('DUAL SURVIVAL','http://dsc.discovery.com/services/taxonomy/DUAL%20SURVIVAL/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/dual-survivor-130x97.jpg')
        main.addDir('FAST N LOUD',"http://dsc.discovery.com/services/taxonomy/FAST%20N'%20LOUD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/fast-n-loud-show-carousel-badge.jpg')
        main.addDir('FLYING WILD ALASKA ','http://dsc.discovery.com/services/taxonomy/FLYING%20WILD%20ALASKA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/flying-wild-alaska-show-carousel-badge.jpg')
        main.addDir('FROZEN PLANET','http://dsc.discovery.com/services/taxonomy/FROZEN%20PLANET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/frozen-planet-show-carousel-badge.jpg')
        main.addDir('GOLD RUSH','http://dsc.discovery.com/services/taxonomy/GOLD%20RUSH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/gold-rush-show-carousel-badge.jpg')
        main.addDir('HOW BOOZE BUILT AMERICA','http://dsc.discovery.com/services/taxonomy/HOW%20BOOZE%20BUILT%20AMERICA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/hbba-show-carousel-badge-130x97.jpg')
        main.addDir('JESSE JAMES: OUTLAW GARAGE','http://dsc.discovery.com/services/taxonomy/OUTLAW%20GARAGE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/outlawgarage_130x97.jpg')
        main.addDir('JUNGLE GOLD','http://dsc.discovery.com/services/taxonomy/JUNGLE%20GOLD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/jungle-gold-show-carousel-badge.jpg')
        main.addDir("KURT SUTTER'S OUTLAW EMPIRES","http://dsc.discovery.com/services/taxonomy/KURT%20SUTTER'S%20OUTLAW%20EMPIRES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/outlaw-empires-show-carousel-badge.jpg')
        main.addDir('LIFE','http://dsc.discovery.com/services/taxonomy/LIFE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/life-show-carousel-badge.jpg')
        main.addDir('MAN VS. WILD','http://dsc.discovery.com/services/taxonomy/MAN%20VS%20WILD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/man-vs-wild-show-carousel-badge.jpg')
        main.addDir('MAYAN DOOMSDAY PROPHECY','http://dsc.discovery.com/services/taxonomy/Mayan%20Doomsday%20Prophecy%20Videos/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mayan-doomsday-130x97.jpg')
        main.addDir('MOONSHINERS','http://dsc.discovery.com/services/taxonomy/MOONSHINERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/moonshiners-full-episodes.jpg')
        main.addDir('MYTHBUSTERS','http://dsc.discovery.com/services/taxonomy/MYTHBUSTERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mythbusters-show-carousel-badge.jpg')
        main.addDir('ONE CAR TOO FAR)','http://dsc.discovery.com/services/taxonomy/ONE%20CAR%20TOO%20FAR/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/one-car-too-far-show-carousel-badge.jpg')
        main.addDir('PLANET EARTH','http://dsc.discovery.com/services/taxonomy/PLANET%20EARTH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/show-badge-planet-earth.jpg')
        main.addDir('PROPERTY WARS','http://dsc.discovery.com/services/taxonomy/PROPERTY%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/show-badge-property-wars-130x97.jpg')
        main.addDir('SHARK WEEK','http://dsc.discovery.com/services/taxonomy/SHARK%20WEEK/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/show-badge-sharkweek-130x97.jpg')
        main.addDir('SHIPWRECK MEN','http://dsc.discovery.com/services/taxonomy/SHIPWRECK%20MEN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge_130x97_full2.jpg')
        main.addDir('SONS OF GUNS','http://dsc.discovery.com/services/taxonomy/SONS%20OF%20GUNS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sons-of-guns-show-carousel-badge.jpg')
        main.addDir('STORM CHASERS','http://dsc.discovery.com/services/taxonomy/STORM%20CHASERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/storm-chasers-show-carousel-badge.jpg')
        main.addDir('SURVIVORMAN','http://dsc.discovery.com/services/taxonomy/SURVIVORMAN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/survivorman-130x97.jpg')
        main.addDir('TEXAS CAR WARS','http://dsc.discovery.com/services/taxonomy/TEXAS%20CAR%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/texas-car-wars-show-carousel-badge.jpg')
        main.addDir('THE DEVILS RIDE','http://dsc.discovery.com/services/taxonomy/THE%20DEVILS%20RIDE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/devils-ride-show-carousel-badge.jpg')
        main.addDir('WINGED PLANET','http://dsc.discovery.com/services/taxonomy/WINGED%20PLANET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/winged-planet-130x97.jpg')
        main.addDir('YUKON MEN','http://dsc.discovery.com/services/taxonomy/YUKON%20MEN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/yukon-men-130-97.jpg')
        main.GA("Adventure","Discovery")
        main.VIEWSB()

def ANIP():
        main.addDir("AMERICA'S CUTEST PET","http://animal.discovery.com/services/taxonomy/AMERICA'S%20CUTEST%20PET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/americascutestpet-130x97.jpg')
        main.addDir('AMERICAN STUFFERS','http://animal.discovery.com/services/taxonomy/AMERICAN%20STUFFERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/americanstuffers-130x97.jpg')
        main.addDir('ANIMAL COPS','http://animal.discovery.com/services/taxonomy/ANIMAL%20COPS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/animalcops-130x97.jpg')
        main.addDir('BAD DOG','http://animal.discovery.com/services/taxonomy/BAD%20DOG!/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/baddog-130x97.jpg')
        main.addDir('BATTLEGROUND: RHINO WARS','http://animal.discovery.com/services/taxonomy/BATTLEGROUND:%20RHINO%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/rhino-wars-130x97.jpg')
        main.addDir('CALL OF THE WILDMAN','http://animal.discovery.com/services/taxonomy/CALL%20OF%20THE%20WILDMAN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/call-of-the-wildman-130x97.jpg')
        main.addDir('CATS 101','http://animal.discovery.com/services/taxonomy/CATS%20101/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/cats101-130x97.jpg')
        main.addDir('CONFESSIONS: ANIMAL HOARDING','http://animal.discovery.com/services/taxonomy/CONFESSIONS:%20ANIMAL%20HOARDING/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/confessionsanimalhoarding-130x97.jpg')
        main.addDir('DOGS 101','http://animal.discovery.com/services/taxonomy/DOGS%20101/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/dogs101-130x97.jpg')
        main.addDir('EATING GIANTS','http://animal.discovery.com/services/taxonomy/WILD%20ANIMAL%20VIDEOS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/eating-giants.jpg')
        main.addDir('FATAL ATTRACTIONS','http://animal.discovery.com/services/taxonomy/FATAL%20ATTRACTIONS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/fatalattractions-130x97.jpg')
        main.addDir('FINDING BIGFOOT','http://animal.discovery.com/services/taxonomy/FINDING%20BIGFOOT/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/findingbigfoot-130x97.jpg')
        main.addDir('GATOR BOYS','http://animal.discovery.com/services/taxonomy/GATOR%20BOYS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/gatorboys-130x97.jpg')
        main.addDir('GLORY HOUNDS',"http://animal.discovery.com/services/taxonomy/GLORY%20HOUNDS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/glory-hounds-130x97.jpg')
        main.addDir('THE HAUNTED','http://animal.discovery.com/services/taxonomy/THE%20HAUNTED/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/thehaunted-130x97.jpg')
        main.addDir('HILLBILLY HANDFISHIN',"http://animal.discovery.com/services/taxonomy/HILLBILLY%20HANDFISHIN'/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/hillbillyhandfishin-130x97.jpg')
        main.addDir("I SHOULDN'T BE ALIVE VIDEOS","http://animal.discovery.com/services/taxonomy/I%20SHOULDN'T%20BE%20ALIVE%20VIDEOS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/ishouldntbealive130x97.jpg')
        main.addDir('INFESTED!','http://animal.discovery.com/services/taxonomy/INFESTED/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/infested-130x97.jpg')
        main.addDir("IT'S ME OR THE DOG","http://animal.discovery.com/services/taxonomy/IT'S%20ME%20OR%20THE%20DOG/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/itsmeorthedog-130x97.jpg')
        main.addDir('LAW ON THE BORDER','http://animal.discovery.com/services/taxonomy/LAW%20ON%20THE%20BORDER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/law-on-the-border-130x97.jpg')
        main.addDir('LOST TAPES','http://animal.discovery.com/services/taxonomy/LOST%20TAPES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/lost-tapes-130x97.jpg')
        main.addDir('LOUSIANA LOCKDOWN','http://dsc.discovery.com/services/taxonomy/Mayan%20Doomsday%20Prophecy%20Videos/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/louisiana-lockdown-130x97.jpg')
        main.addDir('MERMAIDS','http://animal.discovery.com/services/taxonomy/MERMAIDS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mermaids-130x97.jpg')
        main.addDir('MONSTERS INSIDE ME','http://animal.discovery.com/services/taxonomy/MONSTERS%20INSIDE%20ME/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/monstersinsideme-130x97.jpg')
        main.addDir('MUST LOVE CATS','http://animal.discovery.com/services/taxonomy/MUST%20LOVE%20CATS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mustlovecats-130x97.jpg')
        main.addDir('MY CAT FROM HELL','http://animal.discovery.com/services/taxonomy/MY%20CAT%20FROM%20HELL/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mycatfromhell-130x97.jpg')
        main.addDir('MY EXTREME ANIMAL PHOBIA','http://animal.discovery.com/services/taxonomy/MY%20EXTREME%20ANIMAL%20PHOBIA/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/myextremeanimalphobia-130x97.jpg')
        main.addDir('NORTH WOODS LAW','http://animal.discovery.com/services/taxonomy/NORTH%20WOODS%20LAW/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/north-woods-law-130x97.jpg')
        main.addDir('OFF THE HOOK','http://animal.discovery.com/services/taxonomy/OFF%20THE%20HOOK/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/off-the-hook-badge.jpg')
        main.addDir('PIT BOSS','http://animal.discovery.com/services/taxonomy/PIT%20BOSS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/pitboss-130x97.jpg')
        main.addDir('PIT BULLS AND PAROLEES','http://animal.discovery.com/services/taxonomy/PIT%20BULLS%20AND%20PAROLEES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/pitbulls-and-parolees-130x97.jpg')
        main.addDir('PUPPY BOWL','http://animal.discovery.com/services/taxonomy/PUPPY%20BOWL/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/puppy-bowl9-130x97.jpg')
        main.addDir('RAISED WILD','http://animal.discovery.com/services/taxonomy/RAISED%20WILD/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/raised-wild-130x97.jpg')
        main.addDir('RATTLESNAKE REPUBLIC','http://animal.discovery.com/services/taxonomy/RATTLESNAKE%20REPUBLIC/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/rattlesnakerepublic-130x97.jpg')
        main.addDir('RIVER MONSTERS','http://animal.discovery.com/services/taxonomy/RIVER%20MONSTERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/river-monsters-130x97.jpg')
        main.addDir('SWAMP WARS','http://animal.discovery.com/services/taxonomy/SWAMP%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/swampwars-130x97.jpg')
        main.addDir('TANKED','http://animal.discovery.com/services/taxonomy/TANKED/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/tanked-130x97.jpg')
        main.addDir('TOO CUTE','http://animal.discovery.com/services/taxonomy/TOO%20CUTE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/toocute-130x97.jpg')
        main.addDir('UNTAMED & UNCUT','http://animal.discovery.com/services/taxonomy/UNTAMED%20AND%20UNCUT/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/untamedanduncut-130x97.jpg')
        main.addDir('WEIRD, TRUE AND FREAKY','http://dsc.discovery.com/services/taxonomy/YUKON%20MEN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/weirdtrueandfreaky-130x97.jpg')
        main.addDir('WHALE WARS','http://animal.discovery.com/services/taxonomy/WHALE%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/whalewars-130x97.jpg')
        main.addDir('WHALE WARS VIKING SHORES','http://animal.discovery.com/services/taxonomy/WHALE%20WARS%20VIKING%20SHORES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/whale-wars-viking-shores-130x97.jpg')
        main.GA("Adventure","AnimalPlanet")
        main.VIEWSB()
        
def MILIT():
        main.addDir('AIR ACES','aa',90,'http://viewersguide.ca/wp-content/uploads/2013/01/air-aces-ss-280x200.png')
        main.addDir('AN OFFICER AND A MOVIE','http://military.discovery.com/services/taxonomy/AN%20OFFICER%20AND%20A%20MOVIE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/oam.jpg')
        main.addDir('BLACK OPS','http://military.discovery.com/services/taxonomy/BLACK%20OPS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/black_ops.jpg')
        main.addDir('COMBAT COUNTDOWN','http://military.discovery.com/services/taxonomy/COMBAT%20COUNTDOWN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/combat-countdown.jpg')
        main.addDir('COMBAT TECH','http://military.discovery.com/services/taxonomy/COMBAT%20TECH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/combat-tech-130.jpg')
        main.addDir('COMMANDER IN CHIEF','http://military.discovery.com/services/taxonomy/COMMANDER%20IN%20CHIEF/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/commanderinchief.jpg')
        main.addDir('GREAT PLANES','http://military.discovery.com/services/taxonomy/GREAT%20PLANES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/great-planes.jpg')
        main.addDir('GREATEST TANK BATTLES','http://military.discovery.com/services/taxonomy/GREATEST%20TANK%20BATTLES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/greatest-tank-battles.jpg')
        main.addDir('RETURN SALUTE','http://military.discovery.com/services/taxonomy/RETURN%20SALUTE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/returnsalute.jpg')
        main.addDir('SECRETS OF','http://military.discovery.com/services/taxonomy/SECRETS%20OF/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/secrets-of.jpg')
        main.addDir('TOP SECRET WEAPONS REVEALED','http://military.discovery.com/services/taxonomy/TOP%20SECRET%20WEAPONS%20REVEALED/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/top-secret-weapons-revealed.jpg')
        main.addDir('TRIGGERS','http://military.discovery.com/services/taxonomy/TRIGGERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/triggers.jpg')
        main.addDir('ULTIMATE WARFARE','http://military.discovery.com/services/taxonomy/ULTIMATE%20WARFARE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/ultimate-warfare.jpg')
        main.addDir('ULTIMATE WEAPONS','http://military.discovery.com/services/taxonomy/ULTIMATE%20WEAPONS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/ultimate-weapons.jpg')
        main.addDir('WARPLANE','http://military.discovery.com/services/taxonomy/WARPLANE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mc-show-thumb-warplane-130x97.jpg')
        main.addDir('WORLD WAR II IN COLOR','http://military.discovery.com/services/taxonomy/WORLD%20WAR%20II%20IN%20COLOR/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/mc-show-thumb-ww2-color-130x97.jpg')        
        main.GA("Adventure","Military")
        main.VIEWSB()

def SCI():
        main.addDir('AN IDIOT ABROAD','http://science.discovery.com/services/taxonomy/AN%20IDIOT%20ABROAD%20VIDEOS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/anidiotabroad_badge_130x97_v2.jpg')
        main.addDir('ARE WE ALONE','http://science.discovery.com/services/taxonomy/ARE%20WE%20ALONE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_are-we-alone.jpg')
        main.addDir('BIG BIGGER BIGGEST','http://science.discovery.com/services/taxonomy/BIG%20BIGGER%20BIGGEST/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/bigbiggerbiggest-130x97.jpg')
        main.addDir('BUILD IT BIGGER','http://science.discovery.com/services/taxonomy/BUILD%20IT%20BIGGER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/builditbigger-130x97.jpg')
        main.addDir('DARK MATTERS: TWISTED BUT TRUE','http://science.discovery.com/services/taxonomy/DARK%20MATTERS:%20TWISTED%20BUT%20TRUE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_dark-matters.jpg')
        main.addDir('FIREFLY','http://science.discovery.com/services/taxonomy/FIREFLY/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_firefly.jpg')
        main.addDir('FRINGE','http://science.discovery.com/services/taxonomy/FRINGE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/fringe-130x97.jpg')
        main.addDir('HEAD RUSH','http://science.discovery.com/services/taxonomy/HEAD%20RUSH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/headrush.jpg')
        main.addDir('HOW DO THEY DO IT','http://science.discovery.com/services/taxonomy/HOW%20DO%20THEY%20DO%20IT/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/how-do-they-do-it-130x97.jpg')
        main.addDir('HOW THE UNIVERSE WORKS','http://science.discovery.com/services/taxonomy/HOW%20THE%20UNIVERSE%20WORKS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/htuw-fixed-130x97.jpg')
        main.addDir("HOW IT'S MADE","http://science.discovery.com/services/taxonomy/HOW%20IT'S%20MADE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/howitsmade.jpg')
        main.addDir('KILLER ROBOTS','http://science.discovery.com/services/taxonomy/KILLER%20ROBOTS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/killer_robots-130x97.jpg')
        main.addDir('LDRS','http://science.discovery.com/services/taxonomy/LDRS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/ldrs-130x97.jpg')
        main.addDir('MONSTER BUG WARS','http://science.discovery.com/services/taxonomy/MONSTER%20BUG%20WARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/2monsterbugwars-130x97.jpg')
        main.addDir('MUTANT PLANET','http://science.discovery.com/services/taxonomy/MUTANT%20PLANET/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_mutant-planet.jpg')        
        main.addDir('ODDITIES','http://science.discovery.com/services/taxonomy/ODDITIES/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_oddities.jpg')
        main.addDir('ODDITIES SAN FRANCISCO','http://science.discovery.com/services/taxonomy/ODDITIES%20SAN%20FRANCISCO/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_odditiessf.jpg')
        main.addDir('PROPHETS OF SCIENCE FICTION','http://science.discovery.com/services/taxonomy/PROPHETS%20OF%20SCIENCE%20FICTION/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_prophets-of-scifi.jpg')
        main.addDir('PUNKIN CHUNKIN','http://science.discovery.com/services/taxonomy/PUNKIN%20CHUNKIN/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/punkin-chunkin-show-carousel-badge.jpg')
        main.addDir('SCI FI SCIENCE','http://science.discovery.com/services/taxonomy/SCI%20FI%20SCIENCE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sci-fi-sci-130x97.jpg')
        main.addDir("STEPHEN HAWKING'S SCI FI MASTERS","http://science.discovery.com/services/taxonomy/STEPHEN%20HAWKING'S%20SCI%20FI%20MASTERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/sc-showbadge_scifi-masters.jpg')
        main.addDir('STRIP THE CITY','http://science.discovery.com/services/taxonomy/STRIP%20THE%20CITY/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/strip-the-city-130x97.jpg')
        main.addDir('STUCK WITH HACKETT','http://science.discovery.com/services/taxonomy/STUCK%20WITH%20HACKETT/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/stuckwithhacket-130x97.jpg')
        main.addDir('STUFF YOU SHOULD KNOW','http://science.discovery.com/services/taxonomy/STUFF%20YOU%20SHOULD%20KNOW%20VIDEOS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sysk-badge-130x97.jpg')
        main.addDir('THROUGH THE WORMHOLE','http://science.discovery.com/services/taxonomy/THROUGH%20THE%20WORMHOLE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/sc-showbadge_wormhole.jpg')
        main.addDir('TREK NATION','http://science.discovery.com/services/taxonomy/TREK%20NATION/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/trek-nation-130x97.jpg')
        main.addDir('WONDERS WITH BRIAN COX','http://science.discovery.com/services/taxonomy/WONDERS%20WITH%20BRIAN%20COX/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/wonders-brian-cox-130.jpg')        
        main.GA("Adventure","Science")
        main.VIEWSB()

def VELO():
        main.addDir('ALL GIRLS GARAGE','http://velocity.discovery.com/services/taxonomy/ALL%20GIRLS%20GARAGE/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-all-girls-garage.jpg')
        main.addDir('CAR FIX','http://velocity.discovery.com/services/taxonomy/CAR%20FIX/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-carfix.jpg')
        main.addDir('CAFE RACER','http://velocity.discovery.com/services/taxonomy/CAFE%20RACER/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-cafe-racer.jpg')
        main.addDir('CHASING CLASSIC CARS','http://velocity.discovery.com/services/taxonomy/CHASING%20CLASSIC%20CARS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-chasing-classic-cars.jpg')
        main.addDir('EXTREME FISHING','http://velocity.discovery.com/services/taxonomy/EXTREME%20FISHING/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/extreme-fishing-130x97.jpg')
        main.addDir('FIFTH GEAR','http://velocity.discovery.com/services/taxonomy/FIFTH%20GEAR/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/fifth-gear-130x97.jpg')
        main.addDir('INSIDE WEST COAST CUSTOMS','http://velocity.discovery.com/services/taxonomy/INSIDE%20WEST%20COAST%20CUSTOMS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-iwcc.jpg')
        main.addDir('MECUM AUTO AUCTIONS','http://velocity.discovery.com/services/taxonomy/MECUM%20AUTO%20AUCTIONS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-mecum-auctions.jpg')
        main.addDir('ONE OF A KIND','http://velocity.discovery.com/services/taxonomy/ONE%20OF%20A%20KIND/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-one-of-a-kind.jpg')
        main.addDir("OVERHAULIN'","http://velocity.discovery.com/services/taxonomy/OVERHAULIN'/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video",64,'http://static.ddmcdn.com/gif/badge-overhaulin.jpg')
        main.addDir("WHAT'S MY CAR WORTH?",'http://velocity.discovery.com/services/taxonomy/WHATS%20MY%20CAR%20WORTH/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-whats-my-car-worth.jpg')
        main.addDir('WHEELER DEALERS','http://velocity.discovery.com/services/taxonomy/WHEELER%20DEALERS/?num=200&page=0&filter=clip%2Cplaylist%2Cfullepisode&tpl=dds%2Fmodules%2Fvideo%2Fall_assets_grid.html&sort=date&order=desc&feedGroup=video',64,'http://static.ddmcdn.com/gif/badge-wheeler-dealers.jpg')
        main.GA("Adventure","Velocity")
        main.VIEWSB()

def LISTDISC(mname,murl):
        thumbList=[]
        link=main.OPENURL(murl)
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
                main.addPlay(name+'  [COLOR blue]'+view+'[/COLOR]',url,65,thumbList[i])
                i=i+1
        main.GA("Discovery",mname+"-list")

def LINKDISC(name,url):
       
        idlist1=[]
        idlist2=[]
        idlist3=[]
        qualitylist=[]
        ETitleList=[]
        thumbList=[]
        plotList=[]
        #main.GA("Discovery","Watched")
        MainUrl= 'http://dsc.discovery.com'
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        url = MainUrl+url
        xbmc.executebuiltin("XBMC.Notification([B]Please Wait![/B],Playing Link,10000)")
        link=main.OPENURL(url)
        ok=True
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
        main.GA("Discovery-"+mtitle,"Watching")
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
        return ok
