#stuff i didnt make
import tcod as libtcod
import tcod.event as libtcod_event
import numpy as np

#cfgs
import render.render_cfg

#functions


#classes


def render_all(con, entities, game_map, screen_width, screen_height, colours):
	for y in range(game_map.height):
		for x in range(game_map.width):
			wall = game_map.tiles[x][y].block_sight

			if render.render_cfg.initial_render:
				if wall:
					libtcod.console_put_char_ex(con, x, y, '#', libtcod.white , colours.get('dark_wall'))
				else:
					libtcod.console_put_char_ex(con, x, y, '.', libtcod.white, colours.get('dark_ground'))

	if render.render_cfg.initial_render:
		render.render_cfg.initial_render = False

	for entity in entities:
		draw_entity(con, entity)


	libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all(con, entities, colours):
	for entity in entities:
		clear_entity(con, entity, colours)

def draw_entity(con, entity):
	con.default_fg = (entity.colour)
	libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)

def clear_entity(con, entity, colours):
	libtcod.console_put_char_ex(con, entity.x, entity.y, '.', libtcod.white, colours.get('dark_ground'))