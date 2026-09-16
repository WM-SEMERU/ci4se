def stats_printer(stats_queue):
    proc_stats = [ProcessStats(i) for i in range(FLAGS.parallel)]
    print_time = start_time = time.time()
    width = 107
    running = True
    while running:
        print_time += 10
        while time.time() < print_time:
            try:
                s = stats_queue.get(True, print_time - time.time())
                if s is None:
                    running = False
                    break
                proc_stats[s.proc_id] = s
            except queue.Empty:
                pass
        replay_stats = ReplayStats()
        for s in proc_stats:
            replay_stats.merge(s.replay_stats)
        print((' Summary %0d secs ' % (print_time - start_time)).center(
            width, '='))
        print(replay_stats)
        print(' Process stats '.center(width, '-'))
        print('\n'.join(str(s) for s in proc_stats))
        print('=' * width)