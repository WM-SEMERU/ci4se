def _correct_qualimap_genome_results(samples):
    for s in samples:
        if verify_file(s.qualimap_genome_results_fpath):
            correction_is_needed = False
            with open(s.qualimap_genome_results_fpath, 'r') as f:
                content = f.readlines()
                metrics_started = False
                for line in content:
                    if '>> Reference' in line:
                        metrics_started = True
                    if metrics_started:
                        if line.find(',') != -1:
                            correction_is_needed = True
                            break
            if correction_is_needed:
                with open(s.qualimap_genome_results_fpath, 'w') as f:
                    metrics_started = False
                    for line in content:
                        if '>> Reference' in line:
                            metrics_started = True
                        if metrics_started:
                            if line.find(',') != -1:
                                line = line.replace(',', '')
                        f.write(line)