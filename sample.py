import signal
from xbox360controller import Xbox360Controller
with Xbox360Controller(0, axis_threshold=0.2) as controller:
    print("Xbox controller printing in piTankEx")
    while 1:
        print("X %1.3f" % controller.hat.x)
        print("Y %1.3f" % controller.hat.y)
        #Control de los botones pulsados
        if controller.hat.x>=0.9:
            str1 = "r"
        elif controller.hat.x<=-0.9:
            str1 = "l"
        elif controller.hat.y>=0.9:
            str1 = "u"
        elif controller.hat.y<=-0.9:
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
        else: 
            str1 = "N"  

        #Control de joystick derecho como digital
        if controller.axis_r.x > 0.5:
            str2 = "R"
        elif controller.axis_r.x < -0.5:
            str2 = "L"
        elif controller.axis_r.y > 0.5:
            str2 = "D"
        elif controller.axis_r.y < -0.5:
            str2 = "U" 
        else: 
            str2 = "N" 

        #Control de joystick izquierdo para regulacion de velocidad de ruedas
        if controller.axis_l.x > 0.3 or controller.axis_l.x < -0.3: 
            str3 = "%1.3f" % controller.axis_l.x
        else: 
            str3 = "0.0"

        if controller.axis_l.y > 0.3 or controller.axis_l.y < -0.3:
            str4 = "%1.3f" % -controller.axis_l.y
        else:
            str4 = "0.0"

        f1 = open("../piTankEx/xbox360.txt","w+")
        f1.write(str1 + " " + str2 + " " + str3 + " " + str4)
        f1.close()
