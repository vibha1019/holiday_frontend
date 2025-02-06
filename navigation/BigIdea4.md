---
layout: post
title: Big Idea 4 Blog
search_exclude: true
permalink: /bigidea4/
---

# 4.1 The Internet (Video 1)

## Evolution of Computers and Networks
- **1975:** Computers were huge and worked in isolation.  
- Evolution led to **smaller computers** capable of sending and receiving data.  

## Key Concepts  
- **Packet:** A small piece of data sent over a network. It includes the **source** and **destination** information.  
- **Computer Network:** A group of interconnected computing devices capable of sending/receiving data.  
- **Computer System:** A group of computing devices and programs working together for a purpose.  

## Packet Switching  
- The message/file is **broken into packets**, which can be sent in different paths in any order.  
- Example: If sending `"Hello, my name is Soni."`,  
  - `"Soni"` could be sent in one path.  
  - `"name"` could be sent in another path.  
- The **recipient's device** reassembles the packets.  
![image](https://media.geeksforgeeks.org/wp-content/uploads/20240109160206/4514-660.png)

## Routing and Path  
- **Routing:** The process of finding a path from sender to receiver.  
- **Path:** The sequence of connected computing devices that starts at the sender and ends at the receiver.  

## Bandwidth  
- The **maximum amount of data** that can be transmitted in a fixed time.  
- Measured in **bits per second**.  

---

# 4.1 The Internet (Video 2)

## Protocols and Standards  
- **Protocol:** A set of agreed-upon rules that specify the behavior of a system.  
- **OSI (Open Systems Interconnection):** The **7 layers** required for communication.  
- **Internet Engineering Task Force (IETF):**  
  - Manages the development of standards and technical discussions for the internet in an open, collaborative process.  

## Transmission Control Protocol (TCP)  
- Establishes a common standard for sending messages between devices on the internet.  
![image](https://neosnetworks.com/wp-content/uploads/2024/12/OSI-model-vs-TCP-IP-model.png)

## Network Layers  

### **1. Network Access Layer** (Hardware Layer)
- **Includes:**  
  - Fiber, MAC (Media Access Control), Ethernet, NIC (Network Interface Cards), wires.  

### **2. Network/Internet Layer (Data Transmission - IP)**
- **Packets get set up with metadata** (contains routing information).  
- **Routers:** Special-purpose computers with a MAC address that direct packets.  
- **Analogy:** Routers are like people passing a note in class (many different paths possible).  
- **Internet Scalability:**  
  - Designed to **scale** (change in size and meet new demands).  
  - Starts with **Local Area Network (LAN)** → moves to **Autonomous Systems (AS)** → connects to **The Internet**.

### **3. Transport Layer**  
- Handles **how packets are sent** and **error control**.  
- **Transport Control Protocol (TCP):**  
  - Does error checking and recovery (more reliable but slower).  
- **User Datagram Protocol (UDP):**  
  - Performs error checking but discards incorrect packets (faster but less reliable).  

### **4. Internet Layer (IP Addressing)**  
- **Three types of addressing:**  
  1. **Unicast:** One specific device (Internet-wide access, uses TCP).  
  2. **Multicast:** A group of devices (uses a specific IP range, Internet-wide access, uses UDP).  
  3. **Broadcast:** Sent to all devices in a LAN (data stops at the router, uses UDP).  

![image](https://radhikaclasses.com/wp-content/uploads/2021/02/unicast-multicast-broadcast-image3-1-1.jpg)
---

## **Application Layer**
- **Webservers:** Programs running on machines connected to the internet.  
- **DNS (Domain Name System):**  
  - Translates human-readable URLs into IP addresses (e.g., `www.mywebsite.com`).  

### **Key Protocols in the Application Layer**  
- **HTTP (HyperText Transfer Protocol):**  
  - Used to request/receive data from web servers.  
  - Uses **TCP port 80** at the transport layer.  
- **HTTPS (Secure HTTP):**  
  - Like HTTP but with security encryption.  
  - Uses **TCP port 443**.  
```
