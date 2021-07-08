import sys
import numpy as np
import scipy as scipy
import itertools
from treelib import Node, Tree
# pip install treelib

def calculateQ(d):
    #print('calculateQ')
    r = d.shape[0]
    q = np.zeros((r,r))
    for i in range(r):
        for j in range(r):
            if i == j:
                q[i][j] = 0
            else:
                r_A = 0
                r_B = 0
                for k in range(r):
                    r_A += d[i][k]
                    r_B += d[j][k]
                #q[i][j] = d[i][j] - (r_A + r_B)/(r-2)
                q[i][j] = (r-2) * d[i][j] - r_A - r_B
    return q

def LowPair(q):
    r = q.shape[0]
    minVal = float("inf")
    for i in range(0,r):
        for j in range(i,r):
            if (q[i][j] < minVal):
                minVal = q[i][j]
                minIndex = (i,j)
    return minIndex


def NewNodePrime(i,j,d):
    r = d.shape[0]
    r_A = 0
    r_B = 0
    for k in range(r):
        r_A += d[i][k]
        r_B += d[j][k]

    d_AU = (d[i][j] + (r_A - r_B))/ 2
    d_BU = (d[i][j] + (r_B - r_A))/ 2
    '''
    try:
        d_AU = (1. / (2. * (r - 2.))) * ((r - 2.) * d[i][j] + r_A - r_B)
        d_BU = (1. / (2. * (r - 2.))) * ((r - 2.) * d[i][j] - r_A + r_B)
    except ZeroDivisionError:
        d_AU = 0
        d_BU = 0
    '''
    return(d_AU,d_BU)

def DistanceMatrix(f,g,d):
    #print (d)
    r = d.shape[0]
    nd = np.zeros((r-1,r-1))

    # copia de matriz
    ii = jj = 1
    for i in range(0,r):
        if i == f or i == g:
            continue
        for j in range(0,r):
            if j == f or j == g:
                continue
            nd[ii][jj] = d[i][j]
            jj += 1
        ii += 1
        jj = 1

    # Calcular la primera fila y columna
    ii = 1
    for i in range (0,r):
        if i == f or i == g:
            continue
        nd[0][ii] = (d[f][i] + d[g][i] - d[f][g]) / 2.
        nd[ii][0] = (d[f][i] + d[g][i] - d[f][g]) / 2.
        ii += 1

    return nd

def NeighbourJoining(d,s):
    labels = list(s)
    f = open('arbol_philo.py', 'r+')
    f.truncate(0)
    it_a=0
    it_b=0
    arbol = [" "]
    last_parent=""
    string_tree=""
    while d.shape[0] > 2:
        q = calculateQ(d)
        lowestPair = LowPair(q)
        pair_A = lowestPair[0]
        pair_B = lowestPair[1]
        #variable para dibujar
        new_parent=labels[pair_A]+labels[pair_B]

        pairDist = NewNodePrime(pair_A,pair_B,d)
        d = DistanceMatrix(pair_A,pair_B,d)

        draw_dist_A=str(round(pairDist[0],2))
        draw_dist_B=str(round(pairDist[1],2))
        string_tree="("+string_tree+labels[pair_A]+":"+draw_dist_A+","+labels[pair_B]+":"+draw_dist_B+")"
        if (len(labels[pair_A])==1):
            arbol.insert(0,"tree.create_node(\""+labels[pair_A]+"\", \""+labels[pair_A]+"\", parent=\""+new_parent+"\")")
        if (len(labels[pair_A])>1):
            arbol.insert(0,"tree.create_node(\""+draw_dist_A+"\", \""+labels[pair_A]+"\", parent=\""+new_parent+"\")")
        if (len(labels[pair_B])==1):
            arbol.insert(0,"tree.create_node(\""+labels[pair_B]+"\", \""+labels[pair_B]+"\", parent=\""+new_parent+"\")")
        if (len(labels[pair_B])>1):
            arbol.insert(0,"tree.create_node(\""+draw_dist_B+"\", \""+labels[pair_B]+"\", parent=\""+new_parent+"\")")

        labels.pop(pair_B)
        labels[pair_A]=new_parent
        last_parent=new_parent

    if d.shape[0] == 2:
        q = calculateQ(d)
        lowestPair = LowPair(q)
        pair_A = lowestPair[0]
        pair_B = lowestPair[1]
        #variable para dibujar
        new_parent=labels[pair_A]+labels[pair_B]

        pairDist = NewNodePrime(pair_A,pair_B,d)
        d = DistanceMatrix(pair_A,pair_B,d)

        draw_dist_A=str(round(pairDist[0]*2,2))
        draw_dist_B=str(round(pairDist[1]*2,2))
        string_tree="("+string_tree+labels[pair_B]+":"+draw_dist_B+")"
        if (len(labels[pair_A])==1):
            arbol.insert(0,"tree.create_node(\""+labels[pair_A]+"\", \""+labels[pair_A]+"\", parent=\""+new_parent+"\")")
        if (len(labels[pair_A])>1):
            arbol.insert(0,"tree.create_node(\""+draw_dist_A+"\", \""+labels[pair_A]+"\", parent=\""+new_parent+"\")")
        if (len(labels[pair_B])==1):
            arbol.insert(0,"tree.create_node(\""+labels[pair_B]+"\", \""+labels[pair_B]+"\", parent=\""+new_parent+"\")")
        if (len(labels[pair_B])>1):
            arbol.insert(0,"tree.create_node(\""+draw_dist_B+"\", \""+labels[pair_B]+"\", parent=\""+new_parent+"\")")

        labels.pop(pair_B)
        labels[pair_A]=new_parent
        last_parent=new_parent


    print(string_tree)
    arbol.insert(0,"tree.create_node(\"\", \""+last_parent+"\")")
    arbol.insert(0,"tree = Tree()")
    arbol.insert(0,"from treelib import Node, Tree")
    arbol.append("tree.show()")
    for i in arbol:
        f.write(i)
        f.write("\n")



def run(distMatrix,s):
    NeighbourJoining(distMatrix,s)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print ("Usage: neighbour-joining.py")
        sys.exit(1)

    distMatrix = np.array(
         [[0, 0.4, 0.35, 0.6],
            [0.4, 0, 0.45, 0.7],
            [0.35, 0.45, 0, 0.55],
            [0.6, 0.7, 0.55, 0]]
        )
    s="ABCD"
    '''
    distMatrix = np.array(
         [[0, 8, 4, 6],
            [8, 0, 8, 8],
            [4, 8, 0, 6],
            [6, 8, 6, 0]]
        )
    '''
    run(distMatrix,s)
    exec(open("arbol_philo.py").read())
