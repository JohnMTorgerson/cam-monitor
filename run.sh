echo 'running cam-monitor'
cd "$HOME"/Projects/cam-monitor
{ sleep 4; DISPLAY=:0 wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz -v; } &
{ sleep 10; DISPLAY=:0 wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz -v; } &
DISPLAY=:0 python main.py
