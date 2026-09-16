def get_prefix(dir='../'):
    prefix = glob(dir + '*.gkpStore')[0]
    prefix = op.basename(prefix).rsplit('.', 1)[0]
    return prefix