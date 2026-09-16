def write_audacity_labels(audacity_labels, filename):
    with open(filename, 'w') as f:
        for label in audacity_labels:
            f.write('%s\t%s\t%s\n' % (label.start_seconds, label.
                end_seconds, label.label))