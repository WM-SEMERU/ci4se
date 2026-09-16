def rmgen(self, idx):
    stagens = []
    for device, stagen in zip(self.devman.devices, self.call.stagen):
        if stagen:
            stagens.append(device)
    for gen in idx:
        for stagen in stagens:
            if gen in self.__dict__[stagen].uid.keys():
                self.__dict__[stagen].disable_gen(gen)