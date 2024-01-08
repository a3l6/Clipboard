#!/bin/bash

git clone https://github.com/a3l6/Clipboard.git
cd Clipboard
python3 -m pip install virtualenv
python3 -m virtualenv .venv
.venv/bin/python3 -m pip install -r requirements.txt

script_dir=$(realpath $(dirname $0))

mkdir ~/.config/autostart

echo "
[Desktop Entry]
Encoding=UTF-8
Name=Clipboard++
Comment=Clipboard++
Icon=gnome-info
Exec=$script_dir/.venv/bin/python3 $script_dir/main.py
Terminal=false
Type=Application
Categories=

X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=0
" > ~/.config/autostart/clipboard.desktop


echo Done