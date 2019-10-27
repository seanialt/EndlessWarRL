#stuff i didnt make
import tcod as libtcod
import tcod.event as libtcod_event

#cfgs
import console.console_cfg
import entity.entity_cfg

#functions

#classes

class Tile:

	def __init__(self, blocked, block_sight=None):
		self.blocked = blocked

		if block_sight is None:
			block_sight = blocked

		self.block_sight = block_sight