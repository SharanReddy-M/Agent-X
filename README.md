# Agent-X
Adaptive Traffic Signal Controller uses Reinforcement Learning with a Q-Learning agent to dynamically adjust traffic signal timings based on real-time vehicle density and waiting time. The system learns optimal signal actions over time, reducing congestion, minimizing delays, and outperforming traditional fixed-timer traffic control methods.
Adaptive Traffic Signal Controller (RL-Based)
📌 Overview

The Adaptive Traffic Signal Controller is a Reinforcement Learning–based system designed to optimize traffic signal timings dynamically using real-time traffic conditions. Unlike traditional fixed-timer signals, this system learns and adapts automatically to reduce congestion and waiting time.

🎯 Problem Statement

Fixed-time traffic signals cannot handle changing traffic patterns, leading to unnecessary delays and congestion. There is a need for an intelligent system that adapts signal timings based on real-world traffic conditions without manual tuning.

💡 Solution

This project uses a Q-Learning Reinforcement Learning agent that:

Observes traffic state (vehicle count, waiting time)

Selects optimal signal actions (extend or switch green light)

Receives rewards based on traffic improvement

Learns optimal policies over time

🛠 Tools & Technologies

Reinforcement Learning (RL)

Q-Learning Algorithm

Traffic State Simulation / Sensors

Python (if applicable)

🔁 System Workflow

Detect traffic density and waiting time

RL agent selects best signal action

Action applied to traffic signal

Reward calculated based on traffic flow

Policy updated for improved future decisions

📈 Results

Reduced average waiting time

Better traffic flow compared to fixed-timer signals

Adaptive performance during peak and low traffic hours

🌆 Applications

Smart city traffic management

Peak hour congestion control

Emergency vehicle prioritization

👥 Team

Karlapati Akshay

Lagadapati Sriram

Marreddy Sharan Reddy

Mandava Saketh Chowdary
