def wait(predicate, interval=1, message=lambda : 'Waiting...'):
    ball, next_ball = '|/-\\', '|'
    sys.stdout.write('    \x1b[K')
    sys.stdout.flush()
    while not predicate():
        time.sleep(1)
        next_ball = ball[(ball.index(next_ball) + 1) % len(ball)]
        sys.stdout.write('\r ' + str(message()) + ' ' + next_ball + ' \x1b[K')
        sys.stdout.flush()
    print('\r Done. \x1b[K')
    sys.stdout.flush()