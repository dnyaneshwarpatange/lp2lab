# A_Star
This code is for the A* algorithm, a popular pathfinding algorithm used in various applications like gaming, robotics, and maps. Let's break it down step by step:

python
Copy code
def aStarAlgo(start_node, stop_node):
This line defines a function named aStarAlgo that takes two parameters: start_node and stop_node, which represent the starting and ending points of the path we want to find.

python
Copy code
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
Here, we initialize several variables:

open_set is a set containing the start_node initially.
closed_set is an empty set that will hold nodes we have already evaluated.
g is a dictionary to store the cost of getting from the start_node to each node.
parents is a dictionary to keep track of the parent node for each node.
We set the cost of reaching the start_node from itself as 0, and its parent as itself.
python
Copy code
    while len(open_set) > 0:
This initiates a loop that continues until there are nodes left to evaluate in the open_set.

python
Copy code
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
This section selects the node n from the open_set that has the lowest total cost (g[n] + heuristic(n)). The heuristic() function is used to estimate the cost of reaching the goal from a given node.

python
Copy code
        if n == stop_node or Graph_nodes[n] == None:
            pass
If the current node n is the stop_node or if there are no more nodes to explore, we skip to the next iteration of the loop.

python
Copy code
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
This part evaluates the neighbors of node n. It updates the cost of reaching each neighbor (m) from n if a better path is found. It also updates the parent of m and manages the open_set and closed_set.

python
Copy code
        if n == None:
            print('Path does not exist!')
            return None
If there's no feasible path, it prints a message and returns None.

python
Copy code
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
If the stop_node is reached, it reconstructs the path from start_node to stop_node using the parents dictionary and returns the path.

python
Copy code
        open_set.remove(n)
        closed_set.add(n)
Finally, it removes the current node n from the open_set and adds it to the closed_set because it has been evaluated.

python
Copy code
    print('Path does not exist!')
    return None
If the loop completes without finding a path, it prints a message and returns None.

python
Copy code
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
This function returns the neighbors of a given node v from the Graph_nodes dictionary.

python
Copy code
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[n]
This function provides a heuristic estimate of the cost from a given node n to the goal node. It returns a value based on a pre-defined dictionary H_dist.

python
Copy code
Graph_nodes = {
    'A': [('B', 6), ('C', 8),('D',7)],
    'B': [('A', 6), ('D', 8), ('E', 9)],
    'C': [('A', 8), ('D', 16), ('F', 12)],
    'D': [('A', 7), ('C', 16), ('E', 10),('G',21)],
    'E': [('B', 9), ('D', 10), ('H', 11)],
    'F': [('C', 12), ('G', 20)],
    'G': [('F', 20), ('H', 12)],
    'H': [('E', 11), ('G', 12)],
}
This dictionary Graph_nodes represents a graph where each key is a node, and its value is a list of tuples representing its neighbors and the weight of the edges connecting them.

python
Copy code
aStarAlgo('A', 'G')
This line calls the aStarAlgo function with the start_node as 'A' and the stop_node as 'G', initiating the A* algorithm to find the shortest path from 'A' to 'G' in the defined graph.



# BFS
This code performs a Breadth-First Search (BFS) traversal on a graph. Let's break it down:

python
Copy code
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : ['9'],
  '9' : []
}
This dictionary graph represents a graph where each key represents a node, and its corresponding value is a list of adjacent nodes.

python
Copy code
visited = [] # List for visited nodes.
queue = []   # Initialize a queue
visited is an empty list to keep track of visited nodes, and queue is an empty list initialized as a queue, which will store nodes to be visited.

python
Copy code
def bfs(visited, graph, node): #function for BFS
This line defines a function named bfs which takes three parameters: visited (list of visited nodes), graph (the graph), and node (the starting node for BFS).

python
Copy code
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)    # Pop the first element from the queue
    print(m, end=" ")   # Print the node

    for neighbour in graph[m]:  # Iterate through neighbors of current node
      if neighbour not in visited:  # If neighbor not visited
        visited.append(neighbour)  # Mark it as visited
        queue.append(neighbour)    # Add it to the queue for further exploration
This block of code performs the BFS traversal. It starts with the initial node, appends it to both visited and queue, then enters a loop that continues until the queue is empty. Inside the loop:

