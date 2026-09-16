def default_output_name(self, input_file):
    irom_segment = self.get_irom_segment()
    if irom_segment is not None:
        irom_offs = irom_segment.addr - ESP8266ROM.IROM_MAP_START
    else:
        irom_offs = 0
    return '%s-0x%05x.bin' % (os.path.splitext(input_file)[0], irom_offs & 
        ~(ESPLoader.FLASH_SECTOR_SIZE - 1))