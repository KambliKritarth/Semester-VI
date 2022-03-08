tree = {
  '1' : [[1,2,3],[0,4,6],[7,5,8]],
  '2' : [[1,2,3],[4,0,6],[7,5,8]],
  '3' : [[1,2,3],[7,4,6],[0,5,8]],
  '4' : [[0,2,3],[1,4,6],[7,5,8]],
  '5' : [[1,2,3],[4,6,0],[7,5,8]],
  '6' : [[1,2,3],[4,5,6],[7,0,8]],
  '7' : [[1,2,3],[0,4,6],[7,5,8]],
  '8' : [[1,0,3],[4,2,6],[7,5,8]],
  '9' : [[1,2,3],[7,4,6],[5,0,8]],
  '10' : [[1,2,3],[0,4,6],[7,5,8]],
  '11' : [[2,0,3],[1,4,6],[7,5,8]],
  '12' : [[1,2,3],[0,4,6],[7,5,8]],
  '13' : [[1,2,3],[4,6,8],[7,5,0]],
  '14' : [[1,2,3],[4,0,6],[7,5,8]],
  '15' : [[1,2,0],[4,6,3],[7,5,8]],
  '16' : [[1,2,3],[4,5,6],[7,8,0]],
  '17' : [[1,2,3],[4,0,6],[7,5,8]],
  '18' : [[1,2,3],[4,5,6],[0,7,8]]
}
goal = [[1,2,3],[4,5,6],[7,8,0]]
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, tree, node): #function for BFS
    visited.append(node)
    queue.append(node)
    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print (m) 
        for neighbour in tree[m]:
            if neighbour == goal:
                print(neighbour)
            if neighbour not in visited:
                visited.append(neighbour)
            queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, tree, '5') 