It removes the first node from the queue (pop(0)), assigns it to m, and prints it.
It then iterates through the neighbors of m, marking each unvisited neighbor as visited and adding it to the queue for further exploration.
python
Copy code

print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling
This part of the code is the driver code. It simply prints a message indicating that it's performing BFS and then calls the bfs function with the initial node as '5'.

# chatbot
remind_name(): This function asks for the user's name and then prints a greeting with the provided name.
guess_age(): It tries to guess the user's age based on remainders of dividing the age by 3, 5, and 7. Then, it calculates the age and prints it along with a message.
count(): This function prompts the user for a number and then counts from 0 to that number.
test(): It tests the user's programming knowledge by asking a multiple-choice question and repeatedly prompting the user until they provide the correct answer.
end(): This function prints a congratulatory message.
Finally, after defining all functions, the script calls each function in the following order:

remind_name()
guess_age()
count()
test()
end()
This sequence of function calls provides a structured interaction with the user, starting with getting their name, guessing their age, counting to a number, testing their programming knowledge, and ending with a congratulatory message.


# DFS
This code performs a Depth-First Search (DFS) traversal on a graph represented by an adjacency list stored in a dictionary. Let's break it down:

python
Copy code
#Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
Here, graph is a dictionary where each key represents a node, and the corresponding value is a list of adjacent nodes.

python
Copy code
visited = set() # Set to keep track of visited nodes of graph.
visited is a set used to keep track of visited nodes during the DFS traversal.

python
Copy code
def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node, end=" ")

        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
This is a recursive function dfs that performs the Depth-First Search traversal. It takes three parameters: visited (the set of visited nodes), graph (the graph represented as an adjacency list), and node (the current node being visited).

If the current node node has not been visited yet, it prints the node and adds it to the visited set.
Then, for each neighbor of the current node, it recursively calls the dfs function to visit that neighbor.
python

Copy code

print("Following is the Depth-First Search")
dfs(visited, graph, '5')
This part of the code is the driver code. It prints a message indicating that it's performing DFS and then calls the dfs function with the initial node as '5'. This initiates the DFS traversal of the graph starting from node '5'.

# Dijkstra
This Python program implements Dijkstra's single source shortest path algorithm for a graph represented using an adjacency matrix. Let's understand it step by step:

Class Definition (Graph):
This class represents a graph and contains methods to find the shortest path from a source vertex (src) to all other vertices in the graph.
Initialization (__init__ method):
The constructor initializes the graph with the number of vertices (vertices) passed as an argument.
It also initializes an empty adjacency matrix (self.graph) of size vertices x vertices. Each cell in the matrix represents the weight of the edge between the corresponding vertices.
Printing Solution (printSolution method):
This method prints the shortest distances from the source vertex to all other vertices.
Finding Minimum Distance (minDistance method):
This method finds the vertex with the minimum distance value from the set of vertices not yet included in the shortest path tree (sptSet).
Dijkstra's Algorithm (dijkstra method):
This method implements Dijkstra's algorithm to find the shortest paths.
It initializes an array dist to store the shortest distance from the source vertex to each vertex. Initially, distances are set to a large value (represented by 1e7).
It initializes an array sptSet to keep track of vertices included in the shortest path tree.
It iterates over all vertices and picks the minimum distance vertex from the set of vertices not yet processed.
It updates the distances of adjacent vertices if a shorter path is found.
Driver Program:
A Graph object g is created with 9 vertices.
The adjacency matrix representing the graph is defined.
The dijkstra method is called with the source vertex 0.
This program calculates the shortest distances from the source vertex 0 to all other vertices in the graph and prints the results.






# graph colouring backtracking

#Python3 program to implement greedy
#algorithm for graph coloring
This line is a comment indicating that the code below implements the greedy algorithm for graph coloring in Python.

python
Copy code
def addEdge(adj, v, w):
This line defines a function named addEdge that takes three parameters: adj (the adjacency list of the graph), v (the first vertex), and w (the second vertex). This function adds an edge between vertices v and w in the graph.

python
Copy code
    adj[v].append(w)
    
    # Note: the graph is undirected
    adj[w].append(v)
    return adj
Here, the function appends vertex w to the adjacency list of vertex v and vice versa because the graph is undirected. Then, it returns the updated adjacency list.

python
Copy code
#Assigns colors (starting from 0) to all
#vertices and prints the assignment of colors
def greedyColoring(adj, V):
This line defines a function named greedyColoring that takes two parameters: adj (the adjacency list of the graph) and V (the number of vertices in the graph). This function performs graph coloring using the greedy algorithm and prints the assignment of colors.

python
Copy code
    result = [-1] * V
Here, result is initialized as a list of -1 values with a length equal to the number of vertices V. This list will store the color assigned to each vertex.

python
Copy code
    # Assign the first color to first vertex
    result[0] = 0;
The first vertex (index 0) is assigned the color 0.

python
Copy code
    # A temporary array to store the available colors.
    # True value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False] * V
This line initializes an array available with False values to keep track of available colors for each vertex. If available[cr] is True, it means color cr is assigned to one of the adjacent vertices.

python
Copy code
    # Assign colors to remaining V-1 vertices
    for u in range(1, V):
This loop iterates over all vertices starting from the second vertex (index 1) to assign colors.

python
Copy code
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = True
This nested loop processes all adjacent vertices of the current vertex u and flags their colors as unavailable by setting available[result[i]] to True.

python
Copy code
        # Find the first available color
        cr = 0
        while cr < V:
            if (available[cr] == False):
                break
            cr += 1
This loop finds the first available color (cr) by searching for the first False value in the available array.

python
Copy code
        # Assign the found color
        result[u] = cr
The found color cr is assigned to the current vertex u.

python
Copy code
        # Reset the values back to false
        # for the next iteration
        for i in adj[u]:
            if (result[i] != -1):
                available[result[i]] = False
This loop resets the values in the available array back to False for the next iteration, indicating that the colors are available again.

python
Copy code
    # Print the result
    for u in range(V):
        print("Vertex", u, " ---> Color", result[u])
Finally, the function prints the assignment of colors for each vertex.

python
Copy code
#Driver Code
if __name__ == '__main__':
This block of code checks if the script is being run as the main program.

python
Copy code
    g1 = [[] for i in range(5)]
    g1 = addEdge(g1, 0, 1)
    g1 = addEdge(g1, 0, 2)
    g1 = addEdge(g1, 1, 2)
    g1 = addEdge(g1, 1, 3)
    g1 = addEdge(g1, 2, 3)
    g1 = addEdge(g1, 3, 4)
This section of code creates a graph g1 with 5 vertices represented as an adjacency list. It then adds edges between vertices using the addEdge function.

python
Copy code
    print("Coloring of graph 1 ")
    greedyColoring(g1, 5)
It prints a message indicating the graph being colored and then calls the greedyColoring function to color the graph g1.

python
Copy code
    g2 = [[] for i in range(5)]
    g2 = addEdge(g2, 0, 1)
    g2 = addEdge(g2, 0, 2)
    g2 = addEdge(g2, 1, 2)
    g2 = addEdge(g2, 1, 4)
    g2 = addEdge(g2, 2, 4)
    g2 = addEdge(g2, 4, 3)
Similarly, this section creates another graph g2 and adds edges to it.

python
Copy code
    print("\nColoring of graph 2")
    greedyColoring(g2, 5)
It prints a message indicating the second graph being colored and then calls the greedyColoring function to color the graph g2.


# Hospital 

#Import the necessary libraries
import random
These lines import the random library, which is used later to choose a random diagnosis if no specific rule matches the symptoms provided by the user.

python
Copy code
#Define the knowledge base
knowledge_base = {
    "If the patient has a fever, then they may have a cold.": True,
    "If the patient has a cough, then they may have a cold.": True,
    "If the patient has a runny nose, then they may have a cold.": True,
}
Here, knowledge_base is a dictionary containing statements about symptoms and their possible diagnoses. Each statement is a key-value pair, where the key is the symptom statement and the value is True, indicating that having that symptom may lead to a cold.

python
Copy code
#Define the rules
rules = [
    "If the patient has a fever and a cough, then they definitely have a cold.",
    "If the patient has a fever and a runny nose, then they probably have a cold.",
    "If the patient has a cough and a runny nose, then they might have a cold.",
]
rules is a list containing rules based on combinations of symptoms. Each rule is a string representing a logical statement.

