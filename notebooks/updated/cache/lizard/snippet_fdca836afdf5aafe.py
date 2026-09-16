def sample_stack_all(count=10, interval=0.1):

    def print_stack_all(l, ll):
        l1 = list()
        l1.append('*** STACKTRACE - START ***')
        code = []
        for threadId, stack in sys._current_frames().items():
            sub_code = []
            sub_code.append('# ThreadID: %s' % threadId)
            for filename, lineno, name, line in traceback.extract_stack(stack):
                sub_code.append('File: "%s", line %d, in %s' % (filename,
                    lineno, name))
                if line:
                    sub_code.append('  %s' % line.strip())
            if not 'in select' in sub_code[-2] and not 'in wait' in sub_code[-2
                ] and not 'in print_stack_all' in sub_code[-2
                ] and not 'in sample_stack_all' in sub_code[-2
                ] and not 'in checkcache' in sub_code[-2
                ] and not 'do_sleep' in sub_code[-2
                ] and not 'sleep' in sub_code[-1] and not any([(
                'in do_sample' in s) for s in sub_code]):
                code.extend(sub_code)
        for line in code:
            l1.append(line)
        l1.append('*** STACKTRACE - END ***')
        with l:
            ll.extend(l1)

    def do_sample():
        l = threading.RLock()
        ll = list()
        for i in range(count):
            print_stack_all(l, ll)
            time.sleep(interval)
        with l:
            print('\n'.join(ll))
    threading.Thread(target=do_sample).start()