# find_vm_ip

`find_vm_ip` is a Python program that helps users locate the IP address of a virtual machine (VM) on their local network using its MAC address. It also allows users to create custom scripts for specific VMs.

## Features

- Scans the local network for a VM's IP address using its MAC address.
- Automatically connects to the VM via SSH once the IP is found.
- Allows users to create custom scripts for different VMs with unique MAC addresses.

## Requirements

- Python 3.x
- `arp-scan` installed on your system (use `sudo apt install arp-scan` on Debian-based systems).
- SSH access to the VM.

## Installation

1. Clone this repository:

- git clone https://github.com/yourusername/find_vm_ip.git
- cd find_vm_ip

2. Make the scripts executable:

- chmod +x create_find_vm.py

## Usage

### Create a Custom VM Finder Script

- Run the `create_find_vm.py` script to create a custom script for your VM:

- python3 create_find_vm.py

- Follow the prompts to enter the VM's name (any name) and MAC address. The script will generate a new file (e.g., `find_<vmname>.py`).

### Run the Generated Script

- Run the generated script to find the VM's IP address and connect via SSH:

- python3 find_<vmname>.py

### Example

1. Create a script for a VM named `web` with MAC address `01:02:03:04:05:06`:

- python3 create_find_vm.py

- Enter the VM name: web

- Enter the MAC address (format: 000000000000): 010203040506


2. Run the generated script:

- python3 find_web.py

- Here you will enter you sudo password for arp-scan to work.


## License

- I just don't know yet.

## Contributing

- Feel free to fork this repository and submit pull requests to improve the program!

## Disclaimer

- This program uses `sudo` privileges to run `arp-scan`. You do not need to run the program as `sudo`, however, if you experience any issues try running as `sudo`.
