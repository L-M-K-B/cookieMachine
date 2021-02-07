import pyb
import utime
# training
pyb.LED(4).on()
utime.sleep(3)
pyb.LED(4).off()

count = 0
while count <= 5:

    if count % 2 == 0:
        pyb.LED(2).on()
        utime.sleep(3)
        pyb.LED(2).off()
        count += 1
        utime.sleep(3)
    else:
        pyb.LED(3).on()
        utime.sleep(3)
        pyb.LED(3).off()
        count += 1
        utime.sleep(3)

# print some text to the serial console
print('Hello MicroPython!')

pyb.LED(4).on()
utime.sleep(3)
pyb.LED(4).off()
