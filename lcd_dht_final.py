import Adafruit_DHT
import I2C_LCD_driver
import time
import RPi.GPIO as GPIO 

sensor_name = Adafruit_DHT.DHT11
sensor_pin = 17

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("Kanav Home Clock")

time.sleep(2)

try:

    while 1:        
        mylcd.lcd_clear()
        for i in range(9):
            mylcd.lcd_display_string("Time: %s" % time.strftime("%H:%M:%S"), 1)
            mylcd.lcd_display_string("Date: %s" % time.strftime("%d/%m/%Y"), 2)
            i += 1
	    time.sleep(1)
        
	humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin)    
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Temp = {} c".format(temperature),1)
        mylcd.lcd_display_string("hum = {} %".format(humidity),2)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
    mylcd.lcd_clear()