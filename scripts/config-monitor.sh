#!/usr/bin/env bash
CONNECTED_MONITORS=1
LAST_AMOUNT_CONNECTED=$CONNECTED_MONITORS


while [ true ]; do
    CONNECTED_MONITORS=$(xrandr | grep " connected" | wc -l)

    if [[ "$CONNECTED_MONITORS" != "$LAST_AMOUNT_CONNECTED" ]]; then
        LAST_AMOUNT_CONNECTED=$CONNECTED_MONITORS

        if [[ "$CONNECTED_MONITORS" == 1 ]]; then
            xrandr --auto
        else
            xrandr --output HDMI1 --auto --above LVDS1 --auto
        fi

        nitrogen --restore &
    fi

    sleep 1
done