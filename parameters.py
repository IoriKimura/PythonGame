import pygame

pygame.mixer.init()
player_attack_sound = pygame.mixer.Sound("Sounds/player_attack_sound.wav")
# death_sound = pygame.mixer.Sound("Sounds/death_sound.wav")
npc_damage = pygame.mixer.Sound("Sounds/get_damage_npc.wav")
select_sound = pygame.mixer.Sound("Sounds/select_sound.wav")
game_over_sound = pygame.mixer.Sound("Sounds/game_over.wav")

WIDTH = 800
HEIGHT = 600
FPS = 45

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVITY = 0.35
J_POWER = 10
MOVE_SPEED = 7
ATTACK_TIME = 200
ATTACK_WIDTH = 10
ATTACK_HEIGHT = 30

all_sprites = pygame.sprite.Group()
