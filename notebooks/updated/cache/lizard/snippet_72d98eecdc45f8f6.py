def remove_last_match(self, address, size):
    count = 0
    start = address
    end = address + size - 1
    matched = None
    for item in self.__ranges:
        if item.match(start) and item.match(end):
            matched = item
            count += 1
    self.__ranges.remove(matched)
    return count