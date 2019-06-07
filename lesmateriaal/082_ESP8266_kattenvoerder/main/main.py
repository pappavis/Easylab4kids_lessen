# 20190604 zie voorbeeld https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/
import time, utime
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp

esp.osdebug(None)
import gc
gc.collect()

ssid = 'Volksrepubliek'
password = 'C0mmodore64!'
mqtt_server = 'dietpi'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'esp8266_notification'
topic_pub = b'hello'

booted = 0
last_message = 0
message_interval = 5000
next_message = 0
counter = 0
deepsleepAanUit = 0
LedInternalAanUit = False
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('WiFi Connection successful')
print(station.ifconfig())

client = MQTTClient(client_id, mqtt_server, user="admin", password="admin")

def rtc_ticks_ms(rtc):
    timedate = rtc.now()
    return (timedate[5] * 1000) + (timedate[6] // 1000)

def alarm_handler(rtc_o):
    global rtc_irq
    global rtc_irq_count
    if rtc_irq.flags() & RTC.ALARM0:
        rtc_irq_count += 1

def sub_cb(topic, msg):
    print((topic, msg))

    if(booted == 1):
        if topic == topic_sub and msg == b'received':
            print('ESP received hello message')

        if topic == b'LED_INTERNAL':
            import time
            from machine import Pin

            led=Pin(2,Pin.OUT) #create LED object from pin2,Set Pin2 to output
            aantalKnipperen = 5
            if (msg.isdigit()):
                aantalKnipperen = int(msg)
                print('ESP knipperen LEDje')
                client.publish("DEBUG", "client " + str(client_id) + " START knipperen LEDje")

                for herhaal1 in range(0, aantalKnipperen):
                    led.value(1)            #Set led turn on
                    time.sleep(0.2)
                    led.value(0)            #Set led turn off
                    time.sleep(0.5)
                    client.publish("DEBUG", "client " + str(client_id) + " knipperen " + str(herhaal1))
                    
                led.value(1)            #Set led turn off
            else:
                if (msg == b'LED_AAN'):
                    client.publish("DEBUG", "client " + str(client_id) + " ESP LEDje status AAN")
                    led.value(0)            #Set led turn on                    
                            
                if (msg == b'LED_UIT'):
                    client.publish("DEBUG", "client " + str(client_id) + " ESP LEDje status UIT")
                    led.value(1)            #Set led turn on                            

        if topic == b'SERVO_AANUIT' and msg == b'servoaanuit':
            doseerVoer()

        if topic == b'DEEPSLEEP_AANUIT':
            import time, esp
            from machine import RTC
            
            if (msg.isdigit()):
                deepsleepTime = int(msg)
                if (deepsleepTime > 1):
                    print("Deepsleep AAN: " + str(deepsleepTime))
                    client.publish("DEBUG", "client " + str(client_id) + " Deepsleep AAN: " + str(deepsleepTime))
                    deepsleepAanUit = 1
                    
                    # configure RTC.ALARM0 to be able to wake the device
                    rtc = machine.RTC()
                    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

                    print("Zzzzzzzzz")
                    client.publish("DEBUG", "client " + str(client_id) + " Deepsleep tyd:" + str(deepsleepTime))
                    client.publish("DEBUG", "client " + str(client_id) + " Zzzzzzzzz")
                    
                    # put the device to sleep
                    deep_sleep_esp(deepsleepTime * 1000)

                    # check if the device woke from a deep sleep
                    if (machine.reset_cause() == machine.DEEPSLEEP_RESET):
                        print("client " + str(client_id) + "is wakker gewordenXXX.")
                    else:
                        print("POWER ON")

                    #connect_and_subscribe()
                    #time.sleep_ms(50)
                    client.publish("DEBUG", "client " + str(client_id) + " is wakker geworden.")

                else:
                    print("Deepsleep UIT")
                    client.publish("DEBUG", "client " + str(client_id) + " Deepsleep UIT")
                    deepsleepAanUit = 0

def deep_sleep_esp(msecs) :   
    # configure RTC.ALARM0 to be able to wake the device 
    timer = machine.Timer(-1)
    timer.init(period=15000, mode=machine.Timer.ONE_SHOT, callback=lambda t:esp.deepsleep(10000000))

    # set RTC.ALARM0 to fire after X milliseconds (waking the device)
    rtc.alarm(rtc.ALARM0, msecs)

    # put the device to sleep 
    machine.deepsleep()

def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub, LedInternalAanUit
    client.set_callback(sub_cb)
    print("clientID " + str(client_id) + " verbinden aan MQQT: " + mqtt_server)
    client.connect()
    client.publish("ONTWAAKT", str(client_id) + " INIT start")
    client.subscribe(topic_sub)
    client.subscribe("DEBUG")
    client.publish("DEBUG", "client " + str(client_id) + " subscribed aan DEBUG")
    client.subscribe("LED_INTERNAL")
    client.publish("DEBUG", "client " + str(client_id) + " subscribed aan LED_INTERNAL")
    client.subscribe("SERVO_AANUIT")
    client.publish("DEBUG", "client " + str(client_id) + " subscribed aan SERVO_AANUIT")
    client.subscribe("DEEPSLEEP_AANUIT")
    client.publish("DEBUG", "client " + str(client_id) + " subscribed aan DEEPSLEEP_AANUIT")
    client.subscribe("ONTWAAKT")
    client.publish("DEBUG", "client " + str(client_id) + " subscribed aan ONTWAAKT")
    client.subscribe("DEEPSLEEP_AANUIT")
    client.publish("DEBUG", "client " + str(client_id) + " subscribed aan DEEPSLEEP_AANUIT")
    client.publish("ONTWAAKT", str(client_id) + " INIT eind")
    
    return client

def restart_and_reconnect():
    print('MQTT broker verbinding mislukt. Opnieuw proberen...')
    time.sleep_ms(5000)
    machine.reset()

def doseerVoer():
    import time
    from machine import Pin, PWM
    print("START microservo")
    client.publish("DEBUG", "client " + str(client_id) + " START microservo")
    time.sleep(1.5)
    servo = PWM(Pin(14), freq=50, duty=140)
    led=Pin(2,Pin.OUT)        #create LED object from pin2,Set Pin2 to output

    led.value(0)            #Set led turn on
    time.sleep(0.8)
    led.value(1)            #Set led turn off
    print("beweeg microservo 30")
    servo.duty(30)
    time.sleep(0.5)
    led.value(1)            #Set led turn on

    print("EIND microservo")
    client.publish("DEBUG", "client " + str(client_id) + " EIND microservo")


try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()


# ---------------------------------------------------------
#  Main loop
while True:
    try:
        client.check_msg()
        
        # om de paar sekonden, lat hem iets doen, kan jezelf invullen
        if (utime.ticks_ms() > next_message):
            msg = b'Hello #%d' % counter
            client.publish(topic_pub, msg)
            next_message = utime.ticks_ms() + message_interval
            
            print(msg)
            counter += 1

        #na opstart, mag nu MQQT berichten ontvangen.
        if (booted == 0):
            LedInternalAanUit = False
            booted = 1
            next_message = utime.ticks_ms() + message_interval
            
    except OSError as e:
        restart_and_reconnect()
# ---------------------------------------------------------

