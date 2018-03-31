# coding: utf-8
from bs4 import BeautifulSoup

class HtmlParser:
    def parser_list(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        lists = soup.find_all('div', class_='listItem')
        if not lists:
            return None
        urls = []    
        for list in lists:
            link = list.find('a')
            if not link:
                continue
            url = link.get('href')
            urls.append(url)
            
        return urls
        
    def parser_song_list(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        rank_wrap = soup.find('div', id='rankWrap')
        if not rank_wrap:
            return None
            
        songlists = rank_wrap.find_all('li')
        if not songlists:
            return None
        
        urls = []
        for songlist in songlists:
            link = songlist.find('a')
            if not link:
                continue
            url = link.get('href')
            title = link.get('title')
            urls.append({'url': url, 'title': title})
            
        return urls
        