import pygame


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # cost from start node to current node
        self.h = 0  # heuristic cost from current node to target node
        self.f = 0  # total cost (g + h)


def astar(start, target, obstacles):
    open_list = []
    closed_list = []

    start_node = Node(start)
    target_node = Node(target)

    open_list.append(start_node)

    while open_list:
        current_node = open_list[0]
        current_index = 0

        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node.position == target_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get the correct order

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )

            if (
                node_position[0] < 0
                or node_position[0] >= WIDTH
                or node_position[1] < 0
                or node_position[1] >= HEIGHT
            ):
                continue

            if node_position in obstacles:
                continue

            new_node = Node(node_position, current_node)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = (
                (child.position[0] - target_node.position[0]) ** 2
                + (child.position[1] - target_node.position[1]) ** 2
            )
            child.f = child.g + child.h

            if child in open_list:
                if child.g > current_node.g:
                    continue

            open_list.append(child)


def find_shortest_path(start, target, obstacles):
    return astar(start, target, obstacles)


# Pygame initialization
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Obstacles
obstacles = [(1,2), (2,3), (5,7), (2,2), (5,2), (3,3), (6,7), (7,7), (5,3),(4,3)]

# Start and target positions
start_pos = (0, 0)
target_pos = (10,10)

# Find the shortest path
path = find_shortest_path(start_pos, target_pos, obstacles)
print("Shortest Path:", path)

# Draw the search process and obstacles on the screen
def draw_grid():
    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 20):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_rect(position, color):
    rect = pygame.Rect(position[0] * 20, position[1] * 20, 20, 20)
    pygame.draw.rect(screen, color, rect)

def draw_path(path):
    for position in path:
        draw_rect(position, GREEN)

def draw_obstacles(obstacles):
    for position in obstacles:
        draw_rect(position, RED)

import time
# Game loop
running = True
while running:
    screen.fill(BLACK)

    draw_grid()
    draw_path(path)
    
    draw_obstacles(obstacles)
    

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
