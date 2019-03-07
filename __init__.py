import os
import tcod


#############
# CONSTANTS #
#############


window_width = 46
window_height = 20

first = True
fov_px = 20
fov_py = 10
fov_recompute = True
fov_map = None
fov_colors = {
    'dark wall': tcod.Color(0, 0, 100),
    'light wall': tcod.Color(130, 110, 50),
    'dark ground': tcod.Color(50, 50, 150),
    'light ground': tcod.Color(200, 180, 50)
}
fov_init = False
fov_radius = 4

move_controls = {
    'i': (0, -1),  # up
    'k': (0, 1),  # down
    'j': (-1, 0),  # left
    'l': (1, 0),  # right
    tcod.KEY_UP: (0, -1),  # example of alternate key
    tcod.KEY_KP8: (0, -1)  # example of alternate key
}

#####################
# Utility Functions #
#####################


def get_key(key):
    if key.vk == tcod.KEY_CHAR:
        return chr(key.c)
    else:
        return key.vk

#######
# Map #
#######


smap = ['##############################################',
        '#######################      #################',
        '#####################    #     ###############',
        '######################  ###        ###########',
        '##################      #####             ####',
        '################       ########    ###### ####',
        '###############      #################### ####',
        '################    ######                  ##',
        '########   #######  ######   #     #     #  ##',
        '########   ######      ###                  ##',
        '########                                    ##',
        '####       ######      ###   #     #     #  ##',
        '#### ###   ########## ####                  ##',
        '#### ###   ##########   ###########=##########',
        '#### ##################   #####          #####',
        '#### ###             #### #####          #####',
        '####           #     ####                #####',
        '########       #     #### #####          #####',
        '########       #####      ####################',
        '##############################################',
        ]


#############################################
# drawing
#############################################


def draw(first):
    global fov_px, fov_py, fov_map
    global fov_init, fov_recompute, smap

    if first:
        tcod.console_clear(0)
        tcod.console_set_foreground_color(0, tcod.white)
        tcod.console_print_left(0, 1, 1, tcod.BKGND_NONE,
                                "IJKL : move around")
        tcod.console_set_foreground_color(0, tcod.black)
        tcod.console_put_char(0, fov_px, fov_py, '@',
                              tcod.BKGND_NONE)

        for y in range(window_height):
            for x in range(window_width):
                if smap[y][x] == '=':
                    tcod.console_put_char(0, x, y,
                                          tcod.CHAR_DHLINE,
                                          tcod.BKGND_NONE)


if not fov_init:
    fov_init = True
    fov_map = tcod.map_new(window_width, window_height)
    for y in range(window_height):
        for x in range(window_width):
            if smap[y][x] == ' ':
                tcod.map_set_properties(fov_map, x, y, True, True)
            elif smap[y][x] == '=':
                tcod.map_set_properties(fov_map, x, y, True, False)

if fov_recompute:
    fov_recompute = False
    tcod.map_compute_fov(fov_map, fov_px, fov_py, fov_radius, True)

for y in range(window_height):
    for x in range(window_width):
            affect, cell = 'dark', 'ground'
        if tcod.map_is_in_fov(fov_map, x, y):
            affect = 'light'
        if smap[y][x] == '#':
            cell = 'wall'
            color = fov_colors['%s %s' % (affect, cell)]
            tcod.console_set_back(0, x, y, color, tcod.BKGND_SET)