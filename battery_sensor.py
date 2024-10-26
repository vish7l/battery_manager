from serial import Serial, SerialException
import psutil
import time

# Set up serial communication
try:
    ser = Serial("/dev/tty.usbmodem14101", 9600) # Replace 'XXXX' with your Arduino's identifier
except SerialException:
    print("The serial port is already in use. Please close any other applications using it and try again.")
    exit()

time.sleep(2) # Give serial connection a bit of time to initialize

signal_sent = False  # Flag to track if we've already sent the signal

while True:
    battery = psutil.sensors_battery()
    percentage = battery.percent

    if percentage >= 80 and not signal_sent:
        ser.write(b'80') # Send '85' to the Arduino
        signal_sent = True  # Set the flag to indicate we've sent the signal
        time.sleep(60) # Wait for a minute before checking again to avoid spam
    else:
        time.sleep(10) # Check every 10 seconds
