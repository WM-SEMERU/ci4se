def _scale_cores_to_memory(cores, mem_per_core, sysinfo, system_memory):
    total_mem = '%.2f' % (cores * mem_per_core + system_memory)
    if 'cores' not in sysinfo:
        return cores, total_mem, 1.0
    total_mem = min(float(total_mem), float(sysinfo['memory']) - system_memory)
    cores = min(cores, int(sysinfo['cores']))
    mem_cores = int(math.floor(float(total_mem) / mem_per_core))
    if mem_cores < 1:
        out_cores = 1
    elif mem_cores < cores:
        out_cores = mem_cores
    else:
        out_cores = cores
    mem_pct = float(out_cores) / float(cores)
    return out_cores, total_mem, mem_pct