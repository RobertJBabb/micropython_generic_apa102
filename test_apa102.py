import time

# generic dotstar
from generic_dotstar import DotStar
from generic_dotstar import Apa102DotStar as APA102
from generic_dotstar import SpiDotStar as SPIDotStar
from machine import SPI, Pin

# run in Adafruit Dotstar mode
print('Testing DotStar Class')
num_pixels = 8
clk = Pin(13, Pin.OUT)
dout = Pin(15, Pin.OUT)
pixels = DotStar(clk, dout, num_pixels)

pixels[0] = (255, 10, 10, 0.2)
r, g, b = pixels[0]
pixels.show()
time.sleep(2)
pixels.deinit()

# now run in micropython apa102 compatibility mode
print('Testing ESP8266 APA102 Compatibility Class')
clock = Pin(13, Pin.OUT)  # set GPIO13 to output to drive the clock
data = Pin(15, Pin.OUT)  # set GPIO15 to output to drive the data
apa = APA102(clock, data, 8)  # create APA102 driver on the clock and the data pin for 8 pixels
apa[0] = (255, 255, 255, 31)  # set the first pixel to white with a maximum brightness of 31
apa.write()  # write data to all pixels
r, g, b, brightness = apa[0]  # get first pixel colour, note: includes brightness
time.sleep(2)
apa.deinit()

print('Testing MicroPython 1.10 SPI DotStar Compatibility Class')
# spi = SPI(1, sck=Pin(13), mosi=Pin(15), baudrate=1000000)
spi = SPI(1)
spi.init(sck=clock, mosi=data, baudrate=1000000)
pixelp = SPIDotStar(spi, num_pixels)
pixelp[0] = (0, 255, 0)
pixelp.show()
r, g, b = pixelp[0]
time.sleep(2)
pixelp.deinit()
