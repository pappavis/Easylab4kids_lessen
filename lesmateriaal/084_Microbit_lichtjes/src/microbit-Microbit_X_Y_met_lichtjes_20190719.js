input.onButtonPressed(Button.A, function () {
    xPos = 0
    for (let i = 0; i < 4; i++) {
        led.plot(0, xPos)
        basic.pause(100)
        xPos += 1
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
})
let xPos = 0
basic.showString("X")
basic.forever(function () {
	
})
