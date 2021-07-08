#!/usr/bin/env python
##PARA EJECUTAR USA EL SIGUIENTE COMANDO
# python jukes.py ATGGATGGAT TAAGGTAAAA
# las cadenas deben ser de igual tamaño
import math 
import sys
seq1 = sys.argv[1]
# "ATGTCGCTAAGCGCTTCAGATT"
seq2 = sys.argv[2]
# "ATGTCGCATAGCGCTACAGACT" 

print("sequencia 1")
print(seq1)
print("sequencia 2")

print(seq2)


l=len(seq1)

num_match = num_mismatch = 0 

for i in range (0,l):
	if seq1[i] == seq2[i]:
		num_match += 1    
	else:

		num_mismatch += 1

print("numero de coincidencias")
print(num_match)
print("numero de inconsistencias")
print(num_mismatch) 


# print("proportion between mismatches and length of sequence" )

D=(num_mismatch/l)

print(D)

# Usamos D para determinar K, distancia molecular, usando Jukes-cantor model 
print("Jukes-Cantor formula K = (-3/4)ln(1-(4/3)B)")
#K es el total del numero de susituciones divididos por el numero total de nucleotidos alineados
B = D
K =((-3/4)*math.log((1-(B*(4/3))))) 
print("La distancia molecular entre ambas secuencias, K, es:")
print(K)
