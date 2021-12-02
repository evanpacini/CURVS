import RPi.GPIO as GPIO

# Pins for Motor Driver Inputs
Motor1E = 3  # pin to enable channel 1 and 2
Motor1A = 5  # motor 1 control input pin A high-clock
Motor1B = 7  # motor 1 control input pin B high-anticlock

Motor2E = 8  # pin to enable channel 3 and 4
Motor2A = 10  # motor 2 control input pin A high-clock
Motor2B = 12  # motor 2 control input pin B high-anticlock


class MotorControl:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)         # GPIO Numbering
        GPIO.setup(Motor1A, GPIO.OUT)   # All pins as Outputs
        GPIO.setup(Motor1B, GPIO.OUT)
        GPIO.setup(Motor1E, GPIO.OUT)
        GPIO.setup(Motor2A, GPIO.OUT)
        GPIO.setup(Motor2B, GPIO.OUT)
        GPIO.setup(Motor2E, GPIO.OUT)

        GPIO.output(Motor1E, GPIO.HIGH)  # enable both channels
        GPIO.output(Motor2E, GPIO.HIGH)

    def setSpeed(self, v1, v2):
        GPIO.output(Motor1A, v1 > 0)  # HIGH if v is positive
        GPIO.output(Motor1B, v1 < 0 and not v1 == 0)  # HIGH if v is negative
        GPIO.output(Motor2A, v2 > 0)  # HIGH if v is positive
        GPIO.output(Motor2B, v2 < 0 and not v2 == 0)  # HIGH if v is negative

    def __del__(self):
        GPIO.cleanup()


if __name__ == '__main__':
    pass
