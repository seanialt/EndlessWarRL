#stuff i didnt make
import tcod as libtcod
import tcod.event as libtcod_event

#cfgs
import console.console_cfg

#classes
from entity.entity import Entity

player = Entity(int(console.console_cfg.screen_width / 2), int(console.console_cfg.screen_width / 2), '@', libtcod.white)

entities = [player]