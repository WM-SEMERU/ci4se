def led(host, seq, anim, f, d):
    at(host, 'LED', seq, [anim, float(f), d])