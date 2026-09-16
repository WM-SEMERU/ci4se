def probes_used_generate_vector(probe_files_full, probe_files_model):
    import numpy as np
    C_probesUsed = np.ndarray((len(probe_files_full),), 'bool')
    C_probesUsed.fill(False)
    c = 0
    for k in sorted(probe_files_full.keys()):
        if probe_files_model.has_key(k):
            C_probesUsed[c] = True
        c += 1
    return C_probesUsed