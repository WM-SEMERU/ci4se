def log_file_name(ext=False):
    script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    val = script_name + '_' + str(int(time.time())) + '_LOG'
    if ext:
        val += '_' + ext
    val += '.txt'
    return val