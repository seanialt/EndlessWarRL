import tcod as libtcod
import tcod.event as libtcod_event

def handle_keys(key):
	event = key
    # Movement keys
	if event.sym == libtcod_event.K_KP_8:
		return {'move': (0, -1)}
	elif event.sym == libtcod_event.K_KP_2:
		return {'move': (0, 1)}
	elif event.sym == libtcod_event.K_KP_4:
		return {'move': (-1, 0)}
	elif event.sym == libtcod_event.K_KP_6:
		return {'move': (1, 0)}

	if event.sym == libtcod_event.K_RETURN:
		if event.mod & libtcod_event.KMOD_LALT:
			# Alt+Enter: toggle full screen
			return {'fullscreen': True}

	if event.sym == libtcod_event.K_ESCAPE:
		# Exit the game
		return {'exit': True}

	# No key was pressed
	return {}

