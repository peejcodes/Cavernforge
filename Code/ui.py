import pygame

class UI:
    def __init__(self, screen_width, screen_height):
        """
        Initialize the UI class with the screen width and height.

        Args:
            screen_width (int): The width of the screen.
            screen_height (int): The height of the screen.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.health = 100
        self.citizens = 7
        self.money = 1000
        # Initialize Pygame and create the screen surface
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Dwarf/Elf Simulation")

        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (128, 128, 128)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Create UI elements
        self.background_surface = pygame.Surface((screen_width, screen_height))
        self.background_surface.fill(self.WHITE)

        self.minimap_surface = pygame.Surface((200, 250))
        self.minimap_surface.fill(self.GRAY)
        
        self.minimap_surface2 = pygame.Surface((220, 270))
        self.minimap_surface2.fill(self.BLACK)

        self.button_surface = pygame.Surface((screen_width, 64))
        self.button_surface.fill(self.BLACK)

        self.info_bar_surface = pygame.Surface((screen_width, 100))
        self.info_bar_surface.fill(self.BLACK)
        
        self.notifications_bar = pygame.Surface((64, screen_height-100))
        self.notifications_bar.fill(self.BLUE)
        
        self.fontsize = 18
        self.font = pygame.font.Font('../Font/alagard.ttf'  , self.fontsize)  # You can specify the font file path and size

        
              # Create a tooltip surface
        self.tooltip_surface = pygame.Surface((200, 50))
        self.tooltip_surface.fill(self.WHITE)
        self.tooltip_font = pygame.font.Font(None, 24)  # Choose the desired tooltip font and size

        # Define tooltip text and position
        self.tooltip_text = "              tooltip"
        self.tooltip_position = (20,100)


#Shikashi's Fantasy Icons Pack v2/antidote_potion1.png
        self.button_images = [
            pygame.image.load('../Graphics/UI/Shikashi/mining3.png'),
            pygame.image.load('../Graphics/UI/Shikashi/woodcutting3.png'),
            pygame.image.load('../Graphics/UI/Shikashi/basket.png'),
            pygame.image.load('../Graphics/UI/Shikashi/hammer.png'),
            pygame.image.load('../Graphics/UI/Shikashi/stonemason.png'),
            pygame.image.load('../Graphics/UI/Shikashi/zoning.png'),
            pygame.image.load('../Graphics/UI/Shikashi/money6.png'),
            pygame.image.load('../Graphics/UI/Shikashi/inventory.png'),
            pygame.image.load('../Graphics/UI/Shikashi/gear.png'),
            pygame.image.load('../Graphics/UI/Shikashi/map.png')
        ]

        self.button_functions = [
            self.button1_function,
            self.button2_function,
            self.button3_function,
            self.button4_function,
            self.button5_function,
            self.button6_function,
            self.button7_function,
            self.button8_function,
            self.button9_function,
            self.button10_function
        ]

    def draw_ui(self):
        """
        Draw the UI elements on the screen.
        """
        # Draw the background surface
        self.screen.blit(self.background_surface, (0, 0))

        # Draw the info bar along the top of the screen
        self.screen.blit(self.info_bar_surface, (0,0))
        
        #self.write_info(f"Health: {self.health}")
        self.write_info('info')
        
        minimap_bg = pygame.image.load('../Graphics/UI/Shikashi/minimap_bg.png')
        
        
        # Draw the minimap in the top right corner of the screen
        self.screen.blit(self.minimap_surface2, (self.screen_width - 230, 5))
        self.screen.blit(minimap_bg, (self.screen_width - 230, 5))
        self.screen.blit(self.minimap_surface, (self.screen_width - 220, 15))
        
        # Draw the notifications bar along the left of the screen
        #self.screen.blit(self.notifications_bar, (0,100))
        
        # Draw the button row along the bottom
        self.screen.blit(self.button_surface, (0, self.screen_height -64))
        
    
        # Calculate the total width of all buttons and spacing
        total_buttons = len(self.button_images)
        button_width = 64 # Width of the button images
        spacing = 5 # Fixed spacing between buttons
    
        total_width = (button_width * total_buttons) + (spacing * (total_buttons - 1))
    
        # Calculate the starting x position to center the buttons
        start_x = (self.screen_width - total_width) // 2
    
        # Draw the buttons
        button_height = 64
        y = self.screen_height - button_height
        for i, image in enumerate(self.button_images):
            x = start_x + (button_width + spacing) * i
            button_rect = pygame.Rect(x, y, button_width, button_height)
            self.screen.blit(image, button_rect.topleft)
    
         # Draw the buttons and handle tooltips
        for i, image in enumerate(self.button_images):
            x = start_x + (button_width + spacing) * i
            button_rect = pygame.Rect(x, y, button_width, button_height)
            self.screen.blit(image, button_rect.topleft)

 #           # Check if the mouse is hovering over the button
#            if button_rect.collidepoint(pygame.mouse.get_pos()):
#                self.tooltip_text = f"Button {i+1} Tooltip"  # Update the tooltip text
#                self.tooltip_position = pygame.mouse.get_pos()  # Update the tooltip position

 #       # Draw the tooltip if there is text
#        if self.tooltip_text:
#            tooltip_text_rendered = self.tooltip_font.render(self.tooltip_text, True, self.BLACK)
#            tooltip_rect = tooltip_text_rendered.get_rect(center=self.tooltip_position)
#            self.tooltip_surface.fill(self.WHITE)
#            self.tooltip_surface.blit(tooltip_text_rendered, tooltip_rect)
#            self.screen.blit(self.tooltip_surface, (0, 0))

        pygame.display.flip()
        
    
    def handle_button_click(self, pos):
        """
        Handle button click events.
    
        Args:
            pos (tuple): The position of the click event.
        """
        button_width = 64  # Width of the button images
        spacing = 1# Fixed spacing between buttons
    
        total_buttons = len(self.button_images)
        total_width = (button_width * total_buttons-1) + (spacing * (total_buttons - 1))
        start_x = (self.screen_width - total_width) // 2
    
        button_height = 64
        y = self.screen_height - button_height
    
        for i in range(total_buttons):
            button_x = start_x + (button_width + spacing) * i
            button_rect = pygame.Rect(button_x, y, button_width, button_height)
            if button_rect.collidepoint(pos):
                self.button_functions[i]()
            
            
            
    def write_info(self, text):
        """
        Render and display the provided text on the info bar surface.

        Args:
            text (str): The text to be displayed.
        """
        self.info = [f"Health: {self.health}", f"Citizens: {self.citizens}", f"Money: ${self.money}.00"]

        
        # Clear the text that is on there
        self.info_bar_surface.fill(self.BLACK)
        # Render the text
        for index, text in enumerate(self.info):
            rendered_text = self.font.render(text, True, self.WHITE)
        # Position the text on the info bar surface
            text_rect = rendered_text.get_rect(center=(self.screen_width // 4, self.info_bar_surface.get_height() // 4 + (index*self.fontsize) ))

        # Blit the text onto the info bar surface
            self.info_bar_surface.blit(rendered_text, text_rect)


    def button1_function(self):
        """
        Function to be executed when button 1 is clicked.
        """
        print("Mining enabled")

    def button2_function(self):
        """
        Function to be executed when button 2 is clicked.
        """
        print("Woodcutting enabled")

    def button3_function(self):
        """
        Function to be executed when button 3 is clicked.
        """
        print("Gathering enabled")

    def button4_function(self):
        """
        Function to be executed when button 4 is clicked.
        """
        print("Build menu")

    def button5_function(self):
        """
        Function to be executed when button 5 is clicked.
        """
        print("Stonemasonry")

    def button6_function(self):
        """
        Function to be executed when button 6 is clicked.
        """
        print("Zoning")

    def button7_function(self):
        """
        Function to be executed when button 7 is clicked.
        """
        print("Economy")
        self.money+=1000
        self.write_info(self.info)

    def button8_function(self):
        """
        Function to be executed when button 8 is clicked.
        """
        print("Inventory")
       

    def button9_function(self):
        """
        Function to be executed when button 9 is clicked.
        """
        print("Gear")
        self.health += 7
        self.write_info(self.info)

    def button10_function(self):
        """
        Function to be executed when button 10 is clicked.
        """
        print("World map")
        self.citizens += 3
        self.write_info(self.info)


# Example usage
ui = UI(720, 1440)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                ui.handle_button_click(mouse_pos)
    import time
    ui.draw_ui()
    ui.health -= 1
    time.sleep(1)

pygame.quit()
