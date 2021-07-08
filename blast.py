#!/usr/bin/env python
import numpy as np
import math
from Bio.Align import substitution_matrices
from operator import itemgetter
import sys

f=open("leer.txt","w")
# 3 proteinas, 11 nucleotidos
def get_words(seeds, word, slide=3):
  for i in range(0, len(word)-slide+1):
    seeds.append(word[i:i+slide])

# Para proteinas
def get_all_option(data, options=3):
  values = []
  for i in range(0, len(data)):
    for j in range(0, len(data)):
      for k in range(0, len(data)):
        palabra = data[i] + data[j] + data[k]
        values.append(palabra)
  return values

def get_neighbors(seeds, options, matrix, umbral=13):
  answer = []
  start = 0
  for word in seeds:
    for option in options:
      score = 0
      for i in range(len(option)):
        score += matrix[word[i],option[i]] 
      if score>=umbral:
        answer.append((start,option))
    start += 1
  return answer

def evaluar(matrix, palabra, query):
  contador = 0
  for i in range(len(palabra)):
    contador += matrix[palabra[i], query[i]]
  return contador

def extender_1_1(palabra,  query, matrix, pos_palabra, pos_query, umbral=22):

  pos_izq_query = pos_query[0]
  pos_der_query = pos_query[1]

  pos_izq_word = pos_palabra[0]
  pos_der_word = pos_palabra[1]

  value = evaluar(matrix, palabra[pos_izq_word:pos_der_word+1], query[pos_izq_query:pos_der_query+1])
  if value<umbral:
    return (None, None, -1)



  #Uno a Uno
  while pos_izq_query >= 1 and pos_izq_word >= 1 and pos_der_word+1 < len(palabra) and pos_der_query+1 < len(query):
    pos_izq_query-=1
    pos_izq_word-=1  
    pos_der_word+=1
    pos_der_query+=1

    value = evaluar(matrix, palabra[pos_izq_word:pos_der_word+1], query[pos_izq_query:pos_der_query+1])

    if value < umbral:
      pos_der_word-=1
      pos_der_query-=1
      pos_izq_word+=1
      pos_izq_query+=1
      break 

  #Score Evaluacion
  value = evaluar(matrix, palabra[pos_izq_word:pos_der_word+1], query[pos_izq_query:pos_der_query+1])

  return (palabra, palabra[pos_izq_word:pos_der_word+1], value)

def extender(palabra,  query, matrix, pos_palabra, pos_query, umbral=0):

  pos_izq_query = pos_query[0]
  pos_der_query = pos_query[1]

  pos_izq_word = pos_palabra[0]
  pos_der_word = pos_palabra[1]

  #Izquierda
  while pos_izq_query >= 1 and pos_izq_word >= 1:
    pos_izq_query-=1
    pos_izq_word-=1

    if matrix[palabra[pos_izq_word], query[pos_izq_query]] < 0:
      pos_izq_word+=1
      pos_izq_query+=1
      break

  #Derecha
  while pos_der_word+1 < len(palabra) and pos_der_query+1 < len(query):
    pos_der_word+=1
    pos_der_query+=1

    if matrix[palabra[pos_der_word], query[pos_der_query]] < 0:
      pos_der_word-=1
      pos_der_query-=1
      break  

  #Score Evaluacion
  value = evaluar(matrix, palabra[pos_izq_word:pos_der_word+1], query[pos_izq_query:pos_der_query+1])

  return (palabra, palabra[pos_izq_word:pos_der_word+1], value)

def search_database(neighbors, DB, matrix, query, umbral = 22):
  answers = []
  for (indice, vecino) in neighbors:
    for cadena in DB:
        pos = 0
        start = 0
        while True:
          pos = cadena.find(vecino, start)
          if pos == -1:
            break
          valores = extender_1_1(cadena, query, matrix, (pos, pos+len(vecino)-1), (indice, indice+len(vecino)-1), umbral)
          if valores[2]!=-1:          
            answers.append(valores) 
          start = pos + 1
  
  return answers

"""# Prueba del BLAST"""

#Solo para subir una BD. Formato cadena, nombre, código

validos = np.array(['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V'])
BLOSUM62 = substitution_matrices.load("BLOSUM62")
total_options = get_all_option(validos)
#DB1 = sys.argv[1]

file = sys.argv[1]
DB1 = open(file) 
DB =  DB1

matrix_bd = []
bd_evaluar = []
for line in DB:
  division = line.split(",")
  matrix_bd.append(division)
  bd_evaluar.append(division[0])
DB=np.matrix((matrix_bd))

query = sys.argv[2] # Establecer cadena
#query = "AEAED"
seeds = []
get_words(seeds, query)
neighbors = get_neighbors(seeds, total_options, BLOSUM62)
posibles_cadenas = search_database(neighbors, bd_evaluar, BLOSUM62, query, 11)
posibles_cadenas = sorted(posibles_cadenas, key = itemgetter(2), reverse=True)
print(posibles_cadenas)

print(BLOSUM62)
print(BLOSUM62['P','P'])
print(BLOSUM62['R','R'])
print(len(total_options))

DB1.close()

f.write("------- RESULTADO DEL ALINEAMIENTO ---------\n")


f.write("Las posibles cadenas son:\n")
f.write(str(posibles_cadenas)+'\n')
f.write("Total de Opciones son:\n")
f.write(str(len(total_options))+'\n')


