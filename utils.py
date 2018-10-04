#-*- coding: utf-8 -*-
__author__="Negro"

class Complejo:
     def __init__(self, partereal, parteimaginaria):
         self.r = partereal
         self.i = parteimaginaria
         int b=r+i

x = Complejo(3.0, -4.5)
print(x)


"""import requests
from requests import request, session

class MyAuth(requests.auth.AuthBase):
     def __call__(self, a,b):
        # Implement my authentication
         r=a+b
         return r

#requests.get(url, auth=MyAuth(a,b))"""


