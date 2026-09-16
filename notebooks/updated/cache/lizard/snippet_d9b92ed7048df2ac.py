def accept(self, title):
    if self._whitelist and title in self._whitelist:
        return self.WHITELIST_ACCEPT
    if self._blacklist and title in self._blacklist:
        return self.REJECT
    if self._positiveRegex and self._positiveRegex.search(title) is None:
        return self.REJECT
    if self._negativeRegex and self._negativeRegex.search(title) is not None:
        return self.REJECT
    if self._truncated is not None:
        truncated = simplifyTitle(title, self._truncateAfter)
        if truncated in self._truncated:
            if self._truncated[truncated] == title:
                return self.DEFAULT_ACCEPT
            else:
                return self.REJECT
        else:
            self._truncated[truncated] = title
    return self.DEFAULT_ACCEPT