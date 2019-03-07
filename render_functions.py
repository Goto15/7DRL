import tcod as tc

from enum import Enum


class RenderOrder(Enum):
    CORPSE = 1
    ITEM = 2
    ACTOR = 3


def get_names_under_mouse(mouse, entities, fov_map):
    (x, y) = (mouse.cx, mouse.cy)

    names = [entity.name for entity in entities
             if entity.x == x and entity.y == y and tc.map_is_in_fov(fov_map, entity.x, entity.y)]
    names = ', '.join(names)

    return names.capitalize()


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
               bar_width, panel_height, panel_y, mouse, colors):
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
        draw_entity(con, entity, fov_map)

    tc.console_set_default_foreground(con, tc.white)
    tc.console_print_ex(con, 1, screen_height - 2, tc.BKGND_NONE, tc.LEFT, 'HP: {0:02}/{1:02}'.format(player.fighter.hp, player.fighter.max_hp))

    tc.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

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

    tc.console_set_default_foreground(panel, tc.light_gray)
    tc.console_print_ex(panel, 1, 0, tc.BKGND_NONE, tc.LEFT,
                        get_names_under_mouse(mouse, entities, fov_map))

    tc.console_blit(panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map):
    if tc.map_is_in_fov(fov_map, entity.x, entity.y):
        tc.console_set_default_foreground(con, entity.color)
        tc.console_put_char(con, entity.x, entity.y, entity.char, tc.BKGND_NONE)


def clear_entity(con, entity):
    # erase the character that represents this object
    tc.console_put_char(con, entity.x, entity.y, ' ', tc.BKGND_NONE)
