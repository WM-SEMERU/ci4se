def get_info(self):
    if os.path.isfile(self.path):
        total_size = os.path.getsize(self.path)
        total_files = 1
    elif os.path.exists(self.path):
        total_size = 0
        total_files = 0
        for x in os.walk(self.path):
            for fn in x[2]:
                if any(fnmatch.fnmatch(fn, ext) for ext in self.exclude):
                    continue
                fpath = os.path.normpath(os.path.join(x[0], fn))
                fsize = os.path.getsize(fpath)
                if fsize and not is_hidden_file(fpath):
                    total_size += fsize
                    total_files += 1
    else:
        raise exceptions.InvalidInputException
    if not (total_files and total_size):
        raise exceptions.EmptyInputException
    if self.piece_size:
        ps = self.piece_size
    else:
        ps = 1 << max(0, math.ceil(math.log(total_size / 1500, 2)))
        if ps < MIN_PIECE_SIZE:
            ps = MIN_PIECE_SIZE
        if ps > MAX_PIECE_SIZE:
            ps = MAX_PIECE_SIZE
    return total_size, total_files, ps, math.ceil(total_size / ps)