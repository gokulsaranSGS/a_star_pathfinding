import pygame
import math
from queue import PriorityQueue

WIDTH = 700
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* path finding algorithm")


RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)

class Node:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row* width
        self.y = col* width
        self.color = WHITE
        self.neighbor = []
        self.width = width
        self.total_rows = total_rows
    
    def get_position(self):
        return self.row ,self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color ==BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE
    
    def make_start(self):
        self.color = ORANGE
    
    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_path(self):
        self.color = PURPLE
    
    def draw(self,WIN):
        pygame.draw.rect(WIN,self.color,(self.x ,self.y,self.width,self.width))

    def update_neighbor(self,grid):
        self.neighbor = []
        if self.row <self.total_rows -1 and not grid[self.row + 1] [self.col].is_barrier():#down
            self.neighbor.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # up
            self.neighbor.append(grid[self.row - 1][self.col])

        if self.col <self.total_rows -1 and not grid[self.row][self.col+1].is_barrier():#right   
            self.neighbor.append(grid[self.row ][self.col+1])

        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():#right
            self.neighbor.append(grid[self.row ][self.col-1])

    def __lt__(self,other):
        return False
    
    
def h(p1,p2):
    #manhatten distance formula and this is the firsttime using it 
    x1,y1= p1
    x2,y2 = p2 
    return abs(x1-x2)+abs(y1-y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = { (node.row, node.col): float("inf") for row in grid for node in row }
    f_score = { (node.row, node.col): float("inf") for row in grid for node in row }
    g_score[(start.row, start.col)] = 0
    f_score[(start.row, start.col)] = h(start.get_position(), end.get_position())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbor:
            temp_g_score = g_score[(current.row, current.col)] + 1

            if temp_g_score < g_score[(neighbor.row, neighbor.col)]:
                came_from[neighbor] = current
                g_score[(neighbor.row, neighbor.col)] = temp_g_score
                f_score[(neighbor.row, neighbor.col)] = temp_g_score + h(neighbor.get_position(), end.get_position())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[(neighbor.row, neighbor.col)], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

'''
def algorithm(draw , grid , start , end):
    count = 0
    open_set= PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}
    g_score ={node:float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score ={node:float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_position(),end.get_position())

    open_set_hash = {start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            return True #make the final path

        for neighbor in current.neighbor:
            temp_g_score= g_score[current]+1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[current] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_position(),end.get_position())
                if neighbor not in open_set_hash:
                    count +=1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current!= start:
            current.make_closed()
    return False'''
def make_grid(rows,width):
    grid =[]
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,gap,rows)
            grid[i].append(node)
    return grid

def draw_grid(win,rows,width):
    gap = width//rows
    for i in range (rows):
        pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))
        for j in range (rows):
            pygame.draw.line(win,GREY,(j*gap,0),(j*gap,width))

def draw(win,grid,rows,width):
    win.fill(WHITE)

    for row in grid:
        for node  in row:
            node.draw(win)

    draw_grid(win,rows,width)
    pygame.display.update()

def get_clicked_position(pos,rows,width):
    gap = width//rows
    y,x = pos
    row = y // gap
    col = x // gap
    return row,col

def main(win, width):
    ROWS = 60
    grid = make_grid(ROWS, width)
    start = None
    end = None

    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, ROWS, width)
                if 0 <= row < ROWS and 0 <= col < ROWS:  
                    node = grid[row][col]
                    if not start and node != end:
                        start = node
                        start.make_start()
                    elif not end and node != start:
                        end = node
                        end.make_end()
                    elif node != end and node != start:
                        node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, ROWS, width)
                if 0 <= row < ROWS and 0 <= col < ROWS:  
                    node = grid[row][col]
                    node.reset()
                    if node == start:
                        start = None
                    elif node == end:
                        end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbor(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN,WIDTH)