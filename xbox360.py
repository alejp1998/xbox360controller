import signal
import time
from xbox360controller import Xbox360Controller

with Xbox360Controller(0, axis_threshold=0.2) as controller:
    print("Xbox controller writing in piTankEx")
    while 1:
        str1 = 'N'
        str2 = 'N'
        str3 = "0.000"
        str4 = "0.000"

        #Control de los botones pulsados
        if controller.hat.x>=0.5:
            str1 = "r"
        elif controller.hat.x<=-0.5:
            str1 = "l"
        elif controller.hat.y>=0.5:
            str1 = "u"
        elif controller.hat.y<=-0.5:
            str1 = "d"
        elif controller.button_trigger_r.is_pressed:
            str1 = "T"
        elif controller.button_start.is_pressed:
            str1 = 'E'
        elif controller.button_a.is_pressed: 
            str1 = "A"
        elif controller.button_b.is_pressed: 
            str1 = "B"
        elif controller.button_y.is_pressed: 
            str1 = "Y"
        elif controller.button_x.is_pressed: 
            str1 = "X" 

        #Control de joystick derecho como digital
        if controller.axis_r.x > 0.5:
            str2 = "R"
        elif controller.axis_r.x < -0.5:
            str2 = "L"
        elif controller.axis_r.y > 0.5:
            str2 = "D"
        elif controller.axis_r.y < -0.5:
            str2 = "U" 

        #Control de joystick izquierdo para regulacion de velocidad de ruedas
        if controller.axis_l.x > 0.3 or controller.axis_l.x < -0.3: 
            str3 = "%1.3f" % controller.axis_l.x

        if controller.axis_l.y > 0.3 or controller.axis_l.y < -0.3:
            str4 = "%1.3f" % -controller.axis_l.y

        f1 = open("../piTankEx/xbox360.txt","w+")
        f1.write(str1 + " " + str2 + " " + str3 + " " + str4)
        f1.close()

        time.sleep(0.1)#Wait 5 miliseconds before next loop 