python
Copy code
#Define the function to find the diagnosis
def find_diagnosis(symptoms):
    # Check if the symptoms match any of the rules
    for rule in rules:
        if all(symptom in symptoms for symptom in rule.split(" ")):
            return rule

    # If no rules match, then return a random diagnosis
    return random.choice(list(knowledge_base.keys()))
This function find_diagnosis takes a list of symptoms as input and tries to find a diagnosis based on the rules defined. It iterates through the rules list and checks if all symptoms in a rule are present in the input list of symptoms. If a rule matches, it returns that rule. If no rules match, it randomly selects a diagnosis from the knowledge_base.

python
Copy code
#Get the symptoms from the user
symptoms = input("What are your symptoms? ").split(" ")
This line prompts the user to input their symptoms and splits the input string into a list of symptoms based on spaces.

python
Copy code
#Find the diagnosis
diagnosis = find_diagnosis(symptoms)
The find_diagnosis function is called with the symptoms provided by the user, and the result is stored in the variable diagnosis.

python
Copy code
#Print the diagnosis
print("The diagnosis is:", diagnosis)
Finally, the program prints the diagnosis to the user. If a matching rule is found, it prints the rule. Otherwise, it prints a randomly chosen diagnosis from the knowledge base.

# JOb Scheduling 

def printJobScheduling(arr, t):
This line defines a function named printJobScheduling that takes two arguments: arr, which is an array representing the jobs, and t, which is the number of time slots available.

python
Copy code
    n = len(arr)
This line calculates the length of the arr array, which represents the number of jobs.

python
Copy code
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
These lines sort the arr array based on the profit of each job in decreasing order. It iterates over each job in the array and compares the profit of adjacent jobs. If the profit of the current job is less than the profit of the next job, it swaps them.

python
Copy code
    result = [False] * t
    job = ['-1'] * t
These lines initialize two lists: result to keep track of free time slots and job to store the sequence of jobs. Both lists are initially filled with False and '1' respectively.

python
Copy code
    for i in range(len(arr)):
This line iterates through each job in the sorted arr array.

python
Copy code
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
This line iterates through the time slots available for scheduling the current job. It starts from the minimum of t - 1 and the deadline of the current job minus 1, and decrements down to -1.

python
Copy code
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
These lines check if the current time slot j is free. If it is, it marks that slot as occupied, assigns the current job to that slot, and breaks out of the loop.

python
Copy code
    print(job)
Finally, this line prints the sequence of jobs scheduled within the given time slots.

The driver's code initializes an array of job details, calls the printJobScheduling function with this array and the number of time slots available, and prints the sequence of jobs that maximizes profit.

# kruskal

class Graph:
This line defines a class named Graph to represent a graph data structure.

python
Copy code
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
This is the constructor method __init__ for the Graph class. It initializes the graph with the given number of vertices (vertices) and initializes an empty list graph to store the edges of the graph.

python
Copy code
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
This method add_edge adds an edge to the graph. It takes three parameters: u and v representing the vertices connected by the edge, and w representing the weight of the edge. The edge is represented as a list [u, v, w] and added to the graph list.

python
Copy code
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
This method find implements the find operation of the disjoint-set data structure. Given a vertex i and its parent array parent, it recursively finds the parent of the set to which i belongs.

python
Copy code
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
This method apply_union implements the union operation of the disjoint-set data structure. Given two vertices x and y, it merges the sets containing x and y. It also maintains the rank of each set to optimize the union operation.

python
Copy code
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
This method kruskal_algo implements Kruskal's algorithm to find the minimum spanning tree (MST) of the graph. It initializes an empty list result to store the MST edges, and variables i and e to iterate over the graph edges and count the edges added to the MST.

python
Copy code
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
This part of kruskal_algo iterates over the sorted edges of the graph. It checks if adding the current edge (u, v) to the MST will create a cycle. If not, it adds the edge to the MST, updates the parent and rank arrays, and increments the count of edges added to the MST.

python
Copy code
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))
Finally, this part of kruskal_algo prints the edges of the MST.

