from microbit import *
import radio
import random
import microbit

#setup radio
radio.config(length=251, channel=53, power=4)

sending = 1

def Phone():

    #initialise radio
    radio.on()
    while True:       

        
        msg = str(radio.receive())
        
        global sending
        
        if sending >= 2:
            sending = 0
            
        
        #select page
        while sending == 1:

            message = 0
            messages = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '"', ':)', ':(']
            global tosend
            tosend = messages[message]
            sentance = []

            while True:

                msg = str(radio.receive())

                #prevents errors
                if message >= int(len(messages)):
                    message = int(len(messages))

                #scrolls message when received        
                if msg != 'None':
                    display.scroll(msg)
                    display.show(tosend)

                #scrolls through characters                  
                if microbit.pin0.is_touched():
                    message = message - 1
                    tosend = messages[message]
                    display.show(tosend, delay=200)
                    sleep(200)
                    
                if microbit.pin1.is_touched() and tosend != 9:
                    message = message + 1
                    tosend = messages[message]
                    display.show(tosend, delay=200)
                    sleep(200)
                    
                #adds character to list
                if microbit.button_a.is_pressed():
                    sentance.append(tosend)
                    tosend = messages[message]
                    display.scroll(tosend, delay=50)
                
                #sends list as string
                if sending == 1 and microbit.button_b.is_pressed():
                    radio.send(''.join(sentance))
                    display.scroll(''.join(sentance))
                    sentance = []
                    break
            break


Phone()
        
