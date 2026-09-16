def executable(self):
    exe = util.find_executable('bin/symbiotic', exitOnError=False)
    if exe:
        return exe
    else:
        return OldSymbiotic.executable(self)