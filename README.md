![4-ew7H](https://user-images.githubusercontent.com/80645472/147452746-090ae5cf-88a7-4752-b99d-7a236752444c.gif)


# Ex3-OOP
Made by Asaf Yekutiel,Yulia Katz and Avidan Abitbol
GitHub pages:
https://github.com/yukatz
https://github.com/kuty007
https://github.com/avidanAbitbol

## Introduction
This project is an assignment in an object-oriented course at Ariel University.
The project is about implementing a directed weithted graph and exploring some graph algorithms.

## Creating and Implementing Directed Weighted Graph Theory.
this project had 2 main part: in the first part we had to implemment an Directed Weighted Graph Theory,
in the seconde part we run some algorhitms that we build on the DWG to check some skills.

![Screenshot 2021-12-27 102400](https://user-images.githubusercontent.com/80645472/147451867-ab021e18-a248-4612-9bc5-fe54696540c8.png)

# Classes:
 ## Node Data:
 
Represents vertex of Directed Weighted Graph - construct of key and location. 
-https://en.wikipedia.org/wiki/Vertex_(graph_theory)

 ## Directed Weighted Graph:
 
Each DiGraph contain dictionary of his nodes, and each node contain his edges.
In addition each DiGraph holds the number of edges in the graph and a mode counter 
that represent the number of changes in the graph. 
-https://en.wikipedia.org/wiki/Directed_graph

 ## Directed Weighted Graph Algorithms:
 
Represents algorithms that can be used on directed graph:

 isConnected - Cheking if there is a valid path from each node to others. https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
 Shoretest Path - Presents the shortest path between source to destination. https://en.wikipedia.org/wiki/Shortest_path_problem
 Center - Finds the vertex which minimizes the max distance to all the other nodes https://en.wikipedia.org/wiki/Graph_center
 TSP - Travelling salesman problem - Computes a list of consecutive nodes wich go over all the nodes in cities. https://en.wikipedia.org/wiki/Travelling_salesman_problem

private method that we used:

## bfs(to check connectivity) : 

This private method based on breadth-first search. BFS is an algorithm for traversing or searching graph data structures. The method checks whether or not the graph is strongly linked, in other words it checks whether there is a path between node to each other node. The method use counter that count the number of nodes that connected to the source node. If counter value equal to the number of nodes in this graph that means that the source node connected. To check if the whole graph is strongly connected needs to run the method on all the nodes in the graph. The method stored a queue of the visited nodes:
Pop the first node from the queue.
Gets a collection of this node edges.
Goes through all the nodes that have an edge from the pop node.
Check if the node has already been visited, if so skip it(tag = 1 -> visited, tag = -1 -> not visited). Otherwise mark it as visited (update his own tag) and add the node to the queue.
Add this node's neighbors to the queue and repeat these steps The method use counter that count the number of nodes that connected to the source node. After the queue is empty check if the counter value equal to the number of nodes in this graph that means that the source node connected. If so the method will return true, Otherwise false. Note: The method change the tag values. Complexity: O(|V|+|E|), |V|=number of nodes, |E|=number of edges. 
https://en.wikipedia.org/wiki/Breadth-first_search

## Dijkstra :
This private method based on Dijkstra's algorithm. Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. In other words it finds the shortest paths between the source node and the destination node. The method uses the weight of each node to update his current distance from the source node. The method stored a priority queue(priority is determined by the weight) of the visited nodes:
Pop the first node from the queue.
Visit each one of this nodes neighbors:
Check if the node has already been visited, if so skip it(tag = Black -> visited, tag = White -> not visited).
Updates his weight to be the distance between the node and the source node.
Updates his tag To be the node's id from which he came to.
Add this node to the queue.
After going through all the neighbors of the node, updates that we visited this node by change his info to "Black" and therefore will not visit it again.
Repeat these steps until the queue is empty or has reached the destination node. If the queue is empty it means it did not reach the destination node (the graph is not connected), return infinity. Otherwise returns the tag of the destination node. Note: The method change the info, tag and pre values. Complexity: O((|V|+|E|)log|V|), |V|=number of nodes, |E|=number of edges. 
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

# How to run the code:
*&^%$#@*&^%$#@*&^%$#@
