#!/usr/bin/env python
import numpy as np
import math
from Bio import SeqIO
import sys
import array
from ete3 import Tree,PhyloTree, TreeStyle
import sys    
import os
from io import StringIO
from Bio import Phylo
import matplotlib.pyplot as plt
import sys
#mapeo = { 'A':0, 'R':1, 'B':2, 'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19 }

mapeo = {}
for a in range(65, 91):
  mapeo[chr(a)] = a - 65
allineaciones = []


f=open("leer.txt","w")


def get_caminos (cadena1, cadena2, pos_x, pos_y, matrix_similitud, matrix_matching, costo, grupos):
  #cambiamos la condicion inicial, dado que Smith-waterman avanza hasta llega a un valor de 0
  if 0 == matrix_matching[pos_y, pos_x]:
    #print('ingresa alineaciones')
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
  #realmente la matriz inicial se llena de zeros
  for i in range(1, tam_cadena1+1):
    matriz_matching[0, i] = max(matriz_matching[0, i-1]  + costo,0)

  for i in range(1, tam_cadena2+1):
    matriz_matching[i, 0] = max(matriz_matching[0, i-1]  + costo,0)
  for i in range(1, tam_cadena2 + 1):
    for j in range(1, tam_cadena1 + 1):
      matriz_matching[i,j] = max(matriz_matching[i-1, j-1] + matrix_similitud[mapeo[cadena1[j-1]],
                            mapeo[cadena2[i-1]]], matriz_matching[i-1, j] + costo, matriz_matching[i, j-1] + costo, 0)

  return matriz_matching

#Importacion de fastas
#Importacion de fastas
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


matrix_similitud  = np.identity(26)
matrix_similitud = matrix_similitud - 2
for i in range(26):
  matrix_similitud[i,i] = 2

print("Matriz de similitud")
print(matrix_similitud)

print("Matriz DP")
answer = solution_global(secuencia1, secuencia2, matrix_similitud, costo)
print(answer)

allineaciones = []

x_ans, y_and = np.unravel_index(np.argmax(answer, axis=None), answer.shape)
print('posicion del valor maximo')
print(x_ans, y_and)
print("Alineaciones")
get_caminos (secuencia1, secuencia2, y_and, x_ans , matrix_similitud, answer, costo, ["", ""])
for val in allineaciones:
  print(str(val[0][::-1]) + " " + str(val[1][::-1]))
print("Numero de alineaciones")
print(len(allineaciones))
print("Score")
print(answer.max())


f.write("hola "+ dist + '\n')

f.write("Las secuencias son \n")
f.write("Sec1: " +str(secuencia1) +"\n")
f.write("Sec1: " +str(secuencia2) +"\n")
f.write("---------\n")
#for i in (matrix_similitud):
#  f.write(str(i)+'\n')
f.write("---------\n")
for i in (answer):
  f.write(str(i)+'\n')
f.write("---------\n")
for val in allineaciones:
  f.write(str(val[0][::-1]) + " " + str(val[1][::-1]+'\n'))

#f.write('asd = '+ str(answer[3][3]))

f.write("---------\n")

f.write("algo-dist:::::::"+str(dist)+'\n')

if dist=="ag1":
  f.write("numero de coincidencias: "+str(num_match)+"\n")
  f.write("numero de inconsistencias: "+ str(num_mismatch)+"\n")
  f.write("La distancia molecular entre ambas secuencias, K, es: "+ str(K)+"\n")
else:
  if res_dist2==None:
    f.write("Intente tomar el log de un numero negativo\n")
  else:
    f.write("La distancia molecular entre ambas secuencias es: "+ str(res_dist2)+"\n")

f.write("---------\n")
f.write("algo-tree:::::::"+str(tree)+'\n')


f.close()