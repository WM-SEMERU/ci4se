def _handleCallInitiated(self, regexMatch, callId=None, callType=1):
    if self._dialEvent:
        if regexMatch:
            groups = regexMatch.groups()
            if len(groups) >= 2:
                self._dialResponse = int(groups[0]), int(groups[1])
            else:
                self._dialResponse = int(groups[0]), 1
        else:
            self._dialResponse = callId, callType
        self._dialEvent.set()