
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

max = 255
colors = {
        1:(max, 0, 0),
        2:(0, max, 0),
        3:(0, 0, max)
    }
while True:
    
    userInput = input('red color(1) or green color(2) or blue color(3) - enter q to exit')
    if userInput == 'q':break

    try:
        userInput = int(userInput)
    except:
        print('please enter a valid input.')
        continue

    theColor = colors[userInput]
    # if userInput == 1:color=(max, 0, 0) elif userInput == 2 ....
    for i in range(10):
        cp.pixels[i] = theColor
    cp.pixels.show()
