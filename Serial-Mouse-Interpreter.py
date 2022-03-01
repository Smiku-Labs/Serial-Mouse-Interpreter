
import serial
from bitstring import BitArray
import mouse

ser = serial.Serial('COM7', 1200, rtscts=1)

ser.read()

while 1 :
    button_byte = BitArray(ser.read())     

    print('LMB:' + str(not button_byte[5]))
    print('MMB:' + str(not button_byte[6]))
    print('RMB:' + str(not button_byte[7]))

    if button_byte[5]:
        if mouse.is_pressed(button='left'):
            mouse.release(button='left')
    else:
        if not mouse.is_pressed(button='left'):
            mouse.press(button='left')

    if button_byte[6]:
        if mouse.is_pressed(button='middle'):
            mouse.release(button='middle')
    else:
        if not mouse.is_pressed(button='middle'):
            mouse.press(button='middle')

    if button_byte[7]:
        if mouse.is_pressed(button='right'):
            mouse.release(button='right')
    else:
        if not mouse.is_pressed(button='right'):
            mouse.press(button='right')

    x_byte = int.from_bytes(ser.read(), 'big')
    if x_byte >= 128 :
        x_byte -= 256
    print('x:' +  str(x_byte))

    y_byte = int.from_bytes(ser.read(), 'big')
    if y_byte >= 128 :
        y_byte -= 256
    print('y:' +  str(y_byte))

    mouse.move(x_byte, -1 *y_byte, absolute=0)

    x2_byte = int.from_bytes(ser.read(), 'big')
    if x2_byte >= 128 :
        x2_byte -= 256
    print('x2:' +  str(x2_byte))

    y2_byte = int.from_bytes(ser.read(), 'big')
    if y2_byte >= 128 :
        y2_byte -= 256
    print('y2:' +  str(y2_byte))

    mouse.move(x2_byte, -1 * y2_byte, absolute=0)
    


    