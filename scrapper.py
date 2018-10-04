# -*- coding: utf-8 -*-
__author__ = "Negro"


# BeautifulSoup: libreria que rastrea la web haciendo find de html y parseandolo(documentacion)
from bs4 import BeautifulSoup


# Creamos un "soup" para parsear HTML con el parseador "lxml"
soup=BeautifulSoup(GetResponse,"lxml")
