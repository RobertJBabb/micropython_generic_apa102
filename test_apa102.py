import time

# generic dotstar
from generic_dotstar import DotStar as APA102
from machine import Pin

# run in Adafruit Dotstar mode
num_pixels = 8
clk = Pin(13, Pin.OUT)
dout = Pin(15, Pin.OUT)
pixels = APA102(clk, dout, num_pixels)

pixels[0] = (255, 10, 10, 0.2)
r, g, b = pixels[0]
pixels.show()
time.sleep(2)
pixels.deinit()

# now run in micropython apa102 compatibility mode
clock = Pin(13, Pin.OUT)  # set GPIO13 to output to drive the clock
data = Pin(15, Pin.OUT)  # set GPIO15 to output to drive the data
apa = APA102(clock, data, 8, apa102_cmp=True)  # create APA102 driver on the clock and the data pin for 8 pixels
apa[0] = (255, 255, 255, 31)  # set the first pixel to white with a maximum brightness of 31
apa.write()  # write data to all pixels
r, g, b, brightness = apa[0]  # get first pixel colour

time.sleep(2)
apa.deinit()
