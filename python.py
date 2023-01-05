#!/bin/python3

import os

# . Display the O S version – if W indows, display the Windows details; if executed on Linux, display the Linux details.
os.system("uname -a")
# Display the private IP address,
print("Private ip address:")
os.system("ifconfig | grep broadcast | awk '{print $2}'")
print()
# public IP address,
print("Public Ip addrrss:")
os.system("curl -s ifconfig.me")
print()
#the default gateway.
print("Default gateway address: ")
os.system("route -n | grep -i ug | awk '{print $2}'")
print()
# Display the h ard disk size; free and used space.
print("The hard drive: ")
os.system("df -H")
print()
# Display the top five (5) directories and their size.
print("The top five directories:")
os.system("cd / && du -sh * 2>/dev/null | sort -rh | head -5")
print()
# Display the CPU usage; refresh every 10 seconds.
print("The CPU usage:")
os.system("sar -u 10 5")
print()
