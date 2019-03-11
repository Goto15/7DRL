import tcod as tc

from render_functions import RenderOrder
from game_messages import Message
# TODO figure out how to shorten spell casting imports
from item_functions import cast_fireball, cast_confuse, cast_lightning

from components.equippable import Equippable
from components.equipment import EquipmentSlots
from components.item import Item


# TODO get rid of the renderOrder field shouldn't be needed
items = {
    ###############################################################
    #   Consumables
    ###############################################################
    'healing potion': {
        'char': '!',
        'color': tc.violet,
        'name': 'Healing Potion',

        'components': {
            'use-function': 'heal',
            'amount': 40,
        }
    },
    'fireball_scroll': {
        'char': '#',
        'color': tc.red,
        'name': 'Fireball Scroll',

        'component': Item(use_function=cast_fireball, targeting=True, targeting_message=Message(
                          'Left-click a target tile for the fireball, or right-click to cancel.', tc.light_cyan),
                          damage=25, radius=3)
    },
    'confusion_scroll': {
        'char': '#',
        'color': tc.light_pink,
        'name': 'Confusion Scroll',

        'component': Item(use_function=cast_confuse, targeting=True, targeting_message=Message(
                          'Left-click an enemy to confuse it, or right-click to cancel.', tc.light_cyan))
    },
    'lightning_scroll': {
        'char': '#',
        'color': tc.yellow,
        'name': 'Lightning Scroll',

        'component': Item(use_function=cast_lightning, damage=40, maximum_range=5)
    },


    ###############################################################
    #   Equippables
    ###############################################################
    'sword': {
        'char': '/',
        'color': tc.sky,
        'name': 'Sword',

        'component': Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
    },
    'shield': {
        'char': '[',
        'color': tc.darker_orange,
        'name': 'Shield',

        'component': Equippable(EquipmentSlots.OFF_HAND, defense_bonus=1)
    },
}
