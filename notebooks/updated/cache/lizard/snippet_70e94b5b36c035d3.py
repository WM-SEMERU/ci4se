def voip_play2(s1, **kargs):
    dsp, rd = os.popen2(sox_base % '-c 2')
    global x1, x2
    x1 = ''
    x2 = ''

    def play(pkt):
        global x1, x2
        if not pkt:
            return
        if not pkt.haslayer(UDP) or not pkt.haslayer(IP):
            return
        ip = pkt.getlayer(IP)
        if s1 in [ip.src, ip.dst]:
            if ip.dst == s1:
                x1 += pkt.getlayer(conf.raw_layer).load[12:]
            else:
                x2 += pkt.getlayer(conf.raw_layer).load[12:]
            x1, x2, r = _merge_sound_bytes(x1, x2)
            dsp.write(r)
    sniff(store=0, prn=play, **kargs)