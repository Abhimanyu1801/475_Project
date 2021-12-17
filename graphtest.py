import networkx as nx  #NetworkX is a Python-based software package for creating, 
#manipulating, and studying complex networks' structure, dynamics, and function.
import matplotlib.pylab as plt#Matplotlib is a cross-platform,data visualization and graphical plotting library for Python.
from igraph import * #igraph is a library in python for network analysis.
import igraph as igraph
#As For the Clustering Models Only Undirected Graphs Can be Used, We First Used the DiWANN Network Model to Genrate a 
#Undirected Graph gml file and then used Read_GML function to load it into a graph.
g = Graph.Read_GML("475projundirectedDWRNgraphEff.gml")
# p = g.community_label_propagation()
# p = g.community_multilevel()
p = g.community_leading_eigenvector() #The Nodes are moved across communities to determine whether or not they will contribute 
#to the modularity score if they remain.
print(p)

# q = g.modularity(p)
# print(q)

#We will using color pallete to differentiate between the clusters and the no of color will be equal to no of clusters
pal = igraph.drawing.colors.ClusterColoringPalette(len(p))
#Now we assign the colors in each of the vertex in the graph using the help of Clusters.membership and vertex set 
#function(vs) using color as its attribute.
g.vs["color"]= pal.get_many(p.membership)
#we use the number array from 0 to 178 as there are 179 ebtries in the dataset, 0 to 73 corresponds to SARS-CoV-2 
#whereas labels from 74 to 178 represent the SARS-CoV
labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 
143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 
167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178]
out = igraph.plot(g, vertex_label = labels)
out.save('Community_ModularityClusteringVisualizationwithLabels.png')



