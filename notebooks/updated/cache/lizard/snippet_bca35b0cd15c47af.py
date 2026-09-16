def retrieve(self, aclass):
    resu = []
    for x in self.payload:
        try:
            if isinstance(aclass, str):
                if x.name == aclass:
                    resu.append(x)
            elif isinstance(x, aclass):
                resu.append(x)
            resu += x.retrieve(aclass)
        except:
            pass
    return resu