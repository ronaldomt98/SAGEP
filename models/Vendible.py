from abc import ABCMeta, abstractmethod

class Vendible(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def vender():
        pass

    @abstractmethod
    def devolver():
        pass