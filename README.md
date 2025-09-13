# Network Ping Checker 📊

A simple, yet effective Python script to monitor network device availability and log their status to a CSV file. Built for personal network diagnostics and demonstrating basic network automation skills.

---

## 🚀 Key Features

*   **Customizable Host List:** Reads IP addresses from `hosts.csv` for flexible monitoring.
*   **Real-time Status Check:** Pings each host to determine its online/offline status.
*   **Detailed Logging:** Records timestamps, IP addresses, and status to `log.csv` for historical analysis.
*   **Cross-Platform Compatibility:** Uses `subprocess` for `ping` command, supporting both Windows and Unix-like systems.

---

## ✨ Why This Project? (Use Cases)

This script is more than just a basic ping tool. It's designed for practical, real-world network diagnostics, especially useful for:

*   **Home Network Monitoring:** Keep an eye on your router, smart devices, or PCs. Ever wonder why your Wi-Fi suddenly dropped? This can tell you.
*   **Troubleshooting Gaming Lag (e.g., Valorant):** When your online game suddenly disconnects or lags, quickly check if it's your local network, your ISP, or the game server itself.
*   **Basic Network Health Checks:** Verify the uptime of critical devices in a small office or lab environment.
*   **Pre/Post-Configuration Verification:** After making network changes (like VLAN or firewall rules), quickly confirm which devices are reachable.

---

## 🛠 How to Use

### Prerequisites

*   Python 3.x installed.
*   Git installed (for cloning this repository).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/n0teternal/host-checker.git
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd host-checker

### Configuration

1.  **`hosts.csv`:**
    *   Open `hosts.csv` in the project directory.
    *   Add the IP addresses you want to monitor, one IP per line.
        ```
        8.8.8.8
        1.1.1.1
        192.168.1.1
        ```

### Running the Script

1.  Open your terminal or command prompt in the `network-ping-checker` directory.
2.  Run the script using Python:
    ```bash
    py main.py  # For Windows users
    # OR
    # python3 main.py # For Linux/macOS users or if 'py' doesn't work
    ```

The script will print the status of each host to the console and log results to `log.csv`.

---

## 📂 Project Structure
Use code with caution.
Markdown
network-ping-checker/
├── main.py # The core Python script for pinging and logging.
├── hosts.csv # List of IP addresses to monitor.
├── .gitignore # Tells Git to ignore temporary files like 'log.csv'.
└── README.md # This file, explaining the project.
Generated code
---

## 💡 Future Improvements (Ideas for Growth!)

*   Add email or Telegram notifications for offline devices.
*   Implement a loop for continuous monitoring with a delay.
*   Integrate with a simple web interface (Flask/Django) for dashboard view.
*   Add more detailed ping statistics (latency, packet loss).
*   Convert to an executable for easier distribution.

---

## ✉️ Connect & Contribute

Feel free to connect, open issues, or suggest improvements!

**GitHub:** [https://github.com/n0teternal](https://github.com/n0teternal)
**Telegram:** @notttt_eternal
**Name:** Iliya Berezenets
