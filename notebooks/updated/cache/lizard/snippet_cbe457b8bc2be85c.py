def start_srt():
    extensions = ['srt']
    Config.filenames = prep_files(Config.args, extensions)
    Config.patterns = pattern_logic_srt()
    for filename in Config.filenames:
        SrtProject(filename)