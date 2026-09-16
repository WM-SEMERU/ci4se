def play_audio(filename: str):
    import platform
    from subprocess import Popen
    player = 'play' if platform.system() == 'Darwin' else 'aplay'
    Popen([player, '-q', filename])