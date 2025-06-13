import serial
import time

def log_serial_data(port='/dev/ttyACM0', baudrate=115200, output_file='sensor_log.txt'):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Connected to {port} at {baudrate} baud.")

        with open(output_file, 'a') as f:
            while True:
                line = ser.readline().decode(errors='ignore').strip()
                if line:
                    print(line)
                    f.write(line + '\n')
                    f.flush()
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Logging stopped by user.")

if __name__ == '__main__':
    log_serial_data()
