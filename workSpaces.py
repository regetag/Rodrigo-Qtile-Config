from libqtile.command import lazy
from libqtile.config import Key, Group

def set_workspaces(keys, home, mod, mod1, mod2):
    groups = []

    # FOR QWERTY KEYBOARDS
    group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
    group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
    group_layouts = ["floating", "columns", "columns", "columns", "columns", "columns", "columns", "columns", "columns", "floating",]

    for i in range(len(group_names)):
        groups.append(
            Group(
                name=group_names[i],
                layout=group_layouts[i].lower(),
                label=group_labels[i],
            ))

    for i in groups:
        keys.extend([

            #CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
        ])

    return [groups, group_names, group_labels, group_layouts]