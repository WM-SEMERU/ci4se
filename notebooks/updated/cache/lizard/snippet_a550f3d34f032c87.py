def samefile(p1, p2):
    both_exist = os.path.exists(p1) and os.path.exists(p2)
    use_samefile = hasattr(os.path, 'samefile') and both_exist
    if use_samefile:
        return os.path.samefile(p1, p2)
    norm_p1 = os.path.normpath(os.path.normcase(p1))
    norm_p2 = os.path.normpath(os.path.normcase(p2))
    return norm_p1 == norm_p2