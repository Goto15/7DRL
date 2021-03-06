import tcod as tc

from game_states import GameStates
from game_messages import Message
from render_functions import RenderOrder


def kill_player(player):
    player.char = '%'
    player.color = tc.dark_red

    return Message('You died!', tc.dark_red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), tc.gold)

    monster.char = '%'
    monster.color = tc.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    # TODO create a function that determines the correct grammar for a/an
    monster.name = 'remains of a ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message
