def signalStrength(self):
    csq = self.CSQ_REGEX.match(self.write('AT+CSQ')[0])
    if csq:
        ss = int(csq.group(1))
        return ss if ss != 99 else -1
    else:
        raise CommandError()