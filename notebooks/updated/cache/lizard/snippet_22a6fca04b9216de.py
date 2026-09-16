def Filter(self):
    if not self.desc:
        self.short_desc = ''
        return
    for i in range(len(self.desc)):
        if self.desc[i].find(self.executable) >= 0:
            self.desc[i] = self.desc[i].replace(self.executable, self.name)
    self.short_desc = self.desc[0]
    word_list = self.short_desc.split(' ')
    all_names = [self.name, self.short_name]
    while word_list and (word_list[0] in all_names or word_list[0].lower() in
        all_names):
        del word_list[0]
        self.short_desc = ''
    if not self.short_desc and word_list:
        self.short_desc = ' '.join(word_list)