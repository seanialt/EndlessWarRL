#stuff i didnt make
import tcod as libtcod
import tcod.event as libtcod_event

#cfgs
import console.console_cfg
import entity.entity_cfg

#classes
from entity.entity import Entity
from map.tile import Tile

class GameMap:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tiles = self.initialize_tiles()

	def initialize_tiles(self):
		tiles = [[Tile(True) for y in range (self.height)] for x in range(self.width)]

		return tiles

	def is_blocked(self, x, y):
		if self.tiles[x][y].blocked:
			return True

		return False



