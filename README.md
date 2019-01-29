# micropython_generic_apa102
Generic version of APA102 (Dotstar) LED class

This class implements the Adafruit DotStar API, the MicroPython ESP8266 APA102 API, and the MicroPython SPI DotStar API.
The code is derived from the Adafruit DotStar CircuitPython class and back ported to MicroPython.
The focus of this implementation is backward compatibility, performance was a secondary goal.
If GPIO pins are specified for clock and data the older lower performance "bit banging" technique
is used rather than the newer software SPI technique. This preserved the existing API that only required clock and data pins 
instead of an SPI object. 

This implementation has only been tested on the ESP32 and MicroPython 1.9.4

Two example/test files are included. The examples show simple class usage and some variations on the Adafruit DotStar examples that are more compact.

The three APIs supported are:

Adafruit DotStar:
  * Only SPI clock and data pins are required
  * Brightness values are specified as a float between 0.0 and 1.0
  * Color values returned consist of R, G, B tuples
  
Micropython ESP8266 APA102:
  * Only SPI clock and data pins are required
  * Brightness values are specified as an int between 0 and 31
  * Color values returned consist of R, G, B, Brightness tuples
  
MicroPython DotStar:
  * An SPI object is required
  * Brightness values are specified as a float between 0.0 and 1.0
  * Color values returned consist of R, G, B tuples
  
**Adafruit DotStar** (default mode)

color can be one of three things:

 a (r,g,b) list/tuple
 
 a (r,g,b, brightness) list/tuple
                
 a single, longer int that contains RGB values, like 0xFFFFFF
                
 brightness, if specified should be a float 0-1
            
Properties:
  brightness: float 0.0-1.0
  
Methods:

  init(clock, data, number_of_pixels, *, brightness=1.0, auto_write=True,
                 pixel_order=BGR, baudrate=1000000, spi_bus=1, apa102_cmp=False)
                 
  fill(color)
  
  show()
  
  deinit()
  
  Set/Get list element values:
  
   Set values are colors as described above.
    
   Get values are returned as (r,g,b) tuples.
    
    
 **MicroPython APA102** ( ESP8266 compatibility mode, same as above except as noted )
  Get list element values:
    Get values are returned as (r,g,b,brightness) tuples
  write()
  
  **Micropython SPI DotStar**
  
  Same as Adafruit DotStar, but requires and SPI object instead of clock and data Pin objects
  
