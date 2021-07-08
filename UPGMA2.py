#!/usr/bin/env python
import array
import numpy
from ete3 import Tree,PhyloTree, TreeStyle
import sys    
import os
from io import StringIO
from Bio import Phylo
import matplotlib.pyplot as plt
import matplotlib
def matrixMinimum(matrix, length):
    min_index_i = 0
    min_index_j = 0
    minimum=float('inf')
    for i in range (length):
        temp = matrix[i]
        min_value = numpy.min(temp[numpy.nonzero(temp)])
        j = temp.tolist().index(min_value)

        if min_value < minimum: 
            min_index_i = i
            min_index_j = j
            minimum = min_value
   
    return min_index_i,min_index_j


def upgma(matrix, length,dictionary):
    leaves = []
    count = 0
    
    for i in range (0, length):    
        leaves.append("Var"+str(i+1))
    
    numberOfClusters = i+1
    
    while(length>1):
        
        numberOfClusters = numberOfClusters+1
        count = count+1

        min_index_i,min_index_j = matrixMinimum(matrix, length)
        
        leaves.append("Var"+str(numberOfClusters))  
        distance = matrix[min_index_i][min_index_j]/float(2)
        
        size = 0
        if leaves[min_index_i] not in dictionary.keys():
            size = 1
            distance1 = distance
        else:
            size = dictionary[leaves[min_index_i]][4]
            distance1 = distance-max(dictionary[leaves[min_index_i]][0],dictionary[leaves[min_index_i]][2])
        
        if leaves[min_index_j] not in dictionary.keys():
            size = size+1
            distance2 = distance
        else:
            size = size+dictionary[leaves[min_index_j]][4]
            distance2 = distance-max(dictionary[leaves[min_index_j]][0],dictionary[leaves[min_index_j]][2])
        dictionary["Var"+str(numberOfClusters)] = [distance1,leaves[min_index_i],distance2,leaves[min_index_j],size]
        

        matrix = numpy.insert(matrix, length, values=float(0), axis=0)
        matrix = numpy.insert(matrix, length, values=float(0), axis=1)

        for i in range (0, length):
            matrix[-1][i]=matrix[i][-1] = (matrix[i][min_index_i] + matrix[i][min_index_j])/2
        

        if min_index_i < min_index_j:
            matrix = numpy.delete(matrix, min_index_i, 0)
            matrix = numpy.delete(matrix, min_index_i, 1)
            matrix = numpy.delete(matrix, (min_index_j)-1, 0)
            matrix = numpy.delete(matrix, (min_index_j)-1, 1)
            length = len(matrix)
            del leaves[min_index_j]
            del leaves[min_index_i]

        else:
            matrix = numpy.delete(matrix, min_index_i, 0)
            matrix = numpy.delete(matrix, min_index_i, 1)
            matrix = numpy.delete(matrix, min_index_j, 0)
            matrix = numpy.delete(matrix, min_index_j, 1)            
            length = len(matrix)
            del leaves[min_index_i]
            del leaves[min_index_j]
        
    return "Var"+str(numberOfClusters)


def printCluster(dictionary,finalCluster):
    stack = []
    result = []
    stack.append(finalCluster)
    while stack:
        
        current = stack.pop()
        if isinstance( current , float ):
            if isinstance( current_prev , float ):
                result.pop()
                result.append(")")
            result.append(":"+str(current))
            result.append(",")
            
        elif current in dictionary.keys():
            stack.append(dictionary[current][0])
            stack.append(dictionary[current][1])
            stack.append(dictionary[current][2])
            stack.append(dictionary[current][3])
            result.append("(")
        else:
            result.append(current)
        current_prev = current
        
    result.pop()
    result.append(")")  
    return result

def replaceWithSeq(res,length):
    labels=[]
    # print(res)

    for idx in range(1,length+1):
        res=res.replace("Var"+str(idx),chr(65+idx-1))
        # print(res)
    return res



matrix = []
file = "dis.txt"
f = open(file)
matrix = [[x for x in ln.split()] for ln in f]       
matrix = numpy.asarray(matrix)
matrix = matrix.astype(numpy.float)

print("-----------------------")
print(matrix)
print("-----------------------")
length = len(matrix)
dictionary={}
finalCluster = upgma(matrix, length,dictionary)
result=printCluster(dictionary,finalCluster)
# print(result)
result=''.join(result)
result=result+";"
result=replaceWithSeq(result,length)

# print("HOLA")
# tree=PhyloTree(result)
tree=Phylo.read(StringIO(result),"newick")
# Phylo.write(tree,"tree.xml","phyloxml")
# fi = open('Generado.txt', 'w')
# fi.write("Result" + os.linesep)
# fi.write(result)
# fi.write("Tree" + os.linesep)
# fi.write(tree)
# fi.close()
matplotlib.rc('font',size=30)
fig = plt.figure(figsize=(10, 20), dpi=100)
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, axes=axes,do_show=False)
# plt.show()
plt.savefig('v4.png')
print("Result")   
print(result) 
print("TREE")
print(tree)
f.close()  

 
