#stuff i didnt make
import tcod as libtcod
import tcod.event as libtcod_event

#cfgs
import console.console_cfg


def rootStartUp():

	libtcod.console_set_custom_font(console.console_cfg.display_font, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	
	root = libtcod.console_init_root(console.console_cfg.screen_width, console.console_cfg.screen_height, 'EndlessWarRL', False, libtcod.RENDERER_OPENGL2, vsync=True)

	return root

def mainConStartUp(root):
	
	con = libtcod.console.Console(console.console_cfg.screen_width, console.console_cfg.screen_height)
	
	con.blit(root)

	libtcod.console_flush()

	return con
