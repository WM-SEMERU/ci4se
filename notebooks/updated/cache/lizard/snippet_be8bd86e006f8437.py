def main():
    global modem
    modem = bm(port='/dev/ttyACM0', incomingcallback=callback)
    if modem.state == modem.STATE_FAILED:
        print('Unable to initialize modem, exiting.')
        return
    resp = modem.sendcmd('ATI3')
    for line in resp:
        if line:
            print(line)
    try:
        input('Wait for call, press enter to exit')
    except (SyntaxError, EOFError, KeyboardInterrupt):
        pass
    modem.close()