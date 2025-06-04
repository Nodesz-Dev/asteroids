import pygame
from constants import *
from player import *

def main():
    # initialise pygame and set screen size 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a clock object and dt variable for use in handling tick rate of the program
    clock = pygame.time.Clock()
    dt = 0

    # Create the containers we are using to orgnise objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Create and set container variable for all future player objects
    Player.containers = (updatable, drawable)
    # Create the players object
    player = Player((SCREEN_WIDTH/2), 
                    (SCREEN_HEIGHT/2))
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the background of the screen with Black
        screen.fill([0,0,0,255])
        
        # Update all updatable objects
        for thing in updatable:
            thing.update(dt)

        # Draw all drawable objects
        for thing in drawable:
            thing.draw(screen)

        # Apply all drawn objects to screen
        pygame.display.flip()

        # Get the delta time of the last tick of the program (Have locked it to max of 60 ticks a second)
        dt = clock.tick(60)/1000
    


if __name__ == "__main__":
    main()