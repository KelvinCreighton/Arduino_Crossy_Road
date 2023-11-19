import pygame
import random
import requests
from PIL import Image
from io import BytesIO
def load_image(url):
    response = requests.get(url)
    image = pygame.image.load(BytesIO(response.content))
    return image

# GitHub repository URL for characters (replace with your repository URL)
repo_url = "https://github.com/KelvinCreighton/Arduino_Crossy_Road.git"


# List of character URLs
cars =["car.png, car_2.png, car_3.png"]
playerpic=["player.png, player_2.png, player_3.png, player_4.png, player_5.png, player_1.png"]
tree = ["tree.png, log.png"]
picture_path = random.choice(playerpic)

# Open the image using Pillow
img = Image.open(picture_path)

# Display the image
img.show()


class Player:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, w, h)
        self.color = (0, 128, 255)
        self.lives = 3

    def move_x(self, amount):
        self.x += amount
    
    def move_y(self, amount):
        self.y += amount

    def update(self, cam_x, cam_y):
        self.rect.x = self.x + cam_x
        self.rect.y = self.y + cam_y

    def collides_with(self, enemy):
        buffer = 1
        return self.rect.x+self.rect.w-buffer > enemy.rect.x and self.rect.x+buffer < enemy.rect.x+enemy.rect.w and self.rect.y+self.rect.h-buffer > enemy.rect.y and self.rect.y+buffer < enemy.rect.y+enemy.rect.h
    
    def out_of_bounds(self, screen_width, screen_height):
        return self.rect.x+self.rect.w < 0 or self.rect.x > screen_width or self.rect.y+self.rect.h < 0 or self.rect.y > screen_height
    
    def draw(self, screen):
        pygame.image.load(random.choice(playerpic))
        


class Enemy:
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, w, h)
        self.speed = speed
        self.color = (255, 0, 0)

    def update(self, cam_x, cam_y):
        self.rect.x = self.x + cam_x
        self.rect.y = self.y + cam_y
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def move(self):
        self.x += self.speed
    