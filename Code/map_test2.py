import pygame
import numpy as np
import pickle

# Initialize pygame
pygame.init()

# Constants for terrain colors and rect size
TERRAIN_COLORS = {
    "water": (0, 0, 255),
    "beach": (255, 255, 102),
    "forest": (0, 255, 0),
    "rocky mountain": (139, 69, 19),
    "snowy peak": (255, 255, 255),
    "desert": (255, 204, 102),
    "grassland": (173, 255, 47),
    "swamp": (0, 128, 128),
    "canyon": (255, 153, 51),
    "volcano": (153, 0, 0),
    "tundra": (204, 204, 255),
    "jungle": (34, 139, 34),
    "savanna": (255, 215, 0),
    "iceberg": (194, 255, 254),
    "badlands": (184, 65, 0),
    "oasis": (0, 102, 0),
    "lava flow": (255, 97, 3),
    "mesa": (255, 140, 26),
    "tropical island": (0, 204, 153),
    "glacier": (135, 206, 250),
    # Add more terrains here
}

RECT_SIZE = 5
ZOOMED_RECT_SIZE = 64

# Load numpy array from pickle file
with open("adjusted_noise.pkl", "rb") as file:
    island_data = pickle.load(file)

# Create a surface to display the island map
map_surface = pygame.Surface((island_data.shape[1] * RECT_SIZE, island_data.shape[0] * RECT_SIZE))

# Draw colored rects on the map surface based on the terrain data
for y in range(island_data.shape[0]):
    for x in range(island_data.shape[1]):
        value = island_data[y, x]
        if value <= 0.05:
            color = TERRAIN_COLORS["water"]
        elif value <= 0.1:
            color = TERRAIN_COLORS["beach"]
        elif value <= 0.15:
            color = TERRAIN_COLORS["swamp"]
        elif value <= 0.2:
            color = TERRAIN_COLORS["desert"]
        elif value <= 0.26:
            color = TERRAIN_COLORS["grassland"]
        elif value <= 0.3:
            color = TERRAIN_COLORS["rocky mountain"]
        elif value <= 0.35:
            color = TERRAIN_COLORS["canyon"]
        elif value <= 0.4:
            color = TERRAIN_COLORS["tundra"]
        elif value <= 0.45:
            color = TERRAIN_COLORS["forest"]
        elif value <= 0.5:
            color = TERRAIN_COLORS["jungle"]
        elif value <= 0.55:
            color = TERRAIN_COLORS["badlands"]
        elif value <= 0.6:
            color = TERRAIN_COLORS["mesa"]
        elif value <= 0.65:
            color = TERRAIN_COLORS["savanna"]
        elif value <= 0.7:
            color = TERRAIN_COLORS["oasis"]
        elif value <= 0.75:
            color = TERRAIN_COLORS["snowy peak"]
        elif value <= 0.8:
            color = TERRAIN_COLORS["iceberg"]
        elif value <= 0.85:
            color = TERRAIN_COLORS["lava flow"]
        elif value <= 0.9:
            color = TERRAIN_COLORS["volcano"]
        else:
            color = TERRAIN_COLORS["water"]

        pygame.draw.rect(map_surface, color, pygame.Rect(x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE))

# Save the map as an image (e.g., PNG format)
pygame.image.save(map_surface, "island_map.png")

# Function to generate the zoomed map surface
def generate_zoomed_surface(source_surface, zoom_factor):
    zoomed_size = (int(source_surface.get_width() * zoom_factor), int(source_surface.get_height() * zoom_factor))
    return pygame.transform.scale(source_surface, zoomed_size)

# Initialize Pygame display for viewing the zoomed map
window_size = (1440,3088)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Zoomed Island Map")

# Set initial map position for panning
map_x, map_y = 0, 0

# Zoom settings
zoomed = False
zoom_factor = ZOOMED_RECT_SIZE / RECT_SIZE
zoom_x, zoom_y = 0, 0
zoomed_map_surface = None  # Variable to store the zoomed map surface

# Game loop for map display and movement
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Read arrow key input for map movement
            map_speed = 5
            if event.key == pygame.K_DOWN:
                if zoomed:
                    zoom_y += map_speed * zoom_factor
                else:
                    map_y += map_speed
            elif event.key == pygame.K_UP:
                if zoomed:
                    zoom_y -= map_speed * zoom_factor
                else:
                    map_y -= map_speed
            elif event.key == pygame.K_RIGHT:
                if zoomed:
                    zoom_x += map_speed * zoom_factor
                else:
                    map_x += map_speed
            elif event.key == pygame.K_LEFT:
                if zoomed:
                    zoom_x -= map_speed * zoom_factor
                else:
                    map_x -= map_speed
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Left mouse button click to zoom in on a point
            zoomed = not zoomed
            if zoomed:
                # Calculate the clicked point's position on the zoomed map
                zoom_x, zoom_y = event.pos
                print(zoom_x,zoom_y)
                zoom_x /= 5
                zoom_x *= 64
                zoom_y /= 5
                zoom_y *= 64
                zoom_x -= (window_size[0] // 2)
                zoom_y -= (window_size[1] // 2)
                # Generate the zoomed map surface
                zoomed_map_surface = generate_zoomed_surface(map_surface, zoom_factor)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Display the map (overview or zoomed-in)
    if zoomed:
        screen.blit(zoomed_map_surface, (map_x - zoom_x, map_y - zoom_y))
    else:
        screen.blit(map_surface, (map_x, map_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
