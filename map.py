# start node
# end node,

# nodes have 2< boarding spaces

# open set is all nodes current (including start/finish node)

# function to find a node


# Let the node at which we are starting be called the initial node. Let the distance of node Y be the distance from the initial node to Y. Dijkstra's algorithm will assign some initial distance values and will try to improve them step by step.

# Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes.

# Mark all nodes unvisited. Set the initial node as current. Create a set of the unvisited nodes called the unvisited set consisting of all the nodes.

# For the current node, consider all of its unvisited neighbors and calculate their tentative distances. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B (through A) will be 6 + 2 = 8.

# When we are done considering all of the neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.

# If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.

# Select the unvisited node that is marked with the smallest tentative distance, and set it as the new "current node" then go back to step 3.

def node_test(GRAPH, X, Y):
    if GRAPH[X][Y] == 1:
        return False
    
    else:
        intersects = 0
        paths = []
        if GRAPH[X-1][Y] == 0:
            intersects +=1
            paths.append('N')
        if GRAPH[X][Y+1] == 0:
            intersects +=1
            paths.append('E')
        if GRAPH[X+1][Y] == 0:
            intersects +=1
            paths.append('S')
        if GRAPH[X][Y-1] == 0:
            intersects +=1
            paths.append('W')
    
        # print paths
        
        if intersects > 2:
            return True
        else:
            return False
    

def main():
    GRAPH = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    initial = (1,1)
    goal = (10, 10)
    # GRAPH[initial[0]][initial[1]] = 'X'
    # GRAPH[goal[0]][goal[1]] = 'Z'
    
    nodes = [initial]
    
    print ''
    
    row_pos = 0
    for line in GRAPH:
        col_pos = 0
        row = ''
        for i in line:
            row += (str(i) + ' ')
            if node_test(GRAPH, row_pos, col_pos) == True:
                nodes.append( (row_pos, col_pos))
            col_pos +=1
        print row
        row_pos +=1
    nodes.append(goal)
    
    print '\ninitial: ' + str(initial)
    print '   goal: ' + str(goal)
    
    # print node_test(GRAPH, 6, 1)
    print nodes
    
# Tests a coord to see if it is  a node
# def Node_Test(X,Y, GRAPH):
    # if graph[X][Y] has 3 or more 0's adj
    
if __name__ == '__main__':
  main()