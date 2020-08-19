#!/bin/bash
IFS='.' read -ra my_array <<< $(basename $BASH_SOURCE)
pyside2-uic ${my_array[0]}.ui > ${my_array[0]}_uis.py
#pyuic5 ${my_array[0]}.ui -o ${my_array[0]}_ui.py
