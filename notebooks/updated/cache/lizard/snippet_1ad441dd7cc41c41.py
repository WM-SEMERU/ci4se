def sync(self):
    self.elk.send(cp_encode())
    self.get_descriptions(TextDescriptions.SETTING.value)