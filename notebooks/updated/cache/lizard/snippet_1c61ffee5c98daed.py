def origin(self):
    for item in os.popen('git remote -v'):
        split_item = item.strip().split()
        if split_item[0] == 'origin' and split_item[-1] == '(push)':
            return split_item[1]