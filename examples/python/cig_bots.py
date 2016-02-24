#!/usr/bin/python

from __future__ import print_function
from vizia import *

game = DoomGame()
game.load_config("../config/cig.cfg")
game.set_doom_map("map01")
#game.set_doom_map("map02")

game.add_game_args("-host 1")
game.add_game_args("1")
game.add_game_args("-deathmatch")
game.add_game_args("-respawn")
game.set_mode(Mode.ASYNC_SPECTATOR)

game.init()
game.send_game_command("sv_forcerespawn 1");

bots_number = 7
for i in range(bots_number):
	game.send_game_command("addbot")

while not game.is_episode_finished():	
	game.advance_action()
	if game.is_player_dead():
		continue
	print("Frags:", game.get_game_variable(GameVariable.FRAGCOUNT))
