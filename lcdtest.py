# ---------------------------------------------------------------------------
# Sample script to demonstrate Simtelic USB to LCD features.
# 
# Author: Dilshan Jayakody [jayakody2000lk@gmail.com]
# Last updated: 9th March 2024
# ---------------------------------------------------------------------------

import sys
import time
import select
import serial

if sys.platform == 'win32':
    import threading
    import msvcrt
else:
    import termios


def wait_fro_keypress_with_timeout(timeout=5):
    print("   Press any key to start the next test or wait for 10 seconds...")
    if sys.platform == 'win32':
        class KeyboardThread(threading.Thread):
            def __init__(self):
                self.timeout = False
                super().__init__()

            def run(self):
                while True:
                    if msvcrt.kbhit():
                        if ord(msvcrt.getche()) == 13:
                            break
                    if self.timeout:
                        break
                        
        kb_thread = KeyboardThread()
        kb_thread.start()
        kb_thread.join(timeout)
        kb_thread.timeout = True
    else:
        select.select([sys.stdin], [], [], timeout)
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: lcdtest PORT")
        if sys.platform == 'win32':
            print("  e.g: lcdtest COM3")
        else:
            print("  e.g: lcdtest /dev/ttyACM0")
        exit(1)

# Create serial connection on specified port with baud rate of 57600 and 8N1 configuration.
lcd_serial = serial.Serial()
lcd_serial.baudrate = 57600
lcd_serial.port = sys.argv[1]

# Open serial connection.
try:
    lcd_serial.open()
except Exception as e:
    if not lcd_serial.is_open:
        print("Unable to open specified serial port: " + sys.argv[1])
    else:
        print(e)
    exit(1)

# ---------------------------------------------------------------------------
print("1. Show multiline text on LCD screen")
sample_str = '\x1bIP Address\n\r192.168.1.1'
lcd_serial.write(sample_str.encode('ascii'))
wait_fro_keypress_with_timeout()

# ---------------------------------------------------------------------------
print("2. Clearing the LCD screen")
lcd_serial.write('\x1b'.encode('ascii'))
wait_fro_keypress_with_timeout()

# ---------------------------------------------------------------------------
print("3. Set text positions - Demo 1")
sample_str = '\x1b\t\t\t\t\tHello\n\r\t\t\t\t\tWorld'
lcd_serial.write(sample_str.encode('ascii'))
wait_fro_keypress_with_timeout()

# ---------------------------------------------------------------------------
print("4. Set text positions - Demo 2")
sample_str = '\x1bProgress: 00'
lcd_serial.write(sample_str.encode('ascii'))

for pos in range(10, 101, 5):
    time.sleep(0.75)
    sample_str = '\x7f\x7f' + str(pos)
    lcd_serial.write(sample_str.encode('ascii'))

wait_fro_keypress_with_timeout(1)

# ---------------------------------------------------------------------------
print("5. Cursor control and styles")
sample_str = '\x1bPrice: '
lcd_serial.write(sample_str.encode('ascii'))
time.sleep(3)

lcd_serial.write('\x11'.encode('ascii'))
time.sleep(3)

lcd_serial.write('\x13'.encode('ascii'))
time.sleep(3)

lcd_serial.write('\x14'.encode('ascii'))

wait_fro_keypress_with_timeout(1)
lcd_serial.write('\x12'.encode('ascii'))

# ---------------------------------------------------------------------------
print("6. Backlight control")
sample_str = '\x1b\t\t\t\t\tTEST'
lcd_serial.write(sample_str.encode('ascii'))
time.sleep(1)
lcd_serial.write('\x0e'.encode('ascii'))

time.sleep(2)
lcd_serial.write('\x0f\x1b\t\t\t\t\tFinish'.encode('ascii'))

# ---------------------------------------------------------------------------
lcd_serial.close()
