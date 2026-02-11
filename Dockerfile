# HAL OpenClaw - Dockerfile
FROM ubuntu:22.04

# Set timezone and avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Install base dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    openssh-client \
    openssh-server \
    smbclient \
    cifs-utils \
    net-tools \
    dnsutils \
    iputils-ping \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    nodejs \
    npm \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create HAL user
RUN useradd -m -s /bin/bash -G sudo pablo && \
    echo "pablo:25851069" | chpasswd && \
    echo "pablo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/pablo

# Set working directory
WORKDIR /home/pablo/clawd

# Copy HAL code
COPY --chown=pablo:pablo . /home/pablo/clawd/

# Install Node dependencies
RUN cd /home/pablo/clawd && npm install --legacy-peer-deps 2>&1 | tail -5

# Install Python dependencies (if any requirements.txt)
RUN pip3 install --no-cache-dir sshpass 2>&1 | tail -3

# Create memory directory
RUN mkdir -p /home/pablo/clawd/memory && \
    chown -R pablo:pablo /home/pablo/clawd

# Configure SSH for remote access
RUN mkdir -p /run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Expose SSH
EXPOSE 22

# Switch to HAL user
USER pablo

# Default command: start SSH + keep container alive
CMD ["/bin/bash", "-c", "sudo /usr/sbin/sshd -D"]
