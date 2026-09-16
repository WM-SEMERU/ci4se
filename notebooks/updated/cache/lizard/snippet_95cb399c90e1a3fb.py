def main():
    print('Executing faradayio-cli version {0}'.format(__version__))
    try:
        args = setupArgparse()
    except argparse.ArgumentError as error:
        raise SystemExit(error)
    try:
        serialPort = setupSerialPort(args.loopback, args.port)
    except serial.SerialException as error:
        raise SystemExit(error)
    tunName = '{0}-{1}'.format(args.callsign.upper(), args.id)
    isRunning = threading.Event()
    isRunning.set()
    try:
        tun = Monitor(serialPort=serialPort, name=tunName, isRunning=isRunning)
        tun.start()
    except pytun.Error as error:
        print('Warning! faradayio-cli must be run with sudo privileges!')
        raise SystemExit(error)
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        tun.isRunning.clear()
        tun.join()