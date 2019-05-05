import signal
from xbox360controller import Xbox360Controller


def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))
    str1 = "%s" % button.name


def on_button_released(button):
    print('Button {0} was released'.format(button.name))
    str1 = 'N'


def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))
    if axis.name == "Left" :
        str2 = 'N'
        str3 = "%1.3f" % axis.x
        str4 = "%1.3f" % axis.y
    elif axis.name == "Right" :
        str3 = "0.000"
        str4 = "0.000"
        if axis.x > 0.5 :
            str2 = 'R'
        elif axis.x < -0.5 :
            str2 = 'L'
        elif axis.y > 0.5 :
            str2 = 'U'
        elif axis.y < -0.5 :
            str2 = 'D'
try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        # Button A events
        controller.button_a.when_pressed = on_button_pressed
        controller.button_a.when_released = on_button_released

        # Left and right axis move event
        controller.axis_l.when_moved = on_axis_moved
        controller.axis_r.when_moved = on_axis_moved

        signal.pause()
except KeyboardInterrupt:
    pass