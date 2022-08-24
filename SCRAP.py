from asyncore import read
from cgitb import html
import csv
from ctypes.wintypes import HLOCAL
from dataclasses import replace
from distutils.log import info
from faulthandler import cancel_dump_traceback_later
from ntpath import altsep
from os import remove
from posixpath import split
from pyexpat import model
from this import d
from threading import local
from unittest import result
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

df = pd.read_excel('DOMINIOS2022.xlsx')
dfd = pd.DataFrame(columns=['DOMINIOS','TIPO_DOCUMENTO','NRO_DOCUMENTO','NRO_CUIT','PROPIETARIO_APELLIDO','PROPIETARIO_NOMBRE','FECHA_TITULARIDAD','CALLE','NUMERO','PISO','DPTO','CP','LOCALIDAD','PROVINCIA','TELEFONO','CELULAR','EMAIL','MARCA','MODELO','TIPO','PARTIDO'])

dominios = df['DOMINIO']
dominios_list = dominios.tolist()

for dominio in dominios_list:
    print(f'{dominio}')
    url = f'http://74.63.195.38/secu.aspx?patente={dominio}'
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    span = soup.find_all('span')
    #print(span)
    lista_span = []
    for i in span:
        lista_span.append(i.text.split('"'))
    print ( lista_span )

    #print(lista_span)
    
    # data=[]
    # for i in span:
    #     data.extend(i.text.split('\n'))
    #     data1= i.text
    #     data2= data1.split(',')
        
    #     dominio = data2[2]
    #     doctiype = data2[9]
    #     nro_doc = data2[10]
    #     nro_cuit = data2[11]
    #     propietario_apell = data2[12]
    #     propietario_nom = data2[13]
    #     fecha_titu = data2[14]
    #     calle = data2[15]
    #     numero = data2[16]
    #     piso = data2[17]
    #     dpto = data2[18]
    #     cp = data2[19]
    #     localidad = data2[20]
    #     provincia = data2[21]
    #     telefono = data2[22]
    #     celular = data2[23]
    #     email = data2[24]
    #     marca = data2[25]
    #     modelo = data2[26]
    #     tipo = data2[27]
    #     partido = data2[28]
    
    #     print(dominio)
    #     print(doctiype)
    #     print(nro_doc)
    #     print(nro_cuit)
    #     print(propietario_apell)
    #     print(propietario_nom)
    #     print(fecha_titu)
    #     print(calle)
    #     print(numero)
    #     print(piso)
    #     print(dpto)
    #     print(cp)
    #     print(localidad)
    #     print(provincia)
    #     print(telefono)
    #     print(celular)
    #     print(email)
    #     print(marca)
    #     print(modelo)        
    #     print(partido)
