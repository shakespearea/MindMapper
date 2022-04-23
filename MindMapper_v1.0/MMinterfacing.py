from microbit import *
import math

compass.calibrate()

# Creates MIDI control message to transmit any channel, control number, and value
def midiControlChange(chan, n, value):
    MIDI_CC = 0xB0
    if chan > 15:
        return
    if n > 127:
        return
    if value > 127:
        return
    msg = bytes([MIDI_CC | chan, n, value])
    uart.write(msg)

# Starts MIDI output on pin 0
def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

Start()
# Initialise all variables
lastA = False
lastB = False
lastC = False
last_tiltx = 0
last_tilty = 0
last_tiltz = 0
last_pot = 0
last_dir = 0
last_lit = 0
last_mag = 0
last_temp = 0
animation = 0
counter = 0
button_1 = 0
button_2 = 0
button_3 = 0
last_animation = 0

# Set display to reflect initial button settings
display.set_pixel(0, 0, 9)
display.set_pixel(4, 0, 9)

while True:
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    c = pin1.is_touched()
    pot = pin2.read_analog()

    # If pressed, output button counter information as MIDI control messages.
    # All are output on channel 1
    # Buttons A and B will update display to reflect current setting
    # Button A on control number 31
    if a is True and lastA is False:
        midiControlChange(0, 31, button_1)
        display.set_pixel(0, button_1, 0)
        button_1 = (button_1 + 1) % 2
        display.set_pixel(0, button_1, 9)

    # Button B on control number 32
    if b is True and lastB is False:
        midiControlChange(0, 32, button_2)
        display.set_pixel(4, button_2, 0)
        button_2 = (button_2 + 1) % 4
        counter = 0
        display.set_pixel(4, button_2, 9)

    # Button C on control number 33
    if c is True and lastC is False:
        midiControlChange(0, 33, button_3)
        button_3 = (button_3 + 1) % 2

    # Potentiometer value on control number 34
    if last_pot != pot:
        velocity = math.floor(pot / 1024 * 127)
        midiControlChange(0, 34, velocity)

    lastA = a
    lastB = b
    lastC = c
    last_pot = pot

    # If values change, scale and output sensor information as MIDI messages.
    # Accelerometer X axis on control number 21
    current_tiltx = accelerometer.get_x()
    if current_tiltx != last_tiltx:
        mod_y = math.floor(math.fabs(((current_tiltx + 1024) / 2048 * 127)))
        midiControlChange(0, 21, mod_y)
        last_tiltx = current_tiltx

    # Accelerometer Y axis on control number 22
    current_tilty = accelerometer.get_y()
    if current_tilty != last_tilty:
        mod_y = math.floor(math.fabs(((current_tilty + 1024) / 2048 * 127)))
        midiControlChange(0, 22, mod_y)
        last_tilty = current_tilty

    # Accelerometer Z axis on control number 23
    current_tiltz = accelerometer.get_z()
    if current_tiltz != last_tiltz:
        mod_y = math.floor(math.fabs(((current_tiltz + 1024) / 2048 * 127)))
        midiControlChange(0, 23, mod_y)
        last_tiltz = current_tiltz

    # Compass direction on control number 24
    current_dir = compass.heading()
    if current_dir != last_dir:
        mod_y = math.floor((((current_dir - 0) * (127 - 0)) / (359 - 0)) + 0)
        midiControlChange(0, 24, mod_y)
        last_dir = current_dir

    # Magnetism field strength on control number 25
    current_mag = compass.get_field_strength()
    if current_mag != last_mag:
        mod_y = math.floor((((current_mag - 0) * (127 - 0)) / (200000 - 0)) + 0)
        midiControlChange(0, 25, mod_y)
        last_mag = current_mag

    # Light level on control number 26
    current_lit = display.read_light_level()
    if current_lit != last_lit:
        mod_y = math.floor((((current_lit - 0) * (127 - 0)) / (255 - 0)) + 0)
        midiControlChange(0, 26, mod_y)
        last_lit = current_lit

    # Temperature on control number 27
    current_temp = temperature()
    if current_temp != last_temp:
        mod_y = math.floor((((current_temp - 0) * (127 - 0)) / (35 - 0)) + 0)
        midiControlChange(0, 27, mod_y)
        last_temp = current_temp

    if last_animation != animation:
        # if animation has been incremented, change brightness of heart
        display.set_pixel(1, 2, animation)
        display.set_pixel(1, 3, animation)
        display.set_pixel(2, 1, animation)
        display.set_pixel(2, 2, animation)
        display.set_pixel(3, 2, animation)
        display.set_pixel(3, 3, animation)
    last_animation = animation

    # Move to next brightness setting, speed dependent on button B
    counter += 1
    if counter % ((button_2+1)*5) == 0:
        animation += 1
        animation = animation % 10

    sleep(10)
