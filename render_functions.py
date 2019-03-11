import tcod as tc

from enum import auto, Enum

from game_states import GameStates
from menus import character_screen, inventory_menu, level_up_menu


class RenderOrder(Enum):
    STAIRS = auto()
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()


def get_names_under_mouse(mouse, entities, fov_map):
    (x, y) = (mouse.cx, mouse.cy)
    entities_on_square = []

    for entity in entities:
        if entity.x == x and entity.y == y and tc.map_is_in_fov(fov_map, entity.x, entity.y):
            if entity.ai:
                format_entity = entity.name.capitalize() + '-' + str(entity.fighter.hp)
                entities_on_square.append(format_entity.capitalize())
            else:
                entities_on_square.append(entity.name.capitalize())

    return ', '.join(entities_on_square)


def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)

    tc.console_set_default_background(panel, back_color)
    tc.console_rect(panel, x, y, total_width, 1, False, tc.BKGND_SCREEN)

    tc.console_set_default_background(panel, bar_color)
    if bar_width > 0:
        tc.console_rect(panel, x, y, bar_width, 1, False, tc.BKGND_SCREEN)

    tc.console_set_default_foreground(panel, tc.white)
    tc.console_print_ex(panel, int(x + total_width / 2), y, tc.BKGND_NONE, tc.CENTER,
                        '{0}: {1}/{2}'.format(name, value, maximum))


def render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log, screen_width, screen_height,
               bar_width, panel_height, panel_y, mouse, colors, game_state):
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = tc.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                if visible:
                    if wall:
                        tc.console_set_char_background(con, x, y, colors.get('light_wall'), tc.BKGND_SET)
                    else:
                        tc.console_set_char_background(con, x, y, colors.get('light_ground'), tc.BKGND_SET)
                else:
                    if wall:
                        tc.console_set_char_background(con, x, y, colors.get('dark_wall'), tc.BKGND_SET)
                    else:
                        tc.console_set_char_background(con, x, y, colors.get('dark_ground'), tc.BKGND_SET)

    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)

    # Draw all entities in the list
    for entity in entities_in_render_order:
        draw_entity(con, entity, fov_map, game_map)

    tc.console_set_default_foreground(con, tc.white)
    tc.console_print_ex(con, 1, screen_height - 2, tc.BKGND_NONE, tc.LEFT,
                        'HP: {0:02}/{1:02}'.format(player.fighter.hp, player.fighter.max_hp))

    tc.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

    if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        if game_state == GameStates.SHOW_INVENTORY:
            inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'
        else:
            inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'

        inventory_menu(con, inventory_title, player, 50, screen_width, screen_height)

    elif game_state == GameStates.LEVEL_UP:
        level_up_menu(con, 'Level up! Choose a stat to raise:', player, 40, screen_width, screen_height)

    elif game_state == GameStates.CHARACTER_SCREEN:
        character_screen(player, 30, 10, screen_width, screen_height)

    tc.console_set_default_background(panel, tc.black)
    tc.console_clear(panel)

    # Print the game messages, one line at a time
    y = 1
    for message in message_log.messages:
        tc.console_set_default_foreground(panel, message.color)
        tc.console_print_ex(panel, message_log.x, y, tc.BKGND_NONE, tc.LEFT, message.text)
        y += 1

    render_bar(panel, 1, 1, bar_width, 'HP', player.fighter.hp, player.fighter.max_hp,
               tc.light_red, tc.darker_red)
    tc.console_print_ex(panel, 1, 3, tc.BKGND_NONE, tc.LEFT,
                        'Dungeon level: {0}'.format(game_map.dungeon_level))

    tc.console_set_default_foreground(panel, tc.light_gray)
    tc.console_print_ex(panel, 1, 0, tc.BKGND_NONE, tc.LEFT,
                        get_names_under_mouse(mouse, entities, fov_map))

    tc.console_blit(panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map, game_map):
    if tc.map_is_in_fov(fov_map, entity.x, entity.y) or (entity.stairs and game_map.tiles[entity.x][entity.y].explored):
        tc.console_set_default_foreground(con, entity.color)
        tc.console_put_char(con, entity.x, entity.y, entity.char, tc.BKGND_NONE)


def clear_entity(con, entity):
    # erase the character that represents this object
    tc.console_put_char(con, entity.x, entity.y, ' ', tc.BKGND_NONE)
