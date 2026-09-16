def filter_false_positive(df, process_time):
    result = []
    track = []
    count = 0
    for o in df['alerts']:
        count += 1
        if 'closedState' in o:
            if o['closedState'] != 'False Positive':
                if 'distinguishers' in o:
                    try:
                        if 'virus' in o['distinguishers']:
                            if o['distinguishers']['virus'] != 'fetestevent':
                                result.append(o)
                            else:
                                track.append(o)
                        else:
                            result.append(o)
                    except TypeError:
                        result.append(o)
                else:
                    result.append(o)
            else:
                track.append(o)
        elif 'distinguishers' in o:
            try:
                if 'virus' in o['distinguishers']:
                    if o['distinguishers']['virus'] != 'fetestevent':
                        result.append(o)
                    else:
                        track.append(o)
                else:
                    result.append(o)
            except TypeError:
                result.append(o)
    trackfile = open('tracking_fetest_' + process_time + '.txt', 'w')
    numskip = 1
    for item in track:
        trackfile.write('\n\n**** {:d}: Display ID {} ****\n\n{}'.format(
            numskip, item['displayId'], item))
        numskip += 1
    return result