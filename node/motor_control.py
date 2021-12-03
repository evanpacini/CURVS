import RPi.GPIO as GPIO


class MotorControl:
    def __init__(self, EN12: int, A1: int, A2: int, EN34: int, A3: int, A4: int) -> None:
        GPIO.setwarnings(False)  # Disable "channel in use" warnings
        GPIO.setmode(GPIO.BOARD)  # Physical pin numbering

        # All pins set as output
        GPIO.setup(EN12, GPIO.OUT)  # Channel 1,2 Enable
        GPIO.setup(A1, GPIO.OUT)  # Driver input 1
        GPIO.setup(A2, GPIO.OUT)  # Driver input 2
        GPIO.setup(EN34, GPIO.OUT)  # Channel 3,4 Enable
        GPIO.setup(A3, GPIO.OUT)  # Driver input 3
        GPIO.setup(A4, GPIO.OUT)  # Driver input 4

        # Enable both channels (to be replaced by PWM)
        GPIO.output(EN12, GPIO.HIGH)
        GPIO.output(EN34, GPIO.HIGH)

        # Save pin values for class
        self.EN12 = EN12
        self.A1 = A1
        self.A2 = A2
        self.EN34 = EN34
        self.A3 = A3
        self.A4 = A4

    def setVelocity(self, v1: int, v2: int) -> None:
        GPIO.output(self.A1, v1 > 0)  # HIGH if v is positive
        GPIO.output(self.A2, v1 < 0 and not v1 == 0)  # HIGH if v is negative
        GPIO.output(self.A3, v2 > 0)  # HIGH if v is positive
        GPIO.output(self.A4, v2 < 0 and not v2 == 0)  # HIGH if v is negative

    def __del__(self) -> None:
        GPIO.cleanup()


if __name__ == '__main__':
    pass
