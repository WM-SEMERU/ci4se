def fixup_msg(lvl, msg):
    if 'switching to batch mode...' in msg and lvl == logging.ERROR:
        return logging.WARNING, msg
    return lvl, msg