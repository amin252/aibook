print("this is a program for testing a git module")

import socket

def check_internet():
    try:
        # Try to connect to Google's DNS server
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except (socket.error, OSError):
        return False

# Check and print result
if check_internet():
    print("YES")
else:
    print("NO")