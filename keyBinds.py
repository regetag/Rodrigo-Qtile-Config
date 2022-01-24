from libqtile.command import lazy
from libqtile.config import Key

def set_key_binds(home, mod, mod1, mod2):

    keys = [

    # SUPER + FUNCTION KEYS

        Key([mod], "f", lazy.window.toggle_fullscreen()),
        Key([mod], "q", lazy.window.kill()),
        Key([mod], "t", lazy.spawn('xterm')),
        Key([mod], "v", lazy.spawn('pavucontrol')),
        Key([mod], "d", lazy.spawn('nwggrid -p -o 0.4')),
        Key([mod], "Escape", lazy.spawn('xkill')),
        Key([mod], "Return", lazy.spawn('alacritty')),
        Key([mod], "KP_Enter", lazy.spawn('alacritty')),
        Key([mod], "x", lazy.spawn("arcolinux-logout")),

    # SUPER + SHIFT KEYS

        Key([mod, "shift"], "Return", lazy.spawn('thunar')),
        Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#ff3b3b' -sb '#ff3b3b' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
        Key([mod, "shift"], "q", lazy.window.kill()),
        Key([mod, "shift"], "r", lazy.restart()),
        Key([mod, "control"], "r", lazy.restart()),
        Key([mod, "shift"], "x", lazy.spawn("arcolinux-logout")),
        

    # CONTROL + ALT KEYS

        Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),

    # ALT + ... KEYS


    # CONTROL + SHIFT KEYS

        Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),



    # INCREASE/DECREASE BRIGHTNESS
        Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

    # INCREASE/DECREASE/MUTE VOLUME
        Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
        Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    #    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    #    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
    #    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
    #    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

    # QTILE LAYOUT KEYS
        Key([mod], "n", lazy.layout.normalize()),
        Key([mod], "space", lazy.next_layout()),

    # CHANGE FOCUS
        Key([mod], "Up", lazy.layout.up()),
        Key([mod], "Down", lazy.layout.down()),
        Key([mod], "Left", lazy.layout.left()),
        Key([mod], "Right", lazy.layout.right()),
        Key([mod], "k", lazy.layout.up()),
        Key([mod], "j", lazy.layout.down()),
        Key([mod], "h", lazy.layout.left()),
        Key([mod], "l", lazy.layout.right()),


    # RESIZE UP, DOWN, LEFT, RIGHT
        Key([mod, "control"], "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
            ),
        Key([mod, "control"], "Right",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
            ),
        Key([mod, "control"], "h",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
            ),
        Key([mod, "control"], "Left",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
            ),
        Key([mod, "control"], "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
            ),
        Key([mod, "control"], "Up",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
            ),
        Key([mod, "control"], "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
            ),
        Key([mod, "control"], "Down",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
            ),


    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
        Key([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
        Key([mod, "mod1"], "u", lazy.spawn("pavucontrol")),
        Key([mod, "mod1"], "k", lazy.layout.flip_up()),
        Key([mod, "mod1"], "j", lazy.layout.flip_down()),
        Key([mod, "mod1"], "l", lazy.layout.flip_right()),
        Key([mod, "mod1"], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
        Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

            ### Treetab controls
        Key([mod, "control"], "k",
            lazy.layout.section_up(),
            desc='Move up a section in treetab'
            ),
        Key([mod, "control"], "j",
            lazy.layout.section_down(),
            desc='Move down a section in treetab'
            ),



    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "Left", lazy.layout.swap_left()),
        Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
        Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    ]

    return keys
