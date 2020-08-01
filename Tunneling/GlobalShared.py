# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:53:34 2020

@author: usuari
"""

import numpy as np
import random

prob = 1.0
bonus = 1.0

#també escrivim la matriu d'amplades en aquest document
list_amp = np.zeros(10)
for i in range(0,10):
    list_amp[i] = 0.2 + i*0.1
    
#construim la matriu d'amplades de les barreres verticals
barr_vert = np.zeros((10,9,3))
barr_hor = np.zeros((9,10,3))

for i in range(0,10):
    for j in range(0,9):
        for k in range(0,3):
            barr_vert[i,j,k] = random.choice(list_amp)
        
for i in range(0,9):
    for j in range(0,10):
        for k in range(0,3):
            barr_hor[i,j,k] = random.choice(list_amp)


            
#creem vectors amb les possibles posicions x i y de les particules per poder 
#situar els bonus

inrect = 50.0
finrect = 410.0
interval = 90.0

posicions_x = np.arange(inrect,finrect + interval,interval)
posicions_y = np.arange(inrect,finrect + interval,interval)

#seleccionem cinc posicions random dins d'aquests vectors
vales_x = np.zeros(5)
vales_y = np.zeros(5)

for i in range(0,5):
    vales_x[i] = random.choice(posicions_x) + 45.0
    vales_y[i] = random.choice(posicions_y) + 45.0
    
#1:alçada
#2:moment inicial
#3:forma de la barrera
#4:bonus
tauler = [1,2]

caselles_tauler = np.ones((5,5))

for i in range(0,5):
   for j in range(0,5):
        caselles_tauler[i,j] = random.choice(tauler)






        