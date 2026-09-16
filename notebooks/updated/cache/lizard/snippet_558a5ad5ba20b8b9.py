def compact(self):
    previous_value = object()
    redundant = []
    for time, value in self:
        if value == previous_value:
            redundant.append(time)
        previous_value = value
    for time in redundant:
        del self[time]