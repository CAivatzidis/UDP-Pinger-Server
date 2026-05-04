# UDP Pinger - Client & Server

## Project Description

Implementation of a simple **UDP Pinger** (similar to the `ping` command) using Python sockets.  

This project demonstrates core concepts of computer networks:
- UDP socket programming
- Client-Server architecture
- RTT (Round Trip Time) calculation
- Packet loss simulation

## Features
- Server Side:
  - Listens on UDP port 12000
  - Simulates packet loss (randomly drops ~30% of packets)
  - Converts received message to uppercase

- Client Side:
  - Sends 10 "Ping" messages to the server
  - Measures Round Trip Time (RTT) for each successful reply
  - Handles timeouts (1 second)
  - Displays statistics for each ping

## How to Run

1. Start the Server (first)
python3.13 UDPPingerServer.py

2. Start the Client
Open a second terminal and run:
python3.13 UDPPingerClient.py
