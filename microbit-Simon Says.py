from microbit import *
import random
 
left = Image("96300:"
             "96300:"
             "96300:"
             "96300:"
             "96300")
             
right = Image("00369:"
             "00369:"
             "00369:"
             "00369:"
             "00369")
 
plus = Image("00000:"
             "00900:"
             "09990:"
             "00900:"
             "00000")
 
AB = ["A", "B"]
 
#Let's start with a sequence of three characters
sequence = random.choice(AB) + random.choice(AB) + random.choice(AB)
 
            
correct = True
sleep(1000)
 
while correct == True:
  #Let's start by displaying the sequence
  for character in sequence:
        if character=="A":
            display.show(left)
        elif character=="B":
            display.show(right)
        sleep(1000)
        display.show(plus)
        sleep(500)
   
  display.scroll("?")
   
  #Capture user input
  #The numbers of time the user will need to press the buttons depends on the length of the sequence
  maxInputs = len(sequence)
  capturedInputs = 0
  while capturedInputs < maxInputs and correct == True:
     if button_a.is_pressed():
        display.show(left)
        #Did the user guess it wrong? 
        if sequence[capturedInputs] == "B":
            correct = False
        sleep(500)    
        display.show(plus)        
        capturedInputs += 1
     if button_b.is_pressed():
        display.show(right)
       #Did the user guess it wrong? 
        if sequence[capturedInputs] == "A":
            correct = False
        sleep(500)
        display.show(plus)
        capturedInputs += 1
        
  #Add an extra character to the sequence
  if correct==True:
        sequence = sequence + random.choice(AB)
        display.show(Image.HAPPY)
        sleep(1000)
 
#Display Game Over  + final score
if len(sequence)>3:    
    display.scroll("Game Over: Score: " + str(len(sequence))) 
else:
    display.scroll("Game Over: Score: 0")