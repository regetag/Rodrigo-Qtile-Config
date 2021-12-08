#!/usr/bin/env bash
# ---
# Use "run program" to run it only if it is not already running
# Use "program &" to run it regardless
# ---
# NOTE: This script runs with every restart of AwesomeWM
# TODO: run_once


function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

run megasync
run xfce4-clipman
run redshiftgui
lxsession &
# run nm-applet &
# run pamac-tray &
numlockx on &
blueman-applet &
run volumeicon &
picom --config .config/picom/picom-blur.conf --experimental-backends &
bash $HOME/.config/qtile/scripts/configMonitors.sh &