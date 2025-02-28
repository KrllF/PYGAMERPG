import pygame

from config import *


class Spritesheet:
    def __init__(self, file, color):
        self.sheet = pygame.image.load(file).convert()
        self.color = color
    def get_sprite(self, pos, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (pos[0], pos[1], width, height))
        sprite.set_colorkey(self.color)
        return sprite


class BLOCK(pygame.sprite.Sprite):

    def __init__(self, game, pos, type_sprite):
        self.game = game
        self._layer = BLOCK_LAYER
        self.type_sprite = type_sprite

        if self.type_sprite == 'block':
            self.groups = self.game.unvisible
        if self.type_sprite == 'tree':
            self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = pos[0] * TILESIZE
        self.y = pos[1] * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.image.load('images/map/img.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



class Ground(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = pos[0] * TILESIZE
        self.y = pos[1] * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite((64, 352), self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
