#!/usr/bin/env bash
TOTAL_OF_MONITORS=1
nitrogen --restore

function get_connected_monitors()
{
  local CURRENT_TOTAL_OF_MONITORS=$(xrandr -d :0 -q | grep ' connected' | wc -l)
  echo $CURRENT_TOTAL_OF_MONITORS
}

function dual_configuration()
{
  xrandr --output HDMI1 --auto --above LVDS1 --auto
}

function single_configuration()
{
  xrandr --auto
}

while [ true ]
do
  CURRENT_TOTAL_OF_MONITORS="$(get_connected_monitors)" 

  if [  $CURRENT_TOTAL_OF_MONITORS != $TOTAL_OF_MONITORS  ]; then

    if [ $CURRENT_TOTAL_OF_MONITORS == 1 ]; then
      single_configuration
    fi

    if [ $CURRENT_TOTAL_OF_MONITORS == 2 ]; then
      dual_configuration
    fi


    TOTAL_OF_MONITORS="$(CURRENT_TOTAL_OF_MONITORS)"
    nitrogen --restore
  fi

  sleep 1
done
