import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()
    
    def dump(self):
        pickle.dump(self.__cache, open(self.__datasource, "wb"))
    
    def load(self):
        self.__cache = pickle.load(open(self.__datasource, "rb"))

    def add(self, key, obj):
        if isinstance(key, int):
            self.__cache[key] = obj
            self.dump()
    
    def get(self, key):
        if isinstance(key, int):    
            try:
                return self.__cache[key]
            except KeyError:
                pass
    
    def remove(self, key):
        if isinstance(key, int):  
            try:
                self.__cache.pop(key)
                self.dump()
            except KeyError:
                pass
    
    def get_all(self):
        return_list = []
        for i in self.__cache:
            return_list.append(self.__cache[i])
        return return_list