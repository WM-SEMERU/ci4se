def spi(self, **spi_args):
    spi_args, kwargs = self._extract_spi_args(**spi_args)
    shared = 'shared' if kwargs.pop('shared', False) else 'exclusive'
    if kwargs:
        raise SPIBadArgs('unrecognized keyword argument %s' % kwargs.
            popitem()[0])
    for port, pins in SPI_HARDWARE_PINS.items():
        if all((spi_args['clock_pin'] == pins['clock'], spi_args['mosi_pin'
            ] == pins['mosi'], spi_args['miso_pin'] == pins['miso'], 
            spi_args['select_pin'] in pins['select'])):
            try:
                return self.spi_classes['hardware', shared](self, port=port,
                    device=pins['select'].index(spi_args['select_pin']))
            except Exception as e:
                warnings.warn(SPISoftwareFallback(
                    'failed to initialize hardware SPI, falling back to software (error was: %s)'
                     % str(e)))
                break
    return self.spi_classes['software', shared](self, **spi_args)