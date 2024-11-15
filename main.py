from colorama import init
import keyboard, os, time
import maps
from game import Game
from player import Player


init(autoreset=True)

game = Game()
pl = Player()


game.main_menu()