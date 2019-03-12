from item_functions import *
from components.equippable import Equippable
from components.equipment import EquipmentSlots
from components.item import Item


max_items_per_room = [
    [1, 1],
    [2, 4]
]

item_list = {
    ###############################################################
    #   Consumables
    ###############################################################
    'healing_potion': {
        'char': '!',
        'color': tc.violet,
        'name': 'Healing Potion',
        'equippable': False,
        'component': Item(use_function=heal, amount=40)
    },
    'fireball_scroll': {
        'char': '#',
        'color': tc.red,
        'name': 'Fireball Scroll',
        'equippable': False,
        'component': Item(use_function=cast_fireball, targeting=True, targeting_message=Message(
                          'Left-click a target tile for the fireball, or right-click to cancel.', tc.light_cyan),
                          damage=25, radius=3)
    },
    'confusion_scroll': {
        'char': '#',
        'color': tc.light_pink,
        'name': 'Confusion Scroll',
        'equippable': False,
        'component': Item(use_function=cast_confuse, targeting=True, targeting_message=Message(
                          'Left-click an enemy to confuse it, or right-click to cancel.', tc.light_cyan))
    },
    'lightning_scroll': {
        'char': '#',
        'color': tc.yellow,
        'name': 'Lightning Scroll',
        'equippable': False,
        'component': Item(use_function=cast_lightning, damage=40, maximum_range=5)
    },


    ###############################################################
    #   Equippables
    ###############################################################
    'sword': {
        'char': '/',
        'color': tc.sky,
        'name': 'Sword',
        'equippable': True,
        'component': Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
    },
    'shield': {
        'char': '[',
        'color': tc.darker_orange,
        'name': 'Shield',
        'equippable': True,
        'component': Equippable(EquipmentSlots.OFF_HAND, defense_bonus=1)
    },
}

item_chances = {
            'healing_potion': [[35, 1]],
            'sword': [[5, 4]],
            'shield': [[15, 8]],
            'lightning_scroll': [[25, 4]],
            'fireball_scroll': [[25, 6]],
            'confusion_scroll': [[10, 2]],
}
