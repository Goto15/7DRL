import tcod as tc

from render_functions import RenderOrder
from components.ai import BasicMonster


# Max number of monsters per room [max # of monsters, minimum level]
max_monsters_per_room = [
    [2, 1],
    [3, 4],
    [5, 6]
]

# List of monsters with their stats
monster_list = {
    'orc': {
        # Static properties
        'blocks': True,
        'char': 'o',
        'color': tc.desaturated_green,
        'name': 'Orc',
        'render_order': RenderOrder.ACTOR,
        'ai_component': BasicMonster(),

        # Generated stat line properties
        'hp_max': 21,
        'hp_min': 19,
        'def_max': 0,
        'def_min': 0,
        'power_max': 5,
        'power_min': 3,
        'xp_max': 40,
        'xp_min': 30,
    },
    'troll': {
        # Static properties
        'blocks': True,
        'char': 'T',
        'color': tc.darker_green,
        'name': 'Troll',
        'render_order': RenderOrder.ACTOR,
        'ai_component': BasicMonster(),

        # Generated stat line properties
        'hp_max': 33,
        'hp_min': 27,
        'def_max': 3,
        'def_min': 1,
        'power_max': 9,
        'power_min': 7,
        'xp_max': 110,
        'xp_min': 90,
    }
}

# Spawn rates of monsters
monster_chances = {
    'orc': [[80, 1]],
    'troll': [[15, 3],
              [30, 5],
              [60, 7]],
}
