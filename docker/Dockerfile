FROM ros:humble

ENV DEBIAN_FRONTEND=noninteractive

# Install system & Python packages
RUN apt update && apt install -y \
    python3-pip \
    python3-colcon-common-extensions \
    && apt clean

RUN pip install --upgrade pip && \
    pip install \
      pyserial \
      matplotlib \
      streamlit \
      plotext \
      pandas \
      numpy

# Create workspace
WORKDIR /root/ros2_ws

# Add ROS sourcing to .bashrc
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

CMD ["/bin/bash"]
