def update(self, infos):
    for info_in in infos:
        if isinstance(info_in, LearningGene):
            if random.random() < 0.1:
                self.mutate(info_in)
            else:
                self.replicate(info_in)