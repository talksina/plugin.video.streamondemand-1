# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canale Video Corsi Programmazione
# Creato da costaplus
# http://www.mimediacenter.info/foro/viewforum.php?f=36.
# ------------------------------------------------------------
import re

from core import config
from core import logger
from core import scrapertools
from core.item import Item

__channel__ = "programmazione"
__category__ = "D"
__type__ = "generic"
__title__ = "programmazione(IT)"
__language__ = "IT"

DEBUG = config.get_setting("debug")

site = "https://www.youtube.com"


def isGeneric():
    return True


def mainlist(item):
    logger.info("streamondemand.programmazione mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Html 5[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL7A4A3449C649048F", thumbnail="http://i.ytimg.com/vi/TyCvfNt20nM/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Css[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PLD74C5E763D39793D", thumbnail="http://i.ytimg.com/vi/hd8k82aG_O4/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Javascript[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL1A447BA7F7F9EB9E", thumbnail="http:////i.ytimg.com/vi/eXlzdxyThLM/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso PHP[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJc664i2Cv0X0ibM9b1YqRyd", thumbnail="http://i.ytimg.com/vi/0nA1gPWdBWw/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso PHP Mysql[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL101314D973955661", thumbnail="http://i.ytimg.com/vi/QIxmITjITY8/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Jquery[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PLC959BB22285B353F", thumbnail="http://i.ytimg.com/vi/mxl2IcNdbrk/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Java da Zero[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJe2dpE7di4aPJwrQuRD6IDD", thumbnail="http://i.ytimg.com/vi/7PGPLqFpDMc/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Java 2 OOP[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJee1dk24wX-68yHTnMfzdX5", thumbnail="http://i.ytimg.com/vi/h6VoxIAUZoo/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Java Interfaccia Grafica[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJfRML8EDs7v9nwjdOt6dvaf", thumbnail="http://i.ytimg.com/vi/fS7OxhbIlw4/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Java Android[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJeqmBWbE1Rbac2QWHoPCjR2", thumbnail="http://i.ytimg.com/vi/GINLfdq-elE/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Progettazione DB[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJcJPSV4sOfhLtPbtQ-yycFH", thumbnail="http://i.ytimg.com/vi/FnkL4YdWAwE/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso SQL[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PLE555DB6188C967AC", thumbnail="http://i.ytimg.com/vi/jM55Fb9YTfE/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Python[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PLC64779F4E2E7EB10", thumbnail="http://i.ytimg.com/vi/_iX9CSX09Z8/mqdefault.jpg"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Corso Unit 3D[/COLOR]", action="corsi", url="https://www.youtube.com/playlist?list=PL0qAPtx8YtJcbl6ZHwtFIkFxWY-adCeS7", thumbnail="http://i.ytimg.com/vi/QiFBrHp3IGk/mqdefault.jpg"))

    return itemlist


def corsi(item):
    logger.info("streamondemand.programmazione peliculas")
    itemlist = []

    # scarrico il canale
    html = scrapertools.cache_page(item.url)

    # Estraggo l'elenco dei video e titoli
    patron = '<a class="pl-video-title-link.*?href="(.*?)"[^>]+>(.*?)</a>'
    trovati = re.compile(patron, re.DOTALL).findall(html)
    scrapertools.printMatches(trovati)
    max = len(trovati)
    min = 0

    # ciclo sull'elenco trovato
    for VideoUrl, VideoTitolo in trovati:
        # Decodifico Html
        titolo = scrapertools.decodeHtmlentities(VideoTitolo)
        # contatore
        min += 1
        # aggiungo alla lista
        itemlist.append(
            Item(channel=__channel__,
                 action="findvideos",
                 fulltitle=titolo,
                 show=titolo,
                 title="[COLOR azure]" + item.title + " - " + str(min) + "x" + str(max) + "[/COLOR]",
                 url=site + VideoUrl,
                 thumbnail=item.thumbnail,
                 plot=titolo,
                 folder=True)
        )

    if max > 0:
        itemlist.append(
            Item(channel=__channel__,
                 action="HomePage",
                 title="[COLOR yellow]Torna Home[/COLOR]",
                 folder=True)),

    return itemlist


def HomePage(item):
    import xbmc
    xbmc.executebuiltin("ReplaceWindow(10024,plugin://plugin.video.streamondemand)")
