import time, sys

maxValue = 101 # add +1 for your value! Exam. 100 = 101
progressBar = sys.stdout.write

for currentValue in range(maxValue):
    progressBar("\r [ Downloading %d" %currentValue + "% ] " + "#" * currentValue) # "#" * i only for visualization
    time.sleep(.5) # Progressbar speed control
