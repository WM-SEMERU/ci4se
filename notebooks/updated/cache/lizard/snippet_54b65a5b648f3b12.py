def calculate_sampling_decision(trace_header, recorder, sampling_req):
    if trace_header.sampled is not None and trace_header.sampled != '?':
        return trace_header.sampled
    elif not recorder.sampling:
        return 1
    else:
        decision = recorder.sampler.should_trace(sampling_req)
    return decision if decision else 0