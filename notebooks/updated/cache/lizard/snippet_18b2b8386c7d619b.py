def include_revision(revision_num, skip_factor=1.1):
    if skip_factor <= 1.0:
        return True
    return int(math.log1p(revision_num) / math.log(skip_factor)) != int(
        math.log(revision_num + 2.0) / math.log(skip_factor))