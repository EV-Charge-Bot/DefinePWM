import Jetson.GPIO as GPIO
import time, serial
GPIO.setmode(GPIO.BOARD)  
#GPIO.setup(#of pin,GPIO.OUT)

#FL:
FL_IN1=7
FL_IN2=11

#FR:
FR_IN1=12
FR_IN2=15

#BF:
BL_IN1=19
BL_IN2=21

#BR:
BR_IN1=26
BR_IN2=23

#Initialize FL_ENA, FL_IN1, and FL_IN2
FL_PWM= [pin_num] #ENA
GPIO.setup(FL_IN1,GPIO.OUT)
GPIO.setup(FL_IN2,GPIO.OUT)

#Initialize FR_ENA, FR_IN1, and FR_IN2
FR_PWM= [pin_num] #ENA
GPIO.setup(FR_IN1,GPIO.OUT)
GPIO.setup(FR_IN2,GPIO.OUT)

#Initialize BL_ENA, BL_IN1, and BL_IN2
BL_PWM= [pin_num] #ENA
GPIO.setup(BL_IN1,GPIO.OUT)
GPIO.setup(BL_IN2,GPIO.OUT)

#Initialize BR_ENA, BR_IN1, and BR_IN2
BR_PWM= [pin_num] #ENA
GPIO.setup(BR_IN1,GPIO.OUT)
GPIO.setup(BR_IN2,GPIO.OUT)

## Define Motors
Motor_FL=[FL_PWM, FL_IN1, FL_IN2]
Motor_FR=[FR_PWM, FR_IN1, FR_IN2]
Motor_BL=[BL_PWM, BL_IN1, BL_IN2]
Motor_BR=[BR_PWM, BR_IN1, BR_IN2]
PWM_OFF=0
motorSpeed = 0

#to control speed, connect PWM board to PWM pin on GPIO
# and change duty cycle of PWM pin as %
my_PWM=GPIO.setup(pin#,GPIO.OUT) #whatever number for PWM on Jetson
my_PWM=GPIO.PWM(pin#,100) #100 is the freq, unknown range            
DutyCycle=5 #5% range=0-100%
Speed=my_PWM.start(DutyCycle) #control speed
