def generate_pretty_output(self, stat, verbose, output_function, logs=True):
    has_check = False
    for r in self.results:
        has_check = True
        if stat:
            output_function(OUTPUT_CHARS[r.status], fg=COLOURS[r.status],
                nl=False)
        else:
            output_function(str(r), fg=COLOURS[r.status])
            if verbose:
                output_function('  -> {}\n  -> {}'.format(r.description, r.
                    reference_url), fg=COLOURS[r.status])
                if logs and r.logs:
                    output_function('  -> logs:', fg=COLOURS[r.status])
                    for l in r.logs:
                        output_function('    -> {}'.format(l), fg=COLOURS[r
                            .status])
    if not has_check:
        output_function('No check found.')
    elif stat and not verbose:
        output_function('')
    else:
        output_function('')
        for status, count in six.iteritems(self.statistics):
            output_function('{}:{} '.format(status, count), nl=False)
        output_function('')