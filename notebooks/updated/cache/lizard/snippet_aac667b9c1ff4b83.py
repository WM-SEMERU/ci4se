def classorder(self, classes):
    return [classid for classid, classitem in sorted(((classid, classitem) for
        classid, classitem in classes.items() if 'seqnr' in classitem), key
        =lambda pair: pair[1]['seqnr'])] + [classid for classid, classitem in
        sorted(((classid, classitem) for classid, classitem in classes.
        items() if 'seqnr' not in classitem), key=lambda pair: pair[1][
        'label'] if 'label' in pair[1] else pair[1]['id'])]