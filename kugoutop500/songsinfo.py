# coding: utf-8

class SongsInfo:
    def __init__(self):
        self.__songsinfo = []
        
    def add_info(self, info):
        if not info:
            return None
        self.__songsinfo.append(info)
        
    def add_infos(self, infos):
        if not infos:
            return
            
        for info in infos:
            self.add_info(info)
            
            
    def get_infos(self):
        return self.__songsinfo
        