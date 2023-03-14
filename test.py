import time
import sys
import threading
from key_generator import KeyGenerator


def generate_key():
    return KeyGenerator().generate_key(2048)


def animated_loading():
    chars = "/—\|"
    chars = "⢿⣻⣽⣾⣷⣯⣟⡿"
    for char in chars:
        sys.stdout.write("\r" + char)
        time.sleep(0.1)
        sys.stdout.flush()


t = threading.Thread(target=generate_key)
t.start()

while t.is_alive():
    animated_loading()
