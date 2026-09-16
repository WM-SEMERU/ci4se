def build_chunk(oscillators):
    step_random_processes(oscillators)
    subchunks = []
    for osc in oscillators:
        osc.amplitude.step_amp()
        osc_chunk = osc.get_samples(config.CHUNK_SIZE)
        if osc_chunk is not None:
            subchunks.append(osc_chunk)
    if len(subchunks):
        new_chunk = sum(subchunks)
    else:
        new_chunk = numpy.zeros(config.CHUNK_SIZE)
    chunk_amplitude = amplitude.find_amplitude(new_chunk)
    if chunk_amplitude > config.MAX_AMPLITUDE:
        new_chunk = amplitude.normalize_amplitude(new_chunk, config.
            MAX_AMPLITUDE)
        avg_amp = sum(osc.amplitude.value for osc in oscillators) / len(
            oscillators)
        for osc in oscillators:
            if osc.amplitude.value > avg_amp and rand.prob_bool(0.1
                ) or rand.prob_bool(0.01):
                osc.amplitude.drift_target = rand.weighted_rand([(-5, 1), (
                    0, 10)])
                osc.amplitude.change_rate = rand.weighted_rand(osc.
                    amplitude.change_rate_weights)
    return new_chunk.astype(config.SAMPLE_DATA_TYPE).tostring()