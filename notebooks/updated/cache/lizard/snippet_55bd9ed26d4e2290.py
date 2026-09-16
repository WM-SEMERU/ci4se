def post_build(self, p, pay):
    p += pay
    if self.auxdlen != 0:
        print(
            'NOTICE: A properly formatted and complaint V3 Group Record should have an Auxiliary Data length of zero (0).'
            )
        print('        Subsequent Group Records are lost!')
    return p