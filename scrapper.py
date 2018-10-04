# -*- coding: utf-8 -*-
__author__ = "Negro"


# BeautifulSoup: libreria que rastrea la web haciendo find de html y parseandolo(documentacion)
from bs4 import BeautifulSoup
import connection


# Creamos un "soup" para parsear HTML con el parseador "lxml"
URL="https://www.idealista.com/areas/alquiler-viviendas/con-precio-hasta_1100,chalets,casas-de-pueblo,duplex,publicado_ultimas-24-horas/?shape=%28%28ogz%7CFmvuGidtAiztDxzmBg%7BfA%7BeBrcA%7Cz_AtxbEqjvAfxv%40%29%29&ordenado-por=fecha-publicacion-desc"
get=connection.getwithoutAuth(URL)
soupBody=BeautifulSoup(get,"lxml")
findByClass=soupBody.find_all("span", class_="item-price h2-simulated")
findParents=soupBody.findChildren("span")


for i in findByClass:
    
    print(str(i))





