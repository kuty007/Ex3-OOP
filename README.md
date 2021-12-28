![OBbBq3](https://user-images.githubusercontent.com/80645472/147453679-3d4084f1-3aaa-4337-98d4-2a29a48ee295.gif)



# Ex3-OOP
Made by Asaf Yekutiel,Yulia Katz and Avidan Abitbol

GitHub pages:

https://github.com/yukatz 

https://github.com/kuty007

https://github.com/avidanAbitbol

## Introduction
This project is an assignment in an object-oriented course at Ariel University.
The project is about implementing a directed weithted graph and exploring some graph algorithms.

*To learn more about directed graph:
http://math.oxford.emory.edu/site/cs171/directedAndEdgeWeightedGraphs/

## Creating and Implementing Directed Weighted Graph Theory.
This project had 2 main part: in the first part we had to implemment an Directed Weighted Graph,
in the second part we implement and run some algorhitms that we build on the DWG to check some skills.
The issue of the second part is to compare run time between 2 programming languages java VS python about same assignment.

This is the java assignment: https://github.com/yukatz/OOP_2021_Ex2

![Screenshot 2021-12-27 102400](https://user-images.githubusercontent.com/80645472/147451867-ab021e18-a248-4612-9bc5-fe54696540c8.png)

# Classes:
 ## Node Data:
 
Represents vertex of Directed Weighted Graph - construct of key and location. 

https://en.wikipedia.org/wiki/Vertex_(graph_theory)

 ## Directed Weighted Graph:
 ![Graph_cycle](https://user-images.githubusercontent.com/80645472/147454359-0387ac0e-709d-42ec-a23a-cf439a53f1a3.gif)
 
Each DiGraph contain dictionary of his nodes, and each node contain his edges.
In addition each DiGraph holds the number of edges in the graph and a mode counter 
that represent the number of changes in the graph. 

https://en.wikipedia.org/wiki/Directed_graph

 ## Directed Weighted Graph Algorithms:
 Represents algorithms that can be used on directed graph:

 ### isConnected - Cheking if there is a valid path from each node to others.
 Method - Using a ***isConnected*** and ***Transpose*** functions.
 
 
 
 
 
 https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
 
  ### Shoretest Path - Presents the shortest path between source to destination. 
  Method - Checks the shortest route using a Dijkstra function.
  Checking for extreme cases - same node added twice, the node does not exist in the graph.
 
 https://en.wikipedia.org/wiki/Shortest_path_problem
 
 ![spsa](https://user-images.githubusercontent.com/80645472/147453694-41aaa2d4-bbec-4009-81f2-0dafbf440a5e.gif)
 
 
 ### Center - Finds the vertex which minimizes the max distance to all the other nodes
 Method - Checks the shortest path between a vertex and the rest of the vertices, compares the lengths of the orbits and selects the longest one. Do this for each vertex and finally compare the maximum of all and take the lowest.
 *Checking for extreme cases* - if the graph not connected we can't find a center.
 
 
 https://en.wikipedia.org/wiki/Graph_center
 
  ### TSP - Travelling salesman problem - Computes a list of consecutive nodes wich go over all the nodes in cities.
 
 https://en.wikipedia.org/wiki/Travelling_salesman_problem
 
 ![Sa_poland_tsp](https://user-images.githubusercontent.com/80645472/147453871-36d85b77-5dd2-44d3-8109-51fe13cf781a.gif)
 
# Private method that we used:

## Bfs: 
: 
![Graph-BFS](https://user-images.githubusercontent.com/80645472/147453734-bd3b55a8-2914-47fb-a52b-0fffd7afbc2a.gif)

This private method based on breadth-first search. BFS is an algorithm for traversing or searching graph data structures. The method checks whether or not the graph is strongly linked, in other words it checks whether there is a path between node to each other node. The method use counter that count the number of nodes that connected to the source node. If counter value equal to the number of nodes in this graph that means that the source node connected. To check if the whole graph is strongly connected needs to run the method on all the nodes in the graph. The method stored a queue of the visited nodes:
Pop the first node from the queue.
Gets a collection of this node edges.
Goes through all the nodes that have an edge from the pop node.
Check if the node has already been visited, if so skip it(tag = 1 -> visited, tag = -1 -> not visited). Otherwise mark it as visited (update his own tag) and add the node to the queue.
Add this node's neighbors to the queue and repeat these steps The method use counter that count the number of nodes that connected to the source node. After the queue is empty check if the counter value equal to the number of nodes in this graph that means that the source node connected. If so the method will return true, Otherwise false. Note: The method change the tag values. Complexity: O(|V|+|E|), |V|=number of nodes, |E|=number of edges. 
https://en.wikipedia.org/wiki/Breadth-first_search

## Dijkstra :
![dij42f696d6167655f6f7074696d697a65722f396537643165376630626561623238626535303935343931623465646362353163323266396136622e676966](https://user-images.githubusercontent.com/80645472/147453744-c606fc19-6151-479c-97c8-faa4fd2dbbde.gif)

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

# UML

![Screenshot 2021-12-27 195348](https://user-images.githubusercontent.com/80645472/147495979-0326320f-7a04-4bc8-a7a6-82ffa91eba4b.png)



##For more information please visite our wiki pages:
# How to run the code: https://github.com/kuty007/Ex3-OOP.wiki.git
# Compare times between language python VS java: https://github.com/kuty007/Ex3-OOP.wiki.git
