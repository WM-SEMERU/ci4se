def LoadFirmwareImage(chip, filename):
    with open(filename, 'rb') as f:
        if chip.lower() == 'esp32':
            return ESP32FirmwareImage(f)
        else:
            magic = ord(f.read(1))
            f.seek(0)
            if magic == ESPLoader.ESP_IMAGE_MAGIC:
                return ESP8266ROMFirmwareImage(f)
            elif magic == ESPBOOTLOADER.IMAGE_V2_MAGIC:
                return ESP8266V2FirmwareImage(f)
            else:
                raise FatalError('Invalid image magic number: %d' % magic)