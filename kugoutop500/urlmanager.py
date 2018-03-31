# coding: utf-8

class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        
    def add_new_url(self, url):
        if not url or url in self.old_urls:
            return None
        self.new_urls.add(url)
        
    def add_new_urls(self, urls):
        if not urls:
            return
            
        for url in urls:
            self.add_new_url(url)
            
            
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
        