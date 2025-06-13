import plotext as plt
import time
import os

LOG_FILE = "/root/ros2_ws/sensor_log.txt"

def read_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()[-50:]  # Show last 50 lines
        try:
            data = [list(map(float, line.strip().split(','))) for line in lines if ',' in line]
        except ValueError:
            data = []
    return data

while True:
    data = read_log()
    plt.clf()
    if data:
        transposed = list(zip(*data))
        for series in transposed:
            plt.plot(series)
    plt.title("Live Sensor Data (from log)")
    plt.show()
    time.sleep(1)  # update every 1 second