The remaining lines of code create a Graph instance g, add edges to it, and call the kruskal_algo method to find and print the MST of the graph.

# new Chat Bot

def greet():
    print("\nHello I am a chatbot for Gaco Bell. How can I help you ?")
    options = """ 1] Browse menu. \n 2] Order a takeout. \n 3] Book a table. \n 4] Exit"""
    print(options)
This function greet() prints a greeting message and options for the user.
python
Copy code
def greet_1():
    print("\nWhat else ?")
    options = """\n 1] Browse menu. \n 2] Order a takeout. \n 3] Book a table. \n 4] Exit"""
    print(options)
This function greet_1() prints a message asking for further actions and displays options.
python
Copy code
def menu():
    menu = """\nSNACK \n 1] Pohe \n 2] Vadapav \n 3] Pattice \n\n LUNCH \n 1] Vegthali
 2] Chickenthali \n 3] Andathali \n\n  DRINKS \n 1] Soda \n 2] Cocktail"""
    print(menu)
This function menu() prints the menu items.
python
Copy code
def order():
    menu = ["pohe", "vadapav", "pattice", "vegthali", "chickenthali", "andathali", "soda", "cocktail"]
    print("\nWhat would you like to order ?")
    while(True):
        item = input().lower()
        if(item not in menu):
            print("Sorry. We do not serve this item. Choose another item.")
        else:
            break
    number = int(input("how many ? \n"))
    address = input("enter address : ")
    name = input("enter name : ")
    order = {"item" : item, "number": number, "name":name, "address": address}
    print("here is the summary.")
    print(order)
This function order() takes orders from the user, including item, quantity, address, and name, and prints a summary.
python
Copy code
def book():
    date = input("Enter the date.")
    print("Time for booking ?")
    time = input()
    number = int(input("how many people ? \n"))
    name = input("enter name : ")
    booking = {"name":name, "number": number, "date": date, "time": time}
    print("here is the summary.")
    print(booking)
This function book() takes booking details from the user, including date, time, number of people, and name, and prints a summary.
python
Copy code
def end():
    print('Goodbye, have a nice day!')
    print('.................................')
    print('.................................')
    quit()
This function end() prints a goodbye message and exits the program.
Function Calls:
python
Copy code
greet()    
Calls the greet() function to print the initial greeting and options for the user.
Loop for User Interaction:
python
Copy code
while(True):
    option = input()
    if(option == "1" or option == "Browse menu"):
        menu()
    elif(option == "2" or option == "Order a takeout"):
        order()
    elif(option == "3" or option == "Book a table"):
        book()
    elif(option == "4" or option == "Exit"):
        end()
        break
    else:
        print("Please enter a valid choice.")
    greet_1()
This loop continuously takes input from the user and performs actions based on their choice.
Depending on the user input, it calls the corresponding function (menu(), order(), book(), end()).
If the user chooses to exit (option == "4" or "Exit"), it calls the end() function to exit the program. Otherwise, it continues the loop.
After each action, it calls the greet_1() function to prompt the user for further actions.

# n queens 
User Input for Number of Queens:
python
Copy code
print ("Enter the number of queens")
N = int(input())
Asks the user to input the number of queens (N) they want to place on the chessboard.
Initialization of the Chessboard:
python
Copy code
board = [[0]*N for _ in range(N)]
Initializes an empty chessboard (board) of size N x N represented as a 2D list with all elements set to 0.
Function to Check if Queen is Under Attack:
python
Copy code
def is_attack(i, j):
Defines a function is_attack(i, j) to check if a queen placed at position (i, j) is under attack by any other queen.
Checks if there is already a queen in the same row, column, or diagonals.
Function to Place Queens on the Chessboard:
python
Copy code
def N_queen(n):
Defines a recursive function N_queen(n) to place n queens on the chessboard.
Uses backtracking to explore all possible combinations of queen placements.
Queen Placement Logic:
The function tries to place a queen at each position (i, j) on the chessboard.
It checks if placing a queen at (i, j) is safe by calling the is_attack function.
If it's safe, it places the queen at (i, j) and recursively tries to place the remaining queens.
If placing the remaining queens leads to a solution (N_queen(n-1)==True), it returns True.
If not, it removes the queen from (i, j) and tries the next position.
Print the Final Board Configuration:
python
Copy code
N_queen(N)
for i in board:
    print(i)
