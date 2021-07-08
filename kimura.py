#!/usr/bin/env python
##
## Kimura
## USO:
## python kimura.py seq1 seq2

import sys

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

seq1= sys.argv[1]
seq2= sys.argv[2]
print("Kimura")
print(K2Pdistance(seq1,seq2))
