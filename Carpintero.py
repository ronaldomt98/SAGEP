# -*- coding: utf-8 -*-
# !/usr/bin/python
from abc import ABCMeta, abstractmethod
from persistent import *
from .Empleado import Empleado

#...................................CLASE CARPINTERO..........................................
'''CLASE QUE HEREDA DE Empleado'''
class Empleado(Empleado, Persistent):
   
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def fabricar_mueble(self, bien, cantidad):
		pass

   
	def __str__(self):
		return (super().__str__()+'\nRUC: '+self.ruc+'\nMuebles:\n'+str(self.muebles))
		
		
