def set_uppercase(self, uppercase):
    for row in self.rows:
        for key in row.keys:
            if type(key) == VKey:
                if uppercase:
                    key.value = key.value.upper()
                else:
                    key.value = key.value.lower()