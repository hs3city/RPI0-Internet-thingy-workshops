from random import choice
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=2, block_orientation=-90)

while True:
  with canvas(device) as draw:
    point_pos = (choice(range(16)),choice(range(8)))
    draw.point(point_pos, fill=255)

