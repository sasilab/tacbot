import streamlit as st
import pandas as pd
import time
import os

LOG_FILE = "/root/ros2_ws/sensor_log.txt"

st.set_page_config(layout="wide")
st.title("Live Sensor Data")

placeholder = st.empty()

def read_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()[-100:]
        return [list(map(float, line.strip().split(','))) for line in lines if ',' in line]

while True:
    data = read_log()
    if data:
        df = pd.DataFrame(data)
        placeholder.line_chart(df)
    time.sleep(1)
