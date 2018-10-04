# -*- coding: utf-8 -*-
__author__ = "Negro"

# Requests: libreria que realiza los calls con sus opciones (ver documentacion)
import requests
from requests import request, session
from requests.auth import HTTPBasicAuth
# Importamos nuestras librerias de apoyo (ver utils.py)

def getHeaders(URL):
    # Creamos la sesion para poder tener mas operabilidad (mirar documentacion)
    r = requests.Session()
    # Establecemos la URL el statuscode para hacer las calls
    hdrs = requests.get(URL).headers
    return hdrs

def getwithoutAuth(URL):
    # Cogemos los headers
    hdrs = getHeaders(URL)
    # Creamos la sesion para poder tener mas operabilidad (mirar documentacion)
    r = requests.Session()
    # Establecemos la URL el statuscode para hacer las calls
    rget = requests.get(URL,headers=hdrs)
    response = rget.content
    r.close()
    return response


def statuscode(URL):
    # Cogemos los headers
    hdrs = getHeaders(URL)
    
    # Creamos la sesion para poder tener mas operabilidad (mirar documentacion)
    r = requests.Session()
    # Establecemos la URL el statuscode para hacer las calls
    rget = requests.get(URL,headers=hdrs)
    statusCode = rget.status_code
    r.close()
    return statusCode
    






