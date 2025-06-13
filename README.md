Here's the complete content of your `README.md` in proper Markdown format — ready to copy and paste into a file named `README.md`:

---

````markdown
# ROS 2 Docker Workspace for Tacterion DevKit

This repository contains a ROS 2 Humble workspace running inside Docker, integrated with the Tacterion DevKit. It supports sensor data logging and live visualization using CLI or Streamlit.

---

## 🚀 Getting Started

### 🔧 Build Docker Image

```bash
cd docker
docker build -t ros2_humble_image .
````

---

### 🐳 Run Docker Container

```bash
docker run -it --rm \
  --device=/dev/ttyACM0 \
  --network=host \
  -v $(pwd)/../:/root/ros2_ws \
  --name ros2_dev \
  ros2_humble_image
```

---

## 🛠 Inside Container

### Build ROS 2 Workspace

```bash
source /opt/ros/humble/setup.bash
source /root/ros2_ws/.venv/bin/activate
colcon build
source install/setup.bash
```

---

## 📡 Run Sensor Node

```bash
ros2 run tacterion_ros ros_node
```

---

## 📊 Run Visualizer

```bash
ros2 run tacterion_ros visualize_node
```

---

## 🔁 Streamlit Live Dashboard (optional)

```bash
streamlit run live_plot.py
```

---

## 📁 Folder Structure

```
ros2_docker_workspace/
├── docker/                # Dockerfile and build context
├── src/                   # ROS 2 packages (e.g., tacterion_ros)
├── .venv/                 # Python virtual env (optional)
└── README.md              # This file
```

---

## 📦 Dependencies Installed

* ROS 2 Humble
* pyserial
* matplotlib
* streamlit
* plotext
* pandas
* numpy

---

## ✏️ Notes

* Make sure `/dev/ttyACM0` is correct for your sensor.
* Streamlit runs in the browser: [http://localhost:8501](http://localhost:8501)
* Recommended to use:

  ```bash
  sudo rm -rf build install log
  ```

  if permission issues occur when rebuilding.

---

## 🧪 Author

**Sasi** — Raspberry Pi Dev + ROS Enthusiast 🚀
