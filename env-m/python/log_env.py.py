import serial
import csv
import time

# ---- Configuration ----
# Change 'COM3' to match your Arduino's serial port.
# On Windows, it's typically 'COM3' or 'COM4'.
# On macOS, it's something like '/dev/cu.usbmodemXXXXX'.
# On Linux, it's something like '/dev/ttyACM0'.

SERIAL_PORT = 'COM5'

# Match the baud rate in your arduino code
BAUD_RATE = 9600

# File that the data should go
FILE_NAME = "sensor_data.csv"

# Open the serial port connection

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT}")
    time.sleep(2)

except serial.Serial.Exception as e:
    print(
        f"Error: Could not open serial port {SERIAL_PORT}. Please check the port name and ensure the security of it's connection. Also check that the Arduino Serial Monitor is closed.")
    print(e)
    exit()

# Open the CSV file to write to.
# 'a' means append mode, so it won't overwrite the file.
# newline='' is important to prevent extra blank rows in Windows.

try:
    with open(FILE_NAME, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Main loop to get data from the arduino
        print("Starting data log. Press Ctrl + C to stop")
        while True:
            line = ser.readline().decode('utf-8')

            # Read a line from the serial port
            if line and not line.startswith("Timestamp"):
                # Split the string with commas
                data = line.split(',')

                # Write the data to the file
                writer.writerow(data)

                # Print data to file
                print(line)

            time.sleep(0.1)  # delay to stop overloading the system

except KeyboardInterrupt:
    print("\nData logging stopped by user")

except Exception as e:
    print(f"An error has occured : {e}")

finally:
    # Closing the Serial port when finished
    ser.close()
    print("Serial port closed")