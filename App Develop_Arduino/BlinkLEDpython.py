import RPi.GPIO as IO            
import time                            

IO.setmode (IO.BOARD)      
IO.setup(40,IO.OUT)             
IO.output(40,1)                     
time.sleep(1)                       
IO.cleanup()                      
time.sleep(1)                     

#loop is executed second time        
IO.setmode (IO.BOARD)
IO.setup(40,IO.OUT)
IO.output(40,1)
time.sleep(1)
IO.cleanup()
time.sleep(1)

#loop is executed third time
IO.setmode (IO.BOARD)
IO.setup(40,IO.OUT)
IO.output(40,1)
time.sleep(1)
IO.cleanup()
time.sleep(1)