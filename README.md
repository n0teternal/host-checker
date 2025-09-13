code
JSON
download
content_copy
expand_less

{
  "projectName": "Network Ping Checker",
  "description": "A simple, yet effective Python script to monitor network device availability and log their status to a CSV file. Built for personal network diagnostics and demonstrating basic network automation skills.",
  "features": [
    "Customizable Host List: Reads IP addresses from `hosts.csv` for flexible monitoring.",
    "Real-time Status Check: Pings each host to determine its online/offline status.",
    "Detailed Logging: Records timestamps, IP addresses, and status to `log.csv` for historical analysis.",
    "Cross-Platform Compatibility: Uses `subprocess` for `ping` command, supporting both Windows and Unix-like systems."
  ],
  "useCases": [
    {
      "title": "Home Network Monitoring",
      "description": "Keep an eye on your router, smart devices, or PCs. Ever wonder why your Wi-Fi suddenly dropped? This can tell you."
    },
    {
      "title": "Troubleshooting Gaming Lag (e.g., Valorant)",
      "description": "When your online game suddenly disconnects or lags, quickly check if it's your local network, your ISP, or the game server itself."
    },
    {
      "title": "Basic Network Health Checks",
      "description": "Verify the uptime of critical devices in a small office or lab environment."
    },
    {
      "title": "Pre/Post-Configuration Verification",
      "description": "After making network changes (like VLAN or firewall rules), quickly confirm which devices are reachable."
    }
  ],
  "usageInstructions": {
    "prerequisites": [
      "Python 3.x installed.",
      "Git installed (for cloning this repository)."
    ],
    "installation": [
      {
        "step": 1,
        "instruction": "Clone the repository:",
        "command": "git clone https://github.com/n0teternal/network-ping-checker.git"
      },
      {
        "step": 2,
        "instruction": "Navigate into the project directory:",
        "command": "cd network-ping-checker"
      }
    ],
    "configuration": {
      "file": "hosts.csv",
      "steps": [
        "Open `hosts.csv` in the project directory.",
        "Add the IP addresses you want to monitor, one IP per line."
      ],
      "example": "8.8.8.8\n1.1.1.1\n192.168.1.1"
    },
    "running": {
      "instruction": "Open your terminal or command prompt in the `network-ping-checker` directory and run the script using Python.",
      "commands": [
        {
          "platform": "Windows",
          "command": "py main.py"
        },
        {
          "platform": "Linux/macOS",
          "command": "python3 main.py"
        }
      ],
      "output": "The script will print the status of each host to the console and log results to `log.csv`."
    }
  },
  "projectStructure": {
    "root": "network-ping-checker/",
    "files": [
      {
        "name": "main.py",
        "description": "The core Python script for pinging and logging."
      },
      {
        "name": "hosts.csv",
        "description": "List of IP addresses to monitor."
      },
      {
        "name": ".gitignore",
        "description": "Tells Git to ignore temporary files like 'log.csv'."
      },
      {
        "name": "README.md",
        "description": "This file, explaining the project."
      }
    ]
  },
  "futureImprovements": [
    "Add email or Telegram notifications for offline devices.",
    "Implement a loop for continuous monitoring with a delay.",
    "Integrate with a simple web interface (Flask/Django) for dashboard view.",
    "Add more detailed ping statistics (latency, packet loss).",
    "Convert to an executable for easier distribution."
  ],
  "author": {
    "name": "Iliya Berezenets",
    "github": "https://github.com/n0teternal",
    "telegram": "@notttt_eternal"
  },
  "contribution": {
    "message": "Feel free to connect, open issues, or suggest improvements!"
  }
}
