def start():
    os.write(BenchmarkProcess.BACKCHANNEL_OUT, BenchmarkProcess.START)
    response = util.untilConcludes(os.read, BenchmarkProcess.BACKCHANNEL_IN, 1)
    if response != BenchmarkProcess.START:
        raise RuntimeError(
            'Parent process responded with %r instead of START ' % (response,))