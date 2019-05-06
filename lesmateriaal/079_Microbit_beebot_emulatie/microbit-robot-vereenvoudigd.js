function vooruit() {
    rechtVooruit(50)
}

function rechts() {
    draaiRechts90(43)
}

function achteruit() {
    rechtAchteruit(50)
}

function links() {
    draaiRechts90(43)
}

function basisTest() {
    draaiLinks90(40)
    rechtVooruit(50)
    draaiRechts90(45)
    rechtVooruit(50)
    draaiLinks90(40)
    rechtAchteruit(50)
}

function draaiRechts90(motorSnelheid: number) {
    basic.showArrow(ArrowNames.East)
    basic.pause(2000)
    maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CCW, motorSnelheid)
    maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, motorSnelheid)
    basic.pause(470)
    maqueen.motorStopAll()
    basic.clearScreen()
}

function draaiLinks90(motorSnelheid: number) {
    basic.showArrow(ArrowNames.West)
    basic.pause(2000)
    maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, motorSnelheid)
    maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CCW, motorSnelheid)
    basic.pause(470)
    maqueen.motorStopAll()
    basic.clearScreen()
}

function rechtAchteruit(motorSnelheid: number) {
    basic.showArrow(ArrowNames.North)
    basic.pause(2000)
    maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CCW, motorSnelheid)
    maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CCW, motorSnelheid)
    basic.pause(600)
    maqueen.motorStopAll()
    basic.clearScreen()
}

function rechtVooruit(motorSnelheid: number) {
    basic.showArrow(ArrowNames.South)
    basic.pause(2000)
    maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, motorSnelheid)
    maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, motorSnelheid)
    basic.pause(600)
    maqueen.motorStopAll()
    basic.clearScreen()
}
music.playTone(262, music.beat(BeatFraction.Sixteenth))
basic.showString('.')
basic.pause(200)
basic.clearScreen() for (let i = 0; i < 4; i++) {
    music.playTone(220, music.beat(BeatFraction.Eighth))
    links()
    vooruit()
}
rechts()
achteruit()
achteruit()
basic.showString('X')
basic.pause(200)
basic.clearScreen()
music.playTone(349, music.beat(BeatFraction.Quarter))
music.playTone(440, music.beat(BeatFraction.Eighth))
basic.forever(function() {

})