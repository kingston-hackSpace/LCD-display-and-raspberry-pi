#This code builds on the LCD Test script work of Matt Hawkins 
#found here at https://www.raspberrypi-spy.co.uk/

#!/usr/bin/python

import requests
import json
import time
import webbrowser,os,sys
from selenium import webdriver
import RPi.GPIO as GPIO
import serial

LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
E_PULSE = 0.001
E_DELAY = 0.001
 
prog_state = 0
counter = 25
text = ""
generated = False

option_1 = False
option_2 = False
option_3 = False
option_4 = False

def test_options():
    options_string=("",button_1(),"/",button_2(),"/",button_3(),"/",button_4(),"/",button_5(),"...")
    return options_string
 
def main():
	prog_state = 0
  # Main program block
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
	GPIO.setup(LCD_E, GPIO.OUT)  # E
	GPIO.setup(LCD_RS, GPIO.OUT) # RS
	GPIO.setup(LCD_D4, GPIO.OUT) # DB4
	GPIO.setup(LCD_D5, GPIO.OUT) # DB5
	GPIO.setup(LCD_D6, GPIO.OUT) # DB6
	GPIO.setup(LCD_D7, GPIO.OUT) # DB7
	time.sleep(2)
	GPIO.setup(14 , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(25 , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(18 , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(23 , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(24 , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  # Initialise display
	lcd_init()
	time.sleep(2)
	option_1 = False
	option_2 = False
	option_3 = False
	option_4 = False

	while True:
    # Send some test

#		if GPIO.input(14) == GPIO.HIGH:
#			print("pressed",prog_state)
		if prog_state == 0:
	# Send some test
			lcd_string("Press Buttons ",LCD_LINE_1)
			lcd_string("To Make Music",LCD_LINE_2)
			read_serial=ser.readline()
			s[0] = int (ser.readline(),16)
			prog_state = 1
			counter = 3
			text = " "
		if prog_state == 1:
#			test_options()
			read_serial=ser.readline()
			s[0] = int (ser.readline(),16)
			lcd_string("You pressed", LCD_LINE_1)
			if s[0] == 381 and option_1 == False:	
				text +=" 1 "
				option_1 = True
			if s[0] == 373 and option_2 == False:	
				text +=" 2 "
				option_2 = True
			if s[0] == 365 and option_3 == False:	
				text +=" 3 "
				option_3 = True
			if s[0] == 357 and option_4 == False:	
				text +=" 4 "
				option_4 = True
			
			
			lcd_string(text, LCD_LINE_2)
			counter-=1;
			print(counter)
			if counter<0:
				counter = 3
				prog_state = 2
				generated = False
		if prog_state == 2:
			lcd_string("Music Is Being", LCD_LINE_1)
			lcd_string("Generated", LCD_LINE_2)
			init_api(generated,option_1,option_2,option_3,option_4,option_5,option_6,option_7,option_8,option_9,option_10,option_11,option_12,option_13,option_14,option_15,option_16,option_17,option_18,option_19,option_20
)
			time.sleep(E_DELAY)
			prog_state = 3
		if prog_state ==3:
			lcd_string("Enjoy!", LCD_LINE_1)
			lcd_string("", LCD_LINE_2)  
			read_serial=ser.readline()
			s[0] = int (ser.readline(),16)
			if (s[0] == 381):
				os.system("killall chromium-browser")
				option_1=False
				option_2=False
				option_3=False
				option_4=False
				
				prog_state =0

def button_1():
    if GPIO.input(14) == GPIO.HIGH:
        return "1"
def button_2():
    if GPIO.input(25) == GPIO.HIGH:
        return "2"
def button_3():
    if GPIO.input(18) == GPIO.HIGH:
        return "3"
def button_4():
    if GPIO.input(23) == GPIO.HIGH:
        return "4"
def button_5():
    if GPIO.input(24) == GPIO.HIGH:
        return "5"

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()

 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line):
  # Send string to display
 
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 

def init_api(generated,option_1,option_2,option_3,option_4
):
	print ("initialised")
	test_str = str("https://api.sunoaiapi.com/api/v1/gateway/generate/gpt_desc")

	headers = {"api-key":"1MCUw0M1QWJ6VcAcY1cPX+iJoT4acrrN","Content-Type":"application/json"}

	description = "parameters: "

	if option_1 == True:
		description +="Torment "
	if option_2 == True:
		description +="Country Jazz "
	if option_3 == True:
		description +="Chanson soul "
	if option_4 == True:
		description +="ChillWave "
	
	print (description)
	foo = {'gpt_description_prompt': description,"make_instrumental":True, "mv": "chirp-v3-0"}
	response = requests.post(test_str, headers=headers, json=foo)

	music_data = response.json()
  #print("API response", music_data)

	track_id =music_data['data'][0]['song_id']

	wavdl = str("https://API_URL_HERE/api/v1/gateway/query?ids="+track_id)

	print(wavdl)

	headers = {"api-key":"INSERT_API_KEY_HERE","Content_type":"application/json"}

	for i in range (40):
		if(generated==False):
			response = requests.get(wavdl,headers=headers)
			song_data = response.json()
			print("song response", song_data[0]['audio_url'])
			if(song_data[0]['audio_url']):
				generated = True
				print("load browser")
				comma = "'"
				webbrowser.open_new(song_data[0]['audio_url'])
				time.sleep(2)
			else:
				time.sleep(2)

if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1)
    GPIO.cleanup()
 
