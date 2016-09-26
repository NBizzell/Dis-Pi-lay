import RPi.GPIO as GPIO
from time import sleep, time
import picamera

camera = picamera.PiCamera()
question = ""
answer = ""
greenAns = ""
greenQue = ""
complete = 0
score = 0
questionlist = [1,2,3,4,5,6]
start = ""
end = ""
quiztime = ""

GPIO.setmode(GPIO.BOARD)

#set up outputs
GPIO.setup(3, GPIO.OUT) #red
GPIO.setup(5, GPIO.OUT) #green 1
GPIO.setup(11, GPIO.OUT)#green 2
GPIO.setup(15, GPIO.OUT)#green 3
GPIO.setup(21, GPIO.OUT)#green 4
GPIO.setup(29, GPIO.OUT)#green 5
GPIO.setup(33, GPIO.OUT)#green 6
GPIO.setup(37, GPIO.OUT)#green 7
GPIO.setup(10, GPIO.OUT)#green 8
GPIO.setup(16, GPIO.OUT)#green 9
GPIO.setup(22, GPIO.OUT)#green 10
GPIO.setup(26, GPIO.OUT)#green 11
GPIO.setup(36, GPIO.OUT)#green 12

#setup inputs
GPIO.setup(7, GPIO.IN) #button 1
GPIO.setup(13, GPIO.IN)#button 2
GPIO.setup(19, GPIO.IN)#button 3
GPIO.setup(23, GPIO.IN)#button 4
GPIO.setup(31, GPIO.IN)#button 5
GPIO.setup(35, GPIO.IN)#button 6
GPIO.setup(8, GPIO.IN) #button 7
GPIO.setup(12, GPIO.IN)#button 8
GPIO.setup(18, GPIO.IN)#button 9
GPIO.setup(24, GPIO.IN)#button 10
GPIO.setup(32, GPIO.IN)#button 11
GPIO.setup(38, GPIO.IN)#button 12
GPIO.setup(40, GPIO.IN)#start/reset

#set functions

def flashred(number)
    for n in range (0, number)
        GPIO.output(3, GPIO.HIGH)
        sleep(1)
        GPIO.output(3, GPIO.LOW)
        sleep(0.5)
        
