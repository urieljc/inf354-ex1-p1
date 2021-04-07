# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:42:26 2021

@author: BazanJuanCarlos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



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

print("Graficas del Dataset")

suicidio_df=pd.DataFrame(suicidio)
suicidio_df.suicides_no.plot.hist()
plt.show()

suicidio_df.plot.scatter(x="suicides_no", y="population", alpha=0.2)
plt.show()


suicidio_por_pais=suicidio_df.groupby("country")["suicides_no"].mean()
suicidio_por_pais.head(30).plot.barh()


tiempo=suicidio_df["year"].unique()
cantidad=suicidio_df["suicides_no"]

sui_plot=pd.DataFrame({'cantidad':cantidad},index=tiempo)
sui_plot.plot(kind='bar')


print(set( suicidio_df.sex))
colores={"male":"Crimson","female":"RoyalBlue"}
suicid_color=suicidio_df.sex.map(colores)
fig, ax=plt.subplots()
for sexo in set(suicidio_df.sex):
    ax.scatter(
        suicidio_df.suicides_no[suicidio_df.sex==sexo],
        suicidio_df.age[suicidio_df.sex==sexo],
        s=30,
        c=colores[sexo],
        label=sexo)
plt.legend()
plt.show()