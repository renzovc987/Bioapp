#!/usr/bin/env python
import numpy as np
import math
import sys
import array
import numpy
from ete3 import Tree,PhyloTree, TreeStyle
import sys    
import os
from io import StringIO
from Bio import Phylo
import matplotlib.pyplot as plt



mapeo = { 'A':0, 'C':1, 'G':2, 'T':3}

f=open("leer.txt","w")

allineaciones = []

def get_caminos (cadena1, cadena2, pos_x, pos_y, matrix_similitud, matrix_matching, costo, grupos):
  if pos_x + pos_y == 0:
    allineaciones.append(grupos)
    return
  else:
    salida1 = matrix_matching[pos_y-1, pos_x-1] + matrix_similitud[mapeo[cadena1[pos_x-1]], mapeo[cadena2[pos_y-1]]] if pos_x-1 >=0 and pos_y-1 >=0 else -100000
    salida2 = matrix_matching[pos_y, pos_x-1] + costo if pos_x-1 >=0 else -100000
    salida3 = matrix_matching[pos_y-1, pos_x ] + costo if pos_y-1 >= 0 else -100000
    # Verificar posX y posY ya que cadenas depende de ello
    

    if salida1 == matrix_matching[pos_y, pos_x]:
      helper = grupos[:]
      helper[0] += cadena1[pos_x-1]
      helper[1] += cadena2[pos_y-1]
      get_caminos(cadena1, cadena2, pos_x-1, pos_y-1, matrix_similitud, matrix_matching, costo, helper)

    
    if salida2 == matrix_matching[pos_y, pos_x]:
      helper1 = grupos[:]
      helper1[0] += cadena1[pos_x-1]
      helper1[1] += "-"
      get_caminos(cadena1, cadena2, pos_x-1, pos_y, matrix_similitud, matrix_matching, costo, helper1)

    if salida3 == matrix_matching[pos_y, pos_x]:
      helper2 = grupos[:]
      helper2[0] += "-"
      helper2[1] += cadena2[pos_y-1]
      get_caminos(cadena1, cadena2, pos_x, pos_y-1, matrix_similitud, matrix_matching, costo, helper2)

def solution_global(cadena1, cadena2, matrix_similitud, costo):
  tam_cadena1 = len(cadena1)
  tam_cadena2 = len(cadena2)
  
  matriz_matching = np.zeros((tam_cadena2 + 1, tam_cadena1 + 1))
  for i in range(1, tam_cadena1+1):
    matriz_matching[0, i] = matriz_matching[0, i-1]  + costo

  for i in range(1, tam_cadena2+1):
    matriz_matching[i, 0] = matriz_matching[i-1, 0]  + costo

 
  for i in range(1, tam_cadena2 + 1):
    for j in range(1, tam_cadena1 + 1):
      matriz_matching[i,j] = max(matriz_matching[i-1, j-1] + matrix_similitud[mapeo[cadena1[j-1]], mapeo[cadena2[i-1]]], matriz_matching[i-1, j] + costo, matriz_matching[i, j-1] + costo)
  
  return matriz_matching

secuencia1 = sys.argv[1]
secuencia2 = sys.argv[2]
costo = sys.argv[3]
costo = int(costo)
dist = sys.argv[4]
tree = sys.argv[5]


#########AG1############

l=len(secuencia1)
num_match = num_mismatch = 0 
for i in range (0,l):
	if secuencia1[i] == secuencia2[i]:
		num_match += 1    
	else:
		num_mismatch += 1
# print("proportion between mismatches and length of sequence" )
D=(num_mismatch/l)
# Usamos D para determinar K, distancia molecular, usando Jukes-cantor model 
#K es el total del numero de susituciones divididos por el numero total de nucleotidos alineados
B = D
K =((-3/4)*math.log((1-(B*(4/3))))) 

######################

##########AG2############
def K2Pdistance(seq1,seq2):
    ###Kimura distancia = -0.5 log( (1 - 2p -q) * sqrt( 1 - 2q ) )
    ###Donde:
    ####p = Frecuencia de transicion
    ####q = Frecuencia de transversion
    from math import log, sqrt
    pairs = []

    #Hace caso omiso si la secuencia presenta un guion (-)
    for x in zip(seq1,seq2):
        if '-' not in x: pairs.append(x)
        
    ts_count=0
    tv_count=0
    length = len(pairs)
    
    transitions = [ "AG", "GA", "CT", "TC"]
    transversions = [ "AC", "CA", "AT", "TA",
                      "GC", "CG", "GT", "TG" ]

    for (x,y) in pairs:
        if x+y in transitions: ts_count += 1 
        elif x+y in transversions: tv_count += 1
    
    p = float(ts_count) / length
    q = float(tv_count) / length
    try: d = -0.5 * log( (1 - 2*p - q) * sqrt( 1 - 2*q ) )
    except ValueError: 
        print("Intente tomar el log de un numero negativo")
        return None
    return d

res_dist2 = K2Pdistance(secuencia1,secuencia2)
#########################


matrix_similitud = np.matrix(([[2, -7, -5, -7], [-7, 2, -7, -5], [-5, -7, 2, -7], [-7, -5, -7, 2]]))
print("Matriz de similitud")
print(matrix_similitud)

print("Matriz DP")
answer = solution_global(secuencia1, secuencia2, matrix_similitud, costo)
print(answer)

allineaciones = []

print("Alineaciones")
get_caminos (secuencia1, secuencia2, len(secuencia1), len(secuencia2), matrix_similitud, answer, costo, ["", ""])
for val in allineaciones:
  print(str(val[0][::-1]) + " " + str(val[1][::-1]))
print("Score")
print(answer[3][3])


if dist=="ag1":
  g=open("dis.txt","w")
  for i in range (0 , 2):
    for j in range (0,2):
      if(i==j):
        g.write(str(0)+' ')
      else:
        g.write(str(K)+' ')
    g.write('\n')
  g.close() 
  
else:
  g=open("dis.txt","w")
  for i in range (0 , 2):
    for j in range (0,2):
      if(i==j):
        g.write(str(0)+' ')
      else:
        g.write(str(res_dist2)+' ')
    g.write('\n')
  g.close() 







f.write("------- RESULTADO DEL ALINEAMIENTO ---------\n")

f.write("Las secuencias son \n")
f.write("Sec1: " +str(secuencia1) +"\n")
f.write("Sec1: " +str(secuencia2) +"\n")
f.write("----------------------------------\n")

#for i in (matrix_similitud):
#  f.write(str(i)+'\n')
f.write("----------------------------------\n")

for i in (answer):
  f.write(str(i)+'\n')
f.write("----------------------------------\n")

for val in allineaciones:
  f.write(str(val[0][::-1]) + " " + str(val[1][::-1]+'\n'))

#f.write('asd = '+ str(answer[3][3]))

f.write("----------------------------------\n")


#f.write("algo-dist:::::::"+str(dist)+'\n')

if dist=="ag1":
  f.write("numero de coincidencias: "+str(num_match)+"\n")
  f.write("numero de inconsistencias: "+ str(num_mismatch)+"\n")
  f.write("La distancia molecular entre ambas secuencias, K, es: "+ str(K)+"\n")
else:
  if res_dist2==None:
    f.write("Intente tomar el log de un numero negativo\n")
  else:
    f.write("La distancia molecular entre ambas secuencias es: "+ str(res_dist2)+"\n")

f.write("----------------------------------\n")



f.close()
