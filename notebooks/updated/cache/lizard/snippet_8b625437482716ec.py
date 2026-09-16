def get_range(self):
    min, max = 100000, -1
    for cont in self.bar:
        for note in cont[2]:
            if int(note) < int(min):
                min = note
            elif int(note) > int(max):
                max = note
    return min, max