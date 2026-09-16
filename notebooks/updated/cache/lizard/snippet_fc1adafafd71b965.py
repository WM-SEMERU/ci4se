def diagnostics(self):


    class DiagIterator:

        def __init__(self, tu):
            self.tu = tu

        def __len__(self):
            return int(conf.lib.clang_getNumDiagnostics(self.tu))

        def __getitem__(self, key):
            diag = conf.lib.clang_getDiagnostic(self.tu, key)
            if not diag:
                raise IndexError
            return Diagnostic(diag)
    return DiagIterator(self)