from random import randint

from components.bestiary.bestiary import *


def get_monster(monster):
    return monster_list[monster]


def get_monster_chances():
    return monster_chances


def get_monster_list():
    return monster_list


# Generate specific stats
def generate_ai(monster_name):
    monster_stats = get_monster(monster_name)
    return monster_stats['ai_component']


def generate_color(monster_name):
    monster_stats = get_monster(monster_name)
    return monster_stats['color']


def generate_defense(monster_name):
    monster_stats = get_monster(monster_name)
    return randint(monster_stats['def_min'], monster_stats['def_max'])


def generate_hp(monster_name):
    monster_stats = get_monster(monster_name)
    return randint(monster_stats['hp_min'], monster_stats['hp_max'])


def generate_name(monster_name):
    temp_monster_list = get_monster_list()
    return temp_monster_list[monster_name]['name']


def generate_power(monster_name):
    monster_stats = get_monster(monster_name)
    return randint(monster_stats['power_min'], monster_stats['power_max'])


def generate_xp(monster_name):
    monster_stats = get_monster(monster_name)
    return randint(monster_stats['xp_min'], monster_stats['xp_max'])


# Set static properties
def set_blocks(monster_name):
    monster_stats = get_monster(monster_name)
    return monster_stats['blocks']


def set_render_order(monster_name):
    monster_stats = get_monster(monster_name)
    return monster_stats['render_order']


def set_sprite(monster_name):
    monster_stats = get_monster(monster_name)
    return monster_stats['char']
