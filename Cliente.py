# -*- coding: utf-8 -*-
# !/usr/bin/python
from abc import ABCMeta, abstractmethod
from persistent import *
from .Persona import Persona

#...................................CLASE CLIENTE..........................................
'''CASE QUE HEREDA DE Persona '''
class Cliente(Persona, Persistent):

	def __init__(self,ruc='Ninguno', muebles=None, **kwargs):
		super().__init__(**kwargs)
		self.ruc=ruc
		self.muebles=muebles

	def obtener_ruc(self):
		return self.ruc
		
	def comprar(self, bien, cantidad):
		pass

   
	def __str__(self):
		return (super().__str__()+'\nRUC: '+self.ruc+'\nMuebles:\n'+str(self.muebles))
      

