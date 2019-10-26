import tcod as libtcod

import console.console_cfg

def rootStartUp():

	libtcod.console_set_custom_font(console.console_cfg.display_font, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	
	root = libtcod.console_init_root(console.console_cfg.screen_width, console.console_cfg.screen_height, 'EndlessWarRL', False, libtcod.RENDERER_OPENGL2, vsync=True)

	return root

def mainConStartUp(root):
	
	player_x = int(console.console_cfg.screen_width / 2)
	player_y = int(console.console_cfg.screen_width / 2)

	con = libtcod.console.Console(console.console_cfg.screen_width, console.console_cfg.screen_height)

	con.draw_rect(
		player_x, 
		player_y,  
		1, 1,
		ord('@'),
		fg=libtcod.white)
	
	con.blit(root)

	libtcod.console_flush()

	return con
