from maze import Maze
from exception import PathNotFoundException
from stack import Stack
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
        self.mem = []
        m = len(self.navigator_maze)
        n = len(self.navigator_maze[0])
        
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(0)
            self.mem.append(grid_row)
            
            
    def is_valid(self,x,y):
        return ((0<=x<len(self.navigator_maze[0]))and(0<=y<len(self.navigator_maze))and(self.navigator_maze[x][y]==0)and(self.mem[x][y]==0))
        
        
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
       
       s = Stack()
       s.push(start)
      
       while not s.is_empty():
            x1 = s.top()[0]
            y1 = s.top()[1]
            self.mem[x1][y1]=1
            if(x1==end[0] and y1==end[1]):
                return(s.to_list())
            elif (self.is_valid(x1 + 1, y1)):
                s.push((x1 + 1, y1))
                self.mem[x1 + 1][y1] = 1
            elif (self.is_valid(x1 - 1, y1)):
                s.push((x1 - 1, y1))
                self.mem[x1 - 1][y1] = 1
            elif (self.is_valid(x1, y1 - 1)):
                s.push((x1, y1 - 1))
                self.mem[x1][y1 - 1] = 1
            
            elif (self.is_valid(x1, y1 + 1)):
                s.push((x1, y1 + 1))
                self.mem[x1][y1 + 1] = 1
            else:
                s.pop()
       raise PathNotFoundException
