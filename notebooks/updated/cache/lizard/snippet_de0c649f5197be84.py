def rdopkg(*cargs):
    runner = rdopkg_runner()
    return shell.run(runner, cargs=cargs, prog='rdopkg', version=__version__)