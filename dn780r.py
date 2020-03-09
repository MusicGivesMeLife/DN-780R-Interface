import serial
import time

class Deck:
    def __init__(self, port):
        self.port = port
        self.s = serial.Serial(str(self.port), 9600, parity=serial.PARITY_EVEN, timeout=1)
    def reset(self):
        self.s.flushInput()
        self.s.write(b'\x02\x20\x00\x00\x00\x00\x03\x32\x33')
        time.sleep(2)
        return 0
    def status(self):
        self.s.flushInput()
        self.s.write(b'\x02\x30\x00\x00\x00\x00\x03\x33\x33')
        self.ret = list(str(self.s.read(20), 'UTF-8'))
        self.sys_status = int(self.ret[3])
        if self.ret[5] == 'A':
            self.a_loaded = False
        elif self.ret[5] == 'B':
            self.a_loaded = True
        if self.ret[5] == 'A':
            self.b_loaded = False
        elif self.ret[11] == 'B':
            self.b_loaded = True
        if self.ret[4] == '0':
            self.highspeed = False
        elif self.ret[4] == '1':
            self.highspeed = True
        self.counter_a = ((int(self.ret[7])*1000) + (int(self.ret[8])*100) + (int(self.ret[9])*10) + int(self.ret[10]))
        if self.ret[6] == '-':
            self.counter_a = self.counter_a*-1
        self.counter_b = ((int(self.ret[13])*1000) + (int(self.ret[14])*100) + (int(self.ret[15])*10) + int(self.ret[16]))
        if self.ret[12] == '-':
            self.counter_b = self.counter_b*-1
        return 0
    def cpu_vers(self):
        self.s.flushInput()
        self.s.write(b'\x02\x31\x00\x00\x00\x00\x03\x33\x34')
        self.ret = list(str(self.s.read(10), 'UTF-8'))
        self.cpu = ''.join(self.ret[3:7])
        return self.cpu
    def tape_stat(self):
        self.s.flushInput()
        self.s.write(b'\x02\x32\x00\x00\x00\x00\x03\x33\x35')
        self.ret = list(str(self.s.readline(), 'UTF-8'))
    def established(self):
        self.s.flushInput()
        self.s.write(b'\x02\x33\x00\x00\x00\x00\x03\x33\x36')
        self.ret = str(self.s.readline(), 'UTF-8')
    def id(self):
        self.s.flushInput()
        self.s.write(b'\x02\x34\x00\x00\x00\x00\x03\x33\x37')
        self.ret = str(self.s.read(19), 'UTF-8')
        self.id = ''.join(self.ret[3:16])
        return self.id
    def play(self, mecha):
        self.s.flushInput()
        if mecha == 'A':
            self.s.write(b'\x02\x40\x30\x00\x00\x00\x03\x37\x33')
        elif mecha == 'B':
            self.s.write(b'\x02\x40\x31\x00\x00\x00\x03\x37\x34')
        self.ret = str(self.s.readline(), 'UTF-8')
    def stop(self, mecha):
        self.s.flushInput()
        if mecha == 'A':
            self.s.write(b'\x02\x41\x30\x00\x00\x00\x03\x37\x34')
        elif mecha == 'B':
            self.s.write(b'\x02\x41\x31\x00\x00\x00\x03\x37\x35')
        self.ret = str(self.s.readline(), 'UTF-8')
    def close(self):
        self.s.close()
        return 0
