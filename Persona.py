# -*- coding: utf-8 -*-
# !/usr/bin/python
from abc import ABCMeta, abstractmethod
from persistent import *

#......................CLASE PERSONA...............................
class Persona(ABC, Model):

	__metaclass__ = ABCMeta
   
	def __init__(self, nombre='', apellido='', cedula=0, direccion='No especificada', contactos=[]):
		self.nombre = nombre
		self.apellido = apellido
		self.cedula = cedula 
		self.direccion = direccion
		self.contacto = contactos
      
	'---Funciones que permiten obtener los atributos (getters)---'
   
	def obtener_nombre(self):
		return self.nombre
      
	def obtener_apellido(self):
		return self.apellido
   
	def obtener_cedula(self):
		return self.cedula
   
	def obtener_direccion(self):
		return self.direccion
   
	def obtener_contacto(self):
		return self.contactos
      
      
   
	def __str__(self):
		return ('\nNOMBRES Y APELLIDOS: '+self.nombre+' '+self.apellido+'\nCEDULA: '+str(self.cedula)
      +'\nDIRECCION: '+self.direccion+'\nCONTACTOS: '+self.contactos)

