def write_data(self, write_finished_cb):
    self._write_finished_cb = write_finished_cb
    data = bytearray()
    for led in self.leds:
        R5 = int((int(led.r) & 255) * 249 + 1014 >> 11 & 31
            ) * led.intensity / 100
        G6 = int((int(led.g) & 255) * 253 + 505 >> 10 & 63
            ) * led.intensity / 100
        B5 = int((int(led.b) & 255) * 249 + 1014 >> 11 & 31
            ) * led.intensity / 100
        tmp = int(R5) << 11 | int(G6) << 5 | int(B5) << 0
        data += bytearray((tmp >> 8, tmp & 255))
    self.mem_handler.write(self, 0, data, flush_queue=True)