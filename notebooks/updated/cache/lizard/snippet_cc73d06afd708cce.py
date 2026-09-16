async def pair(self):
    protocol = self.atv.service.protocol
    if protocol == const.PROTOCOL_DMAP:
        await self.atv.pairing.start(zeroconf=Zeroconf(), name=self.args.
            remote_name, pairing_guid=self.args.pairing_guid)
    elif protocol == const.PROTOCOL_MRP:
        await self.atv.pairing.start()
    if self.atv.pairing.device_provides_pin:
        pin = await _read_input(self.loop, 'Enter PIN on screen: ')
        self.atv.pairing.pin(pin)
    else:
        self.atv.pairing.pin(self.args.pin_code)
        print('Use {0} to pair with "{1}" (press ENTER to stop)'.format(
            self.args.pin_code, self.args.remote_name))
    if self.args.pin_code is None:
        print('Use any pin to pair with "{}" (press ENTER to stop)'.format(
            self.args.remote_name))
    else:
        print('Use pin {} to pair with "{}" (press ENTER to stop)'.format(
            self.args.pin_code, self.args.remote_name))
    await self.loop.run_in_executor(None, sys.stdin.readline)
    await self.atv.pairing.stop()
    if self.atv.pairing.has_paired:
        print('Pairing seems to have succeeded, yey!')
        print('You may now use these credentials: {0}'.format(self.atv.
            pairing.credentials))
    else:
        print('Pairing failed!')
        return 1
    return 0