from time import sleep
from settings import settings
from gate import gate

class autoclose:
    def __init__(self):
        self.activated = False
        self._close_gate_after_time()


    def _close_gate_after_time(self):
        gate_open_time = 0
        while True:
            if gate.gate_status == 'open' or gate.gate_status == 'inbetween':
                gate_open_time += 1
            else: 
                gate_open_time = 0
            self.activated = False
            if gate_open_time >= settings.get_auto_close_seconds_setting():
                self.activated = True
                while gate.gate_status != 'closed':
                    gate.open_or_close_gate()
                    sleep(30)
            sleep(1)



        