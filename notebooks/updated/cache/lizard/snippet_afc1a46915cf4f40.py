def reset(self):
    self.curr_idx = 0
    random.shuffle(self.idx)
    for i, buck in enumerate(self.sentences):
        self.indices[i], self.sentences[i], self.characters[i], self.label[i
            ] = shuffle(self.indices[i], self.sentences[i], self.characters
            [i], self.label[i])
    self.ndindex = []
    self.ndsent = []
    self.ndchar = []
    self.ndlabel = []
    for i, buck in enumerate(self.sentences):
        self.ndindex.append(ndarray.array(self.indices[i], dtype=self.dtype))
        self.ndsent.append(ndarray.array(self.sentences[i], dtype=self.dtype))
        self.ndchar.append(ndarray.array(self.characters[i], dtype=self.dtype))
        self.ndlabel.append(ndarray.array(self.label[i], dtype=self.dtype))