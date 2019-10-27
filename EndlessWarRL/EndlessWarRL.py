#stuff i didnt make
import tcod as libtcod
import tcod.event as libtcod_event



#cfgs
import console.console_cfg
import entity.entity_cfg
import map.map_cfg

#functions
from console.console import rootStartUp, mainConStartUp
from input_handlers import handle_keys
from render.render_functions import clear_all, render_all

#classes
from entity.entity import Entity
from map.game_map import GameMap

def main():

	#import starting entities (the player)
	entities = entity.entity_cfg.entities

	colours = {
		'dark_wall': libtcod.Color(0, 0, 0),
		'dark_ground': libtcod.Color(5, 10, 5)
    }

	#mkae root console
	root = rootStartUp()
	#make game console
	con = mainConStartUp(root)

	game_map = GameMap(map.map_cfg.map_width, map.map_cfg.map_height)

	while True:
		for event in libtcod_event.wait(1):
			if event.type == "QUIT":
				raise SystemExit()

			else:
				
				render_all(con, entities, game_map, console.console_cfg.screen_width, console.console_cfg.screen_height, colours)

				libtcod.console_flush()

				clear_all(con, entities, colours)

				if event.type == "MOUSEBUTTONDOWN":
					if event.button == libtcod_event.BUTTON_LEFT:
						print('click')

				elif event.type == "KEYDOWN":
					key = event
					action = handle_keys(key)

					move = action.get('move')
					exit = action.get('exit')
					fullscreen = action.get('fullscreen')

					if move:
						dx, dy = move
						if not game_map.is_blocked(entity.entity_cfg.player.x + dx, entity.entity_cfg.player.y + dy):
							entity.entity_cfg.player.move(dx, dy)

					if exit:
						raise SystemExit()

					if fullscreen:
						libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

				elif event.type == "MOUSEMOTION":
					scrx, scry = event.tile
					print('x = ' + str(scrx) + ' y = ' + str(scry))

		libtcod.console_flush()

if __name__ == '__main__':
	main()