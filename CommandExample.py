import dn780r
import time

d = dn780r.Deck("/dev/ttyUSB0")
d.reset()
d.play('A')
time.sleep(5)
d.stop('A')
d.status()
print('Counter A:')
print(d.counter_a)
print('Counter B:')
print(d.counter_b)
print('Model:')
print(d.id())
print('CPU Version:')
print(d.cpu_vers())
d.close()
