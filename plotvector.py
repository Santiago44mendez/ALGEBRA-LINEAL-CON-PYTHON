# -*- coding: utf-8 -*-
"""Copia de Modulo para la graficación de vectores.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1erLEWa_e2NdVo3uNdKIHKNOmXZn495Tu

<p><img alt="logo.fua" height="100px" src="https://www.uamerica.edu.co/wp-content/images/escudo.png" align="left" hspace="10px" vspace="0px"></p>

<p><img alt="logo.fua" height="26px" src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nd.svg" align="right" hspace="0px" vspace="11px"></p>


# <center> <font size="6"> &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp;**ÁLGEBRA LINEAL CON PYTHON &nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;     &nbsp; &nbsp;  &nbsp; MÓDULO PARA LA GRAFICACIÓN DE VECTORES** &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; <center> &nbsp; &nbsp; &nbsp; &nbsp;*Jhonny Osorio Gallego* &nbsp; &nbsp; &nbsp;<p></font>

El siguiente módulo esta diseñado haciendo uso de la librería **NumPy** y **Plotly**, pretende servir de apoyo para la representación gráfica de vectores en el plano y el espacio, como estratégia para la enseñanza de los concéptos vectoriales.

## **FUNCIÓN PARA GENERAR COLORES RGB ALEATORIAMENTE**
"""

import random 
def randomRgbaColor(): 
   r = random.randrange(0, 255) 
   g = random.randrange(0, 255)  
   b =random.randrange(0, 255)
   return "rgb"+ "(" + str(r) + "," + str(g) + ","+ str(b) + ")"

"""## **FUNCIÓN PARA GRAFICAR MULTIPLES VECTORES EN EL PLANO**"""

import plotly.graph_objects as go
import numpy as np


def plotvectors2D(*args):
    '''Función elaborada en el módulo plotly para realizar la gráfica de multiples vectores en el plano cartesiano'''
    
    fig = go.Figure()
    x = []
    y = []
    for V in args:
        color = randomRgbaColor()
        x.append(V[0])
        y.append(V[1])
        fig.add_trace(go.Scatter(x=[V[0]],y=[V[1]],mode='markers',marker=dict(color= color,size=1,),showlegend=False,name="vector "+ str(args.index(V)+1)))
        fig.add_annotation(
        x=V[0],  # Coordenada en x cabeza
        y=V[1],  # Coordenada en y cabeza
        ax=0,  # Coordenada en x de la cola
        ay=0,  # Coordenada en x de la cola
        xref='x',
        yref='y',
        axref='x',
        ayref='y',
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=2.3,
        arrowcolor = color)
        
      
    fig.add_trace(go.Scatter(x=[0],y=[0],mode='markers',marker=dict(color="gray",size=11.5),showlegend=False,opacity=1,name="origen"))
    fig.update_xaxes(title = "$\large{x}$", title_font=dict(size=30, family='latex', color='rgb(1,21,51)'),zerolinecolor="black",autorange = True,showgrid = True) 
    fig.update_yaxes(title = "$\large{y}$", title_font=dict(size=30, family='latex', color='rgb(1,21,51)'), zerolinecolor= "black",autorange = True,showgrid = True) 
    fig.update_layout(font=dict(family="latex",size=20,color="black"))
    #fig.update_layout(title= "",title_font=dict(size=5, family='latex', color='rgb(1,21,51)'),title_x=0.5)
    fig.update_layout(showlegend=False,width=460, height=460)
    fig.show()
