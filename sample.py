import signal
from xbox360controller import Xbox360Controller


def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))
    str1 = "%s" % button.name
    str2 = 'N'
    str3 = "0.000"
    str4 = "0.000"
    f1 = open("../piTankEx/xbox360.txt","w+")
    f1.write(str1 + " " + str2 + " " + str3 + " " + str4)
    f1.close()

def on_button_released(button):
    print('Button {0} was released'.format(button.name))
    str1 = 'N'
    str2 = 'N'
    str3 = "0.000"
    str4 = "0.000"
    f1 = open("../piTankEx/xbox360.txt","w+")
    f1.write(str1 + " " + str2 + " " + str3 + " " + str4)
    f1.close()

def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))
    if axis.name == "Left" :
        str1 = 'N'
        str2 = 'N'
        str3 = "%1.3f" % axis.x
        str4 = "%1.3f" % axis.y
        f1 = open("../piTankEx/xbox360.txt","w+")
        f1.write(str1 + " " + str2 + " " + str3 + " " + str4)
        f1.close()

    elif axis.name == "Right" :
        str1 = "N"
        if axis.x > 0.5 :
            str2 = 'R'
        elif axis.x < -0.5 :
            str2 = 'L'
        elif axis.y > 0.5 :
            str2 = 'U'
        elif axis.y < -0.5 :
            str2 = 'D'
        str3 = "0.000"
        str4 = "0.000"
        f1 = open("../piTankEx/xbox360.txt","w+")
        f1.write(str1 + " " + str2 + " " + str3 + " " + str4)
        f1.close()

try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        # Button events
        controller.button_a.when_pressed = on_button_pressed
        controller.button_a.when_released = on_button_released

        controller.button_b.when_pressed = on_button_pressed
        controller.button_b.when_released = on_button_released

        controller.button_x.when_pressed = on_button_pressed
        controller.button_x.when_released = on_button_released

        controller.button_y.when_pressed = on_button_pressed
        controller.button_y.when_released = on_button_released

        controller.button_start.when_pressed = on_button_pressed
        controller.button_start.when_released = on_button_released

        controller.button_trigger_right.when_pressed = on_button_pressed
        controller.button_trigger_right.when_released = on_button_released

        # Left and right axis move event
        controller.axis_l.when_moved = on_axis_moved
        controller.axis_r.when_moved = on_axis_moved

        signal.pause()
except KeyboardInterrupt:
    pass