import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))

# Game clock
clock = pygame.time.Clock()

# Game time variables
game_time = 0  # Time in seconds
time_multiplier = 1  # Controls the speed of time (e.g., 1 for real-time, 2 for double speed)

# Game loop
running = True

while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                time_multiplier = 2  # Double the speed of time when spacebar is pressed
            if event.key == pygame.K_1:
                time_multiplier = 1
            if event.key == pygame.K_3:
                time_multiplier = 10

    # Update game logic

    # Get the time passed since the last frame in milliseconds
    delta_time = clock.tick(60)

    # Update the game time based on the time passed and the time multiplier
    game_time += delta_time / 1000.0 * time_multiplier

    # Render game graphics
    window.fill((0, 0, 0))

    # Display game time
    font = pygame.font.Font(None, 36)
    time_text = font.render(f"Time: {int(game_time)} seconds", True, (255, 255, 255))
    window.blit(time_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()






"""
    60 frames per second real time
    3600 seconds per hour

    216000 frames per hour real time

    54000 frames per season in game
    18000 frames per 30 day month in game
    600 frames per day (of 360 in a year) in game
    25 frames per hour in game



    1 year in game is 60 minutes in real time

"""





