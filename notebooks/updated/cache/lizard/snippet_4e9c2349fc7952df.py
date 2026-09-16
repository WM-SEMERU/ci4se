def run_benchmarks(dir, models, wav, alphabet, lm_binary=None, trie=None,
    iters=-1):
    r
    assert_valid_dir(dir)
    inference_times = []
    for model in models:
        model_filename = model
        current_model = {'name': model, 'iters': [], 'mean': numpy.infty,
            'stddev': numpy.infty}
        if lm_binary and trie:
            cmdline = (
                './deepspeech --model "%s" --alphabet "%s" --lm "%s" --trie "%s" --audio "%s" -t'
                 % (model_filename, alphabet, lm_binary, trie, wav))
        else:
            cmdline = (
                './deepspeech --model "%s" --alphabet "%s" --audio "%s" -t' %
                (model_filename, alphabet, wav))
        for it in range(iters):
            sys.stdout.write('\rRunning %s: %d/%d' % (os.path.basename(
                model), it + 1, iters))
            sys.stdout.flush()
            rc, stdout, stderr = exec_command(cmdline, cwd=dir)
            if rc == 0:
                inference_time = float(stdout.split('\n')[1].split('=')[-1])
                current_model['iters'].append(inference_time)
            else:
                print('exec_command("%s") failed with rc=%d' % (cmdline, rc))
                print('stdout: %s' % stdout)
                print('stderr: %s' % stderr)
                raise AssertionError('Execution failure: rc=%d' % rc)
        sys.stdout.write('\n')
        sys.stdout.flush()
        current_model['mean'] = numpy.mean(current_model['iters'])
        current_model['stddev'] = numpy.std(current_model['iters'])
        inference_times.append(current_model)
    return inference_times