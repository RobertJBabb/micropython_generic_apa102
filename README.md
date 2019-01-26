# micropython_generic_apa102
Generic version of APA102 (Dotstar) LED class

This class implements both the Adafruit DotStar API and the MicroPython ESP8266 APA102 API.
Its derived from the Adafruit DotStar CircuitPython class and back ported to MicroPython.

Both SPI and GPIO pins are supported.

DotStar
color can be one of three things:
                a (r,g,b) list/tuple
                a (r,g,b, brightness) list/tuple
                a single, longer int that contains RGB values, like 0xFFFFFF
            brightness, if specified should be a float 0-1
            
Properties:
  brightness: float 0.0-1.0
Methods:
  init(clock, data, nUmber_of_pixels, *, brightness=1.0, auto_write=True,
                 pixel_order=BGR, baudrate=1000000, spi_bus=1, apa102_cmp=False)
  fill(color)
  show()
  deinit()
  Set/Get list element values:
    Set values are colors as described above
    Get values are returned as (r,g,b) tuples
    
 APA102 ( ESP8266 compatibility mode, same as above except as noted )
  Set/Get list element values:
    Get values are returned as (r,g,b,brightness) tuples 
  
