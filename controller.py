import pyfirmata
import time
import atexit

# Specify the COM port where Arduino is connected
comport = 'COM9'

# Attempt to connect to the Arduino board
try:
    board = pyfirmata.Arduino(comport)
    print(f"Connected to Arduino on {comport}")
    time.sleep(2)  # Allow time for the connection to stabilize
except Exception as e:
    print(f"Error: Could not connect to Arduino on {comport}")
    print(e)
    exit()

# Register cleanup function to safely close the connection on exit
atexit.register(lambda: board.exit())

# Define LED pins (Digital pins 8 to 12)
led_pins = [board.get_pin(f'd:{pin}:o') for pin in [8, 9, 10, 11, 12]]

def led(fingerUp):
    """
    Controls the LEDs based on the fingerUp list.
    
    :param fingerUp: List of 5 integers (0 or 1) representing finger states.
                     Each element corresponds to one finger:
                     0 = Finger down, 1 = Finger up
    """
    # Validate the input
    if len(fingerUp) != 5 or not all(x in [0, 1] for x in fingerUp):
        print("Invalid input for fingerUp. Must be a list of five 0s and 1s.")
        return

    # Update the LED states
    for pin, state in zip(led_pins, fingerUp):
        pin.write(state)

    print(f"LED states updated to: {fingerUp}")

# Example Usage (Uncomment for testing)
# led([0, 0, 0, 0, 0])  # All LEDs off
# time.sleep(1)
# led([0, 1, 0, 0, 0])  # Turn on LED 1
# time.sleep(1)
# led([0, 1, 1, 0, 0])  # Turn on LEDs 1 and 2
# time.sleep(1)
# led([1, 1, 1, 1, 1])  # All LEDs on
# time.sleep(1)
# led([0, 0, 0, 0, 0])  # All LEDs off
