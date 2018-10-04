# -*- coding: utf-8 -*-
__author__ = "Negro"


# BeautifulSoup: libreria que rastrea la web haciendo find de html y parseandolo(documentacion)
from bs4 import BeautifulSoup
# Requests: libreria que realiza los calls con sus opciones (ver documentacion)

import connection
# Importamos nuestras librerias de apoyo (ver utils.py)
# import utils


class scrapper ():

    def __init__(self,URL):
        self.URL=URL

    
    def GetResponse(self):
        response=connection.getwithoutAuth(URL)
        statuscode=connection.statuscode(URL)
        return response
        
        """if statuscode == 200:
            return response
        elif statuscode == 400:
            print("Bad Request con Status Code %d" % statuscode)
        elif statuscode == 401:
            print("Unauthorized con Status Code %d" % statuscode)
        elif statuscode == 403:
            print("Forbidden con Status Code %d" % statuscode)
        elif statuscode == 404:
            print("Not Found con Status Code %d" % statuscode)
        else:
            print("Server unavaiability")"""

    def ParserRentByPrice(self,response):
        soup=BeautifulSoup(response,"lxml")
        byPrice=soup.find_all("item-price h2-simulated")
        return byPrice
        
        
"""html = BeautifulSoup(rget.text, "html.parser")

    # Obtenemos todos los divs donde están las entradas
    entradas = html.find_all('div', {'class': 'col-md-4 col-xs-12'})

    # Recorremos todas las entradas para extraer el título, autor y fecha
    for i, entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
        titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
        # Sino llamamos al método "getText()" nos devuelve también el HTML
        autor = entrada.find('span', {'class': 'autor'})
        fecha = entrada.find('span', {'class': 'fecha'}).getText()

        # Imprimo el Título, Autor y Fecha de las entradas
        print("%d - %s  |  %s  |  %s" % (i + 1, titulo, autor, fecha))"""





URL="https://www.idealista.com/areas/alquiler-viviendas/con-precio-hasta_1100,chalets,casas-de-pueblo,duplex,publicado_ultimas-24-horas/?shape=%28%28ogz%7CFmvuGidtAiztDxzmBg%7BfA%7BeBrcA%7Cz_AtxbEqjvAfxv%40%29%29&ordenado-por=fecha-publicacion-desc"
d=scrapper(URL)
b=d.GetResponse()
a=d.ParserRentByPrice(b)
c=connection.statuscode(URL)
print (str(c))