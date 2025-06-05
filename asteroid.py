from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__time_since_spawned__ = 0

    def is_self(self, other):
        return (self.position.x == other.position.x and 
                self.position.y == other.position.y and
                self.radius == other.radius and 
                self.velocity == other.velocity)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           "white",
                            self.position,
                            self.radius,
                            2)          
    
    def update(self, dt):
        self.position += self.velocity * dt
        if self.__time_since_spawned__ <= ASTEROID_PASS_THROUGH_TIME:
            self.__time_since_spawned__ += dt

    def pass_through(self):
        if self.__time_since_spawned__ <= ASTEROID_PASS_THROUGH_TIME:
            return True
        return False
        

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        number_of_splits = random.uniform(ASTEROID_MIN_SPLITS,ASTEROID_MAX_SPLITS)
        random_rotation = random.uniform(0,90)
        rotation_increment = 360 / number_of_splits
        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroids = []

        counter = 0
        while counter < number_of_splits:
            
            asteroid = Asteroid(self.position.x, 
                                self.position.y, 
                                new_asteroids_radius)
            
            new_asteroids.append(asteroid)

            counter += 1

        for thing in new_asteroids:
            thing.velocity = self.velocity.rotate(random_rotation)
            random_rotation += rotation_increment
            asteroid.velocity *= random.uniform(ASTEROID_MIN_SPLIT_SPEED,
                                                ASTEROID_MAX_SPLIT_SPEED)
            

        