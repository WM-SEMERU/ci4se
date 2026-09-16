def mix1(servo1, servo2, mixtype=1, gain=0.5):
    v1, v2 = mixer(servo1, servo2, mixtype=mixtype, gain=gain)
    return v1