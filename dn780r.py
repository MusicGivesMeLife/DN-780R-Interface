import serial
import time

class Deck:
    def __init__(self, port):
        self.port = port
        self.s = serial.Serial(str(self.port), 9600, parity=serial.PARITY_EVEN, timeout=5)
        self.all_stat()
    def all_stat(self):
        self.status()
        self.tape_stat()
        self.established()
        return 0
    def reset(self):
        self.s.flushInput()
        self.s.write(b'\x02\x20\x00\x00\x00\x00\x03\x32\x33')
        time.sleep(2)
        return 0
    def status(self):
        self.s.flushInput()
        self.s.write(b'\x02\x30\x00\x00\x00\x00\x03\x33\x33')
        self.ret = list(str(self.s.read(20), 'UTF-8'))
        self.sys_status = str(self.ret[3])
        self.a_stat = self.ret[5]
        self.b_stat = self.ret[11]
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
        self.ret = list(str(self.s.read(8), 'UTF-8'))
        if self.ret[4] == '0':
            self.a_stat = 'A'
            self.recb_a = False
            self.recb_b = False
        elif self.ret[4] == '1':
            self.reca_a = True
            self.reca_b = True
        elif self.ret[4] == '2':
            self.reca_a = False
            self.reca_b = True
        elif self.ret[4] == '3':
            self.reca_a = True
            self.reca_b = False
        elif self.ret[4] == '4':
            self.recb_a = False
            self.recb_b = False
        if self.ret[5] == '0':
            self.b_stat = 'A'
            self.recb_a = False
            self.recb_b = False
        elif self.ret[5] == '1':
            self.recb_a = True
            self.recb_b = True
        elif self.ret[5] == '2':
            self.recb_a = False
            self.recb_b = True
        elif self.ret[5] == '3':
            self.recb_a = True
            self.recb_b = False
        elif self.ret[5] == '4':
            self.recb_a = False
            self.recb_b = False
        return 0
    def established(self):
        self.s.flushInput()
        self.s.write(b'\x02\x33\x00\x00\x00\x00\x03\x33\x36')
        self.ret = list(str(self.s.read(14), 'UTF-8'))
        self.dup = int(self.ret[3])
        self.rev = int(self.ret[4])
        self.dolbya = int(self.ret[5])
        self.dira = not(bool(int(self.ret[6])))
        self.mema = bool(int(self.ret[7]))
        self.dolbyb = int(self.ret[8])
        self.dirb = not(bool(int(self.ret[9])))
        self.memb = bool(int(self.ret[10]))
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
        self.ret = str(self.s.read(6), 'UTF-8')
    def stop(self, mecha):
        self.s.flushInput()
        if mecha == 'A':
            self.s.write(b'\x02\x41\x30\x00\x00\x00\x03\x37\x34')
        elif mecha == 'B':
            self.s.write(b'\x02\x41\x31\x00\x00\x00\x03\x37\x35')
        self.ret = str(self.s.read(6), 'UTF-8')
    def rec(self, mecha):
        self.s.flushInput()
        if mecha == 'A':
            self.s.write(b'\x02\x42\x30\x00\x00\x00\x03\x37\x35')
        elif mecha == 'B':
            self.s.write(b'\x02\x42\x31\x00\x00\x00\x03\x37\x36')
        self.ret = str(self.s.read(6), 'UTF-8')
    def pause_rec(self, mecha):
        self.s.flushInput()
        if mecha == 'A':
            self.s.write(b'\x02\x43\x30\x00\x00\x00\x03\x37\x36')
        elif mecha == 'B':
            self.s.write(b'\x02\x43\x31\x00\x00\x00\x03\x37\x37')
        self.ret = str(self.s.read(6), 'UTF-8')
    def forward(self, mecha, msearch):
        self.s.flushInput()
        if mecha == 'A':
            if msearch == True:
                self.s.write(b'\x02\x44\x30\x31\x00\x00\x03\x41\x38')
            else:
                self.s.write(b'\x02\x44\x30\x30\x00\x00\x03\x41\x37')
        elif mecha == 'B':
            if msearch == True:
                self.s.write(b'\x02\x44\x31\x31\x00\x00\x03\x41\x39')
            else:
                self.s.write(b'\x02\x44\x31\x30\x00\x00\x03\x41\x38')
        self.ret = str(self.s.read(6), 'UTF-8')
    def rewind(self, mecha, msearch):
        self.s.flushInput()
        if mecha == 'A':
            if msearch == True:
                self.s.write(b'\x02\x45\x30\x31\x00\x00\x03\x41\x39')
            else:
                self.s.write(b'\x02\x45\x30\x30\x00\x00\x03\x41\x38')
        elif mecha == 'B':
            if msearch == True:
                self.s.write(b'\x02\x45\x31\x31\x00\x00\x03\x41\x41') #TODO
            else:
                self.s.write(b'\x02\x45\x31\x30\x00\x00\x03\x41\x39')
        self.ret = str(self.s.read(6), 'UTF-8')
    def direction(self, mecha):
        self.s.flushInput()
        if mecha == 'A':
            self.s.write(b'\x02\x46\x30\x00\x00\x00\x03\x37\x39')
        elif mecha == 'B':
            self.s.write(b'\x02\x46\x31\x00\x00\x00\x03\x37\x41')
        self.ret = str(self.s.read(6), 'UTF-8')
    def memory(self, mecha):
        self.s.flushInput()
        if mecha == 'A':
            self.s.write(b'\x02\x47\x30\x31\x00\x00\x03\x41\x42')
        elif mecha == 'B':
            self.s.write(b'\x02\x47\x31\x31\x00\x00\x03\x41\x43')
        self.ret = str(self.s.read(6), 'UTF-8')
    def c_reset(self, mecha):
        self.s.flushInput()
        if mecha == 'A':
            self.s.write(b'\x02\x48\x30\x00\x00\x00\x03\x37\x42')
        elif mecha == 'B':
            self.s.write(b'\x02\x48\x31\x00\x00\x00\x03\x37\x43')
        self.ret = str(self.s.read(6), 'UTF-8')
    def dolby(self, mecha, dolby):
        self.s.flushInput()
        if mecha == 'A':
            if dolby == 0:
                self.s.write(b'\x02\x49\x30\x30\x00\x00\x03\x41\x43')
            elif dolby == 1:
                self.s.write(b'\x02\x49\x30\x31\x00\x00\x03\x41\x44')
            elif dolby == 2:
                self.s.write(b'\x02\x49\x30\x32\x00\x00\x03\x41\x45')
        elif mecha == 'B':
            if dolby == 0:
                self.s.write(b'\x02\x49\x31\x30\x00\x00\x03\x41\x44')
            elif dolby == 1:
                self.s.write(b'\x02\x49\x31\x31\x00\x00\x03\x41\x45')
            elif dolby == 2:
                self.s.write(b'\x02\x49\x31\x32\x00\x00\x03\x41\x46')
        self.ret = str(self.s.read(6), 'UTF-8')
    def twinrec(self):
        self.s.flushInput()
        self.s.write(b'\x02\x4A\x00\x00\x00\x00\x03\x34\x44')
        self.ret = str(self.s.read(6), 'UTF-8')
    def dubbing(self, hispeed):
        if hispeed == False:
            self.s.write(b'\x02\x4B\x30\x00\x00\x00\x03\x37\x45')
        elif hispeed == True:
            self.s.write(b'\x02\x4B\x31\x00\x00\x00\x03\x37\x46')
        self.ret = str(self.s.read(6), 'UTF-8')
    def speed(self, hispeed):
        if hispeed == False:
            self.s.write(b'\x02\x4C\x30\x00\x00\x00\x03\x37\x46')
        elif hispeed == True:
            self.s.write(b'\x02\x4C\x31\x00\x00\x00\x03\x38\x30')
        self.ret = str(self.s.read(6), 'UTF-8')
    def revmode(self, mode):
        self.s.flushInput()
        if mode == 0:
            self.s.write(b'\x02\x4D\x30\x00\x00\x00\x03\x38\x30')
        elif mode == 1:
            self.s.write(b'\x02\x4D\x31\x00\x00\x00\x03\x38\x31')
        elif mode == 2:
            self.s.write(b'\x02\x4D\x32\x00\x00\x00\x03\x38\x32')
        elif mode == 3:
            self.s.write(b'\x02\x4D\x33\x00\x00\x00\x03\x38\x33')
        self.ret = str(self.s.read(6), 'UTF-8')
    def close(self):
        self.s.close()
        return 0