def flashall (number)
    for n in range (0, number)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(29, GPIO.HIGH)
        GPIO.output(33, GPIO.HIGH)
        GPIO.output(37, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(32, GPIO.HIGH)
        GPIO.output(36, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(29, GPIO.LOW)
        GPIO.output(33, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(32, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        sleep(0.5)

    
def buttonQuestion(channel):  

    #set LED based on button press
    if channel == 7
        greenQue = 5
        question = 0
    elif channel == 13
        greenQue = 11
        question = 1
    elif channel == 19
        greenQue = 15
        question = 2
    elif channel == 23
        greenQue = 21
        question = 3
    elif channel == 31
        greenQue = 29
        question = 4
    elif channel == 35
        greenQue = 33
        question = 5

    #check if answer pressed first if not add as question and wait for answer.
    if answer = "":
        #set LED to green and wait for question
        GPIO.output(greenQue, GPIO.HIGH)
    else
        #if so check if correct
        if answer == questionlist[question]:
            #correct light the answers green and stay green
            GPIO.output(greenQue, GPIO.HIGH)
            #set complete to complete +1
            complete = complete + 1
            #set score to  score +1
            score = score + 1
            #reset variables
            question = ""
            answer = ""
            greenAns = ""
            greenQue = ""
        else
            #false flash all red and put out green
            GPIO.output(greenAns, GPIO.low)
            GPIO.output(greenQue, GPIO.low)
            GPIO
            flashred(3)
            question = ""
            answer = ""
            greenAns = ""
            greenQue = ""
            #set score to score -1 to credit right first time.
            score = score - 1
        
def buttonAnswer(channel):
    #set answer to button pressed in 1 - 6 range
    #to use as index for the 6 item answer list
    answer = channel
    
    if channel == 8
        greenAns = 37
    elif channel == 12
        greenAns = 10
    elif channel == 18
        greenAns = 16
    elif channel == 24
        greenAns = 22
    elif channel == 32
        greenAns = 26
    elif channel == 38
        greenAns = 36

    #check if question pressed first if not add as answer and wait for question.
    if question = "":
        #set LED to green and wait for question
        GPIO.output(greenAns, GPIO.HIGH)
    else
        #if so check if correct
        if answer == questionlist[question]:
            #correct light the answers green and stay green
            GPIO.output(greenAns, GPIO.HIGH)
            #set complete to complete +1
            complete = complete + 1
            #set score to  score +1
            score = score + 1
            #reset variables
            question = ""
            answer = ""
            greenAns = ""
            greenQue = ""
        else
            #false flash all red and put out green
            GPIO.output(greenAns, GPIO.low)
            GPIO.output(greenQue, GPIO.low)
            GPIO
            flashred(3)
            question = ""
            answer = ""
            greenAns = ""
            greenQue = ""
            #set score to score -1 to credit right first time.
            score = score - 1

    

#check for new config
    #if start/reset button held in start config mode
if (GPIO.input(40)):
    #set up matches using button presses

else
    #get config information from text file storage then populate the list.
    questionlist = open('file.txt').read().splitlines()

#wait for start button push
while:
    #show leaderboard?
    #wait for button press
    GPIO.wait_for_edge(40, GPIO.RISING)

    #on start button push pause 3 second and take picture

    print ('smile, camera will take picture in 3 seconds')
    camera.start_preview()
    sleep(1)
    camera.capture('image.jpg')
    camera.stop_preview()

    #flash lights 3-2-1-go (start timer)

    print('3')
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    sleep(1)
    print ('2')
    GPIO.output(15, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    sleep(1)
    print('1')
    GPIO.output(15, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    sleep(1)
    print('GO!')
    GPIO.output(15, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)

    #start timer
    start = time.time()
    
    #wait for button press    

    while complete > 6:
 
        GPIO.add_event_detect(7, GPIO.FALLING, callback=buttonQuestion, bouncetime=300)  
        GPIO.add_event_detect(13, GPIO.FALLING, callback=buttonQuestion, bouncetime=300)  
        GPIO.add_event_detect(19, GPIO.FALLING, callback=buttonQuestion, bouncetime=300)  
        GPIO.add_event_detect(23, GPIO.FALLING, callback=buttonQuestion, bouncetime=300)  
        GPIO.add_event_detect(31, GPIO.FALLING, callback=buttonQuestion, bouncetime=300)  
        GPIO.add_event_detect(35, GPIO.FALLING, callback=buttonQuestion, bouncetime=300) 

        GPIO.add_event_detect(8, GPIO.FALLING, callback=buttonAnswer, bouncetime=300)  
        GPIO.add_event_detect(12, GPIO.FALLING, callback=buttonAnswer, bouncetime=300)  
        GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonAnswer, bouncetime=300)  
        GPIO.add_event_detect(24, GPIO.FALLING, callback=buttonAnswer, bouncetime=300)  
        GPIO.add_event_detect(32, GPIO.FALLING, callback=buttonAnswer, bouncetime=300)  
        GPIO.add_event_detect(38, GPIO.FALLING, callback=buttonAnswer, bouncetime=300)  

        print('Score: ' & score & /n & 'Complete: ' & complete)

    #when all matched (record time with photo and score)

    #end time
    end = time.time()
    #calculate total time
    quiztime = end - start

    timescorename = score & quiztime & '.jpg'

    os.rename (image.jpg, timescorename)


    #flash green lights in celebration
    flashall(3)
    print('Well Done!' & /n & 'Your time was: '  & quiztime & /n & 'Your Score was: ' & Score


    #reset variables
    question = ""
    answer = ""
    greenAns = ""
    greenQue = ""

except KeyboardInterrupt:
    
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
    GPIO.cleanup()           # clean up GPIO on normal exit 
