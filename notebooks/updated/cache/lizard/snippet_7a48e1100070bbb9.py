def trec_dataset(directory='data/trec/', train=False, test=False,
    train_filename='train_5500.label', test_filename='TREC_10.label',
    check_files=['train_5500.label'], urls=[
    'http://cogcomp.org/Data/QA/QC/train_5500.label',
    'http://cogcomp.org/Data/QA/QC/TREC_10.label'], fine_grained=False):
    download_files_maybe_extract(urls=urls, directory=directory,
        check_files=check_files)
    ret = []
    splits = [(train, train_filename), (test, test_filename)]
    splits = [f for requested, f in splits if requested]
    for filename in splits:
        full_path = os.path.join(directory, filename)
        examples = []
        for line in open(full_path, 'rb'):
            label, _, text = line.replace(b'\xf0', b' ').strip().decode(
                ).partition(' ')
            label, _, label_fine = label.partition(':')
            if fine_grained:
                examples.append({'label': label_fine, 'text': text})
            else:
                examples.append({'label': label, 'text': text})
        ret.append(Dataset(examples))
    if len(ret) == 1:
        return ret[0]
    else:
        return tuple(ret)