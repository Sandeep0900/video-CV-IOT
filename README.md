# Hand Gesture Controlled LED System

This project demonstrates a hand gesture-controlled LED system that utilizes computer vision, Arduino, and LEDs to provide a seamless interaction between hand gestures and hardware. The project integrates Python-based hand tracking and Arduino for LED control.

## Features
- Real-time hand gesture detection using a webcam.
- Detection of the number of fingers raised.
- Control of LEDs connected to an Arduino Uno based on the detected finger count.
- Smooth communication between Python and Arduino using the PyFirmata library.

## Components Required
1. **Hardware:**
   - Arduino Uno
   - LEDs (5 units)
   - Resistors (220Ω each)
   - Connecting wires
   - Breadboard
   - Webcam
2. **Software:**
   - Python 3.x
   - OpenCV library
   - cvzone library
   - PyFirmata library
   - Arduino IDE (for uploading the StandardFirmata sketch)

## Setup

### Arduino Connection
1. Connect LEDs to digital pins 8, 9, 10, 11, and 12 of the Arduino Uno with resistors in series.
2. Ensure a common ground between the Arduino and the power source of the LEDs.
3. Upload the StandardFirmata sketch from the Arduino IDE to the Arduino Uno.

### Python Environment
1. Install the required Python libraries:
   ```bash
   pip install opencv-python cvzone pyfirmata
   ```
2. Connect the Arduino Uno to your computer and note its COM port (e.g., `COM9`).

## How It Works

### Gesture Detection
1. The `main.py` script uses OpenCV and cvzone’s Hand Tracking Module to detect hand gestures.
2. It identifies the number of fingers raised using the `fingersUp()` function and maps this to specific actions.

### LED Control
1. The `controller.py` script uses the PyFirmata library to communicate with the Arduino Uno.
2. Each finger count corresponds to a specific combination of LEDs being turned on or off.

### Interaction Flow
1. The webcam captures the hand in real time.
2. The `HandDetector` processes the hand's position and identifies the raised fingers.
3. The `controller.py` script receives this data and triggers the corresponding LEDs on the Arduino.

## Code Structure
### `main.py`
This script handles:
- Video capture and gesture detection.
- Sending the detected finger count to `controller.py`.

### `controller.py`
This script handles:
- Communication with the Arduino Uno via PyFirmata.
- Controlling the LEDs based on the finger count received.

## Usage
1. Connect your Arduino Uno to the computer.
2. Upload the StandardFirmata sketch to the Arduino Uno.
3. Run the `main.py` script:
   ```bash
   python main.py
   ```
4. Use hand gestures to control the LEDs:
   - 0 fingers: All LEDs off.
   - 1 finger: LED 1 on.
   - 2 fingers: LEDs 1 and 2 on.
   - 3 fingers: LEDs 1, 2, and 3 on.
   - 4 fingers: LEDs 1, 2, 3, and 4 on.
   - 5 fingers: All LEDs on.

## Future Enhancements
- Add support for multiple hands.
- Use additional hardware like buzzers or motors.
- Integrate with IoT platforms for remote control and monitoring.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [cvzone Hand Tracking Module](https://github.com/cvzone)
- [PyFirmata Documentation](https://pyfirmata.readthedocs.io/)

