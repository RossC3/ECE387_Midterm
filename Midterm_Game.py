import pygame
import smbus
import math
from time import sleep

pygame.init()

#Chip Setup
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H =0x47


screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Midterm Game")



x = 50
y = 440
width = 40
height = 40
vel = 5


gY = 0
i = 0
left = False
right = False
initialPos = 0
run = True



def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    #Write Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    #Write to Configuration Register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    #ACcelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)

    #concatenate higher and lower value
    value = ((high << 8) | low)

    #to get signed value from mpu6050
    if(value> 32768):
        value = value - 65536
    return value

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def getYRotation(x,y,z):
    rads = math.atan2(x, dist(y,z))
    return - math.degrees(rads)
bus = smbus.SMBus(1)
Device_Address = 0x68 #MPU6050 device address

MPU_Init()






while run:
    
    pygame.time.delay(50)
    
    
    
    #REad Accelerometer
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)


    #Read Gyroscope raw value

    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)

    Ax= acc_x/16384.0
    Ay= acc_y/16384.0
    Az= acc_z/16384.0

    Gx= gyro_x/131.0
    Gy= gyro_y//131.0
    Gz= gyro_z/131.0
    
    
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if getYRotation (Ax,Ay,Az) < -5:
        initialPos = 0
        x -= vel 
#        initialPos -=1
#        left = True
#        right = False
        
    if getYRotation (Ax,Ay,Az) > 0:
        initialPos= 0
        x += vel
#        left = False
#        right = True
#        initialPos += 1
    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
    
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0), (x,y,width,height))
    
    i+= 1
    
    print(getYRotation (Ax,Ay,Az))
    pygame.display.update()
    
pygame.quit()