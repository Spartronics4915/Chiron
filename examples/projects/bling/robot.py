import wpilib


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.ledCount = 60

        self.led = wpilib.AddressableLED(0)
        self.buffer: list[wpilib.AddressableLED.LEDData] = [
            wpilib.AddressableLED.LEDData() for _ in range(self.ledCount)
        ]

        self.led.setLength(self.ledCount)
        self.led.setData(self.buffer)
        self.led.start()

        self.hue = 0

    def robotPeriodic(self):
        for i in range(self.ledCount):
            self.buffer[i].setHSV((self.hue + i * 3) % 180, 255, 128)

        self.led.setData(self.buffer)

        self.hue = (self.hue + 1) % 180


if __name__ == "__main__":
    wpilib.run(MyRobot)
