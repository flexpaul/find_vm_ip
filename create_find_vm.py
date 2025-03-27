#!/usr/bin/env python3

import os

# Function to format MAC address
def format_mac_address(mac):
    return ":".join(mac[i:i+2] for i in range(0, len(mac), 2))

# Function to validate MAC address
def is_valid_mac(mac):
    return len(mac) == 12 and mac.isalnum()

# Interactive loop for user input
while True:
    vm_name = input("Enter the VM name: ").strip()
    mac_address = input("Enter the MAC address (format: 000000000000): ").strip()

    if not is_valid_mac(mac_address):
        print("Invalid MAC address format. Please enter 12 alphanumeric characters.")
        choice = input("Press 1 to try again or X to exit: ").strip().lower()
        if choice == 'x':
            print("Thank you for using find_vm_ip. Goodbye!")
            exit(0)
        else:
            continue  # Retry input
    else:
        break  # Valid input, proceed

# Format the MAC address
formatted_mac = format_mac_address(mac_address)

# Define the content of the new script
# Also called the new created script find_vm_ip.py
script_content = f"""#!/usr/bin/env python3
import subprocess

# Define the MAC address of the VM
vm_mac = "{formatted_mac}"

# Run arp-scan and capture output
try:
    result = subprocess.run(
        ["sudo", "arp-scan", "--localnet"],
        capture_output=True,
        text=True
    )

    # Search for the MAC address in the output
    for line in result.stdout.split("\\n"):
        if vm_mac.lower() in line.lower():
            vm_ip = line.split()[0]
            print("VM IP Address Found:", vm_ip)

            # Automatically run the ssh command
            subprocess.run(["ssh", vm_ip])
            break
    else:
        print("VM IP Address not found.")

except Exception as e:
    print("Error:", e)

# Keep the terminal open until the user presses Enter
input("\\nThank you for using find_vm_ip. Goodbye!\\nPress Enter to close...")
"""

# Generate the filename
filename = f"find_{vm_name}.py"

# Check if the file already exists
if os.path.exists(filename):
    print(f"File '{filename}' already exists.")
    while True:
        choice = input("Press 1 to overwrite, 2 to enter a new name, or X to exit: ").strip().lower()
        if choice == '1':
            print(f"Overwriting '{filename}'...")
            break
        elif choice == '2':
            vm_name = input("Enter a new VM name: ").strip()
            filename = f"find_{vm_name}.py"
            if not os.path.exists(filename):
                break
            else:
                print(f"File '{filename}' also exists. Please choose another name.")
        elif choice == 'x':
            print("Exiting without creating a file. Goodbye!")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

# Write the content to the new file
try:
    with open(filename, "w") as file:
        file.write(script_content)
    # Make the new script executable
    os.chmod(filename, 0o755)
    print(f"Script '{filename}' created successfully!")
except Exception as e:
    print("Error creating the script:", e)
