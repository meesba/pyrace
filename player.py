import arcade
import math

class Player(arcade.Sprite):
    """ Player class """

    def __init__(self, image, scale):
        """ Set up the player """

        # Call the parent init
        super().__init__(image, scale)

        # Create a variable to hold our speed. 'angle' is created by the parent
        self.speed = 0

        self.thrust = 0
        self.max_speed = 6
        self.drag = 0.05

    def update(self):
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y
        # # Convert angle in degrees to radians.
        # angle_rad = math.radians(self.angle)

        # # Rotate the ship
        self.angle += self.change_angle

        # # Use math to find our change based on our speed and angle
        # self.center_x += -self.speed * math.sin(angle_rad)
        # self.center_y += self.speed * math.cos(angle_rad)