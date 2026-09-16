def runm():
    signal.signal(signal.SIGINT, signal_handler)
    count = int(sys.argv.pop(1))
    processes = [Process(target=run, args=()) for x in range(count)]
    try:
        for p in processes:
            p.start()
    except KeyError:
        pass
    finally:
        for p in processes:
            p.join()