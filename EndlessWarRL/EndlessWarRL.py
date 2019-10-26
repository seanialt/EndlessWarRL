import tcod as libtcod
import tcod.event as libtcod_event

import console.console_cfg
import entity.entity_cfg

from console.console import rootStartUp, mainConStartUp
from input_handlers import handle_keys

def main():
	
	player_x = int(console.console_cfg.screen_width / 2)
	player_y = int(console.console_cfg.screen_width / 2)

	root = rootStartUp()

	con = mainConStartUp(root)

	while True:
		for event in libtcod_event.wait():
			if event.type == "QUIT":
				raise SystemExit()

			else:
				con.draw_rect(
					player_x, 
					player_y,  
					1, 1,
					ord('@'),
					fg=libtcod.white)
				con.blit(root)

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
						player_x += dx
						player_y += dy

					if exit:
						raise SystemExit()

					if fullscreen:
						libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

				elif event.type == "MOUSEMOTION":
					scrx, scry = event.tile
					print('x = ' + str(scrx) + ' y = ' + str(scry))

		con.clear()
		con.print(
			4, 2, 
			'Hehe die coonrat',
			fg=libtcod.light_grey,
			alignment=libtcod.LEFT)

		libtcod.console_flush()

if __name__ == '__main__':
	main()