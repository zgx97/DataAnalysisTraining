#!/bin/bash

# Export DISPLAY
export DISPLAY=:0.0

# Call Gnome EOG
/usr/bin/eog -f ../DataAnalysisTraining/img.png &

# Time to display
sleep 5

killall eog
