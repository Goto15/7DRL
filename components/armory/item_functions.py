from components.armory.items import *

from render_functions import RenderOrder


def get_item(item):
    return item_list[item]


def get_item_chances():
    return item_chances


def get_item_list():
    return item_list


# Get the item components
def get_component(item):
    item_stats = get_item(item)
    return item_stats['component']


def is_equippable(item):
    item_stats = get_item(item)
    return bool(item_stats['equippable'])


# Set properties
def set_item_sprite(item):
    item_stats = get_item(item)
    return item_stats['char']


def set_item_color(item):
    item_stats = get_item(item)
    return item_stats['color']


def set_item_name(item):
    item_stats = get_item(item)
    return item_stats['name']


def set_item_render_order():
    return RenderOrder.ITEM
