import serial
import serial.tools.list_ports

class D01Sensor:
    def __init__(self, baudrate=115200):
        self.ser = self._find_device(baudrate)

    def _find_device(self, baudrate):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if 'ACM' in port.device or 'USB' in port.device:
                try:
                    return serial.Serial(port.device, baudrate, timeout=1)
                except serial.SerialException:
                    continue
        raise RuntimeError("No suitable serial device found.")

    def read_line(self):
        if self.ser.in_waiting:
            line = self.ser.readline().decode(errors='ignore').strip()
            return line.split(',')
        return None
