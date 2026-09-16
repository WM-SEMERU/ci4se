def matches_pattern(self, other):
    if hasattr(other, 'messageType'):
        messageTypeIsEqual = False
        if self.messageType is None or other.messageType is None:
            messageTypeIsEqual = True
        else:
            messageTypeIsEqual = self.messageType == other.messageType
        extendedIsEqual = False
        if self.extended is None or other.extended is None:
            extendedIsEqual = True
        else:
            extendedIsEqual = self.extended == other.extended
        return messageTypeIsEqual and extendedIsEqual
    return False