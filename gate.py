import RPi.GPIO as GPIO
from time import sleep

class gate:
    def __init__(self, open_sensor_pin, closed_sensor_pin, relay_pin):
        self.open_sensor_pin = open_sensor_pin
        self.closed_sensor_pin = closed_sensor_pin
        self.relay_pin = relay_pin
        self.gate_status = None
        self.relay_state = True
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(open_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(closed_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(self.relay_pin, GPIO.OUT)
            GPIO.add_event_detect(self.open_sensor_pin, GPIO.RISING, callback=self.detect_gate_status)
            GPIO.add_event_detect(self.closed_sensor_pin, GPIO.RISING, callback=self.detect_gate_status)
            GPIO.output(self.relay_pin, self.relay_state)
        except Exception as e:
            print('Error while setting up GPIO for gate: %s'.format(e))


    def detect_gate_status(self, pin):
        if pin == self.open_sensor_pin:
            self.gate_status = 'open'
        elif pin == self.closed_sensor_pin:
            self.gate_status = 'closed'

    def pulse_relay(self):
        for i in range(1):
            self.relay_state = not self.relay_state
            GPIO.output(self.relay_pin, self.relay_state)
            sleep(1)

    def open_or_close_gate(self):
        self.pulse_relay()
        self.gate_status = 'inbetween'


        
