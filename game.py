import pygame
from card import Card
from card import CardEncoder
from pack import Pack

cards = []
p = Pack(cards)

p.generate_pack()

def load_card_images(pack):
    for card in pack:
        card.image = pygame.image.load("card_images/" + str(card.identifier) + ".png");
        width, height = card.image.get_size()
        card.horizontal_dimension = width
        card.vertical_dimension = height

def main():
    sc_width, sc_height = 555, 555
    p = Pack(None)
    p.generate_pack()
    load_card_images(p)
    