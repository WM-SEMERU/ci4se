def _boxFromData(self, messageData):
    inputBoxes = parseString(messageData)
    if not len(inputBoxes) == 1:
        raise MalformedMessage()
    [inputBox] = inputBoxes
    return inputBox