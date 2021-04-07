# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:13:35 2021

@author: BazanJuanCarlos
"""

import pandas as pd
import statistics as stat
import numpy as np
from math import sqrt


suicidio=pd.read_csv("master.csv")
print(suicidio.head()) 
print("____________________________________________")

print('numeros de columnas que posee el data frame')
print(len(suicidio.columns)) 
print("____________________________________________")
print('numeros de filas que posee el data frame')
print(len(suicidio.index)) 
print("____________________________________________")
print("tipos de datos que posee el dataset")
print(suicidio.dtypes) 
print("____________________________________________")
print(" Pregunta 1 Inciso A y B")
#convertir las columnas a array
array1=suicidio[['country']].to_numpy()
array2=suicidio[['year']].to_numpy()
#array3=suicidio[['sex']].to_numpy()
array3=np.array(suicidio['sex'])

array4=suicidio[['age']].to_numpy()
#array5=suicidio['suicides_no'].to_numpy()
array5=np.array(suicidio['suicides_no'])
#array5=array5.astype(int)
#array6=suicidio[['population']].to_numpy()
array6=np.array(suicidio['population'])

#array7=suicidio[['suicides/100k pop']].to_numpy()
array7=np.array(suicidio['suicides/100k pop'])

array8=suicidio[['country-year']].to_numpy()
array9=suicidio[['HDI for year']].to_numpy()
#array10=suicidio[[' gdp_for_year ($)']].to_numpy()
array11=suicidio[['gdp_per_capita ($)']].to_numpy()
array12=suicidio[['generation']].to_numpy()
#creando la funcion para la media suicides_no
dOrder=sorted(array5)
n=len(dOrder)
medio=n/2
print("____________________________________________")
print("calculo de la tabla Numero de Suicidios")
print("____________________________________________")
print("media sin uso de librerias ")
print(sum(array5)/n)
print("____________________________________________")
print("media con e uso de librerias")
media=array5.mean()
print(media)
print("____________________________________________")
l=list(array5)
repetir=0
for i in l:
    #aparece=array5.count(i)
    aparece = l.count(i)
    if aparece > repetir:
        repetir=aparece
moda=[]
for i in l:
    aparece=l.count(i)
    if aparece==repetir and i not in moda:
        moda.append(i)

print("imprimimos la moda si librrias")
print(moda)
print("____________________________________________")
print("moda con el uso de librerias")
moda=stat.mode(array5)
print(moda)

#desviacion standar
suma=0
radicando=0
for valor in l:
    suma +=(valor-media)**2
radicando=suma/(len(l)-1)
vs=sqrt(radicando)
print("____________________________________________")
print("variacon estandar sin el uso de librerias")
print(vs)
print("____________________________________________")
print("variacon estandar con el uso de librerias")
ds=stat.pstdev(array5)
print(ds)
print("____________________________________________")
print("____________________________________________")
print("____________________________________________")

#creando la funcion para la media population
dOrder=sorted(array6)
n=len(dOrder)
medio=n/2
print("____________________________________________")
print("calculo de la tabla Poblacion")
print("____________________________________________")
print("media sin uso de librerias ")
print(sum(array6)/n)
print("____________________________________________")
print("media con e uso de librerias")
media=array6.mean()
print(media)
print("____________________________________________")
l=list(array6)
repetir=0
for i in l:
    #aparece=array5.count(i)
    aparece = l.count(i)
    if aparece > repetir:
        repetir=aparece
moda=[]
for i in l:
    aparece=l.count(i)
    if aparece==repetir and i not in moda:
        moda.append(i)

print("imprimimos la moda si librrias")
print(moda)
print("____________________________________________")
print("moda con el uso de librerias")
moda=stat.mode(array6)
print(moda)

#desviacion standar
suma=0
radicando=0
for valor in l:
    suma +=(valor-media)**2
radicando=suma/(len(l)-1)
vs=sqrt(radicando)
print("____________________________________________")
print("variacon estandar sin el uso de librerias")
print(vs)
print("____________________________________________")
print("variacion estandar con el uso de librerias")
ds=stat.pstdev(array6)
print(ds)
print("____________________________________________")
print("____________________________________________")
print("____________________________________________")

#creando la funcion para la media population
dOrder=sorted(array6)
n=len(dOrder)
medio=n/2
print("____________________________________________")
print("calculo de la tabla Poblacion")
print("____________________________________________")
print("media sin uso de librerias ")
print(sum(array6)/n)
print("____________________________________________")
print("media con e uso de librerias")
media=array6.mean()
print(media)
print("____________________________________________")
l=list(array6)
repetir=0
for i in l:
    #aparece=array5.count(i)
    aparece = l.count(i)
    if aparece > repetir:
        repetir=aparece
moda=[]
for i in l:
    aparece=l.count(i)
    if aparece==repetir and i not in moda:
        moda.append(i)

print("imprimimos la moda si librrias")
print(moda)
print("____________________________________________")
print("moda con el uso de librerias")
moda=stat.mode(array6)
print(moda)

#desviacion standar
suma=0
radicando=0
for valor in l:
    suma +=(valor-media)**2
radicando=suma/(len(l)-1)
vs=sqrt(radicando)
print("____________________________________________")
print("variacon estandar sin el uso de librerias")
print(vs)
print("____________________________________________")
print("variacion estandar con el uso de librerias")
ds=stat.pstdev(array6)
print(ds)
print("____________________________________________")
print("____________________________________________")
print("____________________________________________")

#creando la funcion para la poblacioon/100k
dOrder=sorted(array7)
n=len(dOrder)
medio=n/2
print("____________________________________________")
print("calculo de la tabla poblacion/100k")
print("____________________________________________")
print("media sin uso de librerias ")
print(sum(array7)/n)
print("____________________________________________")
print("media con e uso de librerias")
media=array7.mean()
print(media)
print("____________________________________________")
l=list(array7)
repetir=0
for i in l:
    #aparece=array5.count(i)
    aparece = l.count(i)
    if aparece > repetir:
        repetir=aparece
moda=[]
for i in l:
    aparece=l.count(i)
    if aparece==repetir and i not in moda:
        moda.append(i)

print("imprimimos la moda si librrias")
print(moda)
print("____________________________________________")
print("moda con el uso de librerias")
moda=stat.mode(array7)
print(moda)

#desviacion standar
suma=0
radicando=0
for valor in l:
    suma +=(valor-media)**2
radicando=suma/(len(l)-1)
vs=sqrt(radicando)
print("____________________________________________")
print("variacon estandar sin el uso de librerias")
print(vs)
print("____________________________________________")
print("variacion estandar con el uso de librerias")
ds=stat.pstdev(array7)
print(ds)
print("____________________________________________")
print("____________________________________________")
print("____________________________________________")
print(suicidio.describe())