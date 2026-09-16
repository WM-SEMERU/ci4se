def _connect(self, id_mask):
    all_devices = glob.glob('/dev/ttyUSB*')
    sensors = []
    for device in all_devices:
        try:
            ser = serial.Serial(port=device, timeout=0.5, exclusive=True)
            ser.write('ID\r')
            ser.flush()
            time.sleep(0.05)
            resp = ser.read(13)
            ser.close()
            if len(resp) >= 10 and resp[:len(id_mask)] == id_mask:
                sensors.append((device, resp.rstrip('\r\n')))
        except:
            continue
    sensors = sorted(sensors, key=lambda x: x[1])
    serials = []
    for device, key in sensors:
        ser = serial.Serial(port=device, timeout=0.5)
        serials.append(ser)
        rospy.loginfo('Connected to load cell {} at {}'.format(key, device))
    return serials