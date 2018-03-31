# coding: utf-8

from htmldownloader import HtmlDownloader
from htmlparser import HtmlParser
from urlmanager import UrlManager
from songsinfo import SongsInfo
import requests
import re
import urllib.request
import os

class SpiderMan:
    def __init__(self, path):
        self.mp_dir = path
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.songsinfo = SongsInfo()
        
    def crawl(self, url):
        kugou_html = self.downloader.download_html(url)
        listitems = self.parser.parser_list(kugou_html)
        for listitem in listitems:
            sub_html = self.downloader.download_html(listitem)
            songs = self.parser.parser_song_list(sub_html)
            self.songsinfo.add_infos(songs)
            
        self._download_songs(self.songsinfo.get_infos())
    
    def parse_music_info(self, html):
        reg = re.compile(r'.*{"hash":"(.*)","timelength":.*"album_id":(\d+)}.*')
        song_info = reg.search(html)
        return song_info.group(1), song_info.group(2)
    
    def _download_songs(self, infos):
        for info in infos:
            url = info.get('url')
            title = info.get('title')
            mat = re.split(r'\s+-', title)
            title = mat[1] + ' - ' + mat[0]
            html = self.downloader.download_html(url)
            hash_id, album_id = self.parse_music_info(html)
            param = {
                'r':'play/getdata',
                'hash':hash_id,
                'album_id':album_id,
                '_':'1522500783388'
            }
            load_url = 'http://www.kugou.com/yy/index.php'
            resp = requests.get(load_url, params=param)
            song_info = resp.json()
            play_url = song_info.get('data').get('play_url')
            urllib.request.urlretrieve(play_url, self.mp_dir+title+'.mp3')

    
def main():
    mp_dir = 'mp3/'
    kugou_url = 'http://www.kugou.com/'
    
    try:
        os.mkdir(mp_dir)
    except FileExistsError:
        pass
    
    spider = SpiderMan(mp_dir)
    spider.crawl(kugou_url)

if __name__ == '__main__':
    main()