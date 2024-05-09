import numpy as np 
import networkx as nx

### --- FUNCTIONS --- ###

def create_edges(classroom, model) :
    """Creates the edges of a graph depending on the method(model) decided.

    Args:
        classroom (int[int]): a typical classroom from EFREI
        model (str): a model decided by the user

    Returns:
        edges (float[float][...]) : the edges of the classroom's graph
    """
    if model == "direct" :
        edges = []
        stud = 0
        for i in range(len(classroom)) :
            for j in range(len(classroom[i])) :
                if classroom[i][j] == 1 :
                    if j-1>-1 :
                        if classroom[i][j-1] == 1:
                            edges.append([stud-1,stud])
                    if j+1<len(classroom[i]) :
                        if classroom[i][j+1] == 1:
                            edges.append([stud,stud+1])
                stud += 1
        return edges
    
    if model == "all" :
        pass


def adj_matrix(classroom, edges) :
    """Creates the adjacency matrix from the edges of a graph.

    Args:
        classroom (int[int]): a typical classroom from EFREI
        edges (float[float][...]): the edges of the classroom's graph

    Returns:
        adjM (float[float]): a 2x2 matrix representing the influence of each student of the classroom
    """
    length = len(classroom)*len(classroom[0])
    adjM = np.zeros((length,length))

    for edge in edges:
        i=edge[0]
        j=edge[1]
        if i>=length or j>=length or i<0 or j<0 :
            print(f"Not a Proper Input in Edge {i},{j}")
        else :
            adjM[i][j]=1
            adjM[j][i]=1
    return adjM

def biggest_eig(adjM):
    """Finds the biggest eigen value and the biggest eigenvector of a matrix.

    Args:
        adjM (float[float]): a 2x2 matrix representing the influence of each student of the classroom

    Returns:
        eigval (float): the biggest eigen value of the matrix
        big_eigvect ([float]): the biggest eigen vector of the matrix
    """
    eigvals, eigvects = np.linalg.eig(adjM)
    eig_i = 0
    for i in range(len(eigvals)):
        if eigvals[i] > eigvals[eig_i] :
            eig_i = i
    big_eigvect = []
    for elm in eigvects :
        big_eigvect.append(elm[eig_i])
    return eigvals[eig_i], big_eigvect

### --- VARIABLES --- ###

H116 = [[1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1]]

models = {"direct","all"}

### --- MAIN --- ###

mat = adj_matrix(H116, create_edges(H116, models[0]))
print("The adjacent matrix is : \n")
for i in range(len(mat)) :
    print("[")
    for j in range(len(mat[i])) :
        print(f"{mat[i][j]},", end ='')
    print("]\n")

eig_val, eig_vect = biggest_eig(mat)
print(f"The biggest eigenvalue of this matrix is : {eig_val} \n And its corresponding eigenvector is : {eig_vect}")