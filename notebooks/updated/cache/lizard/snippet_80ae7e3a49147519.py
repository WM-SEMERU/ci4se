def load_coco(image_set, dirname, shuffle=False):
    anno_files = [('instances_' + y.strip() + '.json') for y in image_set.
        split(',')]
    assert anno_files, 'No image set specified'
    imdbs = []
    for af in anno_files:
        af_path = os.path.join(dirname, 'annotations', af)
        imdbs.append(Coco(af_path, dirname, shuffle=shuffle))
    if len(imdbs) > 1:
        return ConcatDB(imdbs, shuffle)
    else:
        return imdbs[0]