# test generic_dotstar
import time
import generic_dotstar
import machine

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 20)
WHITE = (255, 255, 255)
colors = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA]

num_pixels = 8

clk_pin = machine.Pin(13)
data_pin = machine.Pin(15)
pixels = generic_dotstar.DotStar(clk_pin, data_pin, num_pixels, brightness=0.1, auto_write=False)

pixels[0] = (255, 0, 0)
time.sleep(10)


def wheel(pos):
    """Wheel through range of colors"""
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return 0, 0, 0
    if pos < 85:
        return 255 - pos * 3, pos * 3, 0
    if pos < 170:
        pos -= 85
        return 0, 255 - pos * 3, pos * 3
    pos -= 170
    return pos * 3, 0, 255 - pos * 3


def color_fill(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)


def pixel_count(pixc, stepp):
    return (pixc + stepp - 1) // stepp


def slice_alternating(wait):
    print('slice alternating')
    step = 2
    base = 0
    pixels.fill(0)
    pixels.show()
    time.sleep(wait)
    for clr in colors:
        pixels[base::step] = [clr] * pixel_count(num_pixels, step)
        pixels.show()
        time.sleep(wait)
        base = 0 if base else 1


def slice_rainbow(wait):
    print('slice rainbow')
    pixels.fill(0)
    pixels.show()
    time.sleep(0.5)
    step = 1
    for i, clr in enumerate(colors):
        pixels[i::step] = [clr] * pixel_count(num_pixels-i, step)
        pixels.show()
        time.sleep(wait)

    # test get slice on last 2 pixels
    tstget = pixels[-2::step]
    tstget = [RED] * len(tstget)
    pixels[-2::step] = tstget
    pixels.show()
    time.sleep(wait)


def rainbow_cycle(wait):
    print('rainbow cycle')
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    try:
        # Change this number to change how long it stays on each solid color.
        print('Fill colors')
        for c in colors:
            color_fill(c, 0.5)

        # Increase or decrease this to speed up or slow down the animation.
        slice_alternating(1)

        # color_fill(WHITE, 1)
        color_fill(0, 0.5)
        # Increase or decrease this to speed up or slow down the animation.
        slice_rainbow(1)

        time.sleep(1)
        color_fill(0, 0.5)
        # Increase this number to slow down the rainbow animation.
        rainbow_cycle(0.1)

    except KeyboardInterrupt:
        pixels.deinit()
        raise

