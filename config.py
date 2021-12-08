###############################################
### QTILE CONFIGURATION FILE OF DANIEL DIAZ ###
#
#  ____   ____
# |  _ \ |  _ \   Copyright (c) 2020 Daniel Diaz
# | | | || | | |
# | |_| || |_| |  http://www.github.com/Daniel1404/
# |____/ |____/
#                 Copyright (c) 2021 Rodrigo Tavares
#                 http://www.github.com/regetag/
#


####### IMPORTS #########
import os
import subprocess

# from typing import List  # noqa: F401

from libqtile import hook, layout
from libqtile.config import Match

# Local Files
from widgets import MyWidgets
from layouts import Layouts
from keyBinds import set_key_binds
from workSpaces import set_workspaces

home = os.path.expanduser('~')
 
###### MAIN ######
if __name__ in ["config", "__main__"]:
    # Initializes objects

    # Initializes keybindings

    # Mouse
    obj_widgets       = MyWidgets(home)
    obj_layouts       = Layouts()
    
    # Initializes qtile variables

    layouts           = obj_layouts.init_layouts()

    # Append group keys for groups
    ### DISPLAYS WIDGETS IN THE SCREEN ####

    screens           = obj_widgets.init_screen()
    main_widgets_list = obj_widgets.init_widgets_list()
    widgets_screen1   = obj_widgets.init_widgets_screen()



dgroups_key_binder = None

dgroups_app_rules = []  # type: list

follow_mouse_focus = True

bring_front_click = False

cursor_warp = False


floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='dialog'),  # Dialogs stuff
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True

focus_on_window_activation = "smart"

reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
respect_minimize_requests = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])
    subprocess.call([home + '/.local/bin/autostart'])

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True


mod = "mod4"
mod1 = "alt"
mod2 = "control"

keys = set_key_binds(home, mod, mod1, mod2)

[groups, group_names, group_labels, group_layouts] = set_workspaces(keys, home, mod, mod1, mod2)