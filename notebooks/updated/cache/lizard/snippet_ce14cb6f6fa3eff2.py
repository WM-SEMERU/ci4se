def delLadder(name):
    ladders = getKnownLadders()
    try:
        ladder = ladders[name]
        os.remove(ladder.filename)
        del ladders[name]
        return ladder
    except KeyError:
        raise ValueError(
            "given ladder name '%s' is not a known ladder definition" % name)