import sys
import time
import qwiic_serlcd
import json

# Default is 16x2 display with i2c address 0x72
LCD_WIDTH = 16
LCD_ROWS = 2
i2c_addr = 0x72

# Otherwise, specify 16x2 | 20x4 for display model followed by
# optional i2c address
# e.g. python3 serlcd.py 20x4 0x72

if len(sys.argv) > 1:
    if (sys.argv[1] == "16x2"):
        LCD_WIDTH = 16
        LCD_ROWS = 2
    elif (sys.argv[1] == "20x4"):
        LCD_WIDTH = 20
        LCD_ROWS = 4
    else:
        print("invalid display size; exiting", file=sys.stderr)
        sys.exit(0)

if len(sys.argv) > 2:
    i2c_addr = int(sys.argv[2], 16)

# print("starting up serlcd.py with size {0}x{1} using i2c address {2}".format(
#    LCD_WIDTH, LCD_ROWS, hex(i2c_addr)), file=sys.stderr)

myLCD = qwiic_serlcd.QwiicSerlcd(i2c_addr)

myLCD.setContrast(50)
myLCD.clearScreen()
time.sleep(1)

while True:
    try:
        line = sys.stdin.readline()
        try:
            msg = json.loads(line)
        except (ValueError):
            print("JSON parse error", file=sys.stderr)
            continue

        if ('payload' in msg and (type(msg['payload']) == str)):
            pass
        else:
            print("unexpected input, skipping", file=sys.stderr)
            continue

        input = msg['payload']
        resp = {}
        if input == "cl:ose":
            myLCD.clearScreen()
#           print("shutting down serlcd.py", file=sys.stderr)
#           sys.exit(0)
        elif input == "clr:":
            myLCD.clearScreen()
        elif input.startswith("1:"):
            myLCD.setCursor(0, 0)
            myLCD.print(input[2:].ljust(LCD_WIDTH))
        elif input.startswith("2:"):
            myLCD.setCursor(0, 1)
            myLCD.print(input[2:].ljust(LCD_WIDTH))
        elif input.startswith("3:"):
            myLCD.setCursor(0, 2)
            myLCD.print(input[2:].ljust(LCD_WIDTH))
        elif input.startswith("4:"):
            myLCD.setCursor(0, 3)
            myLCD.print(input[2:].ljust(LCD_WIDTH))
        elif input.startswith("contrast:"):
            contrast = int(input.split(':')[1])
            if (contrast >= 0 and contrast <= 255):
                myLCD.setContrast(contrast)
        elif input.startswith("backlight:"):
            rgb = input.split(':')[1].split(',')
            red = int(rgb[0], 16)
            green = int(rgb[1], 16)
            blue = int(rgb[2], 16)
            myLCD.setFastBacklight(red, green, blue)
        else:
            myLCD.setCursor(0, 0)
            myLCD.print(input.ljust(LCD_WIDTH))

    except (EOFError, SystemExit, KeyboardInterrupt):
        print("serlcd.py shutting down", sys.stderr)
        sys.exit(0)
