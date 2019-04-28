function alleLEDSaan2() {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
}
function alleLEDSuit2() {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
}
function Vooruit2() {
    basic.showArrow(ArrowNames.North)
    maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, 50)
    maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, 50)
    basic.pause(1500)
    maqueen.motorStopAll()
    basic.clearScreen()
}
function linksAf2() {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    basic.showArrow(ArrowNames.West)
    maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, 150)
    maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CCW, 150)
    basic.pause(190)
    maqueen.motorStopAll()
    basic.clearScreen()
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
}
function Achteruit2() {
    basic.showArrow(ArrowNames.South)
    maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CCW, 50)
    maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CCW, 50)
    basic.pause(1000)
    maqueen.motorStopAll()
    basic.clearScreen()
}
function rechtAf2() {
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    basic.showArrow(ArrowNames.East)
    maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CCW, 150)
    maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, 150)
    basic.pause(190)
    maqueen.motorStopAll()
    basic.clearScreen()
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        Vooruit2()
    }
    if (receivedNumber == 2) {
        Achteruit2()
    }
    if (receivedNumber == 3) {
        linksAf2()
    }
    if (receivedNumber == 4) {
        rechtAf2()
    }
    maqueen.motorStopAll()
    basic.showIcon(IconNames.Happy)
    basic.pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(3)
})
input.onGesture(Gesture.Shake, function () {
    radio.setGroup(2)
    basic.showNumber(2)
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(4)
})
input.onPinPressed(TouchPin.P0, function () {
    radio.sendNumber(1)
})
input.onPinPressed(TouchPin.P1, function () {
    radio.sendNumber(2)
})
input.onPinPressed(TouchPin.P2, function () {
    radio.sendNumber(1)
    radio.sendNumber(2)
    radio.sendNumber(3)
    radio.sendNumber(4)
})
alleLEDSaan2()
maqueen.motorStopAll()
radio.setGroup(1)
basic.showString("X")
basic.pause(100)
basic.clearScreen()
alleLEDSuit2()
basic.forever(function () {
	
})
control.inBackground(function () {
    if (maqueen.sensor(PingUnit.Centimeters) < 5) {
        maqueen.motorStopAll()
        for (let i = 0; i < 2; i++) {
            basic.showIcon(IconNames.Skull)
            basic.pause(50)
            basic.clearScreen()
        }
    }
})
