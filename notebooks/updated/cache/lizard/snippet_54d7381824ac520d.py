def FromMicroseconds(self, micros):
    self.seconds = micros // _MICROS_PER_SECOND
    self.nanos = micros % _MICROS_PER_SECOND * _NANOS_PER_MICROSECOND