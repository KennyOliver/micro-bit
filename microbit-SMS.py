from microbit import *

import radio



# --- CONFIG ---

# Deadzone

deadzone = 350

# Scroll Speed (ms)

scrollspeed = 500



current = 1

characters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

message = []

space = Image("00000:"

              "00000:"

              "00000:"

              "90009:"

              "99999")

newMessage = Image("05950:"

                   "50505:"

                   "95059:"

                   "99599:"

                   "99999")



tick = Image("00000:"

             "00009:"

             "00090:"

             "90900:"

             "09000")



radio.on()



def drawChar():

    if characters[current] == " ":

        display.show(space)

    else:

        display.show(characters[current])



def appendCurrent():

    if button_a.is_pressed():

        message.append(characters[current])

        print(''.join(message))

        display.show(Image().invert())

        sleep(scrollspeed)

    elif button_b.is_pressed():

        radio.send(''.join(message))

        message = []

        current = 1

        display.show(tick)

        sleep((scrollspeed * 2))



def checkForMessages():

    incoming = radio.receive()

    if incoming:

        display.show(newMessage)

        sleep(250)

        display.clear()

        sleep(250)

        display.show(newMessage)

        sleep(250)

        display.clear()

        sleep(250)

        display.show(newMessage)

        sleep(250)

        display.clear()

        sleep(250)

        display.show(newMessage)

        sleep(250)

        display.clear()

        sleep(250)

        display.scroll(incoming)



while True:

    reading = accelerometer.get_x()

    checkForMessages()

        

    if reading > deadzone:

        if current < (len(characters) - 1):

            current = current + 1

        drawChar()

        appendCurrent()

        sleep(scrollspeed)

    elif reading < (deadzone * -1):

        if current > 0:

            current = current - 1

        drawChar()

        appendCurrent()

        sleep(scrollspeed)

    else:

        drawChar()

        appendCurrent()