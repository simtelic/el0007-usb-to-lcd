# Python script to test Simtelic USB to LCD module

This repository contains a Python script (`lcdtest.py`) that allows you to communicate with LCD displays connected to your computer via a USB-to-LCD adapter.

## Requirements
- Python 3 (https://www.python.org/downloads/)
- pyserial library (https://pyserial.readthedocs.io/en/latest/)

##### Install dependencies (Windows)
```
py -m pip install pyserial
```
##### Install dependencies (Linux)
```
pip install pyserial
```

## Usage

#### Clone the repository:
   
```
git clone https://github.com/simtelic/el0007-usb-to-lcd.git
```

If `git` is not available, download the source code snapshot from [GitHub](https://github.com/simtelic/el0007-usb-to-lcd/archive/refs/heads/main.zip).

#### Run the script:

##### Windows:
Use a application like *Device Manager* to identify the assigned COM port (e.g., COM3).
```
py lcdtest.py COM3 # Replace with your actual serial port
```

##### Linux:
Use a tool like `ls /dev/tty*` or `dmesg | grep tty` to find the serial port assigned to your USB-to-LCD adapter. It's typically named `/dev/ttyACM0`, but it might vary.
```
python3 lcdtest.py /dev/ttyACM0  # Replace with your actual serial port
```

## Additional Notes

- Ensure the USB-to-LCD adapter is properly connected to your computer and the LCD display before running the script.
- This README provides a basic usage guide. More advanced use cases might require additional configuration or code modifications.
