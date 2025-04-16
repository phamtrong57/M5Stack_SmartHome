from m5stack import *
from m5ui import *
from uiflow import *

# Example: Display text on the screen
setScreenColor(0x222222)
label1 = M5TextBox(10, 10, "Hello, UIFlow!", lcd.FONT_Default, 0xFFFFFF, rotate=0)