Calls the N_queen function to place N queens on the chessboard.
Prints the final configuration of the chessboard after placing the queens. Each row represents a row in the chessboard, with 1 indicating the position of a queen and 0 indicating an empty square.

# prims algorithm


Let's break down the code:

Initialization:
python
Copy code
INF = 9999999
N = 5
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]
selected_node = [0, 0, 0, 0, 0]
no_edge = 0
selected_node[0] = True
INF is a constant representing infinity, used for initialization.
N represents the number of vertices in the graph.
G is the adjacency matrix representing the graph.
selected_node is a list to keep track of selected nodes.
no_edge counts the number of edges.
Prim's Algorithm Implementation:
python
Copy code
print("Edge : Weight\n")
while (no_edge < N - 1):
Starts a loop until the number of edges selected is less than N - 1.
Finding Minimum Weight Edge:
python
Copy code
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
Loops through all vertices (m) and their adjacent vertices (n).
Finds the minimum weight edge (a, b) that connects a selected vertex m to an unselected vertex n.
Printing Selected Edge and Weight:
python
Copy code
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
Prints the selected edge (a, b) and its weight.
Marks vertex b as selected.
Increments the count of selected edges (no_edge).
Output:
The program prints the edges and their weights selected by Prim's Algorithm. Each line represents an edge in the Minimum Spanning Tree (MST).

# selection sort
Initialization:
python
Copy code
A = [64, 25, 12, 22, 11]
Initializes the list A with some integer values.
Selection Sort Algorithm:
python
Copy code
for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
Iterates through each element in the list.
For each element at index i, it finds the index (min_idx) of the minimum element from i to the end of the list.
If it finds an element smaller than the current minimum element, it updates min_idx.
After finding the minimum element, it swaps the current element with the minimum element.
Print the Sorted Array:
python
Copy code
print("Sorted array : ")
for i in range(len(A)):
    print("%d" % A[i], end=" ")
Prints the sorted array after sorting.
Each element of the sorted array is printed on the same line separated by spaces.
Output:
The program prints the sorted array in ascending order.


# stockmarket

Class Definition:
python
Copy code
class StockMarketTradingSystem:
Defines a class named StockMarketTradingSystem to manage stock trading operations.
Initializer:
python
Copy code
def __init__(self):
    self.portfolio = {}
Initializes the portfolio attribute as an empty dictionary to store the stocks and their quantities.
Method to Buy Stock:
python
Copy code
def buy_stock(self, symbol, quantity):
    # Simulated logic for buying a stock
    if symbol in self.portfolio:
        self.portfolio[symbol] += quantity
    else:
        self.portfolio[symbol] = quantity
    print(f"Bought {quantity} shares of {symbol}")
Adds the specified quantity of a stock to the portfolio.
If the stock is already in the portfolio, the quantity is incremented.
If the stock is not in the portfolio, a new entry is created.
Prints a message indicating the purchase.
Method to Sell Stock:
python
Copy code
def sell_stock(self, symbol, quantity):
    # Simulated logic for selling a stock
    if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
        self.portfolio[symbol] -= quantity
        print(f"Sold {quantity} shares of {symbol}")
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]
    else:
        print("Not enough shares to sell.")
Removes the specified quantity of a stock from the portfolio if available.
If there are not enough shares to sell, it prints a message.
If all shares of a stock are sold, the entry is removed from the portfolio.
Method to Show Portfolio:
python
Copy code
def show_portfolio(self):
    print("Portfolio:")
    for symbol, quantity in self.portfolio.items():
        print(f"{symbol}: {quantity} shares")
Prints the current portfolio showing each stock symbol and its quantity.
Example Usage:
python
Copy code
if __name__ == "__main__":
    trading_system = StockMarketTradingSystem()
    trading_system.buy_stock("AAPL", 10)
    trading_system.buy_stock("MSFT", 5)
    trading_system.sell_stock("AAPL", 3)
    trading_system.sell_stock("GOOG", 2)  # Not enough shares to sell
    trading_system.show_portfolio()
Creates an instance of the StockMarketTradingSystem.
Buys and sells stocks, then displays the updated portfolio.




