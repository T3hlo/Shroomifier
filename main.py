from machine import Pin,ADC, I2C
from time import sleep
import tm1637
import sht31
import ujson as json

# Humidity tolerance in %
tolerance = 0.01
min_overshoot = 3 #minutes to overhoot once target reached

# Sensor pins
scl_pin=15
sda_pin=14

# power pin for the sensor this can be used to power it down should it freeze
pwr_pin = 13

# LED pin of push button
led_button = 2

# HUID
pot_pin = 26
push_pin = 1

# Relays
rly_0_pin = 5
rly_1_pin = 4


# Set up LEDs
led_pcb = machine.Pin("LED", machine.Pin.OUT)
led = machine.Pin(led_button, machine.Pin.OUT)
    
# initiate display
display = tm1637.TM1637(clk=machine.Pin(16), dio=machine.Pin(17))
display.scroll("shroomifier", delay=200)

#initiate push button
push_button = Pin(push_pin, Pin.IN, Pin.PULL_UP)

# initiate potentiometer
pot = ADC(pot_pin)

# Relays
relay0 = Pin(rly_0_pin, Pin.OUT)
relay1 = Pin(rly_1_pin, Pin.OUT)

# make sure they start turned off
relay0.value(0)
relay1.value(0)

# turn on sensir power
pwr = machine.Pin(pwr_pin, machine.Pin.OUT)
pwr.on()

# set up sensor
i2c = I2C(1, scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin), freq =300000)
sensor = sht31.SHT31(i2c, addr=0x44)

def blink(t=0.5):
    led.on()
    led_pcb.on()
    sleep(t)
    led.off()
    led_pcb.off()
    
    
def get_button():
    return not push_button.value()


def save_config(target):
    '''
    Save the target humidty as json.
    '''
    
    jsonData = {"targetHum": target}

    try:
        with open('config.json', 'w') as f:
            json.dump(jsonData, f)
    except:
        print("Could not save the target variable.")


def read_potentiometer():
    pot_value = pot.read_u16()
    td= 0.1+pot_value/65535
    td = int((td/1.1)*100)

    return 109-td



# try and load target humnidty
try:
    with open('config.json', 'r') as f:
        data = json.load(f)
        target_hum= data["targetHum"]
except:
    target_hum= 85
    
    
print(f'Target humidty: {target_hum} % RH')


def change_target(target_hum):
    
    print('waiting for input')
    
    sleep(1.5)

    while True:

        # remember the settings
        #save_config(target_hum)
        target_hum = read_potentiometer()
        display.humidity(target_hum)

        #blink the LED and the display
        blink(0.1) 
        sleep(0.1)
        blink(0.01) 
        display.clear()
        sleep(0.1)
        
        if get_button():
            print('saving setting')
            print(f'New target: {target_hum}')
            # if user confirms via button save settings
            save_config(target_hum)
            return target_hum
            break
        

def startup_sequence(target_hum):
    
    # At start up wait for user to change target
    counter = 0

    while counter<10:

        display.humidity(target_hum)
          
        #blink the LED and the display
        blink(0.1) 
        sleep(0.2)
        blink(0.1) 
        display.clear()
        sleep(0.5)

        counter +=1    

        target_hum = read_potentiometer()

        if get_button():
            
            sleep(1.5)

            change_target(target_hum)
            
        else:
            continue
        break
        
startup_sequence(target_hum)

while True:

  sleep(1)

  temp, hum = sensor.get_temp_humi()
  print(f'Humidty: {hum} %RH\nTemperature: {temp}')
  
  # check if user wants to update target
  if get_button():
      print('change requested')
      change_target(target_hum)
  
  
  display.humidity(hum)
    

  if hum < target_hum-(target_hum*tolerance):
      
      while hum < target_hum:
         
          #temp, hum = readDHT()
          temp, hum = sensor.get_temp_humi()
          print(f'Humidty: {hum} %RH\nTemperature: {temp}')

          # check if user wants to update target
          if get_button():
              print('change requested')
              change_target(target_hum)
              
          display.humidity(hum)
          
          blink() 

          relay0.value(1)
          relay1.value(1)
          sleep(10)
          
      else:
          print("Target reached deliberate overshoot")
          sleep(60*min_overshoot)
          relay0.value(0)
          relay1.value(0)
          sleep(10)
          
          blink() 

          
  blink() 

  sleep(10)
  






