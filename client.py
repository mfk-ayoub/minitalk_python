import os
import signal
import sys
import time

def putcolor(color):
    if color == 'r':
        print("\033[1;31m", end='')
    elif color == 'g':
        print("\033[1;32m", end='')
    elif color == 'b':
        print("\033[1;34m", end='')
    else:
        print("\033[0m", end='')

def send_char(pid, char_code):
    for i in range(16):
        if (char_code & (0x01 << i)):
            os.kill(pid, signal.SIGUSR1)
        else:
            os.kill(pid, signal.SIGUSR2)
        time.sleep(0.0005)

def sender(pid, msg):
    for char in msg:
        send_char(pid, ord(char))

def signal_handler(sig, frame):
    print("Exit.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    putcolor('g')
    pid = int(input("Enter PID of the server: \033[0m "))
    putcolor('g')
    message = input("Enter message to send: \033[0m ")
    putcolor('d')

    if pid <= 0:
        print(f"PID {pid} is not valid")
        sys.exit(1)

    try:
        os.kill(pid, 0)
    except (OSError, ValueError):
        putcolor('r')
        print(f"Process with PID {pid} does not exist.")
        sys.exit(1)

    try:
        time.sleep(1)
        sender(pid, message)
        sender(pid, "\n")
    except ProcessLookupError:
        putcolor('r')
        print("Error: Server process not found.")
        sys.exit(1